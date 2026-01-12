import json
from openai import OpenAI
from config import OPENAI_API_KEY

class TravelBot:
    def __init__(self, model="gpt-4o-mini", landmark_file="data/landmarks.json"):
        self.client = OpenAI(api_key=OPENAI_API_KEY)
        self.model = model
        self.conversation = [
            {
                "role": "system",
                "content": "You are a friendly travel guide AI for Paris. Be concise and helpful."
            },
            {
                "role": "user",
                "content": "What is the most famous place to visit in Paris?"
            },
            {
                "role": "assistant",
                "content": "The most famous place in Paris is the Eiffel Tower."
            },
        ]
        # Load landmarks info
        with open(landmark_file, "r") as f:
            self.landmarks = json.load(f)

    # noinspection PyTypeChecker
    def ask(self, user_input: str) -> str:
        """Respond to user input using OpenAI API"""
        self.conversation.append({"role": "user", "content": user_input})
        response = self.client.chat.completions.create(model=self.model, messages=self.conversation, temperature=0.5,
                                                       max_tokens=150)
        answer = response.choices[0].message.content
        self.conversation.append({"role": "assistant", "content": answer})
        return answer

    def get_landmark_info(self, name: str) -> str:
        """Return landmark info from local JSON file"""
        info = self.landmarks.get(name)
        if info:
            tips = "\n".join(f"- {tip}" for tip in info["tips"])
            return f"{info['description']}\nTips:\n{tips}"
        return f"Sorry, I don't have information on {name}."
