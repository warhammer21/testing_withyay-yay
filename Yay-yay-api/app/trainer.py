import pandas as pd
from statsmodels.tsa.arima.model import ARIMA


gmv_total_final_set = pd.read_csv('https://raw.githubusercontent.com/warhammer21/Yay-Yay/main/gmv_total_final_set.csv')
model = ARIMA(gmv_total_final_set.y, order=(1,1,2))
model_fit = model.fit()
k = model_fit.get_prediction(start=-5).predicted_mean
print(k,len(k))
