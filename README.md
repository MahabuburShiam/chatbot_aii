# AI Chat Log Summarizer

This is a Python-based tool that summarizes chat logs between a user and an AI. It counts messages, identifies keywords, and gives a simple summary of the conversation.

## Features

- Parses chat logs from `.txt` files
- Counts total, user, and AI messages
- Extracts top 5 keywords (excluding stop words)
- Outputs a simple conversation summary

## Sample Output


## How to Run

1. Clone the repository
2. Navigate to the project folder
3. Install dependencies:
    ```bash
    pip install nltk
    ```
4. Run the script:
    ```bash
    python main.py
    ```

## Notes

- Requires a `chat.txt` file in the `samples/` folder
- Built using basic Python and NLTK for NLP tasks
