import lightningchart as lc
import pandas as pd

# Read the license key
lc.set_license('my_license_key')

# Load the dataset
file_path = 'GLB.Ts+dSST.csv'
data = pd.read_csv(file_path)

# Extract years
x_values = data['Year'].tolist()

# Define colors for each month
colors = [
    lc.Color(0, 128, 255),  # Blue for January
    lc.Color(255, 0, 0),    # Red for February
    lc.Color(0, 255, 0),    # Green for March
    lc.Color(255, 165, 0),  # Orange for April
    lc.Color(75, 0, 130),   # Indigo for May
    lc.Color(238, 130, 238),# Violet for June
    lc.Color(255, 192, 203),# Pink for July
    lc.Color(128, 0, 128),  # Purple for August
    lc.Color(255, 215, 0),  # Gold for September
    lc.Color(0, 255, 255),  # Cyan for October
    lc.Color(255, 20, 147), # DeepPink for November
    lc.Color(139, 69, 19)   # Brown for December
]

# Create the chart
chart = lc.ChartXY(
    theme=lc.Themes.White,
    title='GLOBAL LAND-OCEAN TEMPERATURE INDEX'
)

# Add series for each month
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

for i, month in enumerate(months):
    y_values = data[month].tolist()
    
    # Add line series for each month
    line_series = chart.add_line_series()
    line_series.add(x_values, y_values)
    line_series.set_name(month)
    line_series.set_line_color(colors[i])
    line_series.set_line_thickness(2)  # Set line width

# Customize x-axis
x_axis = chart.get_default_x_axis()
x_axis.set_title('Year')

# Customize y-axis
y_axis = chart.get_default_y_axis()
y_axis.set_title('Temperature Anomaly (C)')

# Customize chart appearance
chart.add_legend(data=chart)

# Open the chart
chart.open()
