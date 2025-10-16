"""
Multi-Tool Agent System with Google ADK
Based on: Building your first Agent workshop (GDG DevFest Danang 2025)

This demonstrates:
1. Single agent with tools (Weather Agent)
2. Multi-agent team with automatic delegation
3. Session management and conversation flow
"""

import os
from typing import Optional
from google.adk.agents import Agent
from google.adk.sessions import InMemorySessionService
from google.adk.runners import Runner
from google.genai import types


# ============================================================================
# STEP 1: Define Tools
# ============================================================================

def get_weather(city: str) -> dict:
    """Lấy báo cáo thời tiết hiện tại cho một thành phố.

    Args:
        city: Tên thành phố (VD: "Hà Nội", "London", "Tokyo")

    Returns:
        dict: {'status': 'success'|'error', 'report': str} hoặc {'error_message': str}
    """
    city_normalized = city.lower().replace(" ", "")

    # Mock weather database
    mock_weather_db = {
        "hanoi": {"status": "success", "report": "☀️ Hà Nội: Nắng đẹp, 25°C"},
        "hànội": {"status": "success", "report": "☀️ Hà Nội: Nắng đẹp, 25°C"},
        "london": {"status": "success", "report": "☁️ London: Nhiều mây, 15°C"},
        "tokyo": {"status": "success", "report": "🌧️ Tokyo: Mưa nhẹ, 18°C"},
    }

    if city_normalized in mock_weather_db:
        return mock_weather_db[city_normalized]
    else:
        return {
            "status": "error",
            "error_message": f"Xin lỗi, không có thông tin thời tiết cho '{city}'."
        }


def say_hello(name: Optional[str] = None) -> str:
    """Cung cấp lời chào thân thiện.

    Args:
        name: Tên người cần chào (optional)

    Returns:
        str: Message chào hỏi
    """
    if name:
        return f"👋 Xin chào, {name}!"
    else:
        return "👋 Xin chào!"


def say_goodbye() -> str:
    """Cung cấp message tạm biệt."""
    return "👋 Tạm biệt! Chúc bạn một ngày tốt lành! ✨"


# ============================================================================
# STEP 2: Define Specialized Sub-Agents
# ============================================================================

AGENT_MODEL = "gemini-2.5-flash"

# Greeting Agent
greeting_agent = Agent(
    model=AGENT_MODEL,
    name="greeting_agent",
    instruction="Nhiệm vụ DUY NHẤT: Chào hỏi thân thiện. "
                "Dùng tool 'say_hello'. "
                "Nếu user cung cấp tên, truyền cho tool. "
                "KHÔNG làm gì khác.",
    description="Xử lý greetings sử dụng 'say_hello'.",
    tools=[say_hello],
)

# Weather Agent (can be used standalone or as sub-agent)
weather_agent = Agent(
    name="weather_agent",
    model=AGENT_MODEL,
    description="Cung cấp thông tin thời tiết cho các thành phố.",
    instruction="Bạn là trợ lý thời tiết. "
                "Khi user hỏi về thời tiết, dùng tool 'get_weather'. "
                "Nếu tool lỗi, thông báo lịch sự. "
                "Nếu thành công, trình bày báo cáo rõ ràng.",
    tools=[get_weather],
)

# Farewell Agent
farewell_agent = Agent(
    model=AGENT_MODEL,
    name="farewell_agent",
    instruction="Nhiệm vụ DUY NHẤT: Tạm biệt lịch sự. "
                "Dùng tool 'say_goodbye' khi user nói bye/tạm biệt. "
                "KHÔNG làm gì khác.",
    description="Xử lý farewells sử dụng 'say_goodbye'.",
    tools=[say_goodbye],
)


# ============================================================================
# STEP 3: Define Root Agent with Multi-Agent Team
# ============================================================================

root_agent = Agent(
    name="weather_assistant_team",
    model=AGENT_MODEL,
    description="Agent điều phối: Weather requests + delegate greetings/farewells.",
    instruction="Bạn là Weather Agent chính điều phối team. "
                "TRÁCH NHIỆM CHÍNH: Cung cấp thông tin thời tiết. "
                "Dùng 'get_weather' CHỈ cho weather requests. "
                "\n\nSUB-AGENTS: "
                "1. 'greeting_agent': Xử lý 'Hi', 'Xin chào' → DELEGATE "
                "2. 'farewell_agent': Xử lý 'Tạm biệt', 'Bye' → DELEGATE "
                "\n\nPHÂN TÍCH query: "
                "- Greeting? → delegate greeting_agent "
                "- Farewell? → delegate farewell_agent "
                "- Weather? → tự xử lý với get_weather "
                "- Khác? → phản hồi lịch sự hoặc nói không xử lý được",
    tools=[get_weather],
    sub_agents=[greeting_agent, farewell_agent]
)


# ============================================================================
# STEP 4: Helper Functions for Agent Interaction
# ============================================================================

async def call_agent_async(
    query: str,
    runner: Runner,
    user_id: str,
    session_id: str
) -> str:
    """
    Gửi query đến agent và trả về response.

    Args:
        query: User's question/request
        runner: Runner instance
        user_id: User identifier
        session_id: Session identifier

    Returns:
        str: Agent's final response
    """
    content = types.Content(role='user', parts=[types.Part(text=query)])

    final_response_text = "⚠️ Agent không tạo ra response."

    async for event in runner.run_async(
        user_id=user_id,
        session_id=session_id,
        new_message=content
    ):
        if event.is_final_response():
            if event.content and event.content.parts:
                final_response_text = event.content.parts[0].text
            elif event.actions and event.actions.escalate:
                final_response_text = f"⚠️ Agent escalated: {event.error_message or 'Không có message.'}"
            break

    return final_response_text


async def create_session_and_runner(
    agent: Agent,
    app_name: str = "Weather Agent Demo",
    user_id: str = "user_1",
    session_id: str = "session_001"
):
    """
    Tạo session service và runner cho agent.

    Args:
        agent: Agent instance to use
        app_name: Application name
        user_id: User identifier
        session_id: Session identifier

    Returns:
        tuple: (session_service, runner, user_id, session_id)
    """
    session_service = InMemorySessionService()

    session = await session_service.create_session(
        app_name=app_name,
        user_id=user_id,
        session_id=session_id
    )

    runner = Runner(
        agent=agent,
        app_name=app_name,
        session_service=session_service
    )

    return session_service, runner, user_id, session_id


# ============================================================================
# STEP 5: Example Usage
# ============================================================================

async def main():
    """
    Example conversation demonstrating:
    1. Automatic delegation to greeting_agent
    2. Weather query handling by root agent
    3. Automatic delegation to farewell_agent
    """
    print("=" * 60)
    print("🤖 Multi-Agent Weather Assistant Demo")
    print("=" * 60)

    # Setup
    _, runner, user_id, session_id = await create_session_and_runner(
        agent=root_agent,
        app_name="Weather Agent Team Demo"
    )

    # Test queries
    queries = [
        "Xin chào!",
        "Thời tiết ở Hà Nội thế nào?",
        "Còn London thì sao?",
        "Cảm ơn, tạm biệt!"
    ]

    for query in queries:
        print(f"\n👤 User: {query}")
        response = await call_agent_async(query, runner, user_id, session_id)
        print(f"🤖 Agent: {response}")

    print("\n" + "=" * 60)
    print("✅ Demo hoàn thành!")
    print("=" * 60)


if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
