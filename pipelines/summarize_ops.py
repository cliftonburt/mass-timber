import pandas as pd
from pipelines.validate import moisture_schema

def summarize_moisture():
    df = pd.read_csv("data/moisture_log.csv", parse_dates=["timestamp"])
    moisture_schema.validate(df)

    print("\n📊 Moisture Summary:")
    print(df.groupby("stack_id")["internal_moisture_pct"].describe())

    print("\n🧊 Most recent 5 readings:")
    print(df.sort_values("timestamp").tail(5))


def summarize_production():
    df = pd.read_csv("data/production_log.csv", parse_dates=["timestamp"])
    production_schema.validate(df)

    print("\n⚙️ Production Summary:")
    print(df.groupby("machine_id")[["clt_panels_output", "motor_temp_c"]].mean())

    print("\n📉 Downtime Events:")
    print(df[df["status"] == "down"].tail(5))
