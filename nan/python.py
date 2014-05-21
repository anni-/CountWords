import operator
import urllib.request
from collections import Counter
import re
words = re.findall('\w+', open('thhgttg.txt').read().lower())
wlist=Counter(words).most_common(100)
print(wlist)

