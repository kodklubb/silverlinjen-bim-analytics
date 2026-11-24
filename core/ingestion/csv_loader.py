from pathlib import Path

import pandas as pd


def load_csv(file_path: str | Path) -> pd.DataFrame:
    """Load a single Revit CSV schedule."""

    path = Path(file_path)

    if not path.is_file():
        raise FileNotFoundError(
            f"CSV file not found: {path}"
        )

    if path.suffix.lower() != ".csv":
        raise ValueError(
            f"Invalid CSV extension: {path.suffix}"
        )

    return pd.read_csv(
        path,
        encoding="utf-8-sig"
    )


def load_csv_directory(
    directory: str | Path
) -> dict[str, pd.DataFrame]:
    """Load all CSV schedules from a directory."""

    path = Path(directory)

    if not path.is_dir():
        raise NotADirectoryError(
            f"Directory not found: {path}"
        )

    csv_files = sorted(path.glob("*.csv"))

    if not csv_files:
        raise ValueError(
            f"No CSV files found in: {path}"
        )

    return {
        file.stem: load_csv(file)
        for file in csv_files
    }