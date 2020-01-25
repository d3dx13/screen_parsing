# screen_parsing

screen_parsing - программа на языке python с использованием [tesseract](https://ru.wikipedia.org/wiki/Tesseract) для быстрого и удобного извлечения текстовой информации из изображения. 



#### Процесс установки

##### Установка tesseract-ocr:

`sudo apt-get install tesseract-ocr`

`sudo add-apt-repository ppa:alex-p/tesseract-ocr`

`sudo apt update`

`sudo apt-get install tesseract-ocr`

##### Добавление датасета с русским языком:

`sudo cp traindata_rus/* /usr/share/tesseract-ocr/4.00/tessdata`

или (в зависимости от версии)

`sudo cp traindata_rus/* /usr/share/tesseract-ocr/tessdata`

Главное, что вам нужна единственная не пустая директория tessdata

##### Установка зависимостей для приложения:

`python3 -m pip install -r requirements.txt`



#### [Отчёт по работе](https://github.com/d3dx13/screen_parsing/blob/master/report/report.pdf)