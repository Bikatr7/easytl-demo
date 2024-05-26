import logging

from easytl import EasyTL

class Translator:

    ## dummy variables
    TRANSLATION_METHOD = "openai"
    text_to_translate = "Hello, how are you?"
    openai_system_message = "Translate the following text to French."
    gemini_prompt = "Translate the following text to French."

##-------------------start-of-handle_cost_estimate_prompt()---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

@staticmethod
async def handle_cost_estimate_prompt(model:str, omit_prompt:bool=False) -> str:

    """

    Handles the cost estimate prompt.

    Parameters:
    model (string) : the model used to translate the text.
    omit_prompt (bool) : whether or not to omit the prompt.
    
    Returns:
    model (string) : the model used to translate the text.
    
    """ 

    translation_instructions_methods = {
        "openai": Translator.openai_system_message,
        "gemini": Translator.gemini_prompt,
        "deepl": None,
        "google translate": None
    }
    
    translation_instructions = translation_instructions_methods[Translator.TRANSLATION_METHOD]

    ## get cost estimate and confirm
    num_entities, min_cost, model = EasyTL.calculate_cost(text=Translator.text_to_translate, service=Translator.TRANSLATION_METHOD, model=model,translation_instructions=translation_instructions)

    print("Note that the cost estimate is not always accurate, and may be higher than the actual cost. However cost calculation now includes output tokens.\n")

    if(Translator.TRANSLATION_METHOD == "gemini"):
        logging.info(f"As of Kudasai v3.4.5, Gemini Pro 1.0 is free to use under 15 requests per minute, Gemini Pro 1.5 is free to use under 2 requests per minute. Requests correspond to number_of_current_batches in the translation settings.")
    
    entity_word = "tokens" if Translator.TRANSLATION_METHOD in ["openai", "gemini"] else "characters"

    logging.info(f"Estimated number of {entity_word} : " + str(num_entities))
    logging.info("Estimated minimum cost : " + str(min_cost) + " USD")

    if(not omit_prompt):
        if(input("\nContinue? (1 for yes or 2 for no) : ") == "1"):
            logging.info("User confirmed translation.")

        else:
            logging.info("User cancelled translation.")
            exit()

    return model