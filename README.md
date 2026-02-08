# Alpaca MCP for Dedalus (Dedalus MCP Python)

This repo packages a **Dedalus MCP** server that exposes a curated subset of Alpaca Trading + Market Data tools over **Streamable HTTP** using Dedalus MCP’s registration model.

Built against the Dedalus MCP Python framework: [dedalus-labs/dedalus-mcp-python](https://github.com/dedalus-labs/dedalus-mcp-python)

## What’s included

The server registers these tools (no `get_news`):

- Account/positions: `get_account_info`, `get_all_positions`, `get_open_position`
- Assets: `get_asset`, `get_all_assets`
- Corporate actions / history: `get_corporate_actions`, `get_portfolio_history`
- Watchlists: `create_watchlist`, `get_watchlists`, `update_watchlist_by_id`, `get_watchlist_by_id`, `add_asset_to_watchlist_by_id`, `remove_asset_from_watchlist_by_id`, `delete_watchlist_by_id`
- Market: `get_calendar`, `get_clock`
- Stocks: `get_stock_bars`, `get_stock_quotes`, `get_stock_trades`, `get_stock_latest_bar`, `get_stock_latest_quote`, `get_stock_latest_trade`, `get_stock_snapshot`
- Crypto: `get_crypto_bars`, `get_crypto_quotes`, `get_crypto_trades`, `get_crypto_latest_bar`, `get_crypto_latest_quote`, `get_crypto_latest_trade`, `get_crypto_snapshot`, `get_crypto_latest_orderbook`
- Options: `get_option_contracts`, `get_option_latest_quote`, `get_option_snapshot`, `get_option_chain`
- Orders: `get_orders`, `place_stock_order`, `place_crypto_order`, `place_option_order`, `cancel_all_orders`, `cancel_order_by_id`
- Positions: `close_position`, `close_all_positions`, `exercise_options_position`

Tool implementations live in `src/alpaca_mcp_server/alpaca_tools.py` and are registered for Dedalus in `src/alpaca_mcp_server/dedalus_server.py`.

## Requirements

- Python **3.10+**
- Alpaca API keys (paper or live)

## Configuration

Set these environment variables:

- `ALPACA_API_KEY`
- `ALPACA_SECRET_KEY`
- `ALPACA_PAPER_TRADE` (optional, default `True`)

Optional overrides (advanced):

- `TRADE_API_URL`, `TRADE_API_WSS`, `DATA_API_URL`, `STREAM_DATA_WSS`

## Run locally

Install and run using your preferred workflow (pip/uv). The package entrypoint is:

```bash
alpaca-mcp-dedalus
```

By default Dedalus MCP serves Streamable HTTP on port **8000**.

## Run with Docker

Build and run:

```bash
docker build -t alpaca-mcp-dedalus .
docker run --rm -p 8000:8000 \
  -e ALPACA_API_KEY=... \
  -e ALPACA_SECRET_KEY=... \
  -e ALPACA_PAPER_TRADE=True \
  alpaca-mcp-dedalus
```

## Notes

- This repo is **Dedalus-only** (FastMCP is not the deployment path here).
- Do not commit real credentials. Use environment variables in your deployment platform.

