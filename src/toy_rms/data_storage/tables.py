"""Data storage utilities for toy-rms."""

from sqlalchemy import Engine
from sqlmodel import Field, SQLModel, create_engine


class OptionPrice(SQLModel, table=True):
    """SQLModel table to store option price data from yfinance."""

    contract_symbol: str = Field(default=None, primary_key=True)
    last_trade_date: str
    strike: float
    last_price: float
    bid: float
    ask: float
    change: float
    percent_change: float
    volume: float
    open_interest: int
    implied_volatility: float
    in_the_money: bool
    contract_size: str
    currency: str
    option_type: str


def get_engine() -> Engine:
    """Get a SQLAlchemy engine for the SQLite database."""
    sqlite_file_name = "database.db"
    sqlite_url = f"sqlite:///{sqlite_file_name}"
    return create_engine(sqlite_url, echo=True)


def migrate_db() -> None:
    """Create the database tables if they don't exist."""
    engine = get_engine()
    SQLModel.metadata.create_all(engine)


if __name__ == "__main__":
    migrate_db()
