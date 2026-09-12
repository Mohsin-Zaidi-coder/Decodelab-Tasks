import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

# Create Gemini client
client = genai.Client(api_key=API_KEY)

# User Inputs
product_name = input("Enter Product Name: ")
platform = input("Enter Platform (LinkedIn/Instagram/Email): ")
tone = input("Enter Tone (Professional/Friendly/Persuasive): ")

temperature = float(input("Enter Temperature (0.0 - 1.0): "))
top_p = float(input("Enter Top_P (0.0 - 1.0): "))

# Dynamic Prompt
prompt = f"""
Write a professional marketing copy.

Product Name: {product_name}
Platform: {platform}
Tone: {tone}

Generate an attractive marketing copy suitable for the selected platform.
"""

# Generate Response
response = client.models.generate_content(
    model="gemini-3.6-flash",
    contents=prompt,
    config=types.GenerateContentConfig(
        temperature=temperature,
        top_p=top_p,
    ),
)

print("\n========== Generated Marketing Copy ==========\n")
print(response.text)