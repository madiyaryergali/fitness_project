FROM python:3.9

COPY requirements.txt .
RUN pip install -r requirements.txt


WORKDIR /code

COPY . .

RUN python manage.py makemigrations
RUN python manage.py migrate

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
