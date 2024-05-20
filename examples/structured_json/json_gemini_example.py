from easytl import EasyTL

text_to_translate = """
The cat lounged in the sunny patch on the windowsill, its fur glowing in the afternoon light. Outside, a butterfly fluttered by, catching the cat's lazy attention for a moment. 
The room was quiet and warm, filled with the soft hum of a distant lawnmower. It was a perfect, peaceful moment.
"""

model = "gemini-1.5-pro-latest"
detailed_instructions = "Translate to Japanese, keep the existing tone. Make sure to structure the output into a json with the text to translation as `input` and the translated text as `output`."
undetailed_instructions = "Translate to Japanese, keep the existing tone."

schema = {
    "type": "object",
    "properties": {
        "input": {
            "type": "string",
            "description": "The text you were given to translate"
        },
        "output": {
            "type": "string",
            "description": "The translated text"
        }
    },
    "required": ["input", "output"]
}

with open("./gemini.txt", "r") as file:
    api_key = file.read()

EasyTL.set_credentials(credentials=api_key, api_type="gemini")

## Gemini's SDK and EasyTL both support the schema, but at the time of writing this their actual endpoint does not, in the future, it will follow the schema even with the undetailed instructions.
result = EasyTL.gemini_translate(text=text_to_translate, model=model, translation_instructions=detailed_instructions, response_type="json", response_schema=schema)

print(result)