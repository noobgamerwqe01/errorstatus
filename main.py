import json
import time
import codecs

from core.ServerStatus import *
from core.Webhook import *
from core.Logger import *
from keep_alive import keep_alive
keep_alive()
# print header text
printHeader()

# import config.json
try:
    info("Try import config")
    with codecs.open('config.json', 'r', 'utf-8') as file:
        config = json.load(file)
    info("Success import config")
except:
    error("Fail import config")

print_config(config)
print("\n")
temp1=0
temp2 = 0
temp3 = 0

o1 = 5
o2 = 5
o3 = 5
while True:
    info("Try Get Server Data")
    serverAddress, serverPort, serverisOnline,s1, serverPlayersOnline, serverPlayersMax, serverVersion, serverMotd, currentDateTime = getStatus(f"{config['SERVER_ADDRESS']}:{config['SERVER_PORT']}")
    success("Success Get Server Data")
    serverAddress2, serverPort, serverisOnline2,s2, serverPlayersOnline, serverPlayersMax, serverVersion, serverMotd, currentDateTime = getStatus(f"{config['SERVER_ADDRESS2']}:{config['SERVER_PORT2']}")
    success("Success Get Server Data")
    serverAddress3, serverPort, serverisOnline3,s3, serverPlayersOnline, serverPlayersMax, serverVersion, serverMotd, currentDateTime = getStatus(f"{config['SERVER_ADDRESS3']}:{config['SERVER_PORT3']}")
    success("Success Get Server Data")

    if s1 == 0:
        embed = {
                "title": f"Server {config['SERVER_ADDRESS']} Offline",
                "description": f"The server {config['SERVER_ADDRESS']}:{config['SERVER_PORT']} is currently offline.",
                "color": 0xFF0000  # Red color for offline status
            }
        
        if temp1 == 0:
            temp1 = 1
            o1 = 1
            if config['MESSAGE_ID'] == "":
                info("MESSAGE_ID not found, trying send first message")
                response = SendWebhook(config['WEBHOOK_URL'],embed)
                config['MESSAGE_ID'] = response

                webhook = DiscordWebhook(url=config['WEBHOOK_URL'], content="<@950095450839580732>")
                response = webhook.execute()

                if response.status_code == 200:
                    print(f"server offline {config['SERVER_ADDRESS']}")
                else:
                    print(f"Failed with status code {response.status_code}")


                # write the message id on config file
                with open('config.json', 'w') as f:
                    json.dump(config, f, indent=4)
                
                success("Success send first message and update MESSAGE_ID")
                config['MESSAGE_ID'] = ""
        

            else:
                info("MESSAGE_ID not found, trying send first message")
                response = SendWebhook(config['WEBHOOK_URL'],embed)
                config['MESSAGE_ID'] = response

                webhook = DiscordWebhook(url=config['WEBHOOK_URL'], content="<@950095450839580732>")
                response = webhook.execute()

                if response.status_code == 200:
                    print(f"server offline {config['SERVER_ADDRESS']}")
                else:
                    print(f"Failed with status code {response.status_code}")


                # write the message id on config file
                with open('config.json', 'w') as f:
                    json.dump(config, f, indent=4)
                
                success("Success send first message and update MESSAGE_ID")
                config['MESSAGE_ID'] = ""
        
    if s2 == 0:
        embed = {
                "title": f"Server {config['SERVER_ADDRESS2']} Offline",
                "description": f"The server {config['SERVER_ADDRESS2']}:{config['SERVER_PORT2']} is currently offline.",
                "color": 0xFF0000  # Red color for offline status
            }
        
        if temp2 == 0:
            temp2 = 1
            o2 = 1
            if config['MESSAGE_ID'] == "":
                info("MESSAGE_ID not found, trying send first message")
                response = SendWebhook(config['WEBHOOK_URL'],embed)
                config['MESSAGE_ID'] = response

                webhook = DiscordWebhook(url=config['WEBHOOK_URL'], content="<@950095450839580732>")
                response = webhook.execute()

                if response.status_code == 200:
                    print(f"server offline {config['SERVER_ADDRESS2']}")
                else:
                    print(f"Failed with status code {response.status_code}")


                # write the message id on config file
                with open('config.json', 'w') as f:
                    json.dump(config, f, indent=4)
                
                success("Success send first message and update MESSAGE_ID")
                config['MESSAGE_ID'] = ""
            

            else:
                info("MESSAGE_ID not found, trying send first message")
                response = SendWebhook(config['WEBHOOK_URL'],embed)
                config['MESSAGE_ID'] = response

                webhook = DiscordWebhook(url=config['WEBHOOK_URL'], content="<@950095450839580732>")
                response = webhook.execute()

                if response.status_code == 200:
                    print(f"server offline {config['SERVER_ADDRESS2']}")
                else:
                    print(f"Failed with status code {response.status_code}")


                # write the message id on config file
                with open('config.json', 'w') as f:
                    json.dump(config, f, indent=4)
                
                success("Success send first message and update MESSAGE_ID")
                config['MESSAGE_ID'] = ""
            
            
    #s3 offline
    if s3 == 0 :
        embed = {
                "title": f"Server **{config['SERVER_ADDRESS3']}** Offline",
                "description": f"The server **{config['SERVER_ADDRESS3']}:{config['SERVER_PORT3']}** is currently offline. <@950095450839580732>" ,
                "color": 0xFF0000  # Red color for offline status
            }
        if temp3 == 0:
            temp3 = 1
            o3 = 1
            if config['MESSAGE_ID'] == "":
                info("MESSAGE_ID not found, trying send first message")
                response = SendWebhook(config['WEBHOOK_URL'],embed)
                config['MESSAGE_ID'] = response

                webhook = DiscordWebhook(url=config['WEBHOOK_URL'], content="<@950095450839580732>")
                response = webhook.execute()

                if response.status_code == 200:
                    print(f"server offline {config['SERVER_ADDRESS3']}")
                else:
                    print(f"Failed with status code {response.status_code}")


                # write the message id on config file
                with open('config.json', 'w') as f:
                    json.dump(config, f, indent=4)
                
                success("Success send first message and update MESSAGE_ID")
                config['MESSAGE_ID'] = ""

            else:
                info("MESSAGE_ID not found, trying send first message")
                response = SendWebhook(config['WEBHOOK_URL'],embed)
                config['MESSAGE_ID'] = response

                webhook = DiscordWebhook(url=config['WEBHOOK_URL'], content="<@950095450839580732>")
                response = webhook.execute()

                if response.status_code == 200:
                    print(f"server offline {config['SERVER_ADDRESS3']}")
                else:
                    print(f"Failed with status code {response.status_code}")


                # write the message id on config file
                with open('config.json', 'w') as f:
                    json.dump(config, f, indent=4)
                
                success("Success send first message and update MESSAGE_ID")
                config['MESSAGE_ID'] = ""
        
    #s1 online
    if s1 == 1 :
        embed = {
                "title": f"Server {config['SERVER_ADDRESS2']} back online",
                "description": f"The server {config['SERVER_ADDRESS']}:{config['SERVER_PORT2']} is back online.",
                "color": 0xFF0000  # Red color for offline status
            }
        if o1 == 1:
            o1 = 5
            temp1 = 0
            if config['MESSAGE_ID'] == "":
                info("MESSAGE_ID not found, trying send first message")
                response = SendWebhook(config['WEBHOOK_URL'],embed)
                config['MESSAGE_ID'] = response
                print(f"server online {config['SERVER_ADDRESS']}")


                # write the message id on config file
                with open('config.json', 'w') as f:
                    json.dump(config, f, indent=4)
                
                success("Success send first message and update MESSAGE_ID")
                config['MESSAGE_ID'] = ""

            else:
                info("MESSAGE_ID not found, trying send first message")
                response = SendWebhook(config['WEBHOOK_URL'],embed)
                config['MESSAGE_ID'] = response

                


                # write the message id on config file
                with open('config.json', 'w') as f:
                    json.dump(config, f, indent=4)
                
                success("Success send first message and update MESSAGE_ID")
                config['MESSAGE_ID'] = ""
            
    #s2 online
    if s2 == 1:
        embed = {
                "title": f"Server {config['SERVER_ADDRESS2']} back online",
                "description": f"The server {config['SERVER_ADDRESS2']}:{config['SERVER_PORT2']} is back online.",
                "color": 0xFF0000  # Red color for offline status
            }
        c2 = 0
        if o2 == 1:
            o2 = 5
            temp2 = 0
            if config['MESSAGE_ID'] == "":
                info("MESSAGE_ID not found, trying send first message")
                response = SendWebhook(config['WEBHOOK_URL'],embed)
                config['MESSAGE_ID'] = response
                print(f"server online {config['SERVER_ADDRESS2']}")
                


                # write the message id on config file
                with open('config.json', 'w') as f:
                    json.dump(config, f, indent=4)
                
                success("Success send first message and update MESSAGE_ID")
                config['MESSAGE_ID'] = ""
                

            else:
                info("MESSAGE_ID not found, trying send first message")
                response = SendWebhook(config['WEBHOOK_URL'],embed)
                config['MESSAGE_ID'] = response
                

                

                # write the message id on config file
                with open('config.json', 'w') as f:
                    json.dump(config, f, indent=4)
                
                success("Success send first message and update MESSAGE_ID")
                config['MESSAGE_ID'] = ""
            
    #s3 online
    if s3 == 1 :
        if o2 == 1:
            o3 = 5
            temp3 = 0
            embed = {
                    "title": f"Server {config['SERVER_ADDRESS3']} back online",
                    "description": f"The server {config['SERVER_ADDRESS3']}:{config['SERVER_PORT2']} is back online.",
                    "color": 0xFF0000  # Red color for offline status
                }
            if config['MESSAGE_ID'] == "":
                    info("MESSAGE_ID not found, trying send first message")
                    response = SendWebhook(config['WEBHOOK_URL'],embed)
                    config['MESSAGE_ID'] = response
                    print(f"server online {config['SERVER_ADDRESS3']}")

                    


                    # write the message id on config file
                    with open('config.json', 'w') as f:
                        json.dump(config, f, indent=4)
                    
                    success("Success send first message and update MESSAGE_ID")
                    config['MESSAGE_ID'] = ""

            else:
                    info("MESSAGE_ID not found, trying send first message")
                    response = SendWebhook(config['WEBHOOK_URL'],embed)
                    config['MESSAGE_ID'] = response

                    # write the message id on config file
                    with open('config.json', 'w') as f:
                        json.dump(config, f, indent=4)
                    
                    success("Success send first message and update MESSAGE_ID")
                    config['MESSAGE_ID'] = ""
    sleep(config['SLEEP'])
