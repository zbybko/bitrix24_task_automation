# Bitrix24 Task Automation to Telegram

This Python project automates interaction between a developer and Bitrix24 by:
1. Retrieving current tasks from Bitrix24.
2. Sending task links to a specified Telegram group, including private groups.

## Features

- **Task Retrieval:** Fetches tasks from Bitrix24 using its API.
- **Telegram Notifications:** Sends task updates to a Telegram group or channel.
- **Private Group Support:** Works seamlessly with private Telegram groups using `Entity`.

## Prerequisites

- Python 3.8 or later installed.
- A Telegram account or bot with access to the target group.
- Bitrix24 API access credentials.

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/zbybko/bitrix24_task_automation
   cd your-repository

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate   # Linux/Mac
   venv\Scripts\activate      # Windows
   
3. Install required dependencies:
   ```bash
   pip install -r requirements.txt

## Configuration

Create a loader.py file in the root of the project with the following variables:

- CHAT_ID = "-100XXXXXXXXXX"  # Replace with your Telegram group/channel ID
- PHONE_NUMBER = "+1234567890"  # Your Telegram phone number
- API_HASH = "your_telegram_api_hash"
- API_ID = "your_telegram_api_id"




