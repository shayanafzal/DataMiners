
# %%
from IPython import get_ipython

# %%
# Import Dependencies
import pandas as pd
from matplotlib import pyplot
from fbprophet import Prophet
from pandas import to_datetime
from pandas import DataFrame
import datetime as dt


# %%
# Read the dataset
sales_df = pd.read_csv("../Resources/Sales_Data - Only the columns we need.csv")
sales_df.head()


# %%
# Get to know the data types of the data in each column
sales_df.info()


# %%
# Convert the InvDate column into datetime64 format
sales_df['InvDate'] = pd.DatetimeIndex(sales_df['InvDate'])
sales_df.head()


# %%
# Remove the data after June 30, 2019 as there is a significant deline on sales
sales_df_new = sales_df.drop(sales_df[sales_df['InvDate'] > '2019-06-30'].index)
sales_df_new.tail()


# %%
# Add a new column month_year to groupby month
sales_df_new['month_year'] = pd.to_datetime(sales_df['InvDate']).dt.to_period('M')
sales_df_new.head()


# %%
# Remove the unwanted column data
sales_df_new_2 = sales_df_new.drop(["YEAR_","MONTH_","InvDate","InvNumber","Market","InvCustomer","CompanyName","ItemClass","SubCategory","Flavours","Product","Description","Config","UOM","Real_Qty"], axis=1)
sales_df_new_2.head()


# %%
# Rearrange the column position
sales_df_new_2 = sales_df_new_2[["month_year","CAD_Value"]]
sales_df_new_2.head()


# %%
# Groupby month and sum the CAD_Value i.e sales
sales_df_new_grouped = sales_df_new_2.groupby(["month_year"], as_index=False)["CAD_Value"].sum()
sales_df_new_grouped


# %%
# Check the data types
sales_df_new_grouped.info()


# %%
# from the prophet documentation every variables should have specific names hence renaming the columns
sales_df_new_grouped = sales_df_new_grouped.rename(columns = {'month_year': 'ds',
                                'CAD_Value': 'y'})
sales_df_new_grouped.head()


# %%
# Plot a time series of the existing data
sales_df_new_grouped.plot()
pyplot.show()


# %%
# Convert "ds" to timestamp format
sales_df_new_grouped['ds'] = sales_df_new_grouped['ds'].dt.to_timestamp('s').dt.strftime('%Y-%m')
sales_df_new_grouped.head()


# %%
# Check the data types
sales_df_new_grouped.info()


# %%
# Initialize Prophet library
model = Prophet()


# %%
# Fit the data in the Prophet model
model.fit(sales_df_new_grouped)


# %%
# Create a dataframe for the future period based on the desired future frequency
future = model.make_future_dataframe(periods=24,freq='M')
future.head()


# %%
# Predict the future months using the Prophet library which analyses the seasonality trends in the dataset
forecast = model.predict(future)
forecast[['ds','yhat','yhat_lower','yhat_upper']].tail() 


# %%
#future = list()
#for i in range(1, 13):
   #date = '2019-%02d' % i
   # future.append([date])
#future = DataFrame(future)
#future.columns = ['ds']
#future['ds']= to_datetime(future['ds'])


# %%
#forecast = model.predict(future)
#print(forecast[['ds','yhat','yhat_lower','yhat_upper']].head())


# %%
# Plot the predicted data. Black dots represent the actual data, blue line respresents the predicted data and blue space indicates the uncertainty which is 80% by default
fig1 = model.plot(forecast)


# %%
# Plot components for seasonality trends
fig2 = model.plot_components(forecast)


# %%
# Python plot for interactive graphs
from prophet.plot import plot_plotly, plot_components_plotly
plot_plotly(model, forecast)


# %%
# Python plot for interactive component graphs
plot_components_plotly(model, forecast)


# %%
forecast[['ds','yhat']].head()


# %%



# %%
# Arima


# %%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# %%
from statsmodels.tsa.stattools import adfuller, kpss


# %%
# Test
# ADF Test
result = adfuller(sales_df_new_grouped.y, autolag='AIC')
print(f'ADF Statistic: {result[0]}')
print(f'p-value: {result[1]}')
for key, value in result[4].items():
    print('Critial Values:')
    print(f'   {key}, {value}')


# %%
# KPSS Test
result = kpss(sales_df_new_grouped.y, regression='c')
print('\nKPSS Statistic: %f' % result[0])
print('p-value: %f' % result[1])
for key, value in result[3].items():
    print('Critial Values:')
    print(f'   {key}, {value}')


