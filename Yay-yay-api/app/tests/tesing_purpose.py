from fbprophet import Prophet
import pickle
import numpy as np
import pandas as pd

# pkl_path = "/Users/shreyakvashisht/PycharmProjects/deploying-machine-learning-models/section-06-model-serving-api/Yay-yay-api/app/tests/Prophet.pkl"
#
# with open(pkl_path, 'rb') as f:
#         m = pickle.load(f)
#         #forecast_df = m.make_future_dataframe(periods=31)
gmv_total_final_set = pd.read_csv('/Users/shreyakvashisht/PycharmProjects/Yay-Yay/gmv_total_final_set.csv')
prophet_final = Prophet(interval_width=0.95,changepoint_prior_scale = 0.1,holidays_prior_scale = 0.5,
                  n_changepoints = 150,seasonality_mode= 'multiplicative')
prophet_final.fit(gmv_total_final_set)

import pickle
pkl_path = "Prophet_checked.pkl"
with open(pkl_path, "wb") as f:
    # Pickle the 'Prophet' model using the highest protocol available.
    pickle.dump(prophet_final, f)

