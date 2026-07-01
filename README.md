# 🌍 Tripio AI – Multi-Agent Travel Planner

> An AI-powered travel planning assistant that generates complete travel plans, including flight search, hotel recommendations, and personalized itineraries using a Multi-Agent Architecture built with LangGraph and FastAPI.

---

## ✨ Features

- ✈️ Intelligent Flight Search
- 🏨 AI-Powered Hotel Recommendations
- 🗺️ Personalized Travel Itinerary Generation
- 🤖 Multi-Agent Workflow using LangGraph
- 💬 Natural Language Travel Planning
- 💾 Persistent Conversation Memory with PostgreSQL
- ⚡ FastAPI Backend
- 🎨 Modern Responsive Web Interface
- 🔎 Web Search Integration using Tavily
- 🌐 Flight Data using AviationStack API

---

# 📸 Demo

> **Home Page**

<p align="center">
  <img src="images/home.png" width="900">
</p>

> **Generated Travel Plan**

<p align="center">
  <img src="images/result.png" width="900">
</p>

*(Add screenshots after creating an `images` folder.)*

---

# 🏗️ Architecture

```text
                        User
                          │
                          ▼
                   FastAPI Backend
                          │
                          ▼
                 LangGraph Workflow
                          │
      ┌───────────────────┼───────────────────┐
      ▼                   ▼                   ▼
 Flight Agent        Hotel Agent       Itinerary Agent
      │                   │                   │
      └───────────────┬───┴───────────────────┘
                      ▼
             Large Language Model (Groq)
                      │
      ┌───────────────┼────────────────┐
      ▼               ▼                ▼
 AviationStack     Tavily Search    PostgreSQL
     API              API          (Checkpointing)
```

---

# 🛠️ Tech Stack

| Category | Technologies |
|----------|--------------|
| Backend | FastAPI |
| AI Framework | LangGraph |
| LLM | Groq (Llama 3.3 70B) |
| Database | PostgreSQL (Supabase) |
| Flight API | AviationStack |
| Search API | Tavily |
| Frontend | HTML, CSS, JavaScript |
| Language | Python 3.11 |

---

# 🚀 How It Works

1. User enters a travel request.
2. FastAPI receives the request.
3. LangGraph coordinates multiple AI agents.
4. Flight Agent searches available flights.
5. Hotel Agent finds suitable hotels.
6. Itinerary Agent creates a personalized travel schedule.
7. Results are combined and returned to the user.

---

# 📂 Project Structure

```text
Tripio/
│
├── static/
│   ├── style.css
│   └── script.js
│
├── templates/
│   └── index.html
│
├── tools/
│   ├── flight_tool.py
│   └── tavily_tool.py
│
├── app.py
├── backend.py
├── requirements.txt
├── .env.example
└── README.md
```

---

# ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/SathvikChoutapally/Tripio-AI-Multi-Agent-Travel-Planner.git
```

Move into the project

```bash
cd Tripio-AI-Multi-Agent-Travel-Planner
```

Create a virtual environment

```bash
python -m venv .venv
```

Activate it

### Windows

```bash
.venv\Scripts\activate
```

### Linux / macOS

```bash
source .venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Create a `.env` file using `.env.example`

Run the application

```bash
python app.py
```

Open

```
http://127.0.0.1:8000
```

---

# 🔑 Environment Variables

Create a `.env` file

```env
GROQ_API_KEY=

TAVILY_API_KEY=

AVIATIONSTACK_API_KEY=

DATABASE_URL=

DEFAULT_ORIGIN_IATA=HYD
```

---

# 🌟 Future Improvements

- User Authentication
- Interactive Maps Integration
- Weather Forecast
- Budget Optimization
- Currency Conversion
- Travel Expense Tracker
- PDF Itinerary Download
- Email Trip Plans
- Voice-based Travel Planning
- Real-time Flight Tracking

---

# 📈 Skills Demonstrated

- Multi-Agent AI Systems
- Prompt Engineering
- FastAPI Development
- REST API Design
- LangGraph
- PostgreSQL Integration
- AI Workflow Orchestration
- External API Integration
- Frontend Development
- Python Backend Development

---

# 🤝 Contributing

Contributions are welcome!

1. Fork the repository
2. Create a feature branch

```bash
git checkout -b feature-name
```

3. Commit changes

```bash
git commit -m "Added new feature"
```

4. Push

```bash
git push origin feature-name
```

5. Create a Pull Request

---

# 📄 License

This project is licensed under the MIT License.

---

# 👨‍💻 Author

**Sathvik Choutapally**

GitHub:
https://github.com/SathvikChoutapally

---

## ⭐ If you found this project useful, consider giving it a star!
