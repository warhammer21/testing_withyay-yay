from typing import Any, List, Optional

from pydantic import BaseModel
#from regression_model.processing.validation import HouseDataInputSchema


class PredictionResults(BaseModel):
    errors: Optional[Any]
    version: str
    predictions: Optional[List[float]]


class ProphetInputSchema(BaseModel):
    Total_number_of_days_for_future_forecast: Optional[int]


# class MultipleHouseDataInputs(BaseModel):
#     inputs: List[HouseDataInputSchema]




class MultipleHouseDataInputs(BaseModel):
    inputs: List[ProphetInputSchema]

    class Config:
        schema_extra = {
            "example": {
                "inputs": [
                    {
                       "Total_number_of_days_for_future_forecast":31
                    }
                ]
            }
        }
