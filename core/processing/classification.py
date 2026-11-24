import ifcopenshell

from core.config.settings import (
    STRUCTURAL_CATEGORIES,
    CSV_CATEGORY_MAPPING,
)


def classify_ifc_element(
    element: ifcopenshell.entity_instance
) -> str:
    """Classify an IFC element into an engineering category."""

    ifc_class = element.is_a()
    name = (element.Name or "").lower()

    if ifc_class == "IfcColumn":
        return "Columns"

    if ifc_class == "IfcBeam":
        return "Beams"

    if element.is_a("IfcWall"):
        return "Walls"

    if ifc_class == "IfcFooting":
        return "Foundations"

    if ifc_class == "IfcSlab":

        if "plint" in name or "footing" in name:
            return "Foundations"

        if "sti_bro" in name:
            return "Bridge Deck"

    if ifc_class == "IfcBuildingElementProxy":

        if "model lines" in name:
            return "Reference Geometry"

    return "Unclassified"


def classify_csv_schedule(schedule_name: str) -> str:
    """Classify a Revit CSV schedule."""

    return CSV_CATEGORY_MAPPING.get(
        schedule_name,
        "Unclassified"
    )


def is_structural(category: str) -> bool:
    """Check if a category belongs to the structural scope."""

    return category in STRUCTURAL_CATEGORIES