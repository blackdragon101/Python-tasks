from datetime import datetime
file1 = open('input.txt','r')
contents = file1.readlines()
file1.close()
file2 = open('backupfile.txt','w')
for lines in contents:
    file2.write(lines)
    now = datetime.now()
    timestamp = now.strftime("%d/%m/%Y %H:%M")
    file2.write(timestamp)
    file2.write('\n')
file2.close()

