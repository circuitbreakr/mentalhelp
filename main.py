import discord
import os
import random

intents = discord.Intents.all()
client = discord.Client(intents=intents)

prev = ''

# function that randomizes a result, rerolling if the result is the same as the previous one pulled
def choose_response(list):  
  # python is stupid and scope is weird so i have to make variables with different names :/
  funct_prev = prev
  response = ''
  
  while True:
    response = random.choice(list)
    if funct_prev != response:
      return response

# returns true if any phrase in the list is inside str, returns false otherwise
def contains(str, list):
  for phrase in list:
    if phrase in str:
      return True
  return False

# user words that the bot will respond to (in dms)
sad = ['therapy', 
       'school is hard',
       'sad',
       'UGH',
       'BRUH',
       ':sob:',
       'bro :sob:',
       'no',
       'no.',
       'im not ok',
       'blah',
       'lalala',
       ':disappointed:',
       'bad',
       'help me pwease :owocry:']
depression = ['death',
              'die',
              'suicide',
              'kill myself',
              'im tired of living',
              'i wish i were dead',
              'i cant take it anymore',
              'i cant do this anymore',
              'i want to give up',
              'life is pointless',
              'whats the point of life?',
              'i need help',
              'im not ok',
              'i am not ok',
              'everyone would be better off without me',
              'why am i even here',
              'i want to die',
              'i want to give up',
              'i cant do anything right',
              'im a burden',
              'my life has no purpose',
              'im going to kill myself',
              'i shouldnt bother people with my problems',
              'i dont want to bother people with my problems',
              'bother',
              'i hate myself']
imposter = ['fraud',
            'sus',
            'not enough',
            'imposter syndrome',
            'fuck up',
            'im not smart enough',
            'im too lazy',
            'everyone is smarter than me',
            'i dont fit in',
            'im not good at anything',
            'i dont know anything',
            'doubt',
            'i keep doubting myself',
            'im stupid',
            'im tired of faking it',
           ]

# message bank that the bot can pull from when responding
encouraging = ['you can do it!',
              'i believe in you!',
               'you got this!'
              ]
comfort = ['it\'s going to be alright!',
          'don\'t worry, it\'ll be okay!']
# responses to imposter syndrome
assure = ['you are enough',
          'you are not alone',
          'you need to let go of your perfectionism',
          'be kind to yourself!',
          'try tracking your success',
          'embrace the feeling, you are better than you think you are',
          'you are just as qualified as anyone else',
          'say yes to new opportunities',
          'talk with someone (301) 314-4357 <- UMD health center',
          'everyone feels like an imposter sometimes, ITS GOING TO BE OK!!',
          'youre underplaying yourself!',
          'stop doubting yourself! :triumph:',
          'keep things in perspective',
          'look at yourself from a different perspective!',
          'fake it til u make it!'
         ]
# if you say help in dms
questions = ['is everything ok?',
            'are you alright?',
            'do you need help?',
            'how are you feeling?',
            'do you want someone to talk to? :)',
            'how was your day?',
            'are you ok?'
            ]

# what the bot does when certain things happen
# on startup
@client.event
async def on_ready():
    print('good morning!')

# when the bot joins a new server
@client.event
async def on_guild_join(guild):
  for channel in guild.text_channels:
    try:
      await channel.send('hi! my name is mentalhelp! if you ever feel sad, upset, or want someone to talk to, feel free to dm me!')
    except Exception:
      continue
    else:
      break

# when a message is sent to it (in dms)
@client.event
async def on_message(message):
  msg = message.content.lower()
  
  # makes sure that the bot doesn't respond to itself
  if message.author == client.user:
      return

  # say hi back if you say hi to it :)
  if msg == 'hello':
      await message.channel.send('hi!!!')
      return
  
  # when a message is sent to it (in dms)
  if isinstance(message.channel, discord.DMChannel):
    if 'help' in msg:
      prev = choose_response(questions)
      await message.channel.send(prev)
    elif 'thanks' in msg or 'thank you' in msg:
      await message.channel.send('you\'re welcome! remember, your mental health is very important! take care of yourself!')
    elif contains(msg, sad):
      prev = choose_response(encouraging)
      await message.channel.send(prev)
    elif contains(msg, imposter):
      prev = choose_response(assure)
      await message.channel.send(prev)
    elif contains(msg, depression):
      prev = choose_response(comfort)
      await message.channel.send(prev)
    else:
      await message.channel.send('im sorry, i cant help with that... :( is there something else bothering you?')
      
  # when a message appears in a server it is in
  else:
    if msg == 'help':
      await message.channel.send('i can see that you\'re not doing alright. message me if you want a little pick-me-up!')

client.run(os.getenv('TOKEN'))