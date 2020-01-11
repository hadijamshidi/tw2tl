import tweepy
import tl
import settings

auth = tweepy.OAuthHandler(settings.API_KEY, settings.API_KEY_SECRET)
auth.set_access_token(settings.ACCESS_TOKEN, settings.ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)

public_tweets = api.home_timeline()


# for tweet in public_tweets:
#     user_id = tweet.user._json['screen_name']
#     if user_id in settings.FAVORITE_USERS:
#         user = settings.FAVORITE_USERS[user_id]
#         tweet_datetime = tweet.created_at
#         tweet_date = str(tweet_datetime)[:10]
#         tweet_desc = "{}، {} در توییتر:".format(user['name'], user["job"]) + "\n"
#         tweet_link = tweet._json["entities"]["urls"][0]["url"]
#         tweet_desc += tweet_link

# print(tweet_desc)
# print(tweet.text)
# tl.send2channel(tweet_desc)

class MyStreamListener(tweepy.StreamListener):

    def on_status(self, status):
        print(status.text)


myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth=api.auth, listener=myStreamListener)
