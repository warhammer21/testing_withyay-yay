import json
from typing import Any
import pickle
import numpy as np
import pandas as pd
#import pandas._libs.arrays
from fastapi import APIRouter, HTTPException
from fastapi.encoders import jsonable_encoder
from loguru import logger

from statsmodels.tsa.arima.model import ARIMA




from app import __version__, schemas
from app.config import settings

api_router = APIRouter()


@api_router.get("/health", response_model=schemas.Health, status_code=200)
def health() -> dict:
    """
    Root Get
    """
    health = schemas.Health(
        name=settings.PROJECT_NAME, api_version=__version__, model_version=model_version
    )

    return health.dict()


@api_router.post("/predict")
async def predict(input_data: schemas.MultipleHouseDataInputs) -> Any:
    """
    Make house price predictions with the TID regression model
    """

    input_df = jsonable_encoder(input_data.inputs)
    input_df =input_df[0]['Total_number_of_days_for_future_forecast']
    gmv_total_final_set = pd.read_csv('https://raw.githubusercontent.com/warhammer21/Yay-Yay/main/gmv_total_final_set.csv')
    model = ARIMA(gmv_total_final_set.y, order=(1,1,2))
    model_fit = model.fit()
    k = model_fit.get_prediction(start=input_df).predicted_mean







    # prophet_final = Prophet(interval_width=0.95,changepoint_prior_scale = 0.1,holidays_prior_scale = 0.5,
    #               n_changepoints = 150,seasonality_mode= 'multiplicative')
    # prophet_final.fit(gmv_total_final_set)
    # forecast_df = prophet_final.make_future_dataframe(periods=input_df,include_history = False)
    # print(forecast_df)
    # forecast = prophet_final.predict(forecast_df)
    #forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].head()

    # Advanced: You can improve performance of your API by rewriting the
    # `make prediction` function to be async and using await here.
    logger.info(f"Making prediction on inputs: {input_data.inputs}")
    logger.info(f"Making prediction on inputs: {type(input_data.inputs)}")
    logger.info(f"Making prediction on inputs: {input_df}")
    #print(input_df.head())

    #results = make_prediction(input_data=input_df.replace({np.nan: None}))

    # if results["errors"] is not None:
    #     logger.warning(f"Prediction validation error: {results.get('errors')}")
    #     raise HTTPException(status_code=400, detail=json.loads(results["errors"]))
    #
    # logger.info(f"Prediction results: {results.get('predictions')}")
    results = 500

    return {
        'predictions':list(k)
    }
