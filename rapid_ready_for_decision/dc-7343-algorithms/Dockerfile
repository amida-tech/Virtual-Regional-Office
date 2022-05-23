FROM python:3.9.3
COPY . /
ENV FLASK_APP /py-root/app.py

WORKDIR py-root
COPY py-root/requirements.txt requirements.txt
RUN pip install -r requirements.txt
WORKDIR ..

CMD ["flask" , "run", "--host=0.0.0.0"]