from instabot import Bot 
from PIL import Image, ImageFont, ImageDraw
from datetime import date
import datetime 
import os
from discord_webhook import DiscordWebhook

current_time = datetime.datetime.now()
today = date.today()
print(today)
bg_image = Image.open("Barwadis1.jpeg")
quote_image = ImageDraw.Draw(bg_image)
d0 = date(2021, 10, 27)
d1 = date(current_time.year, current_time.month, current_time.day)
delta = d1 - d0
print(f"Day {delta.days}")
quote_font = ImageFont.truetype('RobotoSlab-VariableFont_wght.ttf', 52)
quote_text = [f'''                       
                
                
                        
                        
                        Day {delta.days}
        Of trying to have a call 
                with brandon
            Hope he see’s this
        Comment @brawadis
       to support this journey
       
       
                --SohanSeri''']
offset = 0
for i in quote_text:
    i = i.split(".")
    for ix in i:
        quote_image.text((15,15+offset), ix, (0, 0, 0), font=quote_font)
        offset += 100
        quote_image.text((15,15+offset), "", (0, 0, 0), font=quote_font)
        bg_image.save(f"Editday {delta.days}.jpg")

if os.path.isfile("config\\Zoomwithbrawadis_uuid_and_cookie.json"):
    os.remove("config\\Zoomwithbrawadis_uuid_and_cookie.json")

bot = Bot() 

bot.login(username = "Zoomwithbrawadis", 
        password = "Sohan9948081097") 

bot.upload_photo(f"Editday {delta.days}.jpg", 
                caption =f'''Day {delta.days} Less go ✨+ I am sure i can meet him one day ; Zoom with @Brawadis Comment @Brawadis
                .
                .
                .
                .
                .
                .
                .
                @simplistic @fazerug @astonishingawadis @jfiggs @mama.rug @baeeeeelyn @ruq_brawadis_everyday
                .
                .
                .
                .
                .
                .
                .
                .
                .
                .
                #brawadis #follow #fazerug #like #brawadsquad #faze #mamarug #paparug #fazeup #youtube #f #followforfollowback #explorepage #brackie #followback #likeforlikes #shermantheverman #likes #fazeclan #explore #awadis #jackie #brawadisandjackie #brandon #jfigggs #rugrats #support #challenge''')
now = datetime.now()

current_time = now.strftime("%H:%M:%S")
webhook = DiscordWebhook(url='https://discord.com/api/webhooks/903003003752173608/SsCL4FbTQf41Z2DvCLbCwSQVnUPBoxMjLkHP-s_7_ZbrNWm5Ute9HLUggUIFjYQmWByb', rate_limit_retry=True,
                            content=f'Image posted succesfully at {current_time}; its Day {delta.days} Dont give up')
response = webhook.execute()
os.remove(f"Editday {delta.days}.jpg")
