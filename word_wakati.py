from janome.tokenizer import Tokenizer

def word_seq(text, part_of_speech=['名詞'],stop_words=[]):
    """  """
    t = Tokenizer()
    text = text.replace(' ', '')
    results = t.tokenize(text)
    words = []
    for token in results:
        w = token.base_form
        pos = token.part_of_speech.split(',')[0]
        if pos in part_of_speech:
#        if not token.part_of_speech.startswith('記号'):
#        if not token.part_of_speech.split(',')[0] in ['記号', '助詞', '助動詞']:
            if not w in stop_words:
                words.append(w) # 基本形
    return words