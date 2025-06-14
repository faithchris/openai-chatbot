# OpenAI Chatbot with Python

This is a simple AI-powered chatbot built using Python and the OpenAI API. It takes user input and returns an AI-generated response using GPT models.

## Features

- OpenAI Chat Completion integration
- Secure API key handling with `.env`
- Virtual environment setup with `venv`
- Supports both GPT-4o and GPT-3.5-turbo models

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/faithchris/openai-chatbot.git
cd openai-chatbot

### 2. Create and Activate a Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate

### 3. Install Dependencies

After activating your virtual environment, install the required Python packages using pip:

```bash
pip install -r requirements.txt

### 4. Add Your API Key

Create a `.env` file in the root directory and add your OpenAI API key:

```env
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx


### 5. Run the Chatbot

Once everything is set up, you can run the chatbot using:

```bash
python chatt.py