# %%
# Since P-value is greater than the significance level, let’s difference the series and see how the autocorrelation plot looks like.
# For the sales data, a monthly interval is being used to drive the model

import numpy as np, pandas as pd
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
import matplotlib.pyplot as plt
plt.rcParams.update({'figure.figsize':(9,7), 'figure.dpi':120})

# Original Series
fig, axes = plt.subplots(3, 2, sharex=True)

axes[0, 0].plot(sales_df_new_grouped.y); axes[0, 0].set_title('Original Series')
plot_acf(sales_df_new_grouped.y, ax=axes[0, 1])

# 1st Differencing
axes[1, 0].plot(sales_df_new_grouped.y.diff()); axes[1, 0].set_title('1st Order Differencing')
plot_acf(sales_df_new_grouped.y.diff().dropna(), ax=axes[1, 1])

# 2nd Differencing
axes[2, 0].plot(sales_df_new_grouped.y.diff().diff()); axes[2, 0].set_title('2nd Order Differencing')
plot_acf(sales_df_new_grouped.y.diff().diff().dropna(), ax=axes[2, 1])

plt.show()


# %%
#find the order of the AR term (p)

# PACF plot of 1st differenced series
plt.rcParams.update({'figure.figsize':(9,3), 'figure.dpi':120})

fig, axes = plt.subplots(1, 2, sharex=True)
axes[0].plot(sales_df_new_grouped.y.diff()); axes[0].set_title('1st Differencing')
axes[1].set(ylim=(0,5))
plot_pacf(sales_df_new_grouped.y.diff().dropna(), ax=axes[1])

plt.show()


# %%
# Find the order of the MA term (q)
import pandas as pd
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
import matplotlib.pyplot as plt
plt.rcParams.update({'figure.figsize':(9,3), 'figure.dpi':120})

fig, axes = plt.subplots(1, 2, sharex=True)
axes[0].plot(sales_df_new_grouped.y.diff()); axes[0].set_title('1st Differencing')
axes[1].set(ylim=(0,1.2))
plot_acf(sales_df_new_grouped.y.diff().dropna(), ax=axes[1])

plt.show()


# %%
# Building the model

from statsmodels.tsa.arima_model import ARIMA

# 1,1,2 ARIMA Model
model = ARIMA(sales_df_new_grouped.y, order=(1,1,2))
model_fit = model.fit(disp=0)
print(model_fit.summary())


# %%
# build the model without MA.2

# 1,1,1 ARIMA Model
model = ARIMA(sales_df_new_grouped.y, order=(1,1,1))
model_fit = model.fit(disp=0)
print(model_fit.summary())


# %%
# Plot residual errors
residuals = pd.DataFrame(model_fit.resid)
fig, ax = plt.subplots(1,2)
residuals.plot(title="Residuals", ax=ax[0])
residuals.plot(kind='kde', title='Density', ax=ax[1])
plt.show()


# %%
# Actual vs Fitted
model_fit.plot_predict(dynamic=False)
plt.show()


# %%
from statsmodels.tsa.arima_model import ARIMA
import pmdarima as pm

model = pm.auto_arima(sales_df_new_grouped.y, start_p=1, start_q=1,
                      test='adf',       # use adftest to find optimal 'd'
                      max_p=3, max_q=3, # maximum p and q
                      m=1,              # frequency of series
                      d=None,           # let model determine 'd'
                      seasonal=False,   # No Seasonality
                      start_P=0, 
                      D=0, 
                      trace=True,
                      error_action='ignore',  
                      suppress_warnings=True, 
                      stepwise=True)

print(model.summary())


# %%
model.plot_diagnostics(figsize=(7,5))
plt.show()


# %%
# Forecast
n_periods = 2000
fc, confint = model.predict(n_periods=n_periods, return_conf_int=True)
index_of_fc = np.arange(len(sales_df_new_grouped.y), len(sales_df_new_grouped.y)+n_periods)

# make series for plotting purpose
fc_series = pd.Series(fc, index=index_of_fc)
lower_series = pd.Series(confint[:, 0], index=index_of_fc)
upper_series = pd.Series(confint[:, 1], index=index_of_fc)

# Plot
plt.plot(sales_df_new_grouped.y)
plt.plot(fc_series, color='darkgreen')
plt.fill_between(lower_series.index, 
                 lower_series, 
                 upper_series, 
                 color='k', alpha=.15)

plt.title("Final Forecast")
plt.show()


# %%



# %%



# %%



# %%



# %%



