import os
from dotenv import load_dotenv
from google import genai

# Load environment variables
load_dotenv()

# Get Gemini API key
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

print("Gemini API key set:", bool(GEMINI_API_KEY))

if not GEMINI_API_KEY:
    print("\nERROR: Gemini API key not found.")
    print("Please check your .env file.")
    exit()

# Create Gemini client
client = genai.Client(api_key=GEMINI_API_KEY)

# Create chat session
chat = client.chats.create(
    model="gemini-3.6-flash"
)

print("=" * 55)
print("             CUSTOM AI CHATBOT")
print("                WITH MEMORY")
print("=" * 55)
print("Type 'exit' to close the chatbot.")
print("The chatbot will remember this conversation.")
print("=" * 55)

while True:

    # Get user input
    user_message = input("\nYou: ")

    # Exit command
    if user_message.lower() == "exit":
        print("\nChatbot closed. Goodbye!")
        break

    try:
        # Send message to Gemini
        response = chat.send_message(
            message=user_message
        )

        # Get AI response
        assistant_message = response.text

        print("\nAI:", assistant_message)

    except Exception as error:
        print("\nError:", error)