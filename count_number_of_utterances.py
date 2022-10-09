utterances = []
with open('file.txt', 'r') as myfile:
 
 for line in myfile.readlines():
 
   utt = line.strip('\n')
 
   utterances.append(utt)
 
print(len(utterances))
