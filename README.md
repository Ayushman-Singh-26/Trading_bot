# 🚀 Binance Futures Testnet Trading Bot

A lightweight, modular Python CLI application that places MARKET and LIMIT orders on the Binance Futures Testnet (USDT-M).

Built as part of a technical assignment to demonstrate API integration, clean architecture, validation, and logging.

---

## 📌 Features

* ✅ Place MARKET and LIMIT orders
* ✅ Supports BUY and SELL sides
* ✅ CLI-based input using arguments
* ✅ Input validation (symbol, side, type, quantity, price)
* ✅ Structured project architecture
* ✅ Logging of requests, responses, and errors
* ✅ Exception handling for API & user input errors

---

## 🏗️ Project Structure

```
trading_bot/
│
├── bot/
│   ├── client.py          # Binance client wrapper
│   ├── orders.py          # Order placement logic
│   ├── validators.py      # Input validation
│   ├── logging_config.py  # Logging setup
│
├── cli.py                 # CLI entry point
├── .env                   # API credentials (not committed)
├── requirements.txt
└── README.md
```

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```
git clone https://github.com/your-username/trading-bot.git
cd trading-bot
```

### 2. Create Virtual Environment

```
python -m venv .venv
.venv\Scripts\activate   # Windows
# or
source .venv/bin/activate  # Mac/Linux
```

### 3. Install Dependencies

```
pip install -r requirements.txt
```

---

## 🔑 Binance Testnet Setup

1. Go to Binance Futures Testnet:
   https://testnet.binancefuture.com

2. Create API Key & Secret

3. Create a `.env` file in root:

```
API_KEY=your_api_key
API_SECRET=your_api_secret
BASE_URL=https://testnet.binancefuture.com/fapi
```

---

## ▶️ Usage

### MARKET Order

```
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001
```

### LIMIT Order

```
python cli.py --symbol BTCUSDT --side BUY --type LIMIT --quantity 0.001 --price 30000
```

---

## 📊 Example Output

```
=== ORDER SUCCESS ===
Order ID: 12345678
Status: FILLED
Executed Qty: 0.001
Avg Price: 29850.00
```

---

## 📝 Logging

* Logs are stored in:

```
logs/app.log
```

* Includes:

  * API requests
  * API responses
  * Errors & exceptions

---

## ⚠️ Error Handling

Handles:

* Invalid CLI inputs
* Missing parameters
* API errors
* Network failures

---

## 📦 Requirements

* Python 3.x
* python-binance
* python-dotenv

---

## 💡 Assumptions

* Only USDT-M Futures are supported
* Testnet environment is used (no real funds)
* CLI arguments are provided correctly

---

## 🔥 Possible Improvements (Bonus)

* Add Stop-Limit / OCO orders
* Improve CLI UX (interactive prompts)
* Add simple UI dashboard
* Add unit tests

---

## 📧 Submission

Includes:

* Source code
* README
* Log files for:

  * MARKET order
  * LIMIT order

---

## 📜 License

This project is for educational and evaluation purposes.
