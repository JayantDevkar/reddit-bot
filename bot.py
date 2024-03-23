import praw
from Dora import *
import time

reddit = praw.Reddit(client_id='xxx',
                     client_secret='xxx',
                     user_agent='xxx',
                     username='xxx',
                     password='xxx')

# sub where it will be operating
my_subreddit = reddit.subreddit('AboutJayant')

# Phrase to activate bot
call_phrase = '!AskJ'

replied_to = []

# For checking the comments
for comment in my_subreddit.stream.comments():
    redditor = comment.author
    poster = redditor.name
    flag = comment.id not in replied_to
    flag2 = poster != "BeatMyMeatBoi"
    if call_phrase in comment.body and flag and flag2:
        replied_to.append(comment.id)
        qns = comment.body.replace(call_phrase, '')
        # time.sleep(5)
        try:
            reply = get_reply(qns)
            comment.reply(reply)

        except:
            continue
    elif flag2:
        print(poster)

# 		try:
# 			reply = 'You asked: '
# 			comment.reply(reply+qns)
# 			print(poster)
# 		except:
# 			print("eror")
# 	# elif flag and flag2:
# 	# 	print(poster)
# 	# 	comment.reply("Please use <!AskJ> tag to ask questions!")
