
from pydantic import BaseModel


class QuantityKPIs(BaseModel):
    total_elements: int
    structural_elements: int
    excluded_elements: int
    total_volume_m3: float | None
    category_count: int
    material_count: int


class CategoryBreakdown(BaseModel):
    category: str
    element_count: int
    total_volume_m3: float | None
    average_volume_m3: float | None
    min_volume_m3: float | None
    max_volume_m3: float | None
    volume_share_pct: float | None


class StructuralElement(BaseModel):
    global_id: str
    ifc_class: str
    name: str | None
    category: str | None
    material: str | None
    net_volume_m3: float | None


class QuantityReport(BaseModel):
    project: str
    model: str
    section: str
    source: str

    kpis: QuantityKPIs
    categories: list[CategoryBreakdown]
    elements: list[StructuralElement]
