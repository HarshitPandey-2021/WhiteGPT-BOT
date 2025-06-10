
# 🤖 WhiteGPT Discord Bot

**WhiteGPT** is an intelligent Discord chatbot powered by **Together AI** and built with **Python**, **Flask**, and **Discord.py**. It supports both **web chat interface** and **Discord replies**, fully hosted on **Replit** for free — and runs 24/7 using cron jobs.


## ✨ Features

- 🤖 Responds to mentions on Discord (`@WhiteGPT What is AI?`)
- 🌐 Includes a minimal ChatGPT-style **Web UI** (`Flask`)
- 💾 Stores all chats in `chatlogs.json` (user, prompt, response)
- 🔗 Powered by **Together AI** (e.g. `DeepSeek-V3`, `LLaMA`, `Mixtral`)
- 🚀 Hosted free on Replit + cron-job.org for 24/7 uptime


## 🔧 Technologies Used

- Python 3
- Flask (for web UI)
- Discord.py (for bot commands)
- Together AI API
- Replit (deployment)

---

## 🌐 Live Web Chat

You can access the web interface via:

```
https://168c2e60-9336-43f8-beb5-180859ab7d21-00-b3vesoqp8txa.pike.replit.dev/
```

Users can type to the bot in a simple form and get AI responses 🤖.



## 💬 Setup Instructions

1. **Clone the repo** or use Replit
2. Install dependencies:
   ```bash
   pip install discord.py flask together
   ```
3. Add environment variables:
   - `SECRET_KEY` = *your Discord Bot Token*
   - `TOGETHER_API_KEY` = *your Together API Key*
4. Add `keepalive.py` to support web UI & uptime
5. Use [cron-job.org](https://cron-job.org) to ping your Replit URL every 5 minutes

---

## 📁 File Structure

```
├── main.py           # Discord bot logic
├── keepalive.py      # Flask + web UI
├── templates/
│   └── index.html    # HTML Web Chat UI
├── chatlogs.json     # Saved chat history
└── README.md         # This file
```

---

## 🚀 Credits

**Built with ❤️ by Harshit Pandey**  
GitHub → [@HarshitPandey-2021](https://github.com/HarshitPandey-2021)

---

## 🪪 License

Licensed under the [MIT License](LICENSE)
