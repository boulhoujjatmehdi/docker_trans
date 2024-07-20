
FROM python:3.9


WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install -r requirements.txt
RUN if [ ! -f /usr/src/app/manage.py ];then django-admin startproject user_api . ; fi
RUN rm requirements.txt
EXPOSE 8000

CMD python manage.py makemigrations && python manage.py migrate && python manage.py runserver 0.0.0.0:8000