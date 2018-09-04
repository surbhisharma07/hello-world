import requests
res=requests.get('http://api.forismatic.com/api/1.0/?method=getQuote&format=json&lang=en')
data=res.json()
print(data["quoteText"])