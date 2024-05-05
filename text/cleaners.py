""" from https://github.com/Plachtaa/VITS-fast-fine-tuning """

from text.english import english_to_lazy_ipa, english_to_ipa2, english_to_lazy_ipa2
from text.japanese import japanese_to_romaji_with_accent, japanese_to_ipa, japanese_to_ipa2, japanese_to_ipa3
from text.korean import latin_to_hangul, number_to_hangul, divide_hangul, korean_to_lazy_ipa, korean_to_ipa
from text.chinese import chinese_to_ipa, chinese_to_lazy_ipa



# ---------------------------------------------------------------------------- #
# |                                IPA cleaners                              | #
# ---------------------------------------------------------------------------- #
def ipa_cleaner(text, language):
    def get_lang_code(char):
        def is_english(char):
            return 'a' <= char <= 'z' or 'A' <= char <= 'Z'
        def is_japanese(char):
            return '\u3040' <= char <= '\u309F' or '\u30A0' <= char <= '\u30FF' or '\u4E00' <= char <= '\u9FAF'
        def is_korean(char):
            return '\uAC00' <= char <= '\uD7AF'

        if is_japanese(char):
            return 'jp'
        if is_korean(char):
            return 'kr'
        if is_english(char):
            return 'en'
        return ''

    def convert_to_ipa(seq, lang):
        if lang == 'jp':
            return japanese_to_ipa2(seq)
        elif lang == 'kr':
            return korean_to_ipa(seq)
        elif lang == 'en':
            return english_to_ipa2(seq)
        return ''

    cleaned=''
    lang=language
    subseq=''
    for char in text:
        next_lang=get_lang_code(char)
        if next_lang == '' or lang == next_lang or ((lang == 'kr' or lang == 'jp') and next_lang == 'en'):
            subseq+=char
        elif len(subseq) != 0:
            cleaned+=convert_to_ipa(subseq, lang) + ' '
            subseq=char
            lang=next_lang
        else:
            subseq=char
            lang=next_lang
    if len(subseq) != 0:
        cleaned += convert_to_ipa(subseq, lang) + ' '
    return cleaned