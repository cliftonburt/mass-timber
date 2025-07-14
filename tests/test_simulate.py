from pipelines.simulate_moisture import simulate_moisture
from pathlib import Path
import pandas as pd

def test_simulate_output():
    simulate_moisture(5)
    df = pd.read_csv(Path("data/moisture_log.csv"))
    assert not df.empty
    assert "internal_moisture_pct" in df.columns
