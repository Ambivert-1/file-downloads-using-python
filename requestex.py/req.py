import os
import requests
import zipfile

# Define the URL of the ZIP file and the local filename
url = (
    "https://api.worldbank.org/v2/en/indicator/"
    "NY.GDP.MKTP.CD?downloadformat=csv"
)
zip_filename = "gdp_by_country.zip"

# Download the ZIP file using requests
response = requests.get(url)
with open(zip_filename, 'wb') as file:
    file.write(response.content)
print(f"Downloaded {zip_filename} from {url}")

# Extract the contents of the ZIP file
with zipfile.ZipFile(zip_filename, 'r') as zip_ref:
    zip_ref.extractall()
    extracted_files = zip_ref.namelist()  # Get the list of extracted files
    print(f"Extracted the following files: {extracted_files}")

# Optional: Clean up by removing the ZIP file if you no longer need it
os.remove(zip_filename)
print(f"Removed {zip_filename}")

# Optional: Verify the CSV file content (print the first few lines of each CSV file)
for file in extracted_files:
    if file.endswith('.csv'):
        with open(file, 'r', encoding='utf-8') as f:
            print(f"\nContent of {file}:")
            for _ in range(5):  # Print first 5 lines
                print(f.readline().strip())
