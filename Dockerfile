FROM python:3
COPY ./app /app
WORKDIR /app

COPY PDFgenerator.py .
COPY input-1.txt .
COPY input-2.txt .

RUN pip install fpdf

CMD ["python","PDFgenerator.py","input-1.txt","input-2.txt"]