# Night Owls Detector

Программа для вывода списка пользователей проекта [devman.org](https://devman.org/), которые отправляют задание на проверку в промежутке м/у 00:00 и 06:00. Для получения информации о пользователях используются запросы к API: [https://devman.org/api/challenges/solution_attempts/?page=1](https://devman.org/api/challenges/solution_attempts/?page=1).

# Установка

Программа требует для своей работы установленного интерпретатора Python версии 3.5.  
В программе используются сторонние библиотеки:
- [requests](http://docs.python-requests.org/en/master/#)
- [pytz](https://pypi.python.org/pypi/pytz)

Используйте команду pip для установки  библиотеки из файла зависимостей (или pip3 если есть конфликт с предустановленным Python 2):
```
$ pip install -r requirements.txt # В качестве альтернативы используйте pip3
```
Рекомендуется устанавливать зависимости в виртуальном окружении, используя [virtualenv](https://github.com/pypa/virtualenv), [virtualenvwrapper](https://pypi.python.org/pypi/virtualenvwrapper) или [venv](https://docs.python.org/3/library/venv.html). 

# Использование

Пример запуска в Linux, Python 3.5.2:
```
$ python seek_dev_nighters.py
Users, who have sent a solution after 00-00:
bilimus
IvanKumeyko
SergeiKhrustalev
ld38475474
bosemeph
se.mrzv
igorzakhar
imbaquad
olaesean
terentev.phantom
maniak.tux
id460393476
vladmalakhov
beastrock
АндрійКукуруза
skidheif
id16657
id117707374
```

# Цели проекта

Код написан для образовательных целей. Учебный курс для веб-разработчиков - [DEVMAN.org](https://devman.org)