 🤖 WhiteGPT — AI Chatbot for Discord & Web

**WhiteGPT** is a full-stack AI conversational assistant built in **Python** using **Flask & Discord.py**, powered by **Together AI** open models like `DeepSeek-V3`.

It's hosted 24/7 on **Render.com** with both a **modern web chat UI** and support for **Discord replies** using the same model.


## 🌐 Live Chat URL

👉 https://whitegpt-bot-6b68.onrender.com/

Use the web chat with:
✅ Typing animation  
✅ Chat bubbles  
✅ Instant responses  
✅ Reset button  
✅ Seamless design (Mobile + Desktop)



 ✨ Features

- 🤖 Mention the bot on Discord (`@WhiteGPT`) and get GPT answers instantly
- 💬 Ask questions via the web UI (Flask, styled chat window)
- 💡 Powered by Together AI (`deepseek-v3`) and HuggingFace-like chat flow
- 🔁 Reset button clears chat interface
- 💾 All messages stored in `chatlogs.json` with timestamps
- 🚀 Hosted FREE on [Render](https://render.com) — no Replit restarts needed



🔧 Tech Stack

 -Layer       | Tech                         
--------------|------------------------------|
  Backend     | Python, Flask                
  Web UI      | HTML, CSS, JS (no frontend lib) 
  Bot Engine  | discord.py                   
  AI Models   | Together AI (`DeepSeek-V3`)  
  Deployment  | Render.com                   
  Storage     | `chatlogs.json` (per session logging) 



 🛠 Setup Instructions

 1. Clone Repo

```bash
git clone https://github.com/HarshitPandey-2021/WhiteGPT-BOT.git
cd WhiteGPT-BOT
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Add Environment Variables

Create `.env` locally or set in Render:

```
SECRET_KEY = your_discord_token
TOGETHER_API_KEY = your_together_api_key
```

### 4. Run Locally

```bash
python3 main.py
```


## 📁 File Structure


whitegpt-bot/
├── main.py           # Discord bot + keepalive trigger
├── keepalive.py      # Flask server, chat endpoint, logging
├── templates/
│   └── index.html    # Styled web UI (auto responsive)
├── chatlogs.json     # Logs user + GPT replies (timestamped)
├── requirements.txt
└── README.md         # You're reading it!




## 👨‍💻 Author

Made with ❤️ by **Harshit Pandey**  
GitHub → [@HarshitPandey-2021](https://github.com/HarshitPandey-2021)


## 🪪 License

MIT License — free to use, build, and contribute 👍



## ✨ Don't Forget to 🌟 Star the repo if you like it!
