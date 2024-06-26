from easytl import EasyTL

text_to_translate = """
The sun dipped below the horizon, casting a warm, golden glow across the tranquil lake. 
Ripples danced on the water's surface as a gentle breeze rustled the leaves of nearby trees. 
Birds chirped softly, settling into their nests for the night. 
A lone fisherman, silhouetted against the fading light, cast his line one last time, hoping for a final catch before darkness enveloped the landscape.
"""
model = "gpt-3.5-turbo-0125"
instructions = "Translate to Japanese, keep the existing tone. Make sure to structure the output into a json with the text to translation as `input` and the translated text as `output`."

with open("./openai.txt", "r") as file:
    api_key = file.read()

EasyTL.set_credentials(credentials=api_key, api_type="openai")

## OpenAI does not currently support json schema's to my knowledge, Gemini however does.
result = EasyTL.openai_translate(text=text_to_translate, model=model, translation_instructions=instructions, response_type="json")

print(result)

## example output:
"""
{
  "input": "The sun dipped below the horizon, casting a warm, golden glow across the tranquil lake. Ripples danced on the water's surface as a gentle breeze rustled the leaves of nearby trees. Birds chirped softly, settling into their nests for the night. A lone fisherman, silhouetted against the fading light, cast his line one last time, hoping for a final catch before darkness enveloped the landscape.",
  "output": "太陽が地平線の下に沈むと、静かな湖に暖かく黄金色の輝きが広がった。そよ風が近くの木々の葉をかき乱しながら、水面には波紋が踊った。鳥たちはそっと囀り、夜のために巣に落ち着いた。薄れゆく光に映る孤独な漁師は、景色が暗闇に包まれる前に最後の一匹
を期待して、最後に糸を投げた。"
}
"""