import warnings
warnings.filterwarnings('ignore', category=UserWarning)

import pandera as pa
from pandera import Column, DataFrameSchema


moisture_schema = DataFrameSchema({
    "timestamp": Column(pa.DateTime),
    "stack_id": Column(str),
    "ambient_temp_f": Column(float, checks=pa.Check.ge(30)),
    "ambient_humidity_pct": Column(float, checks=pa.Check.between(0, 100)),
    "internal_moisture_pct": Column(float, checks=pa.Check.ge(0)),
    "covered": Column(str, checks=pa.Check.isin(["yes", "no"]))
})


production_schema = DataFrameSchema({
    "timestamp": Column(pa.DateTime),
    "machine_id": Column(str),
    "status": Column(str, checks=pa.Check.isin(["running", "idle", "down"])),
    "clt_panels_output": Column(int, checks=pa.Check.ge(0)),
    "motor_temp_c": Column(float, checks=pa.Check.ge(0)),
    "vibration_level": Column(float, checks=pa.Check.ge(0))
})
