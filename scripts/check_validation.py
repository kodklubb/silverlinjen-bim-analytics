from pprint import pprint

from core.config.settings import (
    IFC_FILE,
    MODEL_DIR,
)

from core.pipeline import (
    process_ifc,
    process_revit_csv,
)

from core.validation.data_quality import (
    validate_ifc_dataset,
    validate_revit_dataset,
)


def main():

    df_ifc = process_ifc(IFC_FILE)

    df_revit = process_revit_csv(MODEL_DIR)

    ifc_quality = validate_ifc_dataset(df_ifc)

    revit_quality = validate_revit_dataset(df_revit)

    print("\nIFC Data Quality:")
    pprint(ifc_quality)

    print("\nRevit CSV Data Quality:")
    pprint(revit_quality)

    print("\nValidation completed successfully!")


if __name__ == "__main__":
    main()