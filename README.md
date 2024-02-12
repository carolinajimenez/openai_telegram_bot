# Chatbot with OpenAI and Telegram

This is a simple chatbot that utilizes the OpenAI API to generate responses based on the GPT-3.5 language model. The chatbot is integrated with Telegram to enable interactive conversations.

## Setup

### Prerequisites

Make sure to have the following libraries installed before running the bot:

- `openai`
- `requests`

You can install them using:

```bash
pip install openai requests
```

### Environment Variables
Before running the bot, configure the following environment variables:

* OPENAI_API_KEY: OpenAI API key. You can obtain it by registering on OpenAI Platform.
* TELEGRAM_TOKEN: Telegram bot access token. You can obtain it by creating a new bot on BotFather.
* OPENAI_PLATZI_MODEL: Specific OpenAI model to use.

## Usage

Run the chatbot.py script:

```bash
python3 src/main.py
```

The bot will be up and running, responding to messages sent through Telegram. (Open Telegram app and start to chat with the bot)

### Code Operation

* get_updates(offset): Retrieves Telegram message updates.
* send_message(chat_id, text): Sends messages through the Telegram API.
* get_openai_response(prompt, model): Retrieves responses from OpenAI GPT-3.5 based on user messages.
* main(): Initiates the main loop of the bot.

### Error Handling

The code handles possible connection errors and rate limits when interacting with the OpenAI API.
