import argparse
import json
import os

from decouple import config
from google.cloud import dialogflow


def create_intent(
    project_id, display_name, training_phrases_parts, message_texts, language_code="ru"
):

    intents_client = dialogflow.IntentsClient()

    parent = dialogflow.AgentsClient.agent_path(project_id)
    training_phrases = []
    for training_phrases_part in training_phrases_parts:
        part = dialogflow.Intent.TrainingPhrase.Part(text=training_phrases_part)
        training_phrase = dialogflow.Intent.TrainingPhrase(parts=[part])
        training_phrases.append(training_phrase)

    text = dialogflow.Intent.Message.Text(text=message_texts)
    message = dialogflow.Intent.Message(text=text)

    intent = dialogflow.Intent(
        display_name=display_name, training_phrases=training_phrases, messages=[message]
    )

    response = intents_client.create_intent(
        request={"parent": parent, "intent": intent, "language_code": language_code}
    )
    return response


def main():
    dialogflow_project_id = config("DIALOGFLOW_PROJECT_ID")
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = config(
        "GOOGLE_APPLICATION_CREDENTIALS"
    )

    parser = argparse.ArgumentParser()
    parser.add_argument("--db_path", default="question.json")
    args = parser.parse_args()
    db_path = args.db_path

    with open(db_path, "r", encoding="utf-8") as f:
        questions = json.load(f)

    for topic, phrases in questions.items():
        create_intent(
            dialogflow_project_id, topic, phrases["questions"], [phrases["answer"]]
        )


if __name__ == "__main__":
    main()
