import pandas as pd
df= pd.read_csv("weather_dataset.csv")
print(df)
#average temparature
avg= df["Temperature"].mean()
print(avg)
#hottest city
hot= df.loc[df["humidity"].idxmax()]
print(hot)
#coldest city
cool= df.loc[df["humidity"].idxmin()]
print(cool)
#city with above 35 temperature
cities= df[df["Temperature"]>35]
print(cities)
#sort by rainfall
sort= df.sort_values("rainfall",ascending=True)
print(sort)