!pip install torch==1.8.1+cu111 torchvision==0.9.1+cu111 torchaudio===0.8.1 -f https://download.pytorch.org/whl/lts/1.8/torch_lts.html
!pip install transformers ipywidgets gradio --upgrade
import gradio as gr                   # UI library
from transformers import pipeline     # Transformers pipeline
#Loading up the pipeline
translation_pipeline = pipeline('translation_en_to_de')
results = translation_pipeline('There is a rock rolling down')
results[0]['translation_text']
#Create Gradio Function Interface
def translate_transformers(from_text):
    results = translation_pipeline(from_text)
    return results[0]['translation_text']
translate_transformers('My name is Tharunika')
interface = gr.Interface(fn=translate_transformers, 
                         inputs=gr.inputs.Textbox(lines=2, placeholder='Text to translate'),
                        outputs='text')
