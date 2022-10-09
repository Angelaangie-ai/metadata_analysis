import re
import collections

frequencies = re.findall('\w+', open('file.txt').read().lower())
cnt = collections.Counter()
words = re.findall('\w+', open('file1.txt').read().lower())
for word in words:
    if word in frequencies:
        cnt[word] += 1
print (cnt)
