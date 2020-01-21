import telethon.sync
from telethon import TelegramClient, events
from telethon.sync import TelegramClient
from telethon import functions, types
from telethon.tl.types import UpdateNewChannelMessage
import settings
import telegram

print("TELEGRAM AUTH start")
client = TelegramClient('hadi', settings.TELEGRAM_API_ID, settings.TELEGRAM_API_ID_HASH)
print("TELEGRAM AUTH finished")

async def send2channel(msg):
	client.send_message(settings.TELEGRAM_CHANNEL, msg)
	pass

async def forward(msg):
    await client.forward_messages(settings.TELEGRAM_CHANNEL, msg)
    pass


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
			# print("USERNAME:", chan.username)
			# await forward(event.original_update.message)
			if chan.username in settings.TELEGRAM_FAVORITE_CHANNELS:
			# print("FORWARDING MESSAGE!")
				await forward(event.original_update.message)
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

def stream_telegram():
	print("TELEGRAM STREAM START")
	client.start()
	client.run_until_disconnected()
