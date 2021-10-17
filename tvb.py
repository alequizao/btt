#!/bin/env python
# -*- coding: utf-8 -*-
while True:
    import tweepy, time, os
    # @tevinobuzao
    cont = 0
    auth = tweepy.OAuthHandler('KLBBnBc3FSf4NPdNJgn9mCrES', 'dXgzuNify7Zn768P8REQLthHTkuy3SOwcjhKnKg1buOnUnxqC3')
    auth.set_access_token('3816042916-JynzyI76GQfR3swX6CzxHHC6ycrtbBmXsQ72hmK',
                          'yUxepjFrAX5tRqHtjFXOsZQYN7dyWkNkSAyHESw6C3eG9')
    api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
    user = api.me()
    search = 'onibus'
    nrTweets = 5
    while True:
        for tweet in tweepy.Cursor(api.search, search).items(nrTweets):
            try:
                print(cont, user.name, user.location, ": @" + tweet.user.screen_name)
                # api.update_status("@" + tweet.user.screen_name + " Já conhece nosso instagram? www.instagram.com/tevinobuzao ",
                #                  in_reply_to_status_id=tweet.id)
                # tweet.favorite()
                cont += 1
                if cont == 11:
                    if os.name == "nt":
                        os.system("cls")
                    else:
                        os.system("clear")
                # tweet.retweet()
                time.sleep(35)
                tweet.retweet()
            except tweepy.TweepError as e:
                print('\033[1;31m' + e.reason + '\033[0;0m')
            except StopIteration:
                time.sleep(10)
                continue