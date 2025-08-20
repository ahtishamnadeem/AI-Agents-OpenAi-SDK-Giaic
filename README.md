# 🎯 Multi-Agent AI Projects

This repository contains three specialized **AI Agents** built with the OpenAI/Gemini Agent SDK and Chainlit.  
Each project demonstrates how to design and run domain-specific agents with **handoffs, tools, and interactive chat**.

---

## 📌 Projects Included

### 1. Career Mentor Agent 🎓
A multi-agent AI system that guides students through **career exploration** using specialized agents and intelligent handoffs.

**Features:**
- Career recommendations based on interests  
- Skill roadmaps with the custom tool `get_career_roadmap()`  
- Handoff between specialized agents:
  - **CareerAgent** – suggests fields  
  - **SkillAgent** – generates learning roadmaps  
  - **JobAgent** – shares real-world job roles and advice  

**Supported Fields:**
- Software Engineering  
- Data Science  
- Medicine  
- General/Custom paths  

---

### 2. Game Master Agent 🎮
An interactive AI **game facilitator** that creates and manages text-based adventures.  

**Features:**
- Dynamic story generation  
- Branching choices for players  
- Maintains context across sessions  
- Can simulate NPCs and plot twists  

---

### 3. Travel Agent ✈️
An AI assistant for **planning trips** and exploring destinations.  

**Features:**
- Destination recommendations  
- Activity suggestions  
- Travel itineraries and budgets  
- Multi-step conversations for refining plans  

---

## ⚙️ Technology Stack

- **Python 3.13+**  
- **Chainlit** – chat UI & session management  
- **OpenAI Agent SDK / Gemini API** – LLM-powered agent framework  
- **Custom Tools** – e.g., career roadmap generator  

---

## 🚀 Setup & Run

For each project (`Career_Mentor-Agent`, `Game-Master-Agent`, `Travel-Agent`):

1. **Navigate to the project folder**:
   ```bash
   cd Project-Name
Install dependencies:

bash
Copy
Edit
uv sync
Create .env file with your Gemini API key:

env
Copy
Edit
GEMINI_API_KEY=your_api_key_here
Run the project:

bash
Copy
Edit
chainlit run main.py
🧪 Testing
Start the Chainlit app in the browser (default: http://localhost:8000).

Begin a chat with the agent.

Try different use cases:

Career guidance → Career Mentor Agent

Play a text-based adventure → Game Master Agent

Plan a trip → Travel Agent

📂 Repository Structure
css
Copy
Edit
Practice-Agents-main/
├── Career_Mentor-Agent/
├── Game-Master-Agent/
└── Travel-Agent/
Each folder contains:

main.py – entry point with agent logic

pyproject.toml – project dependencies

chainlit.md – welcome screen

.env – environment variables (to be created)

👨‍💻 Developer
Developed with ❤️ by CodeWithAhtii