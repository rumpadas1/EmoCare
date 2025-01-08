import random
import json
import os

class MentalHealthChatbot:
    def __init__(self):
        self.greetings = [
            "Hello! How are you feeling today?",
            "Hi there! What's on your mind?",
            "Hey! I'm here to listen. How are you?"
        ]
        self.resources = {
            "sad": [
                "It's okay to feel sad sometimes. You can reach out to a mental health professional.",
                "Consider talking to a trusted friend or family member.",
                "You might find it helpful to visit a local support group."
            ],
            "anxious": [
                "Anxiety can be tough. Have you tried deep breathing exercises?",
                "Consider practicing mindfulness or meditation.",
                "Talking to a therapist can also be very beneficial."
            ],
            "happy": [
                "That's great to hear! It's important to celebrate the good moments.",
                "Keep doing what makes you happy!",
                "Sharing your happiness with others can also uplift them."
            ],
            "stress": [
                "Stress can be overwhelming. Try to take breaks and practice self-care.",
                "Consider engaging in physical activity to relieve stress.",
                "Talking to someone about your stress can also help."
            ]
        }
        self.coping_strategies = [
            "Try deep breathing exercises.",
            "Consider journaling your thoughts.",
            "Take a walk outside to clear your mind.",
            "Listen to your favorite music.",
            "Engage in a hobby you love."
        ]
        self.mood_suggestions = {
            "anxious": [
                "Try some deep breathing exercises.",
                "Listen to calming music.",
                "Take a short walk outside."
            ],
            "sad": [
                "Reach out to a friend or family member.",
                "Watch a funny movie or show.",
                "Engage in a creative activity like drawing or writing."
            ]
        }
        self.user_data_file = 'user_data.json'
        self.user_data = self.load_user_data()

    def load_user_data(self):
        if os.path.exists(self.user_data_file):
            with open(self.user_data_file, 'r') as file:
                return json.load(file)
        return {}

    def save_user_data(self):
        with open(self.user_data_file, 'w') as file:
            json.dump(self.user_data, file)

    def greet_user(self):
        print(random.choice(self.greetings))

    def get_user_input(self):
        return input("You: ")

    def respond_to_user(self, user_input):
        user_input = user_input.lower()
        
        if "sad" in user_input or "depressed" in user_input:
            print("Chatbot: I'm sorry to hear that you're feeling this way.")
            print("Chatbot: Here are some resources you can consider:")
            print(random.choice(self.resources["sad"]))
        elif "anxious" in user_input or "nervous" in user_input:
            print("Chatbot: It's understandable to feel anxious sometimes.")
            print("Chatbot: Here are some strategies you can try:")
            print(random.choice(self.resources["anxious"]))
        elif "happy" in user_input or "good" in user_input:
            print("Chatbot: That's wonderful to hear! Keep it up!")
            print(random.choice(self.resources["happy"]))
        elif "stress" in user_input:
            print("Chatbot: Here are some strategies for managing stress:")
            print(random.choice(self.resources["stress"]))
        elif "cope" in user_input or "stress" in user_input:
            print("Chatbot: Here are some coping strategies you can try:")
            print(random.choice(self.coping_strategies))
        elif "thank you" in user_input:
            print("Chatbot: You're welcome! I'm here for you.")
        elif "exit" in user_input or "quit" in user_input:
            print("Chatbot: Take care! Remember, it's okay to seek help. I'm here if you need me.")
            return False
        elif "help" in user_input:
            self.show_help()
        elif "log mood" in user_input:
            self.log_mood()
        elif "check-in" in user_input:
            self.daily_check_in()
        else:
            print("Chatbot: I'm here to listen. Please tell me more about how you're feeling.")

        return True

    def show_help(self):
        print("Chatbot: Here are some commands you can use:")
        print("- 'log mood': Log your current mood (e.g., sad, happy, anxious).")
        print("- 'check-in': Perform a daily mood check-in.")
        print ("- 'exit' or 'quit': End the conversation.")
        print("- 'help': Show this help message.")

    def log_mood(self):
        mood = input("Chatbot: How are you feeling? (e.g., anxious, sad): ").strip().lower()
        if mood in self.mood_suggestions:
            suggestions = self.mood_suggestions[mood]
            print(f"Chatbot: Suggestions for feeling {mood}:")
            for suggestion in suggestions:
                print(f"- {suggestion}")
            self.user_data['mood_log'] = mood
            self.save_user_data()
        else:
            print("Chatbot: It's okay to feel that way. Consider talking to someone about it.")

    def daily_check_in(self):
        if 'mood_log' in self.user_data:
            print(f"Chatbot: Last logged mood was: {self.user_data['mood_log']}")
        else:
            print("Chatbot: You haven't logged any mood yet. Please log your mood.")

    def run(self):
        self.greet_user()
        while True:
            user_input = self.get_user_input()
            if not self.respond_to_user(user_input):
                break

if __name__ == "__main__":
    chatbot = MentalHealthChatbot()
    chatbot.run()
