import pandas as pd
df= pd.read_csv("IPL_dataset.csv")
print(df)
#high runs
high_runs= df["Runs"].max()
print("highest runs:",high_runs)
#top 5 players
top= df.nlargest(5,"Runs")
print(top)
#team wise average
avg= df.groupby("Team")["Runs"].mean()
print(avg)
#high strike rate
high_sr= df["strike rate"].max()
print("highest strike rate:",high_sr)
#sort by runs
sort_runs= df.sort_values("Runs",ascending=False)
print(sort_runs)