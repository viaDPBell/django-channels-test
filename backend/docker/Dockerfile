FROM python:3.9.16

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# COPY ../requirements.txt .
# COPY ./backend /app/backend
COPY . .


RUN pip install --upgrade pip
# COPY ./backend/requirements.txt /app/backend/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt



# COPY ../. /backend/app

# ENV DJANGO_ENV=development