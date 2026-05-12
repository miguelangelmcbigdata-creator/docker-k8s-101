import os
import random
import psycopg

DATABASE_URL = os.environ["DATABASE_URL"]

def main():
    with psycopg.connect(DATABASE_URL) as conn:
        with conn.cursor() as cur:
            cur.execute("CREATE TABLE IF NOT EXISTS metrics (metric text, value int)")
            cur.execute("DELETE FROM metrics")
            cur.execute("INSERT INTO metrics VALUES (%s,%s)", ("visitas", random.randint(50, 200)))
            cur.execute("INSERT INTO metrics VALUES (%s,%s)", ("ventas", random.randint(1, 20)))
        conn.commit()
    print("ETL OK")

if __name__ == "__main__":
    main()