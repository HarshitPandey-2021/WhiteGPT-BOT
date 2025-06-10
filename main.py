from keepalive import keep_alive
import discord
import os
import asyncio
import json
from datetime import datetime
from together import Together

# 🔐 Load API keys from Replit secrets
together_api_key = os.getenv("TOGETHER_API_KEY")
discord_token = os.getenv("SECRET_KEY")

# ✅ Initialize Together client
client_ai = Together(api_key=together_api_key)

# ✅ Enable intent to read message content
intents = discord.Intents.default()
intents.message_content = True

# ✅ Initialize Discord bot
client = discord.Client(intents=intents)

# 📦 Function to log chats to a JSON file
def log_chat(user, user_id, prompt, response, file_path="chatlogs.json"):
    data = {
        "timestamp": datetime.utcnow().isoformat(),
        "user": str(user),
        "user_id": str(user_id),
        "prompt": prompt,
        "response": response
    }

    try:
        # If it doesn't exist, create new file
        if not os.path.exists(file_path):
            with open(file_path, "w") as f:
                json.dump([data], f, indent=4)
        else:
            with open(file_path, "r+") as f:
                existing = json.load(f)
                existing.append(data)
                f.seek(0)
                json.dump(existing, f, indent=4)

        print(f"📦 Chat logged for {user}")
    except Exception as e:
        print(f"❌ Error saving chat: {e}")

# 🤖 Discord Event: On Bot Ready
@client.event
async def on_ready():
    print(f"✅ Logged in as {client.user}")

# ⚡ Discord Event: On Message
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if client.user in message.mentions:
        prompt = message.content.replace(f"<@{client.user.id}>", "").strip()
        print(f"📨 Prompt from {message.author}: {prompt}")

        await message.channel.typing()

        try:
            # ⚡ Call Together AI in a background thread (prevents freeze)
            response = await asyncio.to_thread(
                client_ai.chat.completions.create,
                model="deepseek-ai/DeepSeek-V3",  # ✅ You can change to llama/meta/mixtral models
                messages=[{"role": "user", "content": prompt}],
                max_tokens=1800,
                temperature=0.7
            )

            reply = response.choices[0].message.content

            # ✂️ If response is too long, split it
            chunks = [reply[i:i+1990] for i in range(0, len(reply), 1990)]
            for chunk in chunks:
                await message.channel.send(chunk)

            # 📝 Log chat into local file
            log_chat(
                user=message.author.name,
                user_id=message.author.id,
                prompt=prompt,
                response=reply
            )

        except Exception as e:
            print("❌ Error during response:", str(e))
            await message.channel.send("Sorry, something went wrong while generating my reply 💥")

keep_alive()
client.run(discord_token)
# 🏁 Start the bot
client.run(discord_token)