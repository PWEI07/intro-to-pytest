from datetime import datetime

import pandas as pd

dates = [pd.Timestamp(2021,1,1), pd.Timestamp(2021,1,2), pd.Timestamp(2021,1,3), pd.Timestamp(2021,1,6)]
a = [1,2,None, 4]
b = [3.2,7,6,-10]
df = pd.DataFrame({'dates': dates, 'a': a, 'b': b},index=dates)
df.interpolate(method='time')
df.loc[pd.Timestamp(2021,1,5)] = [pd.Timestamp(2021,1,5), 2,None]
df.interpolate(method='time')

