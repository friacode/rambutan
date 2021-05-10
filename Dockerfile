FROM python:3.9.0

WORKDIR /home/

RUN echo "rambutan shopping mall template make image 9"

RUN git clone https://github.com/friacode/rambutan.git

WORKDIR /home/rambutan/

RUN pip install -r requirements.txt

RUN pip install gunicorn

RUN pip install mysqlclient

EXPOSE 8000

CMD ["bash", "-c",  "python manage.py collectstatic --noinput --settings=rambutan.settings.deploy && python manage.py migrate --settings=rambutan.settings.deploy && gunicorn rambutan.wsgi --env DJANGO_SETTINGS_MODULE=rambutan.settings.deploy  --bind 0.0.0.0:8000"]