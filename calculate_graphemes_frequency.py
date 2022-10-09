freqs = {}
with open('file.txt') as f:
   for line in f:
       for char in line:
           freqs.setdefault(char, 0)
           freqs[char] += 1
print(freqs)
