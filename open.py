import urllib.request
import os

f = open('links2.txt')


# create folders if they don't exist
try:
    os.chdir('./Unacademy/')

except FileNotFoundError:
    os.mkdir("./Unacademy/")
    os.mkdir("./Unacademy/Doubt-Sessions")
    os.mkdir("./Unacademy/Chapters/")
    os.chdir('./Unacademy/')

i = 1

for line in f:
    chapter_title = line[57:len(line)-15]
    data = urllib.request.urlopen(line)

    if 'Doubt_Clearing' in chapter_title:
        try:
            f2 = open(f'./Doubt-Sessions/{chapter_title + str(i)}.pdf','r')
            i += 1

            continue
        
        except FileNotFoundError:
            f2 = open(f'./Doubt-Sessions/{chapter_title + str(i)}.pdf','wb')
            f2.write(data.read())
            f2.close()

        i += 1
    
    try:
        f2 = open(f'./Chapters/{chapter_title}.pdf','r')
        continue

    except FileNotFoundError:
        f2 = open(f'./Chapters/{chapter_title}.pdf','wb')
        f2.write(data.read())
        f2.close()
        clo




