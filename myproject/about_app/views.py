import logging

from django.shortcuts import render

from django.http import HttpResponse
import random

logger = logging.getLogger(__name__)


# def log(view):
#     def wrapper(request, *args, **kwargs):
#         res = view(request, *args, **kwargs)
#
#         logger.info(f"Функция {view.__name__} вернула {res.content}")
#         return res
#
#     return wrapper



def index(request):
    html = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Document</title>
     </head>
     <body>
  
    <h1>Проект на Django </h1>
      <p>
      Django - это высокоуровневый фреймворк для веб-приложений на языке 
      Python. Он был создан в 2005 году и с тех пор активно развивается и 
      обновляется сообществом разработчиков по всему миру.
    </p>
    <h3>Установка и настройка Django</h3>
      <p>
      Python помогают решить проблему управления зависимостями проектов. 
      Если у вас есть несколько проектов на Python, то вероятность того, 
      что вам придется работать с разными версиями библиотек или самого Python, 
      очень высока. Но использование виртуальных сред позволяет создавать 
      независимые группы библиотек для каждого проекта, что предотвращает 
      конфликты между версиями и не дает одному проекту повлиять на другой. 
      В Python уже есть модуль venv для создания виртуальных сред, который 
      можно использовать как в разработке, так и в производстве.
    </p>
  </body>
</html>
"""
    return HttpResponse(html)



def about(request):
    html = """<!DOCTYPE html>
    <html lang="en">
      <head>
        <meta charset="UTF-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <title>Document</title>
      </head>
      <body>
        <h1>О нас</h1>
        <h3>Компаниям нужны специалисты с ИТ-навыками</h3>
        <p>
    ИТ-специалисты востребованы в финансах, ритейле, образовании и многих 
    других отраслях. Экономика и повседневная жизнь все больше переходит в 
    «цифру», поэтому у ИТ-сферы самые большие перспективы на развитие в 
    ближайшем будущем.
    </p>
      </body>
    </html>
    """
    return HttpResponse(html)
