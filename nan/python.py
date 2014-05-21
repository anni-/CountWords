import operator
import urllib.request
from roundup.backends.indexer_common import STOPWORDS
import requests, collections, bs4
from collections import Counter
import re
words = re.findall('\w+', open('thhgttg.txt').read().lower())
wlist=Counter(words).most_common(100)
print(wlist)
create_tag_image(make_tags(wlist), 'filename.png', size=(1300,1150), background=(0, 0, 0, 255), layout=LAYOUT_MIX, fontname='Molengo', rectangular=True)
