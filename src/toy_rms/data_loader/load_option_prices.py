"""Load option prices for a given ticker symbol."""

from dataclasses import dataclass, field
from typing import NamedTuple, cast

import pandas as pd
import yfinance as yf

from toy_rms.data_storage.tables import OptionPrice, get_engine
from toy_rms.utils.naming import to_snake_case


class Options(NamedTuple):
    """Named tuple to hold options data from yfinance."""

    calls: pd.DataFrame
    puts: pd.DataFrame
    underlying: pd.DataFrame


@dataclass
class TickerStorage:
    """A simple storage class for yfinance Ticker objects.

    Tickers have internal caching, store them in memory to avoid redundant API calls.
    """

    tickers: dict[str, yf.Ticker] = field(default_factory=dict)

    def get_ticker(self, ticker_symbol: str) -> yf.Ticker:
        """Get a Ticker object for the given ticker symbol.

        Creating it if it doesn't exist.
        """
        if ticker_symbol not in self.tickers:
            self.tickers[ticker_symbol] = yf.Ticker(ticker_symbol)
        return self.tickers[ticker_symbol]


global_ticker_storage = TickerStorage()


def prices_for_ticker(ticker: str) -> pd.DataFrame:
    """DataFrame of option prices for the given ticker symbol."""
    stock = global_ticker_storage.get_ticker(ticker)
    options = stock.options
    all_prices = []
    for expiry in options:
        options = cast("Options", stock.option_chain(expiry))
        calls = options.calls
        puts = options.puts
        calls["optionType"] = "call"
        puts["optionType"] = "put"
        all_prices.extend((calls, puts))
    return pd.concat(all_prices).rename(columns=to_snake_case).reset_index(drop=True)


def store_prices_to_db(ticker: str) -> None:
    """Store option prices for the given ticker symbol to the database."""
    engine = get_engine()
    prices = prices_for_ticker(ticker)
    prices.to_sql(
        name=str(OptionPrice.__tablename__),
        con=engine,
        if_exists="replace",
        index=False,
    )


if __name__ == "__main__":
    df = prices_for_ticker("AAPL")
    df.info()
    store_prices_to_db("AAPL")
