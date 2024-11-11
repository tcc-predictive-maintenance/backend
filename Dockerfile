FROM python:3.12

WORKDIR /
COPY ./requirements.txt /requirements.txt

RUN pip install --no-cache-dir --upgrade -r /requirements.txt

COPY ./ /

EXPOSE 8000

CMD ["uvicorn", "main:app"]