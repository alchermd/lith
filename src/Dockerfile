FROM python:3.13-bookworm

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN apt update && apt -y dist-upgrade
RUN apt install -y netcat-traditional
RUN pip install --upgrade pip

COPY requirements.in .
RUN pip install --no-cache-dir -r requirements.in

COPY . .

ENTRYPOINT ["/app/entrypoint.sh"]
