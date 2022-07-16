import requests
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('seaborn-whitegrid')
fig = plt.figure()
ax = plt.axes()

response_conf = requests.get("https://api.covid19api.com/country/singapore/status/confirmed?from=2020-03-01T00:00:00Z&to=2022-04-01T00:00:00Z")
conf_data = response_conf.text

conf_df = pd.read_json(conf_data)

recovered_conf = requests.get("https://api.covid19api.com/country/singapore/status/recovered?from=2020-03-01T00:00:00Z&to=2022-04-01T00:00:00Z")
recovered_data = recovered_conf.text

recovered_df = pd.read_json(recovered_data)


deaths_conf = requests.get("https://api.covid19api.com/country/singapore/status/deaths?from=2020-03-01T00:00:00Z&to=2022-04-01T00:00:00Z")
deaths_data = deaths_conf.text

deaths_df = pd.read_json(deaths_data)

# To get Confirmed, Recovered, Deaths cases on y axis
a = conf_df['Cases']
b = recovered_df['Cases']
c = deaths_df['Cases']


# For X axis
x = conf_df['Date']

# plot
ax.plot(x,a, '-k',label='Confirmed Cases')
ax.plot(x,b, '--g',label='Recovered Cases')
ax.plot(x,c, ':r',label='Death Cases')

plt.title("Total Confirmed Cases in Singapore")
plt.xlabel("Date 2020 till 2022")
plt.ylabel("Cases")
plt.legend()
plt.show()
# print(conf_df)