import settings
import time
from datetime import datetime
import tweepy
import tl

class MyStreamListener(tweepy.StreamListener):

    def on_status(self, status):
        now = self.now()
        screen_name = status.user.screen_name
        print("TWITTER:", status)
        if screen_name in settings.FAVORITE_USERS or True:
            user = settings.FAVORITE_USERS[screen_name]
            tweet_desc = "{}، {} در توییتر:".format(user['name'], user["job"]) + "\n"
            tweet_desc += status.text
            tl.send2channel(tweet_desc)
        else:
            print(now, "Not in list:", screen_name, status.text)

    def on_disconnect(self, notice):
        print("Disconnected", self.now())
        print(notice)

    def now(self):
        return datetime.now()
print("TWITTER AUTH start")
auth = tweepy.OAuthHandler(settings.API_KEY, settings.API_KEY_SECRET)
auth.set_access_token(settings.ACCESS_TOKEN, settings.ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)
print("TWITTER AUTH finish")

following_user_ids = settings.TWITTER_USER_IDS

def stream_twitter():
    # while True:
    # print("TWITTER Listener initializing")
    myStreamListener = MyStreamListener()
    # print("TWITTER Listener initialized")
    try:
        print("twitter streamer started!")
        myStream = tweepy.Stream(auth=api.auth, listener=myStreamListener)
        myStream.filter(follow=following_user_ids, is_async=True)
        print("TWITTER FINISHED")
        # myStream.filter(follow=following_user_ids, is_async=True)
    except Exception as e:
        print("Exception", myStreamListener.now())
        print(e)
        time.sleep(2)



# public_tweets = api.home_timeline()
# for tweet in public_tweets:
#     user_id = tweet.user._json['screen_name']
#     if user_id in settings.FAVORITE_USERS:
#         user = settings.FAVORITE_USERS[user_id]
#         tweet_datetime = tweet.created_at
#         tweet_date = str(tweet_datetime)[:10]
#         tweet_desc = "{}، {} در توییتر:".format(user['name'], user["job"]) + "\n"
#         tweet_link = tweet._json["entities"]["urls"][0]["url"]
#         tweet_desc += tweet_link
#
#         print(tweet_desc)
#         print(tweet.text)
# tl.send2channel(tweet_desc)
