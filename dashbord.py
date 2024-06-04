import lightningchart as lc
import pandas as pd

# Set the license key
lc.set_license('my_license_key')

# Load the dataset
file_path = 'GLB.Ts+dSST.csv'
data = pd.read_csv(file_path)

# Extract years
years = data['Year'].tolist()

# Create a dashboard to arrange the charts
dashboard = lc.Dashboard(
    rows=4,
    columns=3,
    theme=lc.Themes.White
)

# List of month names
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

# List of colors for each month
colors = [
    lc.Color(255, 0, 0),    # Red
    lc.Color(255, 165, 0),  # Orange
    lc.Color(255, 255, 0),  # Yellow
    lc.Color(0, 128, 0),    # Green
    lc.Color(0, 255, 255),  # Cyan
    lc.Color(0, 0, 255),    # Blue
    lc.Color(75, 0, 130),   # Indigo
    lc.Color(238, 130, 238),# Violet
    lc.Color(165, 42, 42),  # Brown
    lc.Color(255, 20, 147), # Deep Pink
    lc.Color(128, 0, 128),  # Purple
    lc.Color(0, 0, 0)       # Black
]

# Loop through each month and create a chart for it
for i, month in enumerate(months):
    # Extract data for the current month
    temperature_anomalies = data[month].tolist()
    
    # Create the chart
    chart = dashboard.ChartXY(
        column_index=i % 3,
        row_index=i // 3
    )
    chart.set_title(f'Temperature Anomaly ({month})')

    # Create the series
    series = chart.add_line_series()
    series.add(years, temperature_anomalies)
    series.set_name(month)
    series.set_line_color(colors[i])
    
    # Customize x-axis
    x_axis = chart.get_default_x_axis()
    x_axis.set_title('Year')
    
    # Customize y-axis
    y_axis = chart.get_default_y_axis()
    y_axis.set_title('Temperature Anomaly (C)')
    
    # Customize chart appearance
    chart.add_legend()

# Open the dashboard
dashboard.open()