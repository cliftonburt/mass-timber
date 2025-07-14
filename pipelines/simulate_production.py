import pandas as pd
import random
from datetime import datetime, timedelta
from pathlib import Path

DATA_DIR = Path("data")
MACHINE_IDS = [f"CNC-{i+1}" for i in range(3)]

def simulate_production(count=10):
    rows = []
    now = datetime.utcnow()

    for _ in range(count):
        timestamp = now.isoformat()
        machine_id = random.choice(MACHINE_IDS)
        status = random.choices(["running", "idle", "down"], weights=[0.7, 0.2, 0.1])[0]
        clt_panels_output = random.randint(1, 3) if status == "running" else 0
        temp_c = round(random.uniform(30, 90), 1)
        vibration_level = round(random.uniform(0.1, 2.5), 2) if status == "running" else 0.0

        rows.append({
            "timestamp": timestamp,
            "machine_id": machine_id,
            "status": status,
            "clt_panels_output": clt_panels_output,
            "motor_temp_c": temp_c,
            "vibration_level": vibration_level
        })
        now += timedelta(minutes=5)

    df = pd.DataFrame(rows)
    output_file = DATA_DIR / "production_log.csv"
    df.to_csv(output_file, mode='a', header=not output_file.exists(), index=False)
    print(f"✅ Simulated {count} production records.")
