import matplotlib.pyplot as plt
import matplotlib.dates as md
import pandas as pd

df = pd.read_csv('/home/tony/multgraph_python/explab16_18_data.csv')
plt.figure(figsize=(20,10)) #width, height
plt.title("CO2 vs Time")
plt.xlabel("fecha y hora")
plt.ylabel("ppm")
plt.xticks(rotation=25)
plt.grid()
datenum = md.date2num(df['Date'])
ax = plt.gca()
xfmt = md.DateFormatter('%Y-%m-%d %H:%M')
ax.xaxis.set_major_formatter(xfmt)
plt.plot(datenum, df['CO2_IPIE'], label='IPIE')
plt.plot(datenum, df['CO2_IPICYT-A'], label='aranet A')
plt.plot(datenum, df['CO2_DBM-D'], label='aranet D')
plt.legend()
plt.show()