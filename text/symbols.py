""" from https://github.com/keithito/tacotron """

'''
Defines the set of symbols used in text input to the model.
'''
_pad        = '_'
_punctuation = ';:,.!?¡¿—…"«»“” '
_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
_letters_ipa = "ɑɐɒæɓʙβɔɕçɗɖðʤəɘɚɛɜɝɞɟʄɡɠɢʛɦɧħɥʜɨɪʝɭɬɫɮʟɱɯɰŋɳɲɴøɵɸθœɶʘɹɺɾɻʀʁɽʂʃʈʧʉʊʋⱱʌɣɤʍχʎʏʑʐʒʔʡʕʢǀǁǂǃˈˌːˑʼʴʰʱʲʷˠˤ˞↓↑→↗↘'̩'ᵻ"

additional_ipa = ['\n', ' ', '!', '"', '#', "'", '(', ')', '*', '+', ',', '-', '.', ':', ';', '=', '?', 'N', 'Q', '[', '\\', ']', '^', '`', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'æ', 'ç', 'ð', 'ŋ', 'ɑ', 'ɔ', 'ə', 'ɛ', 'ɥ', 'ɦ', 'ɪ', 'ɫ', 'ɯ', 'ɸ', 'ɹ', 'ɾ', 'ʃ', 'ʊ', 'ʑ', 'ʒ', 'ʰ', 'ˈ', 'ˌ', 'β', 'θ', '…', '↑', '↓']

# Export all symbols:
symbols = [_pad] + list(_punctuation) + list(_letters) + list(_letters_ipa) + additional_ipa
symbols = list(dict.fromkeys(symbols))

# Special symbol ids
SPACE_ID = symbols.index(" ")
