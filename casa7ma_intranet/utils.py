from googletrans import Translator
from casa7ma_intranet import settings

def default_trans(text, lang):
    translator = Translator()
    return str(translator.translate(text=text, dest=lang).text).capitalize()