import pandas as pd
import matplotlib.pyplot as plt

def create_chart(data):
    # Process the data
    processed_data = []
    for item in data:
        new_item = (item[0], '(' + str(item[3]) + ')')
        processed_data.append(new_item)

    # Create a DataFrame
    df = pd.DataFrame(processed_data, columns=['Label', 'Value'])

    # Extract the values and convert them to int
    df['Value'] = df['Value'].str[1:-1].astype(int)

    # Group by 'Label' and sum 'Value'
    df = df.groupby('Label')['Value'].sum().reset_index()

    # Create a pie chart
    fig, ax = plt.subplots()
    ax.pie(df['Value'], labels=df['Label'], autopct='%1.1f%%')

    # Save the chart as an image in the 'static' directory
    fig.savefig('static/first_chart.png')
