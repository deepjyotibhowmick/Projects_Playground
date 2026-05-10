from google import genai
from google.genai import types

client = genai.Client(api_key='AIzaSyC04UB_rnVmg0lHNf23ntUmLIftafee13M')

# Text generation ///https://ai.google.dev/gemini-api/docs/text-generation
# response = client.models.generate_content(
#     model="gemini-3-flash-preview",
#     contents="How does AI work?"
# )

# Thinking with Gemini
# response = client.models.generate_content(
#     model="gemini-3-pro-preview",
#     contents="How does AI work?",
#     config=types.GenerateContentConfig(
#         thinking_config=types.ThinkingConfig(thinking_level="low")
#     ),
# )

# System instructions and other configurations
# response = client.models.generate_content(
#     model="gemini-3-flash-preview",
#     config=types.GenerateContentConfig(
#         system_instruction="You are a cat. Your name is Neko."),
#     contents="Hello there"
# )
# response = client.models.generate_content(
#     model="gemini-3-flash-preview",
#     contents=["Explain how AI works"],
#     config=types.GenerateContentConfig(
#         temperature=0.1
#     )
# )
#
# print(response.text)

# Streaming responses
# response = client.models.generate_content_stream(
#     model="gemini-3-flash-preview",
#     contents=["Explain how AI works"]
# )
# for chunk in response:
#     print(chunk.text, end="")

chat = client.chats.create(model="gemini-3-flash-preview")

response = chat.send_message("I have 2 dogs in my house.")
print(response.text)

response = chat.send_message("How many paws are in my house?")
print(response.text)

for message in chat.get_history():
    print(f'role - {message.role}',end=": ")
    print(message.parts[0].text)