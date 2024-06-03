with open('input.txt','w') as fileptr:
    for x in range(5):
        line_input = input(f"Enter the line{x+1}: ")
        fileptr.write(line_input)
        fileptr.write('\n')
fileptr.close()
fileptr2 = open('input.txt','r')
read = fileptr2.readlines()
print(read)
fileptr2.close()
fileptr3 = open('output.txt','w')
for lines in read:
    line_no = (read.index(lines)+1)
    word_list = lines.split()
    for words in word_list:
        reverse = words[::-1]
        fileptr3.write(reverse)
    fileptr3.write(str(line_no))
    fileptr3.write('\n')
fileptr3.close()
new_file = open('output.txt','r')
text = new_file.read()
print(text)
new_file.close()








