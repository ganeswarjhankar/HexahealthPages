import requests

API_KEY="rH38bG17hKKB1QC6PHe6xHSUFbwF1al4"
EndPoint="https://api.giphy.com/v1/gifs/trending"

search_word="shrug"
params = {"api_key" : API_KEY,"q":search_word,"limit" : "3","rating":"g"}
response =requests.get(EndPoint,params=params).json()
print(response)
for gif in response["data"]:
    title = gif["title"]
    trending_date = gif["trending_datetime"]
    url = gif["url"]
    print(f"{title} | {trending_date}\{url}\n")

