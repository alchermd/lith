FROM python:3.13-slim-bookworm AS builder

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN pip install --upgrade pip

COPY requirements.in .
RUN pip install --no-cache-dir -r requirements.in

FROM python:3.13-slim-bookworm

WORKDIR /app

RUN apt update && apt -y dist-upgrade
RUN apt install -y netcat-traditional

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

COPY --from=builder /usr/local/lib/python3.13/site-packages/ /usr/local/lib/python3.13/site-packages/
COPY --from=builder /usr/local/bin/ /usr/local/bin/

COPY . .

ENTRYPOINT ["/app/entrypoint.sh"]
