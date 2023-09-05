# Import the requests module, which allows us to send HTTP requests
import requests

# Send an HTTP GET request to the specified URL
response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')

# Use .json() to deserialize the JSON response into a Python dictionary
binfo = response.json()

# Print the updated timestamp of the Bitcoin price information
print('Bitcoin Price as of', binfo['time']['updated'])

# Print the current exchange rate of 1 Bitcoin to US Dollars (USD)
print('1 Bitcoin = $', binfo['bpi']['USD']['rate'])
