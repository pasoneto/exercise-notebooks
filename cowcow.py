import requests
import random

oi = requests.get("https://type.fit/api/quotes").json() 
print(oi[random.randint(1, len(oi))]['text'])
