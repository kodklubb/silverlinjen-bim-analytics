
from fastapi import APIRouter

from apps.api.schemas.quantities import QuantityReport
from apps.api.services.quantity_service import (
    get_quantity_report,
)


router = APIRouter(
    prefix="/quantities",
    tags=["Quantity Analytics"],
)


@router.get(
    "/summary",
    response_model=QuantityReport,
)
def quantity_summary() -> QuantityReport:
    return get_quantity_report()
