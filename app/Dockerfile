# pull official base image
FROM python:3.10-slim

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
COPY ./requirements.txt .
RUN pip install --no-cache-dir --upgrade -r requirements.txt

# copy project
COPY . .

EXPOSE 8002

CMD ["uvicorn", "server.app:app", "--host", "0.0.0.0", "--port", "8002"]




