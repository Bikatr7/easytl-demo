from easytl import EasyTL

text_to_translate = """
The cat lounged in the sunny patch on the windowsill, its fur glowing in the afternoon light. Outside, a butterfly fluttered by, catching the cat's lazy attention for a moment. 
The room was quiet and warm, filled with the soft hum of a distant lawnmower. It was a perfect, peaceful moment.
"""

model = "gemini-1.5-pro-latest"
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

result = EasyTL.gemini_translate(text=text_to_translate, model=model, translation_instructions=undetailed_instructions, response_type="json", response_schema=schema)

print(result)

## example output:
"""
{"input": "The cat lounged in the sunny patch on the windowsill, its fur glowing in the afternoon light. Outside, a butterfly fluttered by, catching the cat's lazy attention for a moment.\nThe room was quiet and warm, filled with the soft hum of a distant lawnmower. It was a perfect, peaceful moment. ", "output": "猫は窓辺の日当たりの良い場所に寝そべり、午後の光を受けて毛皮が輝いていました。外では蝶がひらひらと舞い上がり、猫のぼんやりとした注意を一瞬だけ引きました。\n部屋は静かで暖かく、遠くの芝刈
り機の柔らかな音が響いていました。完璧で穏やかなひとときでした。"}
"""