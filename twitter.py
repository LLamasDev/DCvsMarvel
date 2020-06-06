#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tweepy

consumer_key = # API key
consumer_secret = # API secret key
access_token = # Access token
access_token_secret = # Access token secret

def Auth():
    try:
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        return auth
    except Exception as e:
        return None

def inicioTwitter(texto):
    oauth = Auth()
    api = tweepy.API(oauth)
    api.update_status(texto)