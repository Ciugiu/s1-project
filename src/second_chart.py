import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import numpy as np

def create_chart(data):
    # Process the data
    processed_data = []
    for item in data:
        new_item = (item[0], item[1][:1] + ' ' + str(item[2]), round(item[3]))
        processed_data.append(new_item)

    # Create a DataFrame
    df = pd.DataFrame(processed_data, columns=['Label', 'Year', 'Value'])

    # Get the unique labels and years
    labels = df['Label'].unique()
    years = df['Year'].unique()

    # Create an array for the label positions
    label_positions = np.arange(len(labels))

    # Create a bar for each year in each label
    bar_width = 0.35
    fig, ax = plt.subplots()
    for i, year in enumerate(years):
        # Get the data for this year
        year_data = df[df['Year'] == year]

        # Create an array for the bar heights
        bar_heights = [year_data[year_data['Label'] == label]['Value'].mean() for label in labels]

        # Create the bars
        ax.bar(label_positions + i*bar_width, bar_heights, bar_width, label=year)

    # Set the y-axis limit
    ax.set_ylim([0, 100])

    # Add a percentage sign to the y-axis labels
    fmt = '%.0f%%' # Format you want the ticks, e.g. '40%'
    yticks = mtick.FormatStrFormatter(fmt)
    ax.yaxis.set_major_formatter(yticks)

    # Set the x-axis labels and title
    ax.set_xlabel('Label')
    ax.set_ylabel('Value')
    ax.set_title('Values by label and year')

    # Set the x-axis tick labels
    ax.set_xticks(label_positions + bar_width / 2)
    ax.set_xticklabels(labels)

    # Add a legend
    ax.legend()

    # Save the chart as an image in the 'static' directory
    fig.savefig('static/second_chart.png')