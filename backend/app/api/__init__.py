from .worker import router as worker_router
from .area import router as area_router
from .section import router as section_router
from .error_report import router as error_report_router

from fastapi import APIRouter

router = APIRouter()

router.include_router(worker_router, prefix="/workers", tags=["Workers"])
router.include_router(area_router, prefix="/areas", tags=["Areas"])
router.include_router(section_router, prefix="/sections", tags=["Sections"])
router.include_router(error_report_router, prefix="/error_reports", tags=["Error Reports"])
