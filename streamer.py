import tweepy
import tl
import settings
import time
from datetime import datetime

# auth = tweepy.OAuthHandler(settings.API_KEY, settings.API_KEY_SECRET)
# auth.set_access_token(settings.ACCESS_TOKEN, settings.ACCESS_TOKEN_SECRET)

# api = tweepy.API(auth)

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


#
class MyStreamListener(tweepy.StreamListener):

    def on_status(self, status):
        now = self.now()
        screen_name = status.user.screen_name
        if screen_name in settings.FAVORITE_USERS:
            user = settings.FAVORITE_USERS[screen_name]
            tweet_desc = "{}، {} در توییتر:".format(user['name'], user["job"]) + "\n"
            tweet_desc += status.text
            tl.send2channel(tweet_desc)
            print(now, "YES", status.text)
        else:
            print(now, "Not in list:", screen_name, status.text)

    def on_disconnect(self, notice):
        print("Disconnected", self.now())
        print(notice)

    def now(self):
        return datetime.now()


# following_user_ids = settings.TWITTER_USER_IDS
# while True:
#     myStreamListener = MyStreamListener()
#     try:
#         myStream = tweepy.Stream(auth=api.auth, listener=myStreamListener)
#         myStream.filter(follow=following_user_ids)
#         # myStream.filter(follow=following_user_ids, is_async=True)
#     except Exception as e:
#         print("Exception", myStreamListener.now())
#         print(e)
#         time.sleep(2)

import telethon.sync
from telethon import TelegramClient, events
from telethon.sync import TelegramClient
from telethon import functions, types
from telethon.tl.types import UpdateNewChannelMessage
client = TelegramClient('hadi', settings.TELEGRAM_API_ID, settings.TELEGRAM_API_ID_HASH)

@client.on(events.NewMessage)
async def my_event_handler(event):
    # print("EVENT:", event)
    # print("TYPE:", type(event.original_update), str())
    # print("TO_ID:", event.original_update.message.to_id, event.original_update.message.to_id.channel_id)
    update = event.original_update
    # # if isinstance(original_update, UpdateNewChannelMessage):
    # with TelegramClient('hadi', settings.TELEGRAM_API_ID, settings.TELEGRAM_API_ID_HASH) as client:
    #     result = client(functions.channels.GetFullChannelRequest(
    #         channel=event.original_update.message.to_id.channel_id
    #     ))
    #     print(result.stringify())
    try:
        if isinstance(update, UpdateNewChannelMessage):
            # print("FROM A CHANNEL")
            chan = await client.get_entity(event.original_update.message.to_id)
            print("USERNAME:", chan.username)
            if chan.username in settings.TELEGRAM_FAVORITE_CHANNELS:
                print("FORWARDING MESSAGE!")
                await client.forward_messages(settings.TELEGRAM_CHANNEL, event.original_update.message)
                pass
            # Finally, I need this ...
            # print(chan.title)
            # result = await client(functions.channels.GetFullChannelRequest(
            #     channel=event.original_update.message.to_id.channel_id
            # ))
            # print("result", chan)
            # print("CHANNEL:", chan.__dict__)
            # print("USERNAME:", chan.username)
    except Exception as e:
        print(e)
    # else:
    #     print("NOT CHANNEL")
    # print(event.__dict__)
    # if 'hello' in event.raw_text:
        # await event.reply('hi!')

client.start()
client.run_until_disconnected()
