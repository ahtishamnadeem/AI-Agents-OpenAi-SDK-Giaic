# 🎓 Smart Student Agent 🤖

Smart Student Agent is an **AI-powered academic assistant** designed to help students learn more effectively.  
It leverages **Google Gemini API** and **Chainlit** to provide an interactive chat interface for students.  

---

## 🚀 Features
- ✅ Answer **academic questions** instantly  
- ✅ Provide **effective study tips** for any topic  
- ✅ Summarize **long passages** into short and clear explanations  
- ✅ Runs locally with **Chainlit web UI**  
- ✅ Easy to extend with custom tools  

---

## 🛠️ Tech Stack
- **Python 3.10+**
- **Chainlit** (chat interface)
- **Google Gemini API**
- **Dotenv** (for environment variables)

---

## 📂 Project Structure
```
Smart_Student_Agent/
│── agents.py            # Core Agent logic and Runner class
│── student_agent.py     # Chainlit app, tools, and Gemini integration
│── .env                 # API keys and environment variables
│── requirements.txt     # Dependencies
│── README.md            # Project documentation
└── .gitignore           # Ignored files
```

---

## ⚙️ Installation & Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/Smart_Student_Agent.git
   cd Smart_Student_Agent
   ```

2. **Create a virtual environment (recommended)**
   ```bash
   python -m venv .venv
   source .venv/bin/activate   # On Mac/Linux
   .venv\Scripts\activate      # On Windows
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Setup your environment variables**  
   Create a `.env` file in the root folder and add:
   ```
   GOOGLE_API_KEY=your_api_key_here
   ```

---

## ▶️ Running the App
Run the app using Chainlit:

```bash
chainlit run student_agent.py -w
```

Now open [http://localhost:8000](http://localhost:8000) in your browser 🎉  

---

## 📸 Preview
*(You can add screenshots or a demo GIF here later)*

---

## 📌 Future Improvements
- Add voice-based input/output 🎤  
- Save past conversations 💾  
- More subject-specific tools (Math solver, Code explainer, etc.)  

---

## 👨‍💻 Author
Created by **[CodeWithAhtii](https://github.com/ahtishamnadeem)** ✨
