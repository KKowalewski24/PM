FROM python:3.9-alpine3.13

WORKDIR /usr/src/app
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .

EXPOSE 5001
CMD [ "python", "main.py" ]
