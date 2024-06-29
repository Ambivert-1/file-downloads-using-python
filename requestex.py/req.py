
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

