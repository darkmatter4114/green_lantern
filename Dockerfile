FROM python:3.8

COPY . /app

# ENV app app.py
# ENV FLASK_RUN_HOST 0.0.0.0

WORKDIR /app

RUN pip install --upgrade pip && pip install -r requirements.txt

# ENTRYPOINT [ "/wsgi.py" ]

CMD ["python", "wsgi.py"]
#CMD python -m wsgi.py
