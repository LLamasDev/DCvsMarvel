#!/usr/bin/env python
# -*- coding: utf-8 -*-

import telebot

bot = telebot.TeleBot('TOKEN')

def inicioTelegram(texto):
    bot.send_message(CHATID, texto)