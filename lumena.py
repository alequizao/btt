#!/usr/bin/env python
# -*- coding: utf-8 -*-
import tweepy, time, os
while True:

    # @Pastel
    cont = 0
    auth = tweepy.OAuthHandler('nGDUIbbE7JTfir55tHqlYY51o', 'vD1UGkuMpFJabcmq4CLmnOZuvgtGM589LCFLdAM8GykG70f415')
    auth.set_access_token('1295243400384520192-bFSJg7VmYkcOsDszXKGhGZnGw3U7MH','oUcfTyB6eghfFvPJyZNENeJil0UoOihxiIEiQRUaKqPal')
    api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
    user = api.me()
    '''print(user.name)
    print(user.location)'''
    search = 'lumena'
    nrTweets = 10
    while True:
        for tweet in tweepy.Cursor(api.search, search).items(nrTweets):
            try:
                print(cont, user.name, user.location, ": @" + tweet.user.screen_name)
                if tweet.id == 'quackboot':
                    pass
                #api.update_status("@" + tweet.user.screen_name + " Uma delícia! ", in_reply_to_status_id=tweet.id)
                # tweet.favorite()

                cont += 1
                if cont == 10:
                    if os.name == "nt":
                        os.system("cls")
                    else:
                        os.system("clear")

                tweet.retweet()
                time.sleep(37)
            except tweepy.TweepError as e:
                print('\033[1;31m' + e.reason + '\033[0;0m')
            except StopIteration:
                time.sleep(120)
                continue
