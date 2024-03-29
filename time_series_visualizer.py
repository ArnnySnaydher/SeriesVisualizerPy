import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv',index_col='date',parse_dates=True)
#print(df)

# Clean data
df = df[(df['value']>df['value'].quantile(0.025))&(df['value']<df['value'].quantile(0.975))]
#print(df)

def draw_line_plot():
    # Draw line plot
    fig=plt.figure(figsize=(20,8))
    plt.plot(df , color='brown')
    plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    plt.xlabel('Date')
    plt.ylabel('Page Views')

    plt.show()
    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()
    df_bar['Years'] = df_bar.index.year
    df_bar['Months'] = df_bar.index.month_name()
    
    month = ["January", "February", "March", "April", "May", "June", "July", "August",
              "September", "October", "November", "December"]
    
    df_bar['Months'] = pd.Categorical(df_bar['Months'], categories=month)
    df_bar = df_bar.reset_index()
    print(df_bar)
    
    df_bar_fig = pd.pivot_table(
        df_bar,
        values="value",
        index="Years",
        columns="Months"
    )
    # Draw bar plot
    fig = df_bar_fig.plot(kind='bar').get_figure()
    fig.set_figheight(10)
    fig.set_figwidth(9)
    plt.xlabel('Years')
    plt.ylabel('Average Page Views')
    plt.legend(title='Months')
    plt.show()
    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['Years'] = [d.year for d in df_box.date]
    df_box['Months'] = [d.strftime('%b') for d in df_box.date]

    month = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug",
              "Sep", "Oct", "Nov", "Dec"]
    
    df_box['Months'] = pd.Categorical(df_box['Months'], categories=month)
    # Draw box plots (using Seaborn)
    
    fig,ax = plt.subplots(1,2,figsize=(24,10))
    plt.subplot(1,2,1)
    sns.boxplot(x=df_box["Years"], y=df_box['value']).get_figure()
    plt.title('Year-wise Box Plot (Trend)')
    plt.xlabel('Year')
    plt.ylabel('Page Views')

    plt.subplot(1,2,2)
    sns.boxplot(x=df_box['Months'], y=df_box['value']).get_figure()
    plt.title('Month-wise Box Plot (Seasonality)')
    plt.xlabel('Month')
    plt.ylabel('Page Views')
    plt.show()

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
