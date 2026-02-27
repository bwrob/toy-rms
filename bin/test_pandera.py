from functools import cache

import pandas as pd
import pandera.pandas as pa
from annotated_types import Ge, Gt, Le, Lt, MaxLen, MinLen
from pydantic.fields import FieldInfo
from rich import inspect
from sqlmodel import Field, SQLModel, create_engine


def sqlmodel_to_pa_checks(field_info: FieldInfo) -> list[pa.Check]:
    """Extracts Pydantic/SQLModel metadata and converts to vectorized Pandera checks."""
    checks = []

    # SQLModel/Pydantic v2 stores constraints in the 'metadata' list
    for meta in field_info.metadata:
        if isinstance(meta, Gt):
            checks.append(pa.Check.gt(meta.gt))
        elif isinstance(meta, Ge):
            checks.append(pa.Check.ge(meta.ge))
        elif isinstance(meta, Lt):
            checks.append(pa.Check.lt(meta.lt))
        elif isinstance(meta, Le):
            checks.append(pa.Check.le(meta.le))
        elif isinstance(meta, MinLen):
            checks.append(pa.Check.str_length(min_value=meta.min_length))
        elif isinstance(meta, MaxLen):
            checks.append(pa.Check.str_length(max_value=meta.max_length))

    return checks


@cache
def get_pandera_schema(model: type[SQLModel]) -> pa.DataFrameSchema:
    columns = {}

    for field_name, field_info in model.model_fields.items():
        # 1. Determine the basic type
        dtype = field_info.annotation

        # 2. Extract vectorized checks from Pydantic metadata
        pa_checks = sqlmodel_to_pa_checks(field_info)

        columns[field_name] = pa.Column(
            dtype,
            nullable=not field_info.is_required(),
            checks=pa_checks,
        )

    return pa.DataFrameSchema(
        columns, strict=True, coerce=True, name=model.__tablename__
    )


class Trade(SQLModel, table=True):
    trade_id: str = Field(primary_key=True)
    symbol: str = Field(index=True)
    quantity: float = Field(gt=0)
    price: float
    notional: float


def fast_ingest(df: pd.DataFrame, schema: pa.DataFrameSchema) -> None:
    # This is 100% vectorized. No row-wise Pydantic calls.
    validated_df = schema.validate(df)

    # High speed insert
    with engine.begin() as conn:
        validated_df.to_sql(str(schema.name), conn, if_exists="replace", index=False)


if __name__ == "__main__":
    trade_schema = get_pandera_schema(Trade)
    inspect(trade_schema.columns["quantity"])

    engine = create_engine("sqlite:///risk_mgmt.db")

    inspect(SQLModel.metadata.tables)
    SQLModel.metadata.create_all(engine)

    df = pd.DataFrame(
        {
            "trade_id": ["T1"],
            "symbol": ["AAPL"],
            "quantity": [10.0],
            "price": [150.0],
            "notional": [1500.0],
        }
    )
    fast_ingest(df, trade_schema)
