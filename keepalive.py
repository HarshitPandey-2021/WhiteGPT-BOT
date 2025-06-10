from flask import Flask, render_template, request, jsonify
from threading import Thread
from datetime import datetime
import json, os
from together import Together

app = Flask("WhiteGPT")
client_ai = Together(api_key=os.getenv("TOGETHER_API_KEY"))


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    prompt = data.get("prompt", "").strip()

    if not prompt:
        return jsonify({"response": "Please enter a prompt."})

    # System prompt = Bot personality
    system_prompt = {
        "role":
        "system",
        "content":
        "You are WhiteGPT, a helpful, friendly programming tutor assistant that explains AI, tech, and code like a pro teacher."
    }

    try:
        response = client_ai.chat.completions.create(
            model="deepseek-ai/DeepSeek-V3",
            messages=[system_prompt, {
                "role": "user",
                "content": prompt
            }],
            max_tokens=900,
            temperature=0.7)

        answer = response.choices[0].message.content.strip()

        # Save to chatlogs.json
        log_entry = {
            "prompt": prompt,
            "response": answer,
            "timestamp": datetime.utcnow().isoformat()
        }

        log_file = "chatlogs.json"
        if os.path.exists(log_file):
            with open(log_file, "r") as f:
                logs = json.load(f)
        else:
            logs = []

        logs.append(log_entry)

        with open(log_file, "w") as f:
            json.dump(logs, f, indent=2)

        return jsonify({"response": answer})

    except Exception as e:
        return jsonify({"response": f"⚠️ Error: {str(e)}"})


# ✅ This part was missing!
def run():
    app.run(host="0.0.0.0", port=8080)


def keep_alive():
    t = Thread(target=run)
    t.start()


@app.route("/reset", methods=["POST"])
def reset_chatlog():
    try:
        with open("chatlogs.json", "w") as f:
            json.dump([], f)
        return jsonify({"status": "cleared"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
