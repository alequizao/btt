#!/usr/bin/env python
# -*- coding: utf-8 -*-
import tweepy, time, os
while True:

    # @Pastel
    #AAAAAAAAAAAAAAAAAAAAAJf4MgEAAAAAFIrpXr2IbUZRfMccxqMxjoeVLrw%3D9sondOAd0YWEj8PYG5MHxgXfIFbBOi7oILIwBqzVVDr0E6Nbvi
    cont = 0
    auth = tweepy.OAuthHandler('I6kyr1A332urtyI7stNQ3S8xG', '6HMMZXdwdyfz3LmYZzQ9Aducye3Tjl80m2T9AJNzZmoUWAFQYe')
    auth.set_access_token('1295243400384520192-2zqFOtBKyHl7zItgLUVI9BaukSEnl3','Gvgrst0Xb1s0aTKNAVtOyWeuQthENFLGXdtdVxuEf39b9')
    api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
    user = api.me()
    '''print(user.name)
    print(user.location)'''
    search = 'shopee', 'promoção shopee', 'na shopee'
    nrTweets = 10
    while True:
        for tweet in tweepy.Cursor(api.search, search).items(nrTweets):
            try:
                print(cont, user.name, user.location, ": @" + tweet.user.screen_name)
                if tweet.id == 'shopee_bot':
                    pass
                '''api.update_status("@" + tweet.user.screen_name + " Estou fenotipicamente certa!", in_reply_to_status_id=tweet.id)'''
                # tweet.favorite()

                cont += 1
                if cont == 10:
                    if os.name == "nt":
                        os.system("cls")
                    else:
                        os.system("clear")

                tweet.retweet()
                time.sleep(35)
            except tweepy.TweepError as e:
                print('\033[1;31m' + e.reason + '\033[0;0m')
            except StopIteration:
                time.sleep(120)
                continue
