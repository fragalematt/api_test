# Bitcoin Tracker (Python + Tkinter + CryptoCompare API)

Basic app that displays the live Bitcoin price in USD and shows the last updated time. Includes optional auto-refresh with a user-set refresh interval.

## Features
- Fetches live BTC price (USD) from CryptoCompare
- Displays last updated timestamp
- Auto-refresh every N seconds (default: 30)
- Start / Stop refresh controls
- Set refresh interval from the UI
- Basic error handling with on-screen error messages

## Tech Stack
- Python 3
- Tkinter (GUI)
- CryptoCompare price API

## API Used
CryptoCompare:  
`https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD,JPY,EUR`

This app currently displays USD, but the API response includes JPY and EUR as well if you want to add them to the UI.
