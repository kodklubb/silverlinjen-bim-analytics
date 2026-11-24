import ifcopenshell

from ifcopenshell.util.element import get_materials


def extract_material(
    element: ifcopenshell.entity_instance
) -> str | None:
    """Extract material names associated with an IFC element."""

    materials = get_materials(
        element,
        should_inherit=True
    )

    names = [
        material.Name.strip()
        for material in materials
        if material.Name and material.Name.strip()
    ]

    unique_names = list(dict.fromkeys(names))

    return " | ".join(unique_names) if unique_names else None