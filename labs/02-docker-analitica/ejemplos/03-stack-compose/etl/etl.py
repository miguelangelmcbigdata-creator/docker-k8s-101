import os
import random
from sqlalchemy import create_engine, text
import pandas as pd

DATABASE_URL = os.environ["DATABASE_URL"]


def main() -> None:
    engine = create_engine(DATABASE_URL)
    df = pd.DataFrame(
        {
            "metric": ["visitas", "ventas"],
            "value": [random.randint(80, 200), random.randint(5, 30)],
        }
    )
    with engine.begin() as conn:
        conn.execute(text("CREATE TABLE IF NOT EXISTS metrics (metric TEXT, value INT)"))
        conn.execute(text("DELETE FROM metrics"))
        for _, row in df.iterrows():
            conn.execute(
                text("INSERT INTO metrics (metric, value) VALUES (:m, :v)"),
                {"m": row["metric"], "v": int(row["value"])},
            )
    print("ETL OK")


if __name__ == "__main__":
    main()
