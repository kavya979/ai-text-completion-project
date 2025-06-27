
import os
from dotenv import load_dotenv
import google.generativeai as genai  
import time

# Load environment variables from .env file
load_dotenv()
genai.configure(api_key="YOUR_APT_KEY")

def get_completion(prompt, temperature=0.7, max_tokens=100):
    try:
        model = genai.GenerativeModel("gemini-2.0-flash")
        response = model.generate_content(prompt, generation_config={
            "temperature": temperature,
            "max_output_tokens": max_tokens
        })
        return response.text
    except Exception as e:
        return f"[API Error] {str(e)}"

def get_user_settings():
    try:
        temperature = float(input("Enter creativity level (temperature 0.0 - 1.0): "))
        max_tokens = int(input("Enter maximum number of tokens (e.g., 100): "))
        return temperature, max_tokens
    except ValueError:
        print("Invalid input. Using default parameters: temperature=0.7, max_tokens=100")
        return 0.7, 100

def main():
    print("\nAI Text Completion App")
    print("Type 'exit' to quit\n")

    temperature, max_tokens = get_user_settings()

    while True:
        try:
            user_input = input("\nEnter a prompt: ")
            if user_input.lower() == 'exit':
                break
            if not user_input.strip():
                print("[Input Error] Please enter a valid prompt.")
                continue
            if len(user_input) > 1000:
                print("[Input Error] Prompt too long. Please limit to 1000 characters.")
                continue

            print("\nGenerating response...")
            start_time = time.time()
            output = get_completion(user_input, temperature, max_tokens)
            end_time = time.time()

            print("\n--- Prompt ---\n" + user_input)
            print("\n--- Response ---\n" + output)
            print(f"\n(Response generated in {end_time - start_time:.2f} seconds)")

        except KeyboardInterrupt:
            print("\n[Session Terminated] User exited with Ctrl+C.")
            break
        except Exception as e:
            print(f"[Runtime Error] {e}")

if __name__ == "__main__":
    main()
