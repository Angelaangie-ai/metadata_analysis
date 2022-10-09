count = 0
file = open("ke_sentences.txt", "r")
read_data = file.read()
words = set(read_data.split())
count = len(words)
print("Total Unique Words:", count)
