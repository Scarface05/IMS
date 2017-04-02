# IMS

# Data Retriever
This data retriever has been developed by modifying the code already present in the Mars City/solarstorm database.
Prerequisites:
1. BeautifulSoup

How to run the code:
```sh 
python dataretriever.py "LOCATION WHERE THE DATA IS TO BE STORED"
```

# Client-Server Architecture
Prerequisites:
1. Flask

How a request would look like:
```sh
curl -i http://localhost:5000/todo/api/v1.0/forecasts/
```
This would return a JSON file.
