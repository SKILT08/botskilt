from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import vk_api
import time
import datetime
import random
 
vk = vk_api.VkApi(token="17ef242f5994885165f9439695cc6143abe2c95de63bb34c0c3d96291da9f94fb317c263cd19e5ba23429")
 
vk._auth_token()
 
vk.get_api()

messCount = 0
 
longpoll = VkBotLongPoll(vk, 186642634)
while True:
    try:
        for event in longpoll.listen():
            if event.type == VkBotEventType.MESSAGE_NEW:
                if event.object.peer_id != event.object.from_id:
                    messCount += 1
                    if messCount == 40:
                        delta = datetime.timedelta(hours=3,minutes=0)
                        t = (datetime.datetime.now(datetime.timezone.utc) + delta)
                        newtime = t.strftime("%H:%M")
                        newdate = t.strftime("%d.%m.%Y")
                        vk.method("messages.send",{"peer_id":event.object.peer_id,"message":"Текущее:\nВремя(МСК) : " + newtime + "\nДата : " + newdate,"random_id":0})
                        messCount = 0
    except Exception as ee:
        print(ee)