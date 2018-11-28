def main(words):
  temp=[]
  for word in words:
#sorting characters in words list
     temp.append(sorted(word))
   
   
  for i in range(len(words)):
    for j in range(i+1,len(words)):
      if temp[i] == temp[j]:
         print(i,j)
         print(words[i],words[j])

main(["geeksquiz", "geeksforgeeks", "abcd","forgeeksgeeks", "zuiqkeegs"])
