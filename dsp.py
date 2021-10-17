#!\Users\ALEQUIZAO\AppData\Local\Programs\Python\Python37\python.exe
# -*- coding: utf-8 -*-

import tweepy, time
auth = tweepy.OAuthHandler('JveFRWpMn5H0GHN1koZvfgUSf','CPpX56LEKnX7J0xM5Op0PLMlJHZv0ycDSVx9FM3GsAVYtC8i2x')
auth.set_access_token('1280829459696885762-e85hmml9sdter8yHUiQQHHuxJgGeux','EBYOQRoAAb8zaMcWKC2xKPQHyfRVa00jIMLRD3cJTd7yF')
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
user = api.me()
search = 'desemprego'
nrTweets = 10

for tweet in tweepy.Cursor(api.search, search).items(nrTweets):
    try:
        tweet.retweet()
        print(user.name)
        time.sleep(37)
    except tweepy.TweepError as e:
        print(user.name,'\033[1;31m' + e.reason + '\033[0;0m')
        continue
