# Gemini API Answer Generator

## Overview

This project is a tool for generating answers based on prompts using the Gemini API key. It utilizes a chaining process to gather information from the Gemini API and form responses to given prompts.

## Features

- **Prompt-based Answer Generation**: Given a prompt, the tool interacts with the Gemini API to collect relevant data and generate an answer.
  
- **Chaining Process**: The tool employs a chaining process to gather additional context and refine responses, enhancing the accuracy and relevance of generated answers.
  
- **Customization**: Users can customize the behavior of the tool by adjusting parameters and configurations to suit their specific requirements.

## Installation

1. Clone the repository to your local machine:

    ```bash
    git clone https://github.com/your_username/gemini-api-answer-generator.git
    ```

2. Navigate to the project directory:

    ```bash
    cd gemini-api-answer-generator
    ```

3. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Obtain Gemini API Key: Visit the Gemini website and register for an API key.

2. Configure API Key: Replace `'YOUR_API_KEY'` and `'YOUR_API_SECRET'` in the `config.py` file with your Gemini API key and secret.

3. Run the tool:

    ```bash
    python answer_generator.py
    ```

4. Follow the prompts to input your query or question.

5. View the generated answer.

## Contributing

Contributions are welcome! If you have any ideas for improvements, new features, or bug fixes, please open an issue or submit a pull request.
