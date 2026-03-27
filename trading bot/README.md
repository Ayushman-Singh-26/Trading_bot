# Binance Futures Testnet Trading Bot

## Setup

1. Clone repo
2. Install dependencies:

```
pip install -r requirements.txt
```
3. Create `.env` file and add:

```
API_KEY=your_key
API_SECRET=your_secret
```

## Run Example

### Market Order
```
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001
```

### Limit Order
```
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 60000
```

## Features

- Market & Limit Orders
- CLI Input
- Input Validation
- Logging (`trading_bot.log`)
- Error Handling

## Assumptions

- Using Binance Futures Testnet
- Only USDT-M futures supported
