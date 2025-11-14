import gradio as gr
import os
from openai import OpenAI

api_key = os.environ.get("OPENROUTER_API_KEY")

if not api_key:
    print("OPENROUTER_API_KEY not found in environment secrets!")
    client = None
else:
    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=api_key,
    )
    
def compare_models(user_prompt):
    if not client:
        return "Error: API Key not configured.", "Error: API Key not configured.", "Error: API Key not configured."

    model_1 = "mistralai/mistral-7b-instruct"
    model_2 = "meta-llama/llama-3-8b-instruct"
    model_3 = "anthropic/claude-3-haiku" # <-- This is the new, working model

    try:
        response_1 = client.chat.completions.create(
            model=model_1,
            messages=[{"role": "user", "content": user_prompt}]
        )
        output_1 = response_1.choices[0].message.content
    except Exception as e:
        output_1 = f"Error calling {model_1}: {e}"

    try:
        response_2 = client.chat.completions.create(
            model=model_2,
            messages=[{"role": "user", "content": user_prompt}]
        )
        output_2 = response_2.choices[0].message.content
    except Exception as e:
        output_2 = f"Error calling {model_2}: {e}"

    try:
        response_3 = client.chat.completions.create(
            model=model_3,
            messages=[{"role": "user", "content": user_prompt}]
        )
        output_3 = response_3.choices[0].message.content
    except Exception as e:
        output_3 = f"Error calling {model_3}: {e}"

    return output_1, output_2, output_3

demo = gr.Interface(
    fn=compare_models,
    inputs=gr.Textbox(label="Enter your prompt", lines=3),
    outputs=[
        gr.Textbox(label="Model 1: Mistral 7B"),
        gr.Textbox(label="Model 2: LLaMA 3 8B"),
        gr.Textbox(label="Model 3: Claude 3 Haiku") # <-- I updated the label to match
    ],
    title="🤖 OpenRouter Model Arena",
    description="Enter one prompt and see the results from three different AI models side-by-side. (Powered by OpenRouter)"
)

demo.launch() # <-- I fixed the typo here (removed extra parenthesis)