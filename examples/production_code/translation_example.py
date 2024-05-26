import typing
import logging
import asyncio

from easytl import EasyTL

## dummy classes and variables
class ModelTranslationMessage:
    pass

class SystemTranslationMessage:
    pass

class MaxBatchDurationExceededException(Exception):
    pass

class FileEnsurer:
    do_interrupt = False

class Translator:

    _semaphore = asyncio.Semaphore(value=5)
    decorator_to_use = ()
    openai_temperature = 0.5
    openai_top_p = 1.0
    openai_stop = None
    openai_max_tokens = 1000
    openai_presence_penalty = 0.0
    openai_frequency_penalty = 0.0
    gemini_temperature = 0.5
    gemini_top_p = 1.0
    gemini_top_k = 50
    gemini_stop_sequences = None
    gemini_max_output_tokens = 1000
    deepl_context = "general"
    deepl_split_sentences = False
    deepl_preserve_formatting = False
    deepl_formality = "default"
    TRANSLATION_METHOD = "openai"
    
##-------------------start-of-handle_translation()---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

@staticmethod
async def handle_translation(model:str, 
                                batch_number:int,
                                length_of_batch:int, 
                                text_to_translate:typing.Union[str, ModelTranslationMessage],
                                translation_instructions:typing.Union[str, SystemTranslationMessage, None]):

    """

    Handles the translation requests for the specified service.

    Parameters:
    model (string) : The model of the service used to translate the text.
    batch_number (int) : Which batch we are currently on.
    length_of_batch (int) : How long the batches are.
    text_to_translate (typing.Union[str, ModelTranslationMessage]) : The text to translate.
    translation_instructions (typing.Union[str, SystemTranslationMessage, None]) : The translation instructions.

    Returns:
    batch_number (int) : The batch index.
    text_to_translate (str) : The text to translate.
    translated_text (str) : The translated text

    """

    ## Basically limits the number of concurrent batches
    async with Translator._semaphore:
        num_tries = 0

        while True:

            ## For the webgui
            if(FileEnsurer.do_interrupt == True):
                raise Exception("Interrupted by user.")
            
            logging.info(f"Trying translation for batch {batch_number} of {length_of_batch}...")

            try:

                translation_methods = {
                    "openai": EasyTL.openai_translate_async,
                    "gemini": EasyTL.gemini_translate_async,
                    "deepl": EasyTL.deepl_translate_async,
                    "google translate": EasyTL.googletl_translate_async
                }
                
                translation_params = {
                    "openai": {
                        "text": text_to_translate,
                        "decorator": Translator.decorator_to_use,
                        "translation_instructions": translation_instructions,
                        "model": model,
                        "temperature": Translator.openai_temperature,
                        "top_p": Translator.openai_top_p,
                        "stop": Translator.openai_stop,
                        "max_tokens": Translator.openai_max_tokens,
                        "presence_penalty": Translator.openai_presence_penalty,
                        "frequency_penalty": Translator.openai_frequency_penalty
                    },
                    "gemini": {
                        "text": text_to_translate,
                        "decorator": Translator.decorator_to_use,
                        "model": model,
                        "temperature": Translator.gemini_temperature,
                        "top_p": Translator.gemini_top_p,
                        "top_k": Translator.gemini_top_k,
                        "stop_sequences": Translator.gemini_stop_sequences,
                        "max_output_tokens": Translator.gemini_max_output_tokens
                    },
                    "deepl": {
                        "text": text_to_translate,
                        "decorator": Translator.decorator_to_use,
                        "context": Translator.deepl_context,
                        "split_sentences": Translator.deepl_split_sentences,
                        "preserve_formatting": Translator.deepl_preserve_formatting,
                        "formality": Translator.deepl_formality
                    },
                    "google translate": {
                        "text": text_to_translate,
                        "decorator": Translator.decorator_to_use
                    }
                }
                
                assert isinstance(text_to_translate, ModelTranslationMessage if Translator.TRANSLATION_METHOD == "openai" else str)
                
                translated_message = await translation_methods[Translator.TRANSLATION_METHOD](**translation_params[Translator.TRANSLATION_METHOD])

            ## will only occur if the max_batch_duration is exceeded, so we just return the untranslated text
            except MaxBatchDurationExceededException:

                logging.error(f"Batch {batch_number} of {length_of_batch} was not translated due to exceeding the max request duration, returning the untranslated text...")
                break

