---------------------------------------------------------------------------------------------------------------------------------------------------
## **Table of Contents** <a name="table-of-contents"></a>

- [**Table of Contents** ](#table-of-contents-)
- [**Notes**](#notes)
- [**Getting Started**](#getting-started)
- [**Running the Code Examples**](#running-the-code-examples)
- [Available Examples (More to come) ](#available-examples-more-to-come-)
  - [Basic Examples (in examples/)  ](#basic-examples-in-examples--)
  - [JSON Response Examples (in examples/structured\_json/) ](#json-response-examples-in-examplesstructured_json-)
  - [Production code examples (in examples/production\_code/) ](#production-code-examples-in-examplesproduction_code-)

---------------------------------------------------------------------------------------------------------------------------------------------------

## **Notes**<a name="notes"></a>

This repository demonstrates a use case for the EasyTL Python package. [EasyTL GitHub Repository](https://github.com/bikatr7/easytl)

This repository contains examples of how to use EasyTL with the Gemini, OpenAI, Anthropic, and DeepL APIs. EasyTL also supports Google Translate and Microsoft Azure Translator, but these are not demonstrated here.

---------------------------------------------------------------------------------------------------------------------------------------------------

## **Getting Started**<a name="getting-started"></a>

1. Clone the repository:
    ```bash
    git clone https://github.com/Bikatr7/easytl-demo.git
    ```

2. Navigate to the project directory:
    ```bash
    cd easytl-demo
    ```
3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```
4. Create the following API key files in the root directory (at least one is required):
    - `gemini.txt` with your Google API key
    - `openai.txt` with your OpenAI API key
    - `anthropic.txt` with your Anthropic API key
    - `deepl.txt` with your DeepL API key

---------------------------------------------------------------------------------------------------------------------------------------------------

## **Running the Code Examples**<a name="running-the-code-examples"></a>

Pick an example from the `examples` directory and run it. For example:
```bash
python examples/basic_gemini_example.py
```

In the root of `examples/`, you will find generic basic examples for each API. You can use these as a starting point for what EasyTL can do. Some examples require specific APIs. See the [Available Examples](#available-examples) section for more information.

## Available Examples (More to come) <a name="available-examples"></a>

### Basic Examples (in examples/)  <a name="basic-examples"></a>

- `basic_gemini_example.py` - Demonstrates the basic functionality of EasyTL with the Gemini API
- `basic_openai_example.py`- Demonstrates the basic functionality of EasyTL with the OpenAI API
- `basic_anthropic_example.py` - Demonstrates the basic functionality of EasyTL with the Anthropic API
- `basic_deepl_example.py` - Demonstrates the basic functionality of EasyTL with the DeepL API

### JSON Response Examples (in examples/structured_json/) <a name="json-response-examples"></a>

- `json_gemini_example.py` - Demonstrates how to return a JSON response with EasyTL using the Gemini API
- `json_openai_example.py` - Demonstrates how to return a JSON response with EasyTL using the OpenAI API

### Production code examples (in examples/production_code/) <a name="production-code-examples"></a>

These examples are not intended to be actually ran, but rather to showcase how EasyTL can be used in production code.

- `cost_estimate_example.py` - Showcases some production code found in [Kudasai](https://github.com/bikatr7/kudasai) that uses EasyTL to estimate the cost of a translation job.
- `translation_example.py` - Showcases some production code found in [Kudasai](https://github.com/bikatr7/kudasai) that uses EasyTL to translate text.