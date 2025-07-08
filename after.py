import gradio as gr
from transformers import pipeline

# Load English to French translator
translator = pipeline("translation_en_to_fr")

# Define function for Gradio
def translate_text(text):
    result = translator(text, max_length=100)
    return result[0]['translation_text']

# Create Gradio interface
interface = gr.Interface(
    fn=translate_text,
    inputs=gr.Textbox(lines=4, label="Enter English Text"),
    outputs=gr.Textbox(label="French Translation"),
    title="English to French Translator",
    description="Type in English and get a French translation using Hugging Face Transformers"
)

# Launch the web app
interface.launch()
