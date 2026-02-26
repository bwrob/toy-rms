from dataclasses import dataclass, field

import pandas as pd
import yfinance as yf


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
    stock = global_ticker_storage.get_ticker(ticker)
    options = stock.options
    all_prices = []
    for exp in options:
        opt = stock.option_chain(exp)
        calls = opt.calls
        puts = opt.puts
        calls["optionType"] = "call"
        puts["optionType"] = "put"
        all_prices.extend((calls, puts))
    return pd.concat(all_prices)


if __name__ == "__main__":
    df = prices_for_ticker("AAPL")
    df.info()
