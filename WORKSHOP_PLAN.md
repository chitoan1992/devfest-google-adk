# Workshop Plan: Build Your First Agent with Google ADK

## 🎯 Workshop Overview

**Duration:** 90 minutes
**Audience:** 100 Students (tech-focused, post Agentic Coding session)
**Format:** Hands-on Colab + Live Demo + Interactive Q&A
**Goal:** Students build working agents and understand hackathon workflow

---

## 📋 Detailed Outline với Speaking Notes

### 0. Pre-Workshop Setup (Before session starts)

**Checklist:**
- [ ] Colab notebook đã public và tested
- [ ] API credit links ready
- [ ] Demo apps prepared (backup nếu live coding fail)
- [ ] Slides với visuals/diagrams ready
- [ ] Terminal/Colab screen share setup

---

## PART 1: INTRODUCTION (5 phút)

### Slide 1: Hook Opening

**Script:**
> "Chào mọi người! Tôi có một câu hỏi: Có bao nhiêu người trong phòng này từng xem phim Iron Man? *[Pause for hands]*
>
> Trong phim, Tony Stark có JARVIS - một AI assistant có thể hiểu ngôn ngữ tự nhiên, điều khiển thiết bị, thậm chí đưa ra quyết định chiến thuật.
>
> **10 năm trước**, JARVIS chỉ là khoa học viễn tưởng.
> **5 năm trước**, những agent như vậy chỉ xuất hiện trong các phòng lab của Google, OpenAI.
> **Hôm nay**, trong 90 phút tới, bạn và tôi sẽ cùng nhau xây dựng một AI agent tương tự."

**Visual:** Slide với ảnh JARVIS → Google Research Lab → Code editor

---

### Slide 2: Learning Outcomes

**Script:**
> "Sau workshop này, bạn sẽ có thể:
> - ✨ Build agent đầu tiên với tools - một Weather Bot thực sự hoạt động
> - 👥 Thiết kế multi-agent teams - giống như một team startup, mỗi agent có chuyên môn riêng
> - 🚀 Setup fullstack app với ADK Starter Pack - từ code đến UI chỉ trong vài phút
> - 📋 **Quan trọng nhất** - Áp dụng vào hackathon: từ ý tưởng → MVP → Pitch trong vài giờ
>
> Và điều đặc biệt: Tất cả sẽ được thực hành trực tiếp trên Google Colab, không cần setup môi trường phức tạp."

**Interactive Moment:**
> "Trước khi bắt đầu, cho tôi biết: Có bao nhiêu bạn đã từng code với LLMs API? *[Count hands]* Tuyệt! Còn bao nhiêu bạn chưa bao giờ? *[Count]* Perfect - workshop này sẽ phù hợp cho tất cả!"

---

### Slide 3: Why ADK?

**Script:**
> "Có thể một số bạn đã nghe về LangChain, AutoGen, hoặc các frameworks khác. Vậy tại sao chúng ta học ADK?
>
> **Câu trả lời:** ADK là framework chính thức từ Google, được tối ưu cho Gemini models. Nó có:
> - 🎯 Simpler API - ít boilerplate hơn
> - 🚀 Native Gemini integration - performance tốt nhất
> - 👥 Built-in multi-agent orchestration - không cần custom logic
> - 🏗️ Production-ready templates - từ prototype đến production
>
> Quan trọng nhất: **ADK được thiết kế cho builders, không phải researchers.**"

**Visual:** So sánh code snippet: LangChain vs ADK (same task, ADK ngắn hơn)

---

## PART 2: SETUP (10 phút)

### Slide 4: Getting API Credits

**Script:**
> "Okay, bây giờ chúng ta sẽ setup environment. Tin tốt: Tất cả đều miễn phí!
>
> **Bước 1:** Truy cập link này để nhận Gemini API credits:
> `https://trygcp.dev/claim/gdg-mientrung-road-to-devfest-code-1`
>
> *[Share screen - demo flow lấy credit trong 30 giây]*
>
> Hướng dẫn chi tiết ở slide: *[show QR code]*
>
> Mọi người có **3 phút** để claim credit. Ai gặp issue raise hand nhé!"

**Action:**
- Share link in chat
- Show QR code on slide
- Walk around or monitor chat for questions
- Play background music while people setup (optional)

**Timer:** 3 minutes countdown on screen

---

### Slide 5: Open Colab Notebook

**Script:**
> "Giờ mở notebook của chúng ta. Link trong chat: *[paste link]*
>
> Click vào → **Copy to Drive** (góc trên cùng) để bạn có thể edit được.
>
> *[Show screen: Click 'Copy to Drive' button]*
>
> Ai đã copy xong cho tôi một thumbs up 👍 *[Wait for confirmation]*"

**Interactive Check:**
> "Quick check: Mọi người đã thấy cells với code Python chưa? Nếu thấy giao diện trắng hoặc lỗi, Ctrl+F5 refresh lại."

**Action:**
- Paste Colab link: `https://colab.research.google.com/github/.../Building_your_first_Agent_vn.ipynb`
- Wait for majority to confirm (70%+)

---

### Slide 6: Install ADK & Configure

**Script:**
> "Trong notebook, chúng ta sẽ:
> 1. Cài đặt Google ADK: `!pip install -U -q google-adk`
> 2. Configure API key
> 3. Import libraries
>
> **Quan trọng:** Khi chạy cell configure API, paste API key bạn vừa lấy vào.
>
> *[Demo: Click Secrets icon bên trái → Add 'GOOGLE_API_KEY']*
>
> Tip: Dùng Colab Secrets để không bị lộ key khi share notebook."

**Action:**
- Run cells 1-3 trong notebook
- Show output: ✅ Đã import thành công các thư viện ADK!

**Time Check:** 10 minutes elapsed

---

## PART 3: BƯỚC 1 - WEATHER AGENT (20 phút)

### Slide 7: What is an Agent?

**Script:**
> "Trước khi code, clarify khái niệm:
>
> **LLM (như ChatGPT):** Chỉ biết *nói chuyện*. Hỏi 'thời tiết Hà Nội?' → Nó đoán hoặc nói 'tôi không biết'.
>
> **Agent:** LLM + Tools = Can *take actions*.
> Agent có thể:
> - Gọi API để lấy data thực
> - Query database
> - Execute code
> - Control devices
>
> **Formula:**
> `Agent = Model + Instructions + Tools + Description`"

**Visual:** Diagram showing:
```
User Query → Agent (Brain) → Tool (Hands) → Real World
                ↓
           Response
```

---

### Slide 8: Anatomy of a Tool

**Script:**
> "Tool là gì? Rất đơn giản: **Một Python function với docstring tốt.**
>
> Ví dụ tool `get_weather()`:
>
> *[Show code trên slide]*
> ```python
> def get_weather(city: str) -> dict:
>     \"\"\"Lấy thời tiết cho một thành phố.
>
>     Args:
>         city: Tên thành phố
>     Returns:
>         dict: Weather report
>     \"\"\"
> ```
>
> **Điểm quan trọng:** Docstring = 'instruction manual' cho LLM.
> LLM đọc docstring để hiểu:
> - Tool này làm GÌ?
> - KHI NÀO nên dùng?
> - THAM SỐ nào cần truyền?
>
> Docstring tốt = Agent thông minh!"

**Interactive Question:**
> "Câu hỏi: Nếu tôi bỏ docstring đi, agent vẫn gọi được tool không? *[Pause]*
> Trả lời: Được, nhưng LLM sẽ không biết KHI NÀO nên gọi, và truyền GÌ vào params!"

---

### Slide 9: Hands-on - Create Weather Tool

**Script:**
> "Okay, giờ code thật! Scroll xuống cell 'Tool lấy thời tiết'.
>
> Code này đã có sẵn - nhiệm vụ của bạn: **Run cell và quan sát output.**
>
> *[Run cell trên screen share]*
>
> Output sẽ test tool với các thành phố:
> - Hà Nội → ☀️ Success
> - Đà Nẵng → ☀️ Success
> - Unknown Location → ❌ Error handling
>
> Ai thấy colored output giống tôi? 👍"

**Action:**
- Run cell `get_weather` definition
- Show test outputs với colors
- Point out: Tool trả về dict với status/report

**Pause for questions:** "Questions về tool definition?"

---

### Slide 10: Create Weather Agent

**Script:**
> "Giờ tạo Agent - bộ não sẽ điều khiển tool này.
>
> Scroll xuống cell 'Định nghĩa Weather Agent'. Quan sát 5 thành phần:
>
> 1. **name**: 'weather_agent' - ID duy nhất
> 2. **model**: 'gemini-2.5-flash' - LLM nào được dùng
> 3. **description**: Tóm tắt ngắn - dùng cho delegation (sẽ học sau)
> 4. **instruction**: Hướng dẫn chi tiết - 'Khi user hỏi về thời tiết, dùng tool get_weather'
> 5. **tools**: `[get_weather]` - List các tools agent có thể dùng
>
> Run cell này!"

**Action:**
- Run cell create `weather_agent`
- Show output: ✅ Agent 'weather_agent' đã sẵn sàng!

---

### Slide 11: Setup Runner & Session

**Script:**
> "Để chạy agent, cần 2 thứ:
>
> **1. SessionService** - Lưu conversation history
> Giống như 'memory' của agent, nhớ những gì user đã nói.
>
> **2. Runner** - Engine điều phối
> Nhận input từ user → Gọi agent → Execute tools → Return response.
>
> *[Analogy]*: Giống như bạn thuê 1 assistant (agent):
> - SessionService = Notebook ghi chú của assistant
> - Runner = Bạn - người giao task và nhận kết quả
>
> Run cell setup này!"

**Visual:** Diagram:
```
User ←→ Runner ←→ Agent ←→ Tools
              ↓
        SessionService
        (Memory/History)
```

**Action:**
- Run cell setup SessionService + Runner
- Show outputs confirming session created

---

### Slide 12: Test Weather Agent - LIVE!

**Script:**
> "Moment of truth! Chúng ta sẽ chat với agent.
>
> Scroll xuống cell 'Chạy Conversation'. Code này sẽ:
> 1. Hỏi 'Thời tiết ở Hà Nội như thế nào?'
> 2. Hỏi tiếp 'Còn Paris thì sao?'
> 3. Hỏi 'Cho tôi biết thời tiết ở London'
>
> Quan sát workflow:
> - 👤 User query hiển thị màu xanh
> - 🔍 Tool execution log màu cyan
> - 🤖 Agent response màu xanh lá
>
> Ready? 3...2...1...Run! 🚀"

**Action:**
- Run conversation cell
- **Pause at each log** to explain:
  - "Nhìn kìa: Tool 'get_weather' được gọi với city='Hà Nội'"
  - "Agent nhận kết quả, format lại thành response thân thiện"
  - "Conversation history được lưu - nên câu 2 'Còn Paris?' agent vẫn hiểu context"

**Interactive Moment:**
> "Ai muốn test với thành phố khác? Gọi tên thành phố! *[Take 2-3 suggestions, edit code live]*"

**Time Check:** 30 minutes elapsed (including setup)

---

### Slide 13: Coding Challenge

**Script:**
> "Okay, challenge cho các bạn! 💪
>
> **Nhiệm vụ:** Nâng cấp tool `get_weather()` để dùng **real API** thay vì mock data.
>
> API: `https://goweather.xyz/weather/{city}`
> Example: https://goweather.xyz/weather/Danang
>
> **Hints:**
> - Dùng `requests` library: `requests.get(url).json()`
> - Parse response: `{'temperature': '27°C', 'description': 'Partly cloudy'}`
> - Error handling: API có thể return 404
>
> **Time:** 5 phút. Ai làm xong first raise hand! 🏆
>
> Hoặc nếu muốn skip, scroll xuống solution cell."

**Action:**
- Set 5-minute timer on screen
- Monitor chat for questions
- Prepare to show solution after timer

**Optional:** Offer small prize for first completion (GDG sticker, etc.)

**Solution reveal:**
```python
import requests

def get_weather(city: str) -> dict:
    try:
        url = f"https://goweather.xyz/weather/{city}"
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()
        return {
            "status": "success",
            "report": f"🌤️ {city}: {data['temperature']}, {data['description']}"
        }
    except Exception as e:
        return {"status": "error", "error_message": str(e)}
```

---

## PART 4: BƯỚC 2 - MULTI-AGENT TEAM (20 phút)

### Slide 14: Why Multi-Agent?

**Script:**
> "Câu hỏi: Nếu bạn build một ứng dụng phức tạp - vừa weather, vừa calendar, vừa email, vừa search... bạn sẽ nhét TẤT CẢ tools vào một agent?
>
> *[Pause for thought]*
>
> **Vấn đề với 'God Agent':**
> - ❌ Instructions quá dài → LLM confused
> - ❌ Khó debug khi có lỗi
> - ❌ Không scale được
> - ❌ Mỗi task cần model khác nhau (translation cần multilingual model, code cần code-optimized model)
>
> **Giải pháp: Agent Team!**
>
> Giống như startup: CEO (root agent) delegate tasks cho specialists (sub-agents):
> - Marketing Agent
> - Finance Agent
> - Tech Agent
>
> Mỗi agent chuyên sâu một việc → Hiệu quả hơn!"

**Visual:**
- Slide 1: Single agent với 20 tools (messy diagram)
- Slide 2: Root agent + 4 sub-agents, mỗi agent có 5 tools (clean diagram)

---

### Slide 15: Multi-Agent Architecture

**Script:**
> "Hôm nay chúng ta sẽ mở rộng Weather Agent thành một team:
>
> ```
> Root Agent (weather_agent_v2)
>     ├── Greeting Agent → say_hello()
>     ├── Weather capability → get_weather()
>     └── Farewell Agent → say_goodbye()
> ```
>
> **Automatic Delegation Magic:**
> User: 'Xin chào!'
> → Root agent đọc descriptions của sub-agents
> → Thấy 'Greeting Agent xử lý greetings'
> → Tự động delegate
> → Greeting Agent execute `say_hello()`
> → Return result
>
> **Không cần if-else logic!** LLM tự quyết định delegation dựa trên `description`."

**Interactive Question:**
> "Đoán xem: Nếu user nói 'Xin chào! Thời tiết Hà Nội thế nào?', agent sẽ xử lý như thế nào?
>
> *[Wait for answers in chat]*
>
> A) Chỉ chào
> B) Chỉ weather
> C) Cả hai
> D) Error
>
> *[Reveal: C - LLM đủ thông minh để handle multi-intent query!]*"

---

### Slide 16: Create Sub-Agents

