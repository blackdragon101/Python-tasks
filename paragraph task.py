para = input("Enter the paragraph: ")
para1 = para.replace(' ',',')
para2 = para1.split(',')
total_words = len(para2)
print(f"The total number of words in the paragraph are:{total_words}")
dict = {}
for words in para2:
    dict.update({words:para2.count(words)})
print(dict)













