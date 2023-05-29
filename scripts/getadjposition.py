from collections import defaultdict as dd
import toml
import wn

###
### python3 getadjposition.py > ../web/etc/adjposition.examples.toml 
### 


en = wn.Wordnet('omw-en:1.4')

cutoff = 25

adjps = dd(list)

for s in en.senses():
    if (adjp := s.adjposition()):
        lemma = s.word().lemma()
        freq = sum(s.counts())
        sid = s.synset().id[7:]
        adjps[adjp].append((freq, str(lemma), sid))

### Keep the most frequent
short = dd(list)

for adjp in adjps:
    for triple in sorted(adjps[adjp], reverse=True)[:cutoff]:
        # toml requires a homogenous array
        short[adjp].append([str(x) for x in triple])
        
print(toml.dumps(short))
