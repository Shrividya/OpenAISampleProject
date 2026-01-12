from openaichatbot import TravelBot

def main():
    bot = TravelBot()
    print("Welcome to the Paris Travel Guide Bot! Type 'exit' to quit.")
    print("You can also type 'landmark: <name>' to get info from local database.")

    while True:
        user_input = input("You: ").strip()
        if user_input.lower() in ["exit", "quit"]:
            print("Goodbye!")
            break
        elif user_input.lower().startswith("landmark:"):
            landmark_name = user_input.split(":", 1)[1].strip()
            print(bot.get_landmark_info(landmark_name))
        else:
            answer = bot.ask(user_input)
            print(f"Bot: {answer}")

if __name__ == "__main__":
    main()
