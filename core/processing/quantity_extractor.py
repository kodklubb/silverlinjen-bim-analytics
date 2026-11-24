import ifcopenshell

from ifcopenshell.util.element import get_psets


def extract_quantities(
    element: ifcopenshell.entity_instance
) -> dict:
    """Extract quantity values from IFC quantity sets."""

    quantity_sets = get_psets(
        element,
        qtos_only=True,
        should_inherit=False
    )

    quantities = {}

    for set_name, values in quantity_sets.items():
        for key, value in values.items():

            if key == "id":
                continue

            if key in quantities and quantities[key] != value:
                raise ValueError(
                    f"Conflicting quantity: {key} "
                    f"for {element.GlobalId}"
                )

            quantities[key] = value

    return quantities