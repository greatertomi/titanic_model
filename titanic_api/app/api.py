import schemas
from typing import Any
import json
import numpy as np
import pandas as pd
from loguru import logger

from fastapi import APIRouter, HTTPException
from fastapi.encoders import jsonable_encoder
from .config import settings
from classification_model import __version__ as model_version
from classification_model.predict import make_prediction

api_router = APIRouter()

version = "0.0.3"


@api_router.get('/titanic', response_model=schemas.Titanic, status_code=200)
def titanic() -> dict:
    titanic = schemas.Titanic(name=settings.PROJECT_NAME, api_version=version, model_version=model_version)
    return titanic.dict()


async def predict(input_data: schemas.MultipleTitanicDataInputSchema) -> Any:
    input_df = pd.DataFrame(jsonable_encoder(input_data.inputs))
    logger.info(f"Making predictions on inputs: {input_data.inputs}")
    results = make_prediction(input_data=input_df.replace({np.nan: None}))

    if results["errors"] is not None:
        logger.warning(f"Prediction validation error: {results.get('errors')}")
        raise HTTPException(status_code=400, detail=json.loads(results["errors"]))

    logger.info(f"Prediction results: {results.get('predictions')}")

    return results
