from easytl import EasyTL

text_to_translate = "I'm pretty sure that I'm a human. I'm not a robot. Do you understand me?"
target_language = "JA"

with open("./deepl.txt", "r") as file:
    api_key = file.read()

EasyTL.set_credentials(credentials=api_key, api_type="deepl")

result = EasyTL.deepl_translate(text=text_to_translate, target_lang=target_language)

print(result)

## example output:
## 私は人間だと確信している。ロボットじゃない。私のことがわかりますか？