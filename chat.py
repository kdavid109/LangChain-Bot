import os
import openai
import gradio


openai.organization = 'org-ecFtjeqt8mslWFlkPPFYM4O3'
openai.api_key = os.getenv("api_key")
openai.Model.list()

messages = [{"role": "system", "content": "You are a sport caster that talks like Mike Breen and Steve Buckhantz" }]
#user input

def MidasAI(user_input):
  messages.append({"role":"user", "content": user_input})
  response = openai.ChatCompletion.create(
    model = "gpt-3.5-turbo",
    messages = messages
  )
  chat_reply = response["choices"][0]["message"]["content"]
  messages.append({"role": "sport caster", "content" : chat_reply})
  return chat_reply


"""""
demo = gradio.Interface(fn = MidasAI, inputs = "text", outputs = "text", title = "Your Title")
demo.launch()
"""