import os
import pandas as pd

# Set input and output paths
input_folder = "data"  # Replace with your folder path
output_file = "combined_output.csv"

# Define column names based on data structure
columns = [
    "time", "latitude", "longitude", "wind_dir", "wind_speed",
    "visibility", "temp", "dewpoint", "pressure", "precipitation_1hr",
    "precipitation_6hr", "precipitation_24hr", "snow_depth"
]

all_data = []

# Loop through all .txt files
for filename in os.listdir(input_folder):
    if filename.endswith(".txt"):
        file_path = os.path.join(input_folder, filename)

        with open(file_path, "r") as f:
            for line in f:
                line = line.strip()

                # Skip empty lines or end markers
                if not line or line.startswith(("$$", ";")):
                    continue

                # Only process lines that start with a time-like value (e.g., 145200)
                if line[0].isdigit() and len(line) > 10:
                    parts = line.split()  # Split on any whitespace

                    # Only append if number of fields matches expected columns
                    if len(parts) == len(columns):
                        parts.append(filename)  # optional: track source
                        all_data.append(parts)

# Add source file column to headers
columns_with_source = columns + ["source_file"]

# Create DataFrame
df = pd.DataFrame(all_data, columns=columns_with_source)

# Save to CSV
df.to_csv(output_file, index=False)
print(f"✅ Combined data saved to {output_file}")
