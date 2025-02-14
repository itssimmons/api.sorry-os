FROM python:3.10-alpine

WORKDIR /app

COPY . .

RUN apk add --no-cache gcc musl-dev
RUN pip install pipenv
RUN pipenv install --system --deploy

EXPOSE 8000

CMD ["pipenv", "run", "python", "main.py"]