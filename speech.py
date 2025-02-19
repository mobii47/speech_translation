import json
import azure.cognitiveservices.speech as speech

API_KEY = '9be613324ecf4277b3131129c0ee09c9'
ENDPOINT = '<ENDPOINT>'

media_file_path = '<audio file path>'

translation_config = speech.translation.SpeechTranslationConfig(
    subscription=API_KEY, endpoint=ENDPOINT)

translation_config.speech_recognition_language = 'ja-JP'
translation_config.add_target_language('en')


audio_config = speech.audio.AudioConfig(filename=media_file_path)
recognizer = speech.translation.TranslationRecognizer(
    translation_config=translation_config, audio_config=audio_config)

result = recognizer.recognize_once()
vars(result)

# translatin status
result.reason

source_language_text = result.text
duration = result.duration // pow(60, 4)
result.translations['en']

translation_json = json.loads(result.json)
translation_json['RecognitionStatus']
translation_json['Duration']
translation_json['Text']
for translated in translation_json['Translation']['Translations']:
    print(translated['Language'])
    print(translated['Text'])
    print()



recognizer = speech.translation.TranslationRecognizer(
    translation_config=translation_config, audio_config=audio_config)
outputs = []
toStop = False
while not toStop:
    if result.reason == speech.ResultReason.Canceled:
        toStop = True
        break
    result = recognizer.recognize_once()
    translation_json = json.loads(result.json)
    for translated in translation_json['Translation']['Translations']:        
        print(translated['Language'])
        print(translated['Text'])
        outputs.append({'language': translated['Language'],  'text': translated['Text']})
        
print(outputs)
