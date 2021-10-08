import speech_recognition as sr
import moviepy.editor as mp
import os
from deep_translator import GoogleTranslator
from pipelines import pipeline


class ML:
    def getFileName(self, path):
        filename, file_ext = os.path.splitext(path)
        return filename, file_ext

    # converting audio to text
    def convert_audio_to_original_text(self, path, src_lang):
        filename, file_ext = self.getFileName(path)
        r = sr.Recognizer()
        print(filename, file_ext)
        if 'wav' not in file_ext:
            clip = mp.VideoFileClip(path)
            clip.audio.write_audiofile(f'{filename}.wav', codec='pcm_s16le')

        with sr.AudioFile(f'{filename}.wav') as source:
            print('Fetching file')
            audio_text = r.record(source)
            try:
                print('Converting audio transcripts into text ...')
                text = r.recognize_google(audio_text, language=src_lang)
                return text
            except:
                return 'Something went wrong'

    # translate the generated text
    def convert_original_text_to_specific_lang(self, text, tgt_lang):
        translated = GoogleTranslator(source='auto',
                                      target=tgt_lang).translate(text)
        return translated

    def generate_questions(self, text):
        nlp = pipeline("question-generation")
        return nlp(
            text
        )  # returns list of dictionaries containing answers and questions


'''
    Language mapping
'''
# {
#   "Afrikaans": [
#     ["South Africa", "af-ZA"]
#   ],
#   "Arabic" : [
#     ["Algeria","ar-DZ"],
#     ["Bahrain","ar-BH"],
#     ["Egypt","ar-EG"],
#     ["Israel","ar-IL"],
#     ["Iraq","ar-IQ"],
#     ["Jordan","ar-JO"],
#     ["Kuwait","ar-KW"],
#     ["Lebanon","ar-LB"],
#     ["Morocco","ar-MA"],
#     ["Oman","ar-OM"],
#     ["Palestinian Territory","ar-PS"],
#     ["Qatar","ar-QA"],
#     ["Saudi Arabia","ar-SA"],
#     ["Tunisia","ar-TN"],
#     ["UAE","ar-AE"]
#   ],
#   "Basque": [
#     ["Spain", "eu-ES"]
#   ],
#   "Bulgarian": [
#     ["Bulgaria", "bg-BG"]
#   ],
#   "Catalan": [
#     ["Spain", "ca-ES"]
#   ],
#   "Chinese Mandarin": [
#     ["China (Simp.)", "cmn-Hans-CN"],
#     ["Hong Kong SAR (Trad.)", "cmn-Hans-HK"],
#     ["Taiwan (Trad.)", "cmn-Hant-TW"]
#   ],
#   "Chinese Cantonese": [
#     ["Hong Kong", "yue-Hant-HK"]
#   ],
#   "Croatian": [
#     ["Croatia", "hr_HR"]
#   ],
#   "Czech": [
#     ["Czech Republic", "cs-CZ"]
#   ],
#   "Danish": [
#     ["Denmark", "da-DK"]
#   ],
#   "English": [
#     ["Australia", "en-AU"],
#     ["Canada", "en-CA"],
#     ["India", "en-IN"],
#     ["Ireland", "en-IE"],
#     ["New Zealand", "en-NZ"],
#     ["Philippines", "en-PH"],
#     ["South Africa", "en-ZA"],
#     ["United Kingdom", "en-GB"],
#     ["United States", "en-US"]
#   ],
#   "Farsi": [
#     ["Iran", "fa-IR"]
#   ],
#   "French": [
#     ["France", "fr-FR"]
#   ],
#   "Filipino": [
#     ["Philippines", "fil-PH"]
#   ],
#   "Galician": [
#     ["Spain", "gl-ES"]
#   ],
#   "German": [
#     ["Germany", "de-DE"]
#   ],
#   "Greek": [
#     ["Greece", "el-GR"]
#   ],
#   "Finnish": [
#     ["Finland", "fi-FI"]
#   ],
#   "Hebrew" :[
#     ["Israel", "he-IL"]
#   ],
#   "Hindi": [
#     ["India", "hi-IN"]
#   ],
#   "Hungarian": [
#     ["Hungary", "hu-HU"]
#   ],
#   "Indonesian": [
#     ["Indonesia", "id-ID"]
#   ],
#   "Icelandic": [
#     ["Iceland", "is-IS"]
#   ],
#   "Italian": [
#     ["Italy", "it-IT"],
#     ["Switzerland", "it-CH"]
#   ],
#   "Japanese": [
#     ["Japan", "ja-JP"]
#   ],
#   "Korean": [
#     ["Korea", "ko-KR"]
#   ],
#   "Lithuanian": [
#     ["Lithuania", "lt-LT"]
#   ],
#   "Malaysian": [
#     ["Malaysia", "ms-MY"]
#   ],
#   "Dutch": [
#     ["Netherlands", "nl-NL"]
#   ],
#   "Norwegian": [
#     ["Norway", "nb-NO"]
#   ],
#   "Polish": [
#     ["Poland", "pl-PL"]
#   ],
#   "Portuguese": [
#     ["Brazil", "pt-BR"],
#     ["Portugal", "pt-PT"]
#   ],
#   "Romanian": [
#     ["Romania", "ro-RO"]
#   ],
#   "Russian": [
#     ["Russia", "ru-RU"]
#   ],
#   "Serbian": [
#     ["Serbia", "sr-RS"]
#   ],
#   "Slovak": [
#     ["Slovakia", "sk-SK"]
#   ],
#   "Slovenian": [
#     ["Slovenia", "sl-SI"]
#   ]
# }
