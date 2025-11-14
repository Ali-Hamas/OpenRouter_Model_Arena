# OpenRouter Model Arena

This is a simple web application that lets you compare responses from three different AI models side-by-side using the OpenRouter API.

# Features:

Enter one prompt and get three different outputs.

Easily compare the results from different models.

Uses the Gradio library for a simple user interface.

# Models Used:

Mistral 7B (mistralai/mistral-7b-instruct)

LLaMA 3 8B (meta-llama/llama-3-8b-instruct)

Claude 3 Haiku (anthropic/claude-3-haiku)

# How to Run:

Make sure you have Python installed.

Install the required libraries: pip install gradio openai

Set your OpenRouter API key as an environment variable named OPENROUTER_API_KEY.

    On Windows (CMD): set OPENROUTER_API_KEY=your-key-here

    On macOS/Linux: export OPENROUTER_API_KEY='your-key-here'

Save the code as a Python file (e.g., app.py).

Run the file from your terminal: python app.py

Open the local URL provided in your terminal (like http://127.0.0.1:7860) in your browser.