**Script:**
> "Tạo specialized tools trước. Scroll xuống cell 'Tools cho Greeting và Farewell':
>
> ```python
> def say_hello(name: Optional[str] = None) -> str:
>     \"\"\"Cung cấp lời chào thân thiện\"\"\"
>
> def say_goodbye() -> str:
>     \"\"\"Cung cấp message tạm biệt\"\"\"
> ```
>
> Simple nhưng đủ để demo delegation. Run cell test!"

**Action:**
- Run cell define tools
- Show test outputs

---

### Slide 17: Create Sub-Agents (cont.)

**Script:**
> "Giờ tạo 2 sub-agents. Cell 'Định nghĩa Sub-Agents':
>
> **Greeting Agent:**
> - description: 'Xử lý greetings sử dụng say_hello'
> - instruction: 'Nhiệm vụ DUY NHẤT: Chào hỏi. KHÔNG làm gì khác.'
>
> **Farewell Agent:**
> - description: 'Xử lý farewells sử dụng say_goodbye'
> - instruction: 'Nhiệm vụ DUY NHẤT: Tạm biệt. KHÔNG làm gì khác.'
>
> **Chìa khóa delegation: `description` phải RÕ RÀNG, NGẮN GỌN!**
>
> Run cell!"

**Action:**
- Run cell create sub-agents
- Show output confirmations

---

### Slide 18: Create Root Agent with Sub-Agents

**Script:**
> "Bước cuối: Tạo root agent điều phối team.
>
> Cell 'Định nghĩa Root Agent với Sub-Agents':
>
> Key line:
> ```python
> sub_agents=[greeting_agent, farewell_agent]
> ```
>
> Root agent giữ lại tool `get_weather` cho weather requests, nhưng delegate greetings/farewells.
>
> Instruction của root agent chỉ rõ:
> - 'Greeting? → delegate greeting_agent'
> - 'Farewell? → delegate farewell_agent'
> - 'Weather? → tự xử lý'
>
> Run!"

**Action:**
- Run cell create root agent
- Show sub-agent list in output

---

### Slide 19: Test Agent Team - LIVE DEMO

**Script:**
> "Giờ test magic! Cell 'Test Agent Team':
>
> 3 queries:
> 1. 'Xin chào!' → Expect: greeting_agent
> 2. 'Thời tiết ở Đà Nẵng?' → Expect: root agent
> 3. 'Cảm ơn, tạm biệt!' → Expect: farewell_agent
>
> Watch cho delegation logs! Ready? Run! 🎬"

**Action:**
- Run test cell
- **Pause after each query:**
  - "Query 1: Nhìn log - 🔔 say_hello được gọi! Delegation thành công!"
  - "Query 2: get_weather được gọi - root agent tự xử lý"
  - "Query 3: say_goodbye được gọi - farewell_agent activate!"

**Interactive Question:**
> "Ai thấy delegation logs rõ ràng? 👍
> Có ai thấy agent bị confused hoặc gọi sai tool không? *[Debug nếu có issues]*"

**Time Check:** 50 minutes elapsed

---

### Slide 20: Key Takeaways - Multi-Agent

**Script:**
> "Điểm chính từ phần này:
>
> ✅ **Separation of Concerns:** Mỗi agent một trách nhiệm → Dễ maintain
> ✅ **Automatic Delegation:** LLM tự routing dựa trên `description`
> ✅ **Scalability:** Thêm capability = thêm sub-agent, không cần refactor root
> ✅ **Flexibility:** Sub-agents có thể dùng models khác nhau (multilingual, code-specific, etc.)
>
> **Real-world use case:**
> Customer support bot:
> - FAQ Agent (simple responses)
> - Technical Support Agent (access docs, create tickets)
> - Escalation Agent (transfer to human)
> - Sentiment Analysis Agent (detect angry customers)
>
> Root agent orchestrates based on user query!"

**Visual:** Diagram of customer support multi-agent system

---

## PART 5: BƯỚC 3 - ADK STARTER PACK (25 phút)

### Slide 21: From Notebook to Production

**Script:**
> "Okay, bạn đã build agents trong Colab. Nhưng câu hỏi:
>
> **Làm sao để users thực sự dùng agent của bạn?**
>
> Bạn không thể bảo họ: 'Mở Colab, run cell 1, 2, 3, paste API key...' 😅
>
> Bạn cần:
> - ✅ Web UI để chat
> - ✅ Backend API
> - ✅ Database cho sessions
> - ✅ Authentication
> - ✅ Deployment setup
>
> Tự build từ đầu? → 2-3 ngày.
>
> **ADK Starter Pack? → 5 phút!** 🚀"

---

### Slide 22: What is ADK Starter Pack?

**Script:**
> "ADK Starter Pack = Boilerplate fullstack app cho agent applications.
>
> Bao gồm:
> - 🏗️ **Backend:** FastAPI + ADK agents + session management
> - 🎨 **Frontend:** React + Vite + modern UI components
> - 🔧 **DevOps:** Docker, Makefile, environment configs
> - 📦 **Examples:** Sample agents để học
>
> **Templates available:**
> - gemini-fullstack (we'll use this)
> - gemini-simple
> - multi-agent-chat
>
> Giống như Create React App, nhưng cho AI agents!"

**Visual:** Screenshot of running fullstack app (chat UI + agent response)

---

### Slide 23: Installation - Option 1 (Recommended)

**Script:**
> "2 cách install:
>
> **Option 1: uvx (recommended)**
> ```bash
> uvx agent-starter-pack create my-agent
> # Choose: gemini-fullstack
> ```
>
> uvx = như npx, tự động download + run latest version.
>
> **Option 2: Git clone**
> ```bash
> git clone https://github.com/GoogleCloudPlatform/agent-starter-pack
> ```
>
> Vì Colab không support uvx tốt, hôm nay tôi sẽ demo bằng **Cloud Shell**."

**Action:**
- Switch to Cloud Shell tab (pre-opened)
- OR use local terminal if on laptop

---

### Slide 24: Live Demo - Create Project

**Script:**
> "Okay, watch me create project real-time! *[Share screen: Terminal]*
>
> ```bash
> $ uvx agent-starter-pack create devfest-agent
> ```
>
> *[Wait for prompts]*
>
> Select template: `gemini-fullstack` ← Arrow down + Enter
>
> *[Wait for installation - explain while waiting]*
>
> Nó đang:
> - Clone template
> - Setup directory structure
> - Install Python dependencies (ADK, FastAPI, etc.)
> - Setup frontend (React, Vite, TailwindCSS)
>
> Takes ~30 seconds..."

**Action:**
- Run command
- Show directory structure: `cd devfest-agent && tree -L 2`

---

### Slide 25: Project Structure Walkthrough

**Script:**
> "Explore structure:
>
> ```
> devfest-agent/
> ├── app/
> │   ├── agents/          ← Agent definitions (Python)
> │   ├── tools/           ← Tool functions
> │   ├── main.py          ← FastAPI backend
> │   └── .env             ← Environment config (API keys)
> ├── frontend/
> │   ├── src/
> │   │   ├── components/  ← React components
> │   │   └── App.tsx      ← Main app
> │   └── package.json
> └── Makefile             ← Dev commands
> ```
>
> **Separation of concerns:**
> - Backend (Python/ADK) handles agent logic
> - Frontend (React) handles UI/UX
> - Makefile simplifies commands (make dev, make build, etc.)"

**Action:**
- Open file explorer
- Show key files: `app/agents/agent.py`, `frontend/src/App.tsx`

---

### Slide 26: Configure Environment

**Script:**
> "Before running, configure API key.
>
> Create `app/.env`:
> ```env
> GOOGLE_GENAI_USE_VERTEXAI=0
> GOOGLE_API_KEY=your_api_key_here
> ```
>
> Replace `your_api_key_here` với key bạn lấy lúc đầu workshop.
>
> **Pro tip:** Không commit .env vào git! (Đã có trong .gitignore)"

**Action:**
- Create .env file
- Paste API key (blur on screen!)
- Show .gitignore includes `.env`

---

### Slide 27: Run the App!

**Script:**
> "Commands to run:
>
> ```bash
> make install  # Install all dependencies (backend + frontend)
> make dev      # Run both servers
> ```
>
> *[Run make install]*
>
> Chờ ~1 minute để install packages...
>
> *[After install completes]*
>
> ```bash
> make dev
> ```
>
> Hai servers sẽ chạy:
> - Backend: http://localhost:8000
> - Frontend: http://localhost:5173
>
> *[Wait for servers to start]*
>
> Let's open frontend!"

**Action:**
- Run commands
- Open browser to localhost:5173
- Show chat interface

---

### Slide 28: Live Interaction with Fullstack Agent

**Script:**
> "Đây rồi - một chat interface hoàn chỉnh! *[Show UI]*
>
> Mình sẽ chat với agent:
>
> *[Type]* 'Hello! What can you do?'
>
> *[Wait for response]*
>
> Agent responds với description của capabilities.
>
> *[Type]* 'What's the weather in Hanoi?'
>
> *[Show response - should indicate weather functionality]*
>
> Điểm hay:
> - ✅ Streaming responses (type hiệu ứng)
> - ✅ Chat history preserved
> - ✅ Error handling UI
> - ✅ Mobile responsive (resize browser to show)
>
> **All of this in 5 minutes setup!**"

**Action:**
- Demo 2-3 interactions
- Show network tab (API calls to backend)
- Show backend logs in terminal

---

### Slide 29: Customize Agent for Your Use Case

**Script:**
> "Bây giờ customize! Mở `app/agents/agent.py`:
>
> *[Show code]*
>
> ```python
> agent = Agent(
>     name='my_agent',
>     model='gemini-2.5-flash',
>     instruction='...',  # ← Change this
>     tools=[...]          # ← Add your tools
> )
> ```
>
> **Exercise:** Replace với weather agent từ Bước 1!
>
> 1. Copy `get_weather` tool → `app/tools/weather.py`
> 2. Import tool in `agent.py`
> 3. Add to agent tools list
> 4. Update instruction
> 5. Restart: `Ctrl+C` → `make dev`
>
> Ai muốn thử? *[If time allows, do it live]*"

**Action:**
- Show file editing
- Copy-paste weather tool
- Update agent.py
- Restart servers
- Test in UI

---

### Slide 30: Deployment Options

**Script:**
> "Khi ready để deploy production:
>
> **Backend options:**
> - Google Cloud Run (recommended for Gemini)
> - Vercel
> - Railway
> - Any Docker host
>
> **Frontend options:**
> - Vercel (easiest)
> - Netlify
> - GitHub Pages (static)
>
> **Database:**
> Starter Pack dùng InMemorySession → sessions mất khi restart.
> Production: Dùng Firebase, PostgreSQL, etc.
>
> *[Show deployment guide in README.md]*
>
> Makefile có commands: `make build`, `make docker`, v.v."

**Visual:** Slide với logos: Cloud Run, Vercel, Railway

**Time Check:** 75 minutes elapsed

---

## PART 6: BONUS - HACKATHON TOOLKIT (15 phút)

### Slide 31: From Agent to Hackathon Win

**Script:**
> "Okay, bạn đã biết build agents. Nhưng trong hackathon:
>
> **Challenges:**
> - ❌ Ý tưởng hay nhưng scope quá rộng
> - ❌ Mất thời gian vào features không quan trọng
> - ❌ Pitch không thuyết phục judges
> - ❌ Demo bị bugs last minute
>
> **Solution:** Dùng agents để ACCELERATE workflow!
>
> 2 bonus agents:
> 1. 📋 **MVP Planning Agent** → Idea to actionable brief
> 2. 🎤 **Pitch Generator Agent** → Create irresistible pitch
>
> Workflow:
> ```
> Ý tưởng → MVP Planner → Project Brief → AI Studio → App
>                                          ↓
>                         Pitch Generator → Landing Page
> ```"

**Visual:** Flowchart diagram

---

### Slide 32: MVP Planning Agent

**Script:**
> "**Vấn đề:** Bạn có ý tưởng 'AI-powered study buddy app' - tính năng gì nên build?
>
> ❌ **Sai lầm thường gặp:**
> - Video call integration
> - AI tutor chatbot
> - Gamification với points
> - Social network features
> - Calendar sync
> - Payment system
>
> → Quá nhiều! Hackathon 24h làm sao xong?
>
> ✅ **MVP Planning Agent giúp:**
> 1. User empathy analysis → Hiểu pain point thực sự
> 2. Feature brainstorm
> 3. Prioritize theo MoSCoW (Must/Should/Could/Won't)
> 4. Shortlist 3-5 core features
> 5. Generate project brief
>
> Output: Markdown document → paste vào AI Studio → App generated! 🚀"

---

### Slide 33: Live Demo - MVP Planning Agent

**Script:**
> "Test với ý tưởng: 'Study Buddy AI'
>
> *[Scroll to MVP Planning cell in notebook]*
>
> Input:
> ```
> Ứng dụng AI giúp sinh viên tìm study partners dựa trên:
> - Learning style
> - Subject/major
> - Schedule
> - Goals
> ```
>
> *[Run cell]*
>
> Agent analysis:
> - Target users: University students
> - Pain point: Học một mình ineffective, khó tìm partner compatible
> - Must-have features:
>   1. Profile creation (learning style quiz)
>   2. AI matching algorithm
>   3. Chat interface to connect
> - Won't-have (for MVP): Video call, payments, gamification
>
> Brief generated: *[Show markdown output]*"

**Action:**
- Run MVP planning agent cell
- Scroll through output
- Highlight project brief section

---

### Slide 34: Use Brief with AI Studio Apps

**Script:**
> "Giờ magic trick! 🪄
>
> 1. Copy brief từ agent
> 2. Open https://aistudio.google.com/apps
> 3. Paste brief vào prompt
> 4. Click 'Generate'
>
> *[Demo on screen]*
>
> AI Studio sẽ tự động generate:
> - React components
> - UI layout
> - API endpoints
> - Sample data
> - Styling
>
> 30 giây → Hoàn chỉnh app template!
>
> **Alternative builders:**
> - WebSim.ai (instant prototypes)
> - Builder.io (visual-first)
> - Replit (full IDE)"

**Action:**
- Switch to AI Studio tab
- Paste brief
- Show generated app preview
- Click through components

---

### Slide 35: Pitch Generator Agent

**Script:**
> "Bạn đã có MVP. Giờ thuyết phục judges!
>
> **4 Pillars of Winning Pitches:**
>
> 1. 🎯 **Extreme Clarity** - Judges hiểu ngay trong 10 giây
>    Format: '[Product] helps [User] do [Action] in [Timeframe]'
>
> 2. 💎 **Obvious Value** - ROI rõ ràng, không cần giải thích
>    Bad: 'Our app is innovative'
>    Good: 'Save students 5 hours/week finding study partners'
>
> 3. ⚡ **Low Friction** - Demo mượt, judges dễ imagine adoption
>    No bugs visible, clear user flow
>
> 4. 📦 **Smart Packaging** - Every slide có purpose
>    Hook → Problem → Solution → Traction → Ask (135 seconds total)
>
> **Pitch Generator Agent** creates deck theo framework này!"

**Visual:** Slide showing 4 pillars with examples

---

### Slide 36: Live Demo - Pitch Generator

**Script:**
> "Test với 'Study Buddy AI':
>
> *[Run Pitch Generator cell]*
>
> Input: Project description + target audience
>
> Agent generates:
> - **Hook:** 'Imagine never studying alone for a failed exam again...'
> - **Problem:** '68% students struggle to find compatible study partners'
> - **Solution:** 'Study Buddy AI matches you in 60 seconds based on learning DNA'
> - **Traction:** 'MVP tested with 50 students, 4.8/5 rating'
> - **Ask:** 'Join our beta program at studybuddy.ai'
>
> Pitch content: *[Show output]*
>
> Timing notes included: 15s hook, 30s problem, etc."

**Action:**
- Run pitch generator cell
- Scroll through generated pitch
- Point out timing allocations

---

### Slide 37: Pitch to Landing Page

**Script:**
> "Final magic: Pitch → Landing page
>
> 1. Copy pitch output
> 2. Open Gemini (or Claude)
> 3. Prompt:
>
> ```
> Create a modern HTML landing page for this hackathon project.
> Use Tailwind CSS, hero section, problem-solution sections,
> demo video placeholder, CTA buttons.
>
> [PASTE PITCH CONTENT]
> ```
>
> *[Show Gemini generating HTML]*
>
> 4. Download HTML
> 5. Deploy to Vercel/Netlify (1-click)
>
> **Result:** Professional landing page in 2 minutes! 🎨"

**Action:**
- Paste in Gemini
- Show generated HTML preview
- Mention deployment options

**Time Check:** 85 minutes elapsed

---

## PART 7: WRAP-UP & CHALLENGE (5 phút)

### Slide 38: What We Covered

**Script:**
> "Trong 90 phút, bạn đã:
>
> ✅ **Bước 1:** Build single agent với tools (Weather Bot)
> ✅ **Bước 2:** Multi-agent team với delegation
> ✅ **Bước 3:** Fullstack app với ADK Starter Pack
> ✅ **Bonus 1:** MVP Planning workflow
> ✅ **Bonus 2:** Pitch generation
>
> **From zero to production-ready agent app!**
>
> Điều quan trọng nhất: Bạn hiểu được **thinking process**:
> - Khi nào cần tools vs chỉ LLM
> - Khi nào dùng single vs multi-agent
> - Cách structure project cho scale
> - Workflow từ idea → MVP → pitch"

---

### Slide 39: Vibe Coding Challenge

**Script:**
> "Final challenge! 💪
>
> **Nhiệm vụ:**
> 1. Chọn 1 ý tưởng hackathon (hoặc dùng ý tưởng sẵn)
> 2. Run qua MVP Planning Agent
> 3. Generate app với AI Studio/WebSim
> 4. Create pitch với Pitch Generator
> 5. Deploy landing page
>
> **Deadline:** End of hackathon event!
>
> **Prize:** Best project wins:
> - GDG merch
> - Feature trên GDG social
> - Potential mentorship
>
> Share link project trong Discord/Telegram group!
>
> Tag: #GDGDevFest #ADKAgents #VibeCoding"

**Visual:** QR code to submission form

---

### Slide 40: Key Quote

**Script:**
> "Trước khi kết thúc, remember this:
>
> > **'Công việc của bạn không còn là viết mã nữa. Công việc của bạn là viết nên câu chuyện — cái WHY và WHAT — thật rõ ràng để AI sẽ lo phần HOW.'**
>
> Trong thời đại AI:
> - Bạn là **orchestrator**, không phải coder
> - Bạn là **storyteller**, không phải implementer
> - Bạn là **architect**, không phải builder
>
> Focus on outcomes, not outputs. Focus on problems, not solutions.
>
> AI handles the HOW. You define the WHY."

**Visual:** Quote displayed prominently

---

### Slide 41: Resources & Stay Connected

**Script:**
> "Resources cho bạn:
>
> **Docs:**
> - ADK GitHub: github.com/google/adk-python
> - Starter Pack: github.com/GoogleCloudPlatform/agent-starter-pack
> - Gemini API: aistudio.google.com
>
> **Community:**
> - GDG Miền Trung: facebook.com/Gdgmientrung
> - Workshop repo: *[Show link]*
> - Feedback form: *[Show QR code]*
>
> **Next steps:**
> - Explore MCP servers (Model Context Protocol)
> - Build with Gemini 2.0 Flash Thinking Mode
> - Contribute to ADK community
>
> Stay in touch! Connect on LinkedIn/Twitter: @chitoan1992"

**Visual:**
- QR codes for resources
- Social media handles
- Community links

---

### Slide 42: Q&A

**Script:**
> "Câu hỏi? 🙋
>
> Một số câu hỏi hay mình dự đoán:
>
> **Q: ADK vs LangChain - khi nào dùng gì?**
> A: ADK nếu dùng Gemini + cần multi-agent. LangChain nếu multi-model hoặc complex chains.
>
> **Q: Chi phí API như thế nào?**
> A: Gemini Flash rất rẻ (~$0.075/1M tokens). Credit hôm nay đủ build vài projects.
>
> **Q: Production considerations?**
> A: Rate limiting, caching, database sessions, monitoring, error handling.
>
> **Q: Support tiếng Việt không?**
> A: Yes! Gemini multilingual. Instructions và tools có thể full tiếng Việt.
>
> Câu hỏi khác?"

**Action:**
- Take 5-10 questions
- Note questions for FAQ doc
- Share contact for follow-ups

---

### Slide 43: Thank You!

**Script:**
> "Cảm ơn mọi người đã tham gia! 🙏
>
> Remember:
> - Notebook: *[Link in chat]*
> - Feedback: *[QR code]*
> - Challenge submission: *[Link]*
>
> Chúc các bạn thành công trong hackathon!
>
> Go build something amazing! 🚀
>
> *[Play outro music, show contact info slide while people leave]*"

**Visual:**
- Thank you graphic
- GDG DevFest logo
- Contact information
- Event hashtags

---

## 📝 Interactive Questions Throughout Workshop

### Strategic Pauses for Engagement:

**Every 15 minutes:**
- "Quick check: Ai đang theo kịp? 👍 Ai cần tôi slow down? 🙋"
- "Questions so far? Không hiểu gì cứ hỏi nhé!"

**After each major section:**
- "5-second break - stretch, grab water, questions in chat!"

**Interactive Polls (use Slido or show of hands):**

1. **Before Bước 1:**
   "Poll: Bạn đã bao giờ dùng LLM API chưa?
   A) Yes, nhiều lần
   B) Yes, vài lần
   C) Chưa bao giờ"

