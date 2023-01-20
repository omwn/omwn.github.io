from collections import defaultdict as dd
import toml

import wn
en = wn.Wordnet('omw-en:1.4')

cutoff = 25

tops = dd(list)

for s in en.senses():
    top = s.synset().lexfile()
    lemma = s.word().lemma()
    freq = sum(s.counts())
    sid = s.synset().id[7:]
    tops[top].append((freq, str(lemma), sid))

### Keep the most frequent
short = dd(lambda: dd(list))

for top in tops:
    (pos, topic) = top.split('.')
    for triple in sorted(tops[top], reverse=True)[:cutoff]:
        # toml requires a homogenous array
        short[pos][topic].append([str(x) for x in triple])


print(toml.dumps(short))
