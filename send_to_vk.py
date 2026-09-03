import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from decouple import config

VK_API = config('VK_API')
vk_session = vk_api.VkApi(token=VK_API)

longpoll = VkLongPoll(vk_session)

for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW:
        print('Новое сообщение:')
        if event.to_me:
            print('Для меня от: ', event.user_id)
        else:
            print('От меня для: ', event.user_id)
        print('Текст:', event.text)