from easytl import EasyTL

string = input("Enter the text you want to translate: ")
model = "gemini-pro"
instructions = "Translate to Japanese, informal casual, Young male speaker."

with open("gemini.txt", "r") as file:
    api_key = file.read()

EasyTL.set_credentials(credentials=api_key, api_type="gemini")

result = EasyTL.gemini_translate(text=string, model=model, translation_instructions=instructions)

print(result)