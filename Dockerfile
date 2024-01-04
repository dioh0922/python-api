FROM python:3.10

WORKDIR /usr/src/app
ENV FLASK_APP=server.py
ENV FLASK_RUN_HOST=0.0.0.0

COPY ./requirements.txt /usr/src/lib/requirements.txt

RUN apt-get update && apt-get -y upgrade
RUN apt-get install -y build-essential

RUN apt-get install -y libhdf5-dev
RUN apt-get install -y tesseract-ocr tesseract-ocr-jpn tesseract-ocr-eng libtesseract-dev libleptonica-dev tesseract-ocr-script-jpan tesseract-ocr-script-jpan-vert 

COPY ./module/ocr/tessdata/jpn.traineddata /usr/share/tesseract-ocr/5/tessdata/jpn.traineddata

RUN pip install --upgrade pip
RUN pip install wheel
RUN pip install pandas
RUN pip install -r /usr/src/lib/requirements.txt
COPY . .
CMD ["flask", "run"]