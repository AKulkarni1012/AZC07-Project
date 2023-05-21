import openai
import gradio

openai.api_key = "Enter your OpenAPIKey here"

messages = [{"role": "system", "content": "Can you please assist users with writing emails and responding to their Slack mesaages using the appropriate format"}]

def CustomChatGPT(user_input):
    messages.append({"role": "user", "content": user_input})
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = messages
    )
    ChatGPT_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    return ChatGPT_reply

demo = gradio.Interface(fn=CustomChatGPT, inputs = "text", outputs = "text", title = "Email and Text Assistant")

demo.launch(share=True)
