from pprint import pprint

from core.config.settings import IFC_FILE

from core.ingestion.ifc_loader import (
    load_ifc,
    get_project_info,
    get_elements,
)


def main():
    print("Loading IFC model...")

    model = load_ifc(IFC_FILE)

    print("\nProject information:")
    pprint(get_project_info(model))

    elements = get_elements(model)

    print("\nTotal elements:", len(elements))

    print("\nIFC loader completed successfully!")


if __name__ == "__main__":
    main()