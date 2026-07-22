from fastapi import APIRouter
from app.schemas.profile import ProfileRequest, ProfileResponse
from app.services.data_engine_service import DataEngineService

router = APIRouter(prefix="/profile", tags=["Data Profiling"])


@router.post("", response_model=ProfileResponse)
async def profile_dataset(payload: ProfileRequest):
    """Automatically profiles dataset columns, detecting numerical, categorical, missing, and duplicate metrics."""
    return DataEngineService.profile_table(payload.dataset_id)
