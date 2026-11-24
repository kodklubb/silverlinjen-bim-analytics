from pathlib import Path

import ifcopenshell


def load_ifc(file_path: str | Path) -> ifcopenshell.file:
    """Load an IFC model from a file."""

    path = Path(file_path)

    if not path.is_file():
        raise FileNotFoundError(
            f"IFC file not found: {path}"
        )

    if path.suffix.lower() != ".ifc":
        raise ValueError(
            f"Invalid IFC file extension: {path.suffix}"
        )

    return ifcopenshell.open(str(path))


def get_project_info(model: ifcopenshell.file) -> dict:
    """Extract basic project metadata."""

    projects = model.by_type("IfcProject")

    if not projects:
        raise ValueError("No IfcProject found in model.")

    project = projects[0]

    return {
        "project_name": project.Name,
        "project_id": project.GlobalId,
        "description": project.Description,
        "schema": model.schema,
    }


def get_elements(model: ifcopenshell.file) -> list:
    """Retrieve all IFC elements."""

    return model.by_type("IfcElement")