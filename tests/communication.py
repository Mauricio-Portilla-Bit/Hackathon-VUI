import requests
from cleantext import clean

url = "https://us-central1-srbanorte23.cloudfunctions.net/dialogflowGateway"
msg = {"sessionId": "srbanorte23",
        "queryInput": {
            "text": {
                "text": "¿cuánto saldo tengo actualmente?",
                "languageCode": "es"
            }
        }}
response = requests.post(url, json=msg)
print(response.json())
response = response.json()
response_text = response["fulfillmentText"]
print(response_text)

print("-----------------------------")
response_text_clean = clean(response_text, no_emoji=True).replace("\n", " ")
print(response_text_clean)

#print("-----------------------------")

#print(repr(clean(response_text, no_emoji=True).strip()))


