from collections import Counter
from pprint import pprint

from core.config.settings import IFC_FILE, MODEL_DIR

from core.ingestion.ifc_loader import (
    load_ifc,
    get_elements,
)

from core.ingestion.csv_loader import (
    load_csv_directory,
)

from core.processing.classification import (
    classify_ifc_element,
    classify_csv_schedule,
    is_structural,
)


def main():

    # IFC Classification
    model = load_ifc(IFC_FILE)
    elements = get_elements(model)

    categories = [
        classify_ifc_element(element)
        for element in elements
    ]

    print("\nIFC category distribution:")
    pprint(dict(Counter(categories)))

    structural_count = sum(
        is_structural(category)
        for category in categories
    )

    print("\nStructural elements:", structural_count)

    # CSV Ingestion
    datasets = load_csv_directory(MODEL_DIR)

    print("\nCSV schedules:")

    for name, df in datasets.items():

        category = classify_csv_schedule(name)

        print(
            f"{category}: {len(df)} rows"
        )

    print("\nTotal CSV files:", len(datasets))

    print(
        "Total CSV rows:",
        sum(len(df) for df in datasets.values())
    )

    print("\nIngestion check completed!")


if __name__ == "__main__":
    main()