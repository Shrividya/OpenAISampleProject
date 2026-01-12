import os
import dotenv

dotenv.load_dotenv()

# Make sure your OPENAI_API_KEY is set in environment variables
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    raise ValueError("Please set your OPENAI_API_KEY in environment variables.")
