FROM python:3.9
LABEL maintainer="proenix@proenix.pl"

RUN apt update -y 
RUN apt install -y gconf-service libasound2 libatk1.0-0 libc6 libcairo2 libcups2 libdbus-1-3 libexpat1 libfontconfig1 libgcc1 libgconf-2-4 libgdk-pixbuf2.0-0 libglib2.0-0 libgtk-3-0 libnspr4 libpango-1.0-0 libpangocairo-1.0-0 libstdc++6 libx11-6 libx11-xcb1 libxcb1 libxcomposite1 libxcursor1 libxdamage1 libxext6 libxfixes3 libxi6 libxrandr2 libxrender1 libxss1 libxtst6 ca-certificates fonts-liberation libappindicator1 libnss3 lsb-release xdg-utils wget
RUN pip3 install pyppeteer gunicorn requests werkzeug 
RUN pyppeteer-install

ADD img.py /img.py

EXPOSE 80

ENTRYPOINT ["gunicorn"]

CMD ["-b", "0.0.0.0:80", "--log-file", "-", "img:application"]