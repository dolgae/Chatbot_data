import pandas as pd

df = pd.read_csv('ChatbotData.csv', encoding='utf-8')
sentences = list(df['Q']) + list(df['A'])
tokenized_sentences = [s.split() for s in sentences]
sent_len_by_token = [len(t) for t in tokenized_sentences]
sent_len_by_emjeol = [len(s.replace(' ','')) for s in sentences]
# print(sent_len_by_emjeol)

from konlpy.tag import Okt

okt = Okt()

morph_tokenized_sentences = [okt.morphs(s.replace(' ', '')) for s in sentences]
sent_len_by_morph = [len(t) for t in morph_tokenized_sentences]

print(sent_len_by_morph)