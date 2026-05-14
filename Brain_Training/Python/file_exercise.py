print("testing starts here:")
f= open("E:\python\code_2023\poem.txt", "r")
# print(f.readlines()[0])
# tok = f.readlines()[1].split()
# print(len(tok))
# print(tok)
# print(tok[1])

'''poem.txt contains famous poem "Road not taken" by poet Robert Frost. 
You have to read this file in your python program and find out words with maximum occurance.'''

print("program starts here:")
poem_str={}
# print(type(poem_str))

for file in f:
    words = file.split()
    print(f"Checking words {words}")
    # print(words)
    for index in words:
        print(index.lower())
        value_found = poem_str.get(index.lower())
        print(f"Value found: {value_found}")
        if value_found == None:
            poem_str[index.lower()] = 1
        else:
            poem_str[index.lower()] += 1

print(poem_str)
word_occurance=list(poem_str.values()) #converting into list
# print(word_occurance)
maxoc=max(word_occurance)       #getting max value from the dict
print("Max occurance of any word is :", maxoc)

for key,val in poem_str.items():
    if val == maxoc:
        print(key,":",val)


# for ind in poem_str:
#     print(ind, "==>", poem_str[ind])

f.close()



# word_stats={}
#
# with open("poem.txt","r") as f:
#     for line in f:
#       words=line.split(' ')
#       for word in words:
#         if word in word_stats:
#           word_stats[word]+=1
#         else:
#           word_stats[word] = 1
#
# print(word_stats)
#
# word_occurances = list(word_stats.values())
# max_count = max(word_occurances)
# print("Max occurances of any word is:",max_count)
#
# print("Words with max occurances are: ")
# for word, count in word_stats.items():
#     if count==max_count:
#         print(word, ":", count)
