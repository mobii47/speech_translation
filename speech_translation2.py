import azure.cognitiveservices.speech as speechsdk

def translation_from_mic():
    speech_key = "9be613324ecf4277b3131129c0ee09c9"
    service_region = "eastus"
    """performs one-shot speech translation from input from the default microphone"""
    # <TranslationOnceWithMic>
    # set up translation parameters: source language and target languages
    src_lang_config = speechsdk.languageconfig.AutoDetectSourceLanguageConfig(
    languages=[
        "en-US",
        "fr-FR",
        "de-DE",
        "es-ES",
    ])
#     speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=service_region)
#     speech_config.set_property(
#         property_id=speechsdk.PropertyId.SpeechServiceConnection_LanguageIdMode, value='Continuous')
#     speech_recognizer = speechsdk.SpeechRecognizer(
#     speech_config=speech_config, auto_detect_source_language_config=src_lang_config
# )
    translation_config = speechsdk.translation.SpeechTranslationConfig(
        subscription=speech_key, region=service_region,
        speech_recognition_language='en-US',
        target_languages=('de', 'fr', 'zh-Hans', 'ja', 'en-US'))
    # translation_config.set_property(
        # property_id=speechsdk.PropertyId.SpeechServiceConnection_LanguageIdMode, value='Continuous')

    audio_config = speechsdk.audio.AudioConfig(use_default_microphone=True)

    # Creates a translation recognizer using and audio file as input.
    recognizer = speechsdk.translation.TranslationRecognizer(
        translation_config=translation_config, audio_config=audio_config)

    # Starts translation, and returns after a single utterance is recognized. The end of a
    # single utterance is determined by listening for silence at the end or until a maximum of 15
    # seconds of audio is processed. It returns the recognized text as well as the translation.
    # Note: Since recognize_once() returns only a single utterance, it is suitable only for single
    # shot recognition like command or query.
    # For long-running multi-utterance recognition, use start_continuous_recognition() instead.
    result = recognizer.start_continuous_recognition()

    # Check the result
    if result.reason == speechsdk.ResultReason.TranslatedSpeech:
        print("""Recognized: {}
        German translation: {}
        French translation: {}
        Chinese translation: {}
        Japaneese translation: {}
        English translation: {}""".format(
            result.text, result.translations['de'],
            result.translations['fr'],
            result.translations['zh-Hans'],
            result.translations['ja'],
            result.translations['en'],))
    elif result.reason == speechsdk.ResultReason.RecognizedSpeech:
        print("Recognized: {}".format(result.text))
    elif result.reason == speechsdk.ResultReason.NoMatch:
        print("No speech could be recognized: {}".format(result.no_match_details))
    elif result.reason == speechsdk.ResultReason.Canceled:
        print("Translation canceled: {}".format(result.cancellation_details.reason))
        if result.cancellation_details.reason == speechsdk.CancellationReason.Error:
            print("Error details: {}".format(result.cancellation_details.error_details))

translation_from_mic()