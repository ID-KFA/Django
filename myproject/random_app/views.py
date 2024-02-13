import logging

from django.shortcuts import render

from django.http import HttpResponse
from .forms import Game

import random
from random import choice, randint

logger = logging.getLogger(__name__)


def log(view):
    def wrapper(request, *args, **kwargs):
        res = view(request, *args, **kwargs)

        logger.info(f"Функция {view.__name__} вернула {res.content}")
        return res

    return wrapper


# class Rand(View)
@log
def coin(request):
    return HttpResponse(random.choice(["Орел", "Решка"]))


@log
def dice(request):
    i = random.randint(0, 6)
    logger.info(f"Выпало {i}")
    return HttpResponse(f"Выпало {i}")


def rand_hundred(request):
    i = random.randint(0, 100)
    logger.info(f"Выпало {i}")
    return HttpResponse(f"Выпало {i}")


def gen_coin(request, num):
    results = [choice(["Орел", "Решка"]) for _ in range(num)]
    context = {"game_name": "Монетка", "results": results}
    print(results)
    return render(request, "random_app/games.html", context)


def gen_dice(request, num):
    results = [randint(1, 7) for _ in range(num)]
    print(results)
    context = {"game_name": "Кости", "results": results}
    return render(request, "random_app/games.html", context)


def gen_number(request, num):
    results = [random.randint(0, 100) for _ in range(num)]
    print(results)
    context = {"game_name": "Случайное число", "results": results}
    return render(request, "random_app/games.html", context)


def game(request):
    if request.method == "POST":
        form = Game(request.POST)
        if form.is_valid():
            choose = form.cleaned_data.get("choose")
            attempts = form.cleaned_data.get("attempts")
            if choose == "coin":
                return gen_coin(request, attempts)
            if choose == "dice":
                return gen_dice(request, attempts)
            if choose == "rand_number":
                return gen_number(request, attempts)
    else:
        form = Game()
    return render(request, "random_app/games2.html", {"form": form})
