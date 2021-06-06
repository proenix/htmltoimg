# htmltoimg

Tool to generate images from provided html code using pyppeteer.

## Docker repositiory

https://hub.docker.com/r/proenix/htmltoimg

## Examples

As a response returns file is or 500 error.

### Using curl:

Generate JPEG with quality 50, 200x500px. Content of "contents" is base64 encoded html (here sample.html)

```
curl --location --request POST 'http://127.0.0.1:5000/' \
--header 'Content-Type: application/json' \
--data-raw '{
    "contents": [
        "PCFET0NUWVBFIGh0bWw+CjxodG1sIGxhbmc9ImVuIj4KICA8aGVhZD4KICAgIDxtZXRhIGNoYXJzZXQ9InV0Zi04IiAvPgogICAgPHRpdGxlPlNhbXBsZSBwYWdlPC90aXRsZT4KICAgIDxzdHlsZT4KICAgICAgICBib2R5IHsKICAgICAgICAgICAgd2lkdGg6IDIwMHB4OwogICAgICAgICAgICBoZWlnaHQ6IDQwMHB4OwogICAgICAgIH0KICAgICAgLnNhbXBsZSB7CiAgICAgICAgYmFja2dyb3VuZDogI2ZhZmFmYTsKICAgICAgfQogICAgPC9zdHlsZT4KICA8L2hlYWQ+CiAgPGJvZHk+CiAgICA8ZGl2IGNsYXNzPSJzYW1wbGUiPgogICAgICA8aDI+SDIgVGl0bGU8L2gyPgogICAgICA8aDM+SDMgVGl0bGU8L2gzPgogICAgICA8aW1nIHNyYz0iaHR0cDovL3BsYWNla2l0dGVuLmNvbS8xMDAvMTAwIiAvPgogICAgPC9kaXY+CiAgICAgIDxoMj5IMiBUaXRsZTwvaDI+CiAgICAgIDxoMz5IMyBUaXRsZTwvaDM+CiAgICAgIDxpbWcgc3JjPSJodHRwOi8vcGxhY2VraXR0ZW4uY29tLzEwMC8xMDAiIC8+CiAgICA8L2Rpdj4KICA8L2JvZHk+CjwvaHRtbD4K"
    ],
    "options": {
        "width": 200,
        "height": 500,
        "format": "jpeg",
        "quality": 50
    }
}'
```

Generate PNG with transparent background. Content of "contents" is base64 encoded html (here sample.html)

```
curl --location --request POST 'http://127.0.0.1:5000/' \
--header 'Content-Type: application/json' \
--data-raw '{
    "contents": [
        "PCFET0NUWVBFIGh0bWw+CjxodG1sIGxhbmc9ImVuIj4KICA8aGVhZD4KICAgIDxtZXRhIGNoYXJzZXQ9InV0Zi04IiAvPgogICAgPHRpdGxlPlNhbXBsZSBwYWdlPC90aXRsZT4KICAgIDxzdHlsZT4KICAgICAgICBib2R5IHsKICAgICAgICAgICAgd2lkdGg6IDIwMHB4OwogICAgICAgICAgICBoZWlnaHQ6IDQwMHB4OwogICAgICAgIH0KICAgICAgLnNhbXBsZSB7CiAgICAgICAgYmFja2dyb3VuZDogI2ZhZmFmYTsKICAgICAgfQogICAgPC9zdHlsZT4KICA8L2hlYWQ+CiAgPGJvZHk+CiAgICA8ZGl2IGNsYXNzPSJzYW1wbGUiPgogICAgICA8aDI+SDIgVGl0bGU8L2gyPgogICAgICA8aDM+SDMgVGl0bGU8L2gzPgogICAgICA8aW1nIHNyYz0iaHR0cDovL3BsYWNla2l0dGVuLmNvbS8xMDAvMTAwIiAvPgogICAgPC9kaXY+CiAgICAgIDxoMj5IMiBUaXRsZTwvaDI+CiAgICAgIDxoMz5IMyBUaXRsZTwvaDM+CiAgICAgIDxpbWcgc3JjPSJodHRwOi8vcGxhY2VraXR0ZW4uY29tLzEwMC8xMDAiIC8+CiAgICA8L2Rpdj4KICA8L2JvZHk+CjwvaHRtbD4K"
    ],
    "options": {
        "width": 200,
        "height": 500,
        "format": "png",
        "transparent": true,
    }
}'
```
