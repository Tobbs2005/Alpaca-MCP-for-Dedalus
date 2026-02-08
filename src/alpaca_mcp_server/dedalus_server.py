"""
Dedalus MCP entrypoint for Alpaca MCP Server.

This registers a minimal, explicitly enumerated toolset using Dedalus MCP's
registration model (`@tool` + `server.collect()`), then serves over Streamable HTTP.

Reference: https://github.com/dedalus-labs/dedalus-mcp-python
"""

from __future__ import annotations

import asyncio

from dedalus_mcp import MCPServer, tool

from . import alpaca_tools as _t


get_account_info = tool(description="Get current account info (balances, status, buying power).")(
    _t.get_account_info
)
get_all_positions = tool(description="Get all open positions in the account.")(_t.get_all_positions)
get_open_position = tool(description="Get details for a specific open position.")(_t.get_open_position)

get_asset = tool(description="Get details for a single asset by symbol.")(_t.get_asset)
get_all_assets = tool(description="List assets with optional filters (status, class, exchange).")(
    _t.get_all_assets
)

get_corporate_actions = tool(description="Retrieve corporate action announcements.")(_t.get_corporate_actions)
get_portfolio_history = tool(description="Get account portfolio history (equity and P/L).")(
    _t.get_portfolio_history
)

create_watchlist = tool(description="Create a watchlist with symbols.")(_t.create_watchlist)
get_watchlists = tool(description="List all watchlists for the account.")(_t.get_watchlists)
update_watchlist_by_id = tool(description="Update a watchlist's name and/or symbols by ID.")(
    _t.update_watchlist_by_id
)
get_watchlist_by_id = tool(description="Get a watchlist by its ID.")(_t.get_watchlist_by_id)
add_asset_to_watchlist_by_id = tool(description="Add a symbol to a watchlist by ID.")(
    _t.add_asset_to_watchlist_by_id
)
remove_asset_from_watchlist_by_id = tool(description="Remove a symbol from a watchlist by ID.")(
    _t.remove_asset_from_watchlist_by_id
)
delete_watchlist_by_id = tool(description="Delete a watchlist by ID.")(_t.delete_watchlist_by_id)

get_calendar = tool(description="Get market calendar for a date range.")(_t.get_calendar)
get_clock = tool(description="Get current market status and next open/close.")(_t.get_clock)

get_stock_bars = tool(description="Get historical OHLCV bars for stocks.")(_t.get_stock_bars)
get_stock_quotes = tool(description="Get historical quote data (bid/ask) for stocks.")(_t.get_stock_quotes)
get_stock_trades = tool(description="Get historical trade prints for stocks.")(_t.get_stock_trades)
get_stock_latest_bar = tool(description="Get the latest minute bar for one or more stocks.")(
    _t.get_stock_latest_bar
)
get_stock_latest_quote = tool(description="Get the latest quote for one or more stocks.")(
    _t.get_stock_latest_quote
)
get_stock_latest_trade = tool(description="Get the latest trade for one or more stocks.")(
    _t.get_stock_latest_trade
)
get_stock_snapshot = tool(description="Get comprehensive snapshots for one or more stocks.")(
    _t.get_stock_snapshot
)

get_crypto_bars = tool(description="Get historical OHLCV bars for crypto.")(_t.get_crypto_bars)
get_crypto_quotes = tool(description="Get historical quote data for crypto.")(_t.get_crypto_quotes)
get_crypto_trades = tool(description="Get historical trades for crypto.")(_t.get_crypto_trades)
get_crypto_latest_bar = tool(description="Get the latest minute bar for crypto.")(_t.get_crypto_latest_bar)
get_crypto_latest_quote = tool(description="Get the latest quote for crypto.")(_t.get_crypto_latest_quote)
get_crypto_latest_trade = tool(description="Get the latest trade for crypto.")(_t.get_crypto_latest_trade)
get_crypto_snapshot = tool(description="Get snapshot (quote/trade/bars) for crypto.")(_t.get_crypto_snapshot)
get_crypto_latest_orderbook = tool(description="Get the latest orderbook for crypto.")(
    _t.get_crypto_latest_orderbook
)

get_option_contracts = tool(description="Retrieve option contracts for underlying symbol(s).")(
    _t.get_option_contracts
)
get_option_latest_quote = tool(description="Get the latest quote for one or more option contracts.")(
    _t.get_option_latest_quote
)
get_option_snapshot = tool(
    description="Get snapshot (quote/trade/IV/Greeks) for one or more option contracts."
)(_t.get_option_snapshot)
get_option_chain = tool(description="Get option chain snapshots for an underlying symbol.")(_t.get_option_chain)

get_orders = tool(description="Retrieve orders with optional filters.")(_t.get_orders)

place_stock_order = tool(description="Place a stock order using the specified order type and parameters.")(
    _t.place_stock_order
)
place_crypto_order = tool(description="Place a crypto order (market/limit/stop_limit).")(_t.place_crypto_order)
place_option_order = tool(description="Place an options order for single or multi-leg strategies.")(
    _t.place_option_order
)

cancel_all_orders = tool(description="Cancel all open orders.")(_t.cancel_all_orders)
cancel_order_by_id = tool(description="Cancel a specific order by its ID.")(_t.cancel_order_by_id)

close_position = tool(description="Close an open position for a single symbol.")(_t.close_position)
close_all_positions = tool(description="Close all open positions.")(_t.close_all_positions)
exercise_options_position = tool(description="Exercise a held option contract.")(_t.exercise_options_position)


def build_server() -> MCPServer:
    server = MCPServer("alpaca-trading")
    for fn in [
        get_account_info,
        get_all_positions,
        get_open_position,
        get_asset,
        get_all_assets,
        get_corporate_actions,
        get_portfolio_history,
        create_watchlist,
        get_watchlists,
        update_watchlist_by_id,
        get_watchlist_by_id,
        add_asset_to_watchlist_by_id,
        remove_asset_from_watchlist_by_id,
        delete_watchlist_by_id,
        get_calendar,
        get_clock,
        get_stock_bars,
        get_stock_quotes,
        get_stock_trades,
        get_stock_latest_bar,
        get_stock_latest_quote,
        get_stock_latest_trade,
        get_stock_snapshot,
        get_crypto_bars,
        get_crypto_quotes,
        get_crypto_trades,
        get_crypto_latest_bar,
        get_crypto_latest_quote,
        get_crypto_latest_trade,
        get_crypto_snapshot,
        get_crypto_latest_orderbook,
        get_option_contracts,
        get_option_latest_quote,
        get_option_snapshot,
        get_option_chain,
        get_orders,
        place_stock_order,
        place_crypto_order,
        place_option_order,
        cancel_all_orders,
        cancel_order_by_id,
        close_position,
        close_all_positions,
        exercise_options_position,
    ]:
        server.collect(fn)
    return server


async def serve() -> None:
    server = build_server()
    await server.serve()


def main() -> None:
    asyncio.run(serve())


if __name__ == "__main__":
    main()