2. **Before Multi-Agent:**
   "Poll: Theo bạn, app nào cần multi-agent?
   A) Simple chatbot
   B) Customer support system
   C) Calculator
   D) Complex automation platform"

3. **Before Bonus:**
   "Poll: Trong hackathon, bạn thường struggle với?
   A) Ý tưởng
   B) Implementation
   C) Pitch/presentation
   D) Time management"

---

## 💡 Tips for Delivery

### Energy Management:
- **High energy:** Introduction, demos, challenge reveals
- **Moderate:** Technical explanations, code walkthroughs
- **Interactive:** Q&A, polls, hands-on coding

### Backup Plans:
1. **If live coding fails:** Pre-recorded demo video ready
2. **If API issues:** Screenshots of expected outputs
3. **If ahead of schedule:** Deep dive into one student's idea
4. **If behind schedule:** Skip Bonus 2, focus on core 3 steps

### Engagement Tactics:
- **Call on specific people:** "Hey [name], what do you think?"
- **Real-world examples:** Relate to apps students use (Zalo, Grab, etc.)
- **Humor:** Light jokes about bugs, AI hallucinations
- **Stories:** Share your hackathon experiences

### Visual Aids:
- Code snippets với syntax highlighting
- Diagrams cho architecture
- Before/After screenshots
- GIFs cho workflows

---

## 🎤 Speaking Notes - Tone & Style

**Tone:**
- Enthusiastic but not over-the-top
- Technical but accessible
- Confident but humble ("I'm learning too!")

**Avoid:**
- Jargon without explanation
- Going too fast on code
- Assuming everyone knows concepts
- Being condescending to beginners

**Encourage:**
- Questions anytime
- Experimentation
- Mistakes as learning
- Sharing discoveries

---

## ✅ Pre-Workshop Checklist

**24 hours before:**
- [ ] Test full notebook end-to-end
- [ ] Confirm API credits available
- [ ] Prepare backup demos
- [ ] Print QR codes for resources
- [ ] Test screen sharing setup

**1 hour before:**
- [ ] Load all tabs (Colab, AI Studio, Cloud Shell, etc.)
- [ ] Test microphone & camera
- [ ] Join event Discord/chat
- [ ] Have water ready
- [ ] Set phone to silent

**During workshop:**
- [ ] Monitor chat for questions
- [ ] Watch time every 10 minutes
- [ ] Adjust pace based on audience
- [ ] Encourage hands-up for help

---

This plan provides comprehensive coverage while maintaining flexibility to adapt based on audience engagement and time constraints. Good luck with the workshop! 🚀
