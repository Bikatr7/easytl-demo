```markdown
# EasyTL Use Case Demonstration

## This is a work in progress

This repository demonstrates a use case for the EasyTL Python package. [EasyTL GitHub Repository](https://github.com/bikatr7/easytl)

### Getting Started

1. Navigate to the project directory:
    ```bash
    cd easytl-demo
    ```
2. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```
3. Create the following API key files in the root directory (at least one is required):
    - `gemini.txt` with your Google API key
    - `openai.txt` with your OpenAI API key
    - `anthropic.txt` with your Anthropic API key

### Running the Code

Pick an example from the `examples` directory and run it. For example:
```bash
python examples/basic_gemini_example.py
```

In the root of `examples/`, you will find generic basic examples for each API. You can use these as a starting point for what EasyTL can do. Some examples require specific APIs.

### Available Examples (More to come)

- `basic_x_example.py` - Demonstrates the basic functionality of EasyTL with each API (Gemini, OpenAI, Anthropic)
- `json_gemini_example.py` - Demonstrates how to return a JSON response with EasyTL using the Gemini API
- `json_openai_example.py` - Demonstrates how to return a JSON response with EasyTL using the OpenAI API
```