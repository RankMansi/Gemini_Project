import google.generativeai as genai
import os
import dotenv

dotenv.load_dotenv()

gemini_api_key = os.getenv("GOOGLE_GEMINI_AI")
genai.configure(api_key = gemini_api_key)

prompt = input("Enter your question: ")

model = genai.GenerativeModel('gemini-pro')
response = model.generate_content(prompt)

print(response.text)