import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

df = pd.read_csv('fcc-forum-pageviews.csv' , index_col='date',parse_dates=True)

df = df[(df['value']>df['value'].quantile(0.025))&(df['value']<df['value'].quantile(0.975))]

df_bar = df.copy(deep=True)
df_bar['year'] = df_bar.index.year
months = ["January", "February", "March", "April", "May", "June", "July", "August",
              "September", "October", "November", "December"]
df_bar['month'] = df_bar.index.month_name()
df_bar['month'] = pd.Categorical(df_bar['month'], categories=months)
df_bar_pivot = pd.pivot_table(
        df_bar,
        values="value",
        index="year",
        columns="month"
    )

    # Draw bar plot
fig = df_bar_pivot.plot(kind='bar').get_figure()
fig.set_figheight(6)
fig.set_figwidth(8)
plt.xlabel('Years')
plt.ylabel('Average Page Views')
plt.legend(title='Months')
plt.show()