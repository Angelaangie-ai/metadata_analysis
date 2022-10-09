file = open("file.txt", "r")

read = file.readlines()

for sentence in read:

 line = sentence.split()

 for each in line:

   line2 = each.lower()

   line2 = line2.strip("!,@:#$%^&*()_+=")

   if line2.isdigit():

     print(line2)
