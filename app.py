from sentencepiece import SentencePieceProcessor
import gradio as gr

sp = SentencePieceProcessor(model_file="tokenizer.model")

def tokenize(input_text):
    tokens = sp.EncodeAsIds(input_text)
    return f"Number of tokens: {len(tokens)}"

iface = gr.Interface(fn=tokenize, inputs=gr.inputs.Textbox(lines=7), outputs="text")
iface.launch()