FROM sujith760/api:v2

WORKDIR /home/ubuntu/api/oopsapidev

COPY . .

RUN apt-get update && apt-get install -y build-essential libpq-dev

RUN mv requirement.txt requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
