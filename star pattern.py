# This is a python program to make A star pattern.
# n = 4
# for no_of_lines in range(1, n+1):
#     for no_of_stars in range(1, no_of_lines+1):
#         print("*", end='')
#     print()
# for iteration in range(3,0,-1):
#     print('*'*iteration)

userdata_file = open("file1.txt","a")
newdata = userdata_file.write(" i can say it")
userdata_file.close()
newfile = open("file1.txt","r")
read = newfile.read()
print(read)
newfile.close()


