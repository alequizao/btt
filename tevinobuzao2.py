#!/bin/env python
# -*- coding: utf-8 -*-
while True:
    import tweepy, time, os
    import socket

    confiaveis = ['www.google.com', 'www.yahoo.com', 'www.bb.com.br']
    # @tevinobuzao
    cont = 0
    auth = tweepy.OAuthHandler('hwJqCXu8DJxtV1s4kUn73afSq','m2pg9MGlEdkvrBu0d6djrKKQxUZM659m8HPrNdMo9k76Rb4uss')
    auth.set_access_token('1406298399629103105-7xQPUIDPSx4xgTJ7HaXZ01G0VsYtmB','Qpjz5HvqeptjjIbDRDF40ABGVLo4v6raCsND2MCRXzffF')
    api = tweepy.API(auth, wait_on_rate_limit=True,wait_on_rate_limit_notify=True)
    user = api.me()
    '''print(user.name)
    print(user.location)'''
    search = 'busao'
    nrTweets = 50

    while True:
        for tweet in tweepy.Cursor(api.search, search).items(nrTweets):
            try:
                print(cont, user.name, user.location, ": @" + tweet.user.screen_name)
                # api.update_status("@" + tweet.user.screen_name + " Já conhece nosso instagram? www.instagram.com/tevinobuzao ",in_reply_to_status_id=tweet.id)


                cont += 1
                if cont == 11:
                    if os.name == "nt":
                        os.system("cls")
                    else:
                        os.system("clear")

                tweet.retweet()
                time.sleep(20)
                #tweet.retweet()
                #tweet.favorite()



            except tweepy.TweepError as e:
                print('\033[1;31m' + e.reason + '\033[0;0m')
            except StopIteration:
                time.sleep(10)
                continue



