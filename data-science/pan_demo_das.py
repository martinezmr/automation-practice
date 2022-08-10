import pandas as pd

olympic_series_participation = pd.Series([205,204,201,200,197], index = [2012,2008,2004,2000,1996])
olympic_series_country = pd.Series(['London', 'Beijing', 'Athens', 'Sydney', 'Atlanta'], index=[2012,2008,2004,2000,1996])

df_olympic_series = pd.DataFrame({'No. of Participating Countries': olympic_series_participation, 'Host Cities': olympic_series_country})

print(df_olympic_series)