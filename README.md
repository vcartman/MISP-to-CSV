# MISP-to-CSV
Python MISP to CSV export script ***without*** a PyMISP integrations. The script uses the MISP API to retrieve data from the MISP tenant. It connects to the MISP instance using the provided API credentials and makes API requests to fetch the desired data.

# What to change
Add the domain and API-key at line 5 and 6
`url = "https://domain.com"
api_key = "API-KEY"`

Change how many pages you want to export at line 19:
`"page":1,`

Change which threat intel you want to export at line 26:
`"tags": {
        "OR": [
            "tlp:green"
        ]
    }
`
# How do you run it?
python .\misp-to-csv.py

# Tested on
Python 3.7
MISP v2.4.171 

[!["Buy Me A Coffee"](https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png)](https://www.buymeacoffee.com/victorpas)

# Description of the script
- Connect to the MISP tenant:
  - The script establishes a connection to the MISP instance by providing the necessary authentication credentials such as the API key or username and password.
  - It uses the MISP API endpoint URL to make requests to the MISP instance.

- Fetch data from the MISP tenant:
  - The script sends API requests to the MISP instance to retrieve the desired data.
  - It can fetch various types of data such as events, attributes, indicators, or other relevant information based on the requirements.

- Process the retrieved data:
  - Once the data is received from the MISP tenant, the script processes it according to the desired format, which in this case is CSV.
  - It extracts the necessary fields and organizes the data in a tabular format suitable for CSV conversion.

- Convert the processed data to CSV:
  - The script converts the processed data into CSV format.
  - It uses a CSV library or built-in functions to generate the CSV file.
  - The relevant data fields are mapped to the corresponding columns in the CSV file.

- Save the CSV file:
  - The script saves the generated CSV file to a specified location.
  - It may include a timestamp or unique identifier in the file name to distinguish between different data retrievals.

By following this process, the script connects to the MISP tenant, retrieves the desired data via the MISP API, processes it, converts it to CSV format, and finally saves it as a CSV file.
