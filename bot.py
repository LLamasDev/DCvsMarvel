#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import time
from random import randrange
from googletrans import Translator
from twitter import *
from telegram import *

with open('./json/superheroes.json') as f:
    data = json.load(f)

translator = Translator()
textoES = "Comienza una nueva batalla."
textoEN = translator.translate(textoES, src='es', dest='en')
texto = "🇪🇸 " + textoES + "\n🇬🇧 " + textoEN.text
inicioTelegram(texto)
inicioTwitter(texto)
time.sleep(10)

while True:
    tamanoDC = len(data['DC'])
    tamanoMarvel = len(data['Marvel'])

    if tamanoDC == 0:
        textoES = "Gana Marvel, han sobrevivido " + str(tamanoMarvel) + " superhéroes."
        textoEN = translator.translate(textoES, src='es', dest='en')
        texto = "🇪🇸 " + textoES + "\n🇬🇧 " + textoEN.text
        inicioTelegram(texto)
        inicioTwitter(texto)

        break
    elif tamanoMarvel == 0:
        textoES = "Gana DC, han sobrevivido " + str(tamanoDC) + " superhéroes."
        textoEN = translator.translate(textoES, src='es', dest='en')
        texto = "🇪🇸 " + textoES + "\n🇬🇧 " + textoEN.text
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
            textoES = superheroDC + " ha derrotado a " + superheroMarvel + "."
            textoEN = translator.translate(textoES, src='es', dest='en')
            texto = "🇪🇸 " + textoES + "\n🇬🇧 " + textoEN.text
            inicioTelegram(texto)
            inicioTwitter(texto)

            del data['Marvel'][numeroMarvel]
        elif ganador == 1:
            textoES = superheroMarvel + " ha derrotado a " + superheroDC + "."
            textoEN = translator.translate(textoES, src='es', dest='en')
            texto = "🇪🇸 " + textoES + "\n🇬🇧 " + textoEN.text
            inicioTelegram(texto)
            inicioTwitter(texto)

            del data['DC'][numeroDC]
    
    time.sleep(300)