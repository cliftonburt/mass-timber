import pandas as pd
import random
from datetime import datetime, timedelta
from pathlib import Path

DATA_DIR = Path("data")
STACK_IDS = [f"STACK-{i+1}" for i in range(5)]

def simulate_moisture(count=10):
    rows = []
    now = datetime.utcnow()

    for _ in range(count):
        ts = now.isoformat()
        stack_id = random.choice(STACK_IDS)
        ambient_temp = round(random.uniform(50, 90), 1)
        ambient_humidity = round(random.uniform(30, 90), 1)
        covered = random.choice(["yes", "no"])

        # Moisture content logic
        base = 18 if covered == "yes" else 22
        drift = random.uniform(-2.0, 2.0)
        humidity_effect = (ambient_humidity - 50) * 0.05
        internal_moisture = round(max(8, base + drift + humidity_effect), 1)

        rows.append({
            "timestamp": ts,
            "stack_id": stack_id,
            "ambient_temp_f": ambient_temp,
            "ambient_humidity_pct": ambient_humidity,
            "internal_moisture_pct": internal_moisture,
            "covered": covered
        })
        now += timedelta(minutes=10)

    df = pd.DataFrame(rows)
    output_file = DATA_DIR / "moisture_log.csv"
    df.to_csv(output_file, mode='a', header=not output_file.exists(), index=False)
    print(f"✅ Simulated {count} moisture records.")
