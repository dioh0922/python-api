#
pip install --upgrade pip
pip install -r requirements.txt
sudo apt-get install -y tesseract-ocr tesseract-ocr-jpn tesseract-ocr-eng libtesseract-dev libleptonica-dev tesseract-ocr-script-jpan tesseract-ocr-script-jpan-vert 
sudo cp ./tessdata/jpn.traineddata /usr/share/tesseract-ocr/5/tessdata/jpn.traineddata
