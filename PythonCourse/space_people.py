# Note you need to run 'pip install requests' to use the requests module
import requests

weatheralert = requests.get('https://api.weather.gov/alerts/active/count')
json = weatheralert.json()

print(json)
