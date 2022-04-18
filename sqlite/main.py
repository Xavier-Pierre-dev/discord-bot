import os
import discord
import requests
import json
import random
#from replit import db
from keep_alive import keep_alive
import sqlite3
from dotenv import load_dotenv, find_dotenv


load_dotenv(find_dotenv())
my_secret = os.getenv("TOKEN")


conn = sqlite3.connect("database.db")
c = conn.cursor()

c.execute("DROP TABLE IF EXISTS encouragement")

# Create the table, read the article below if you
# are unsure of what they mean
# https://www.w3schools.com/sql/sql_datatypes.asp
SQL_STATEMENT = """CREATE TABLE IF NOT EXISTS encouragement (
	encouragement_number INTEGER PRIMARY KEY,
	encouragement_sentence VARCHAR(20),
	UNIQUE(encouragement_sentence)
);"""
c.execute(SQL_STATEMENT)


db={"responding":"true"}
print(db["responding"])

# Insert some users into our database
c.execute("""INSERT INTO encouragement VALUES (23, "My sentence 1");""")
c.execute("""INSERT INTO encouragement VALUES (5, "My sentence 2");""")
c.execute("""INSERT INTO encouragement VALUES (7, "My sentence 3");""")
c.execute("""INSERT INTO encouragement VALUES (11, "My sentence 4");""")
c.execute("""INSERT INTO encouragement VALUES (8, "My sentence 5");""")




client = discord.Client()


sad_words = ["sad", "depressed", "unhappy", "angry", "miserable", "depressing"]

starter_encouragements = [
    "Cheer up!",
    "Hang in there.",
    "You are a great person / bot!"
]

if "responding" not in db.keys():
    db["responding"] = True


def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + " -" + json_data[0]['a']
    return (quote)


def update_encouragements(encouraging_message):
    #if "encouragements" in db.keys():
        #encouragements = db["encouragements"]
        #encouragements.append(encouraging_message)
        print(encouraging_message)
        c.execute("INSERT INTO encouragement VALUES (NULL, \"" + encouraging_message + "\");")
        #db["encouragements"] = encouragements
    #else:
    #    db["encouragements"] = [encouraging_message]


def delete_encouragment(index):
    print("DELETE * FROM encouragement WHERE (encouragement_number = "+ str(index) +")")
    statement = "DELETE FROM encouragement WHERE (encouragement_number = \""+ str(index) +"\")"
    c.execute(statement)
    #encouragements = db["encouragements"]
    #if len(encouragements) > index:
    #    del encouragements[index]
    #    db["encouragements"] = encouragements


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    msg = message.content

    if msg.startswith('$inspire'):
        quote = get_quote()
        await message.channel.send(quote)

    if db["responding"]:
        options = starter_encouragements
        #if "encouragements" in db.keys():
        #    options = options + db["encouragements"]

        if any(word in msg for word in sad_words):
            #await message.channel.send(random.choice(options))
            resp = c.execute("SELECT encouragement_sentence FROM encouragement ORDER BY RANDOM() LIMIT 1")
            row = resp.fetchall()
            await message.channel.send(row[0][0])

    if msg.startswith("$new"):
        encouraging_message = msg.split("$new ", 1)[1]
        update_encouragements(encouraging_message)

        await message.channel.send("New encouraging message added.")

    if msg.startswith("$del"):
        encouragements = []
        index = int(msg.split("$del", 1)[1])
        delete_encouragment(index)
        encouragements = db["encouragements"]
        #if "encouragements" in db.keys():
            #index = int(msg.split("$del", 1)[1])
            #delete_encouragment(index)
            #encouragements = db["encouragements"]

        await message.channel.send(encouragements)

    if msg.startswith("$list"):
        encouragements = []
        resp = c.execute("SELECT encouragement_sentence FROM encouragement")
        rows = resp.fetchall()
        my_resp = ""
        for row in rows:
            my_resp = my_resp + row[0] + "\n"
        await message.channel.send(my_resp)
        #if "encouragements" in db.keys():
        #    encouragements = db["encouragements"]
        #await message.channel.send(encouragements)

    if msg.startswith("$responding"):
        value = msg.split("$responding ", 1)[1]

        if value.lower() == "true":
            db["responding"] = True
            await message.channel.send("Responding is on.")
        else:
            db["responding"] = False
            await message.channel.send("Responding is off.")




keep_alive()
client.run(my_secret)