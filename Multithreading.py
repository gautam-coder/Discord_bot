import os
import threading
import discord
#Discord_Bot_Token=os.environ['Discord_Bot_token']

Discord_Bot_Token_list=["put all the 100 discord tokens in list"]
#print(Discord_Bot_Token_list)

def run_all(token_id):
    client=discord.Client(intents=discord.Intents.all())
    print(str(token_id)+"is logged in",end=" ")
    @client.event
    async def on_message(message):
        print("blah blah")

    client.run(token_id)

#Multithreading

threads=[]
for i in range(0,99):
    thread=threading.Thread(target=run_all,args=(Discord_Bot_Token_list[i],))
    threads.append(thread)
    thread.start()

#Wait All threads to finish

for i in threads:
    i.join()
    
