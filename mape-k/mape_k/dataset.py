from pathlib import Path

from loguru import logger
from tqdm import tqdm
import typer
import pandas as pd
from mape_k.config import RAW_DATA_DIR, INTERIM_DATA_DIR

app = typer.Typer()


@app.command()
def main(
    # ---- REPLACE DEFAULT PATHS AS APPROPRIATE ----
    input_path: Path = RAW_DATA_DIR / "sensor1.csv",
    output_path: Path = INTERIM_DATA_DIR / "dataset.csv",
    # ----------------------------------------------
):
    # ---- SETTING INDEX AND COLUMNS ----
    logger.info("Processing dataset...")
    data_df = pd.read_csv(input_path)
    cols_to_use = ["timestamp", "vibration_x", "vibration_y", "vibration_z", "class"]
    data_df = data_df[cols_to_use]
    data_df = data_df.set_index("timestamp")
    data_df.to_csv(output_path)
    logger.success("Processing dataset complete.")
    # -----------------------------------------


if __name__ == "__main__":
    app()
