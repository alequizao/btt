#!\Users\ALEQUIZAO\AppData\Local\Programs\Python\Python37\python.exe
# -*- coding: utf-8 -*-

import tweepy, time, os

# Desemprego bot
cont=0
auth = tweepy.OAuthHandler('5K4XRMs1ETTex2MnMhcbmpN6r','EPtG4AOnGQ3cu8cwAC2UO5nW095uXJ4UGOmaRn1lm6tAsAik7c')
auth.set_access_token('1280829459696885762-QCoAlkLKFZDoKtn3C2FwlJYBB7aU6O','HBffiIzOwrWzs78Zv3twdYBNjLoH5tnMLbeWZtvNrwPtG')
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
user = api.me()
'''print(user.name)
print(user.location)'''
search = 'desemprego'
nrTweets = 10
while True:
    for tweet in tweepy.Cursor(api.search, search).items(nrTweets):
        try:

            print(cont, user.name, user.location, ": @" + tweet.user.screen_name)
            # api.update_status("@" + tweet.user.screen_name + " Já conhece nosso instagram? www.instagram.com/tevinobuzao ",
            #                  in_reply_to_status_id=tweet.id)
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


time.sleep(30)

