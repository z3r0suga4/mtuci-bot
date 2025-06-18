FROM python:3.9
COPY requirements.txt .
RUN pip install -r requirements.txt
WORKDIR /app
ENV TZ="Europe/Moscow"
CMD ["python", "./bot.py"]