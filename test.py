import requests
import json

url = "http://127.0.0.1:5000/"

payload = json.dumps({
  "contents": [
    "PCFET0NUWVBFIGh0bWw+CjxodG1sIGxhbmc9ImVuIj4KICA8aGVhZD4KICAgIDxtZXRhIGNoYXJzZXQ9InV0Zi04IiAvPgogICAgPHRpdGxlPlNhbXBsZSBwYWdlPC90aXRsZT4KICAgIDxzdHlsZT4KICAgICAgICBib2R5IHsKICAgICAgICAgICAgd2lkdGg6IDIwMHB4OwogICAgICAgICAgICBoZWlnaHQ6IDQwMHB4OwogICAgICAgIH0KICAgICAgLnNhbXBsZSB7CiAgICAgICAgYmFja2dyb3VuZDogI2ZhZmFmYTsKICAgICAgfQogICAgPC9zdHlsZT4KICA8L2hlYWQ+CiAgPGJvZHk+CiAgICA8ZGl2IGNsYXNzPSJzYW1wbGUiPgogICAgICA8aDI+SDIgVGl0bGU8L2gyPgogICAgICA8aDM+SDMgVGl0bGU8L2gzPgogICAgICA8aW1nIHNyYz0iaHR0cDovL3BsYWNla2l0dGVuLmNvbS8xMDAvMTAwIiAvPgogICAgPC9kaXY+CiAgICAgIDxoMj5IMiBUaXRsZTwvaDI+CiAgICAgIDxoMz5IMyBUaXRsZTwvaDM+CiAgICAgIDxpbWcgc3JjPSJodHRwOi8vcGxhY2VraXR0ZW4uY29tLzEwMC8xMDAiIC8+CiAgICA8L2Rpdj4KICA8L2JvZHk+CjwvaHRtbD4K"
  ],
  "options": {
    "width": 200,
    "height": 500,
    "format": "jpeg",
    "transparent": True,
    "quality": 50
  }
})
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
