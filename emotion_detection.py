import requests
import json


def emotion_detector(text_to_analyze):
    URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    Headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = {"raw_document": {"text": text_to_analyze}}

    r = requests.post(URL, headers=Headers, json=input_json)
    my_json = r.json()
    predicted_emotions = my_json.get('emotionPredictions', [])
    myfirstemotion = predicted_emotions[0]


    emotions = myfirstemotion.get('emotion', {})

    anger = emotions.get('anger', 0.0)
    disgust = emotions.get('disgust', 0.0)
    fear = emotions.get('fear', 0.0)
    joy = emotions.get('joy', 0.0)
    sadness = emotions.get('sadness', 0.0)

    dominant_emotion = max(emotions, key=emotions.get) if emotions else "Unknown" 

    emotion_dict ={
    'anger': anger,
    'disgust': disgust,
    'fear': fear,
    'joy': joy,
    'sadness': sadness,
    'dominant_emotion': dominant_emotion
    }

    return emotion_dict

if __name__ == '__main__':
    text = "I love this new technology."
    emotion = emotion_detector(text)