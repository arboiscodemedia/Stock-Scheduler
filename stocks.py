import pandas as pd
from alpha_vantage.timeseries import TimeSeries
import time

api_key = 'GLI74OU8A24234L1'

ts = TimeSeries(key=api_key, output_format='pandas')
data, meta_data = ts.get_intraday(symbol='MSFT', interval = '1min', outputsize = 'full')
#print(data)
df =  pd.DataFrame(data)

filename= "filename"
timestr= time.strftime("%Y%m%d-%H%M%S")


df.to_excel("./file-storage/"+filename+timestr+".xlsx",sheet_name='Results')