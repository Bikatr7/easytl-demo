from easytl import EasyTL
from easytl.exceptions import RequestException

text_to_translate = "I'm pretty sure that I'm a human. I'm not a robot. Do you understand me?"
target_language = "JA"

with open("./azure.txt", "r") as file:
    api_key = file.read()

EasyTL.set_credentials(credentials=api_key, api_type="azure")

is_valid, e = EasyTL.test_credentials("azure", "northcentralus") 

result = EasyTL.azure_translate(text=text_to_translate, target_lang=target_language, azure_region="northcentralus", azure_endpoint="https://api.cognitive.microsofttranslator.com")

print(result)

## example output:
## 私は人間だと確信している。ロボットじゃない。私のことがわかりますか？