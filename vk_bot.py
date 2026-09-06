import logging
import random
import time

import vk_api as vk
from decouple import config
from vk_api.longpoll import VkEventType, VkLongPoll

from dialogflow import detect_intent_text
from tg_logger import setup_logger

logger = logging.getLogger(__name__)


def send_to_vk(event, vk_api, message):
    vk_api.messages.send(
        peer_id=event.peer_id, message=message, random_id=random.randint(1, 1000)
    )


def main():
    setup_logger(config("TG_BOT_TOKEN"), config("TG_USER_ID"), "ВК-бот запущен")
    google_key = config("GOOGLE_APPLICATION_CREDENTIALS")
    dialogflow_project_id = config("DIALOGFLOW_PROJECT_ID")
    vk_token = config("VK_API")

    while True:
        try:
            vk_session = vk.VkApi(token=vk_token)
            vk_api = vk_session.get_api()

            longpoll = VkLongPoll(vk_session)

            for event in longpoll.listen():
                if event.type == VkEventType.MESSAGE_NEW and event.to_me:
                    continue

                answer = detect_intent_text(
                    google_key,
                    dialogflow_project_id,
                    f"vk-{event.peer_id}",
                    event.text,
                    language_code="ru",
                )
                if answer.intent.is_fallback:
                        continue

                send_to_vk(event, vk_api, answer.fulfillment_text)
        except Exception:
            logger.exception("Ошибка в ВК-боте")
            time.sleep(10)


if __name__ == "__main__":
    main()
