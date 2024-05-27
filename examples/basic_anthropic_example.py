from easytl import EasyTL

text_to_translate = "Hiya, I'm Lauren. I'll be your lab partner, shall we get started?"
model = "claude-3-sonnet-20240229"
instructions = "Translate to Japanese, informal polite, Middle aged women speaker."

with open("./anthropic.txt", "r") as file:
    api_key = file.read()

EasyTL.set_credentials(credentials=api_key, api_type="anthropic")

result = EasyTL.anthropic_translate(text=text_to_translate, model=model, translation_instructions=instructions)

print(result)

## example output:
## こんにちは、ローレンさん。私も一緒に実験を始めましょうか。頑張りましょうね