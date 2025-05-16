# 🤖 DeepSeek Telegram Bot

A lightweight Telegram bot that integrates with the DeepSeek API to process and respond to user queries intelligently.

---

## 🚀 Features

- Interacts with users on Telegram
- Forwards queries to the DeepSeek API
- Sends back intelligent responses from DeepSeek

---

## 🧰 Requirements

- Python 3.7 or higher
- A Telegram Bot Token
- A DeepSeek API Key and Endpoint

---

## 📦 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/deepseek-telegram-bot.git
cd deepseek-telegram-bot
```

### 2. Create and Activate a Virtual Environment

#### On macOS/Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

#### On Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install Dependencies

Install the required libraries (including `python-telegram-bot`):

```bash
pip install -r requirements.txt
```

Or manually install if no `requirements.txt`:

```bash
pip install python-telegram-bot requests python-dotenv
```

---

## 🔐 Environment Variables

Set the following environment variables either in your shell or in a `.env` file:

```env
DEEPSEEK_API_KEY=your_deepseek_api_key
DEEPSEEK_API_ENDPOINT=https://your-deepseek-api-endpoint.com
TELEGRAM_BOT_TOKEN=your_telegram_bot_token
```

You can create a `.env` file in the project directory for automatic loading.

---

## ▶️ Running the Bot

Simply run:

```bash
python bot.py
```

The bot will start and listen for incoming messages on Telegram.

---

## 📁 Project Structure

```
bot.py               # Main bot logic
.env (optional)      # Environment variables
README.md            # Project documentation
requirements.txt     # Python dependencies
```

---

## 🧪 Example Usage

> **User**: "Summarize this article..."  
> **Bot**: "Here’s a summary from DeepSeek: ..."

---

## 🛠️ Customization

- Modify `bot.py` to enhance behavior or add new features.
- Leverage the full power of the [python-telegram-bot](https://docs.python-telegram-bot.org/) library.

---

## 📄 License

This project is licensed under the MIT License.

---

## 🙌 Contributions

Feel free to fork, open issues, or submit pull requests to improve the bot!
