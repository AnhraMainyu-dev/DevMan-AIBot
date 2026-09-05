import os

from google.cloud import dialogflow


def detect_intent_text(google_key, project_id, session_id, text, language_code):
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = google_key
    session_client = dialogflow.SessionsClient()
    session = session_client.session_path(project_id, session_id)

    text_input = dialogflow.TextInput(text=text, language_code=language_code)
    query_input = dialogflow.QueryInput(text=text_input)

    response = session_client.detect_intent(
        request={"session": session, "query_input": query_input}
    )
    return response.query_result
