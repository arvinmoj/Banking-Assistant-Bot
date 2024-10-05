# Banking Assistant API

This project is a banking assistant API that integrates with a Telegram bot to process user messages and interact with an external API.

## Project Structure

- **docker-compose.yml**: Defines the services, networks, and environment configurations for running the application in Docker.
- **src/**: Contains the source code for the application.
  - **tg_bot.py**: Handles Telegram bot interactions, including receiving messages and sending responses.
  - **api_handler.py**: Manages API requests to an external service.
  - **utils/**: Contains utility modules, such as logging configuration.

## Prerequisites

- Docker and Docker Compose installed on your machine.
- A `.env` file with the necessary environment variables:
  - `TELEGRAM_TOKEN`: Your Telegram bot token.
  - `API_KEY`: API key for the external service.
  - `API_URL`: URL of the external API.

## Setup

1. Clone the repository.
2. Create a `.env` file in the root directory with the required environment variables.
3. Build and run the Docker containers using Docker Compose:

   ```bash
   docker-compose up --build
   ```

## Usage

- The Telegram bot will start and listen for messages.
- Send a message to the bot, and it will process the message using the external API and respond accordingly.

## Code Overview

### Telegram Bot

The bot is implemented in `tg_bot.py` and includes:

- **send_telegram_message**: Sends messages to users via the Telegram bot.
- **handle_message**: Processes incoming messages and interacts with the external API.

Relevant code snippet: