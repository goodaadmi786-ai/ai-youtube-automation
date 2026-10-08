from datetime import datetime

topic = "5 Amazing Facts About the Human Brain"

script = f"""
🎬 AI YOUTUBE SHORT

Topic: {topic}

HOOK:
Did you know your brain can do something absolutely amazing?

FACT 1:
The human brain contains billions of neurons that communicate with each other.

FACT 2:
Your brain uses a significant amount of the body's energy, even when you are resting.

FACT 3:
Your brain is constantly processing information from your surroundings, even when you are not consciously thinking about it.

ENDING:
Which brain fact surprised you the most?
Follow for more amazing facts!

Generated: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
"""

with open("output_script.txt", "w", encoding="utf-8") as f:
    f.write(script)

print(script)
print("\n✅ Script generated successfully!")
