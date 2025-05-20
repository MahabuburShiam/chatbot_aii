# AI Chat Log Summarizer

This is a Python-based tool that summarizes chat logs between a user and an AI. It counts messages, identifies keywords, and gives a simple summary of the conversation.

## Features

- Parses chat logs from `.txt` files
- Counts total, user, and AI messages
- Extracts top 5 keywords (excluding stop words)
- Outputs a simple conversation summary
## sample chat
User: Hello!
AI: Hi! How can I assist you today?
User: Can you explain what Python is?
AI: Sure! Python is a popular programming language.
User: What can I use it for?
AI: You can use Python for web development, data analysis, and AI.

## Sample Output
Summary:
- The conversation had 6 exchanges.
- User sent 3 messages, AI sent 3.
- Most common keywords: python, use, data, ai, development
- The user asked mainly about Python and its uses.

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
