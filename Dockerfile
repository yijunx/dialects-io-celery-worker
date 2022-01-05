FROM python:3.9

ENV PYTHONDONTWRITEBYTECODE 1

WORKDIR /opt/yijun/code

COPY './requirements.txt' .

RUN pip install -r requirements.txt

CMD ["python", "-m", "app.main"]