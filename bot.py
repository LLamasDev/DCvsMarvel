#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import time
from random import randrange
from twitter import *
from telegram import *

with open('./json/superheroes.json') as f:
    data = json.load(f)

while True:
    tamanoDC = len(data['DC'])
    tamanoMarvel = len(data['Marvel'])

    if tamanoDC == 0:
        texto = "Gana Marvel, han sobrevivido " + str(tamanoMarvel) + " superhéroes."
        inicioTelegram(texto)
        inicioTwitter(texto)

        break
    elif tamanoMarvel == 0:
        texto = "Gana DC, han sobrevivido " + str(tamanoDC) + " superhéroes."
        inicioTelegram(texto)
        inicioTwitter(texto)

        break
    else:
        numeroDC = randrange(tamanoDC)
        numeroMarvel = randrange(tamanoMarvel)
        superheroDC = data['DC'][numeroDC]['superhero']
        superheroMarvel = data['Marvel'][numeroMarvel]['superhero']
        ganador = randrange(2)

        if ganador == 0:
            texto = superheroDC + " ha derrotado a " + superheroMarvel + "."
            inicioTelegram(texto)
            inicioTwitter(texto)

            del data['Marvel'][numeroMarvel]
        elif ganador == 1:
            texto = superheroMarvel + " ha derrotado a " + superheroDC + "."
            inicioTelegram(texto)
            inicioTwitter(texto)

            del data['DC'][numeroDC]
    
    time.sleep(300)