#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tweepy,time,os


auth = tweepy.OAuthHandler('TDPq0cli0D50LFUoIiER1gDj8','Zc094PoIDScXpr6FbsTXijFLAYbWEt5bSbnKTnpl6wBNig4IFp')
auth.set_access_token('110866998-ieqzzuyKCmrT8bbLX6IQOQhM5PZGeU1YyMDgHRbt','AhOXSAHyeJEvGW6abLj37lIg4mljNqSq1rCMhKAHI8TLx')
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
user = api.me()

search = 'AÇAI'
numero = 5
cont = 0
while True:
    for tweet in tweepy.Cursor(api.search, search).items(numero):
        try:
            # print(tweet.text.encode("utf-8"))
            # if((tweet.text.encode("utf-8"))=='preciso trabalhar'):
            print(cont, user.name, user.location, ": @" + tweet.user.screen_name)
            '''api.update_status(
                "@" + tweet.user.screen_name + " Pau na sua bunda!  ",
                in_reply_to_status_id=tweet.id)'''
            cont += 1
            if cont == 11:
                if os.name == "nt":
                    os.system("cls")
                else:
                    os.system("clear")


            # print("tuite enviado corretamente")
            tweet.retweet()
            time.sleep(36)
        except tweepy.TweepError as e:
            print('\033[1;31m' + e.reason + '\033[0;0m')
        except StopIteration:
            time.sleep(120)
            continue


time.sleep(30)