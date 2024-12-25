import google.generativeai as genai
import os
import gradio as gr

genai.configure(api_key=os.environ["GOOGLE_API_KEY"])

# Defina o prompt inicial
initial_prompt = "Você é um super herói de resvistas em quadrinho"

# Escolha o modelo a ser usado com o prompt inicial
model = genai.GenerativeModel("gemini-1.5-flash",
                              system_instruction=initial_prompt)


# Inicie um chat sem parâmetros iniciais
chat = model.start_chat()


def gradio_wrapper(message, _history):
    # Envie a mensagem para o chat e obtenha a resposta
    # O gradio pega a mensagem digitada no browser por quem o usa e o entrega
    # para essa função
    response = chat.send_message(message)
    return response.text


# Crie a interface do chat passando a função de wrapper
chat_interface = gr.ChatInterface(gradio_wrapper)

# Inicie a interface
chat_interface.launch()
