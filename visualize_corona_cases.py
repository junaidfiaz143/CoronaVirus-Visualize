import pandas as pd
import matplotlib.pyplot as plt

url = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/archived_data/daily_case_updates/02-14-2020_1123.csv"

df = pd.read_csv(url, error_bad_lines=False)
print(df)

spltied_url = url.split("/")

plt.title(spltied_url[len(spltied_url)-1].split("_")[0])
df.plot(x ='Deaths', y='Confirmed', kind='bar')
plt.show()