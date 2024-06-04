import lightningchart as lc
import pandas as pd
# Read the license key
lc.set_license('my_license_key')
# Load the dataset
file_path = 'Land Ocean Temperature Index (C).xlsx'
data = pd.read_excel(file_path)
# Extract values
x_values = data['Year'].tolist()
y_values_no_smoothing = data['No_Smoothing'].tolist()

# Create the Area Chart
chart = lc.ChartXY(
    theme=lc.Themes.White,
    title='Global Temperature Changes (Area Chart)'
)

# Add Area Series
area_series = chart.add_area_series()
area_series.add(x_values, y_values_no_smoothing)
area_series.set_name('Temperature Anomaly')

# Customize x-axis
x_axis = chart.get_default_x_axis()
x_axis.set_title('Year')

# Customize y-axis
y_axis = chart.get_default_y_axis()
y_axis.set_title('Temperature Anomaly (C)')

# Open the chart
chart.open()
