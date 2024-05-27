from easytl import EasyTL

text_to_translate = "Hey! What the hell do you think you are doing?"
model = "gpt-3.5-turbo-0125"
instructions = "Translate to Japanese, rude, young male speaker."

with open("./openai.txt", "r") as file:
    api_key = file.read()

EasyTL.set_credentials(credentials=api_key, api_type="openai")

result = EasyTL.openai_translate(text=text_to_translate, model=model, translation_instructions=instructions)

print(result)

## example output:
## やぁ！お前、一体何を考えてやがるんだ？