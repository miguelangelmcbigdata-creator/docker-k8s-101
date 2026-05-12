from pathlib import Path
import pandas as pd

IN_FILE = Path("input/ventas.csv")
OUT_FILE = Path("output/resumen.csv")


def main() -> None:
    df = pd.read_csv(IN_FILE)
    resumen = (
        df.groupby("categoria", as_index=False)["monto"]
        .sum()
        .rename(columns={"monto": "monto_total"})
    )
    OUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    resumen.to_csv(OUT_FILE, index=False)
    print("ETL OK")
    print(resumen)


if __name__ == "__main__":
    main()
