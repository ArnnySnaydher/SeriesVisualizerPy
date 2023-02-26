import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

df = pd.read_csv('fcc-forum-pageviews.csv' , index_col='date',parse_dates=True)

df = df[(df['value']>df['value'].quantile(0.025))&(df['value']<df['value'].quantile(0.975))]

df_bar = df.copy()

df_bar['Years'] = df_bar.index.year
df_bar['Months'] = df_bar.index.month_name()
#print(df_bar)

month = ["January", "February", "March", "April", "May", "June", "July", "August",
              "September", "October", "November", "December"]

df_bar['Months'] = pd.Categorical(df_bar['Months'], categories=month)

print(df_bar)

# df_bar_fig = pd.pivot_table(
#         df_bar,
#         values="value",
#         index="Years",
#         columns="Months"
#     )
# #     # Draw bar plot
# fig = df_bar_fig.plot(kind='bar').get_figure()
# fig.set_figheight(10)
# fig.set_figwidth(9)
# plt.xlabel('Years')
# plt.ylabel('Average Page Views')
# plt.legend(title='Months')
# plt.show()

