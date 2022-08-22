from typing import Any, List, Optional

from pydantic import BaseModel
from classification_model.processing.validation import TitanicDataInputSchema


class PredictionResults(BaseModel):
    errors: Optional[Any]
    version: str
    predictions: Optional[List[float]]


class MultipleTitanicDataInputSchema(BaseModel):
    inputs: List[TitanicDataInputSchema]

    class Config:
        schema_extra = {
            "example": {
                "inputs": [
                    {
                        "pclass": "1",
                        "name": "Master. Hudson Taylor",
                        "sex": "male",
                        "age": "29",
                        "sibsp": "0",
                        "parch": "0",
                        "ticket": "24160",
                        "fare": "211.3375",
                        "cabin": "C22",
                        "embarked": "S",
                        "boat": "?",
                        "body": "Montreal, PQ / Chesterville, ON"
                    }
                ]
            }
        }
