from nsepy import get_history
from datetime import datetime
import dateutil.relativedelta
import pandas as pd
to_date=datetime.now()
to_date=datetime.strftime(to_date,'%Y %m %d')
to_date=datetime.strptime(to_date,'%Y %m %d')
from_date=to_date - dateutil.relativedelta.relativedelta(months=18)   #can write months=6 | manths=10 | year=1 | days=10
data=get_history(symbol='HINDUNILVR',start=from_date,end=to_date)
# print(data)
df = pd.DataFrame(data)
df.to_csv('file2.csv')
