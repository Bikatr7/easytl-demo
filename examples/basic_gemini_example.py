from easytl import EasyTL

text_to_translate = "Hello, my name is Takeshi. I am a software engineer, it's nice to meet you."
model = "gemini-pro"
instructions = "Translate to Japanese, formal polite, Young male speaker."

with open("./gemini.txt", "r") as file:
    api_key = file.read()

EasyTL.set_credentials(credentials=api_key, api_type="gemini")

result = EasyTL.gemini_translate(text=text_to_translate, model=model, translation_instructions=instructions)

print(result)

## example output:
## 初めまして。私は武と申します。ソフトウェアエンジニアをしております。よろしくお願いいたします。