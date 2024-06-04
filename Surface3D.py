import numpy as np
import lightningchart as lc
import pandas as pd

# Read the license key
lc.set_license('my_license_key')

# Load the dataset
file_path = 'Land Ocean Temperature Index (C).xlsx'
data = pd.read_excel(file_path)

# Ensure there are no missing values
data = data.dropna()

# Extract year from the date
data['Year'] = data['Year'].astype(int)

# Create a grid for the heatmap
years = data['Year'].unique()
temperature_anomalies = data['No_Smoothing'].values

# Reshape the temperature anomalies to form a grid
temperature_grid = np.tile(temperature_anomalies, (len(years), 1))

# Initialize LightningChart
chart = lc.Surface3D(
    data=temperature_grid.tolist(),
    min_value=np.min(temperature_anomalies),
    max_value=np.max(temperature_anomalies),
    min_color=lc.Color(0, 0, 255),  # Blue
    max_color=lc.Color(255, 0, 0),  # Red
    theme=lc.Themes.White,
    title='3D Surface Temperature Chart',
    xlabel='Year',
    ylabel='Temperature Anomaly',
    zlabel='Temperature (°C)'
)

# Set camera position for better view
chart.set_camera_location(1, 1, 2)

# Show plot
chart.open()


