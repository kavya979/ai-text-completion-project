# AI Text Completion Project

This project is a simple Python-based AI text completion tool using **Google Gemini (gemini-2.0-flash)** via the `google-generativeai` API.

## 🔧 Setup

1. **Clone the repository**

2. **Create a virtual environment (optional but recommended)**

   ```bash
   python -m venv venv
   source venv/bin/activate  # or venv\Scripts\activate on Windows
````

3. **Install dependencies**

   ```bash
   pip install google-generativeai python-dotenv
   ```

4. **Create a `.env` file**

   Add your Google API key inside a `.env` file in the root directory:

   ```
   GOOGLE_API_KEY=your_google_api_key_here
   ```

## 🚀 Usage

Run the script:

```bash
python ai_text_completion_project.py
```

You will be prompted to:

* Enter a prompt for completion
* View the AI-generated output

To exit the app, type `exit`.

