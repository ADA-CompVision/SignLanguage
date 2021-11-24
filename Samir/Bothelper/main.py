import re
import pandas as pd
from datetime import datetime

# WARNING! CHANGE STARTDATE
startDate = '01.11.2021'

dateFormat = "%d.%m.%Y"
startDate = datetime.strptime(startDate, dateFormat)
imageFile = 'receive_image_logs.txt'
videoFile = 'receive_video_logs.txt'
csv_file = f'result_{datetime.now().strftime(dateFormat)}.csv'
studentsList = dict()
regex = "(\d{2}\.\d{2}\.\d{4}), (\d{2}:\d{2}:\d{2}):\s*(.*?) saved.*?2021/(\w)"
letters = ['A', 'B', 'C', 'Ç', 'D', 'E', 'Ə', 'F', 'G', 'Ğ', 'H', 'I', 'İ', 'J', 'K',
           'L', 'M', 'N', 'O', 'Ö', 'P', 'Q', 'R', 'S', 'Ş', 'T', 'U', 'Ü', 'V', 'X', 'Y', 'Z']

def fillStudentsList(file):
    with open(file, 'r', encoding='utf-8') as logs:
        for log in logs:
            z = re.match(regex, log)
            if z:
                segments = z.groups()
                uploadDate = datetime.strptime(segments[0], dateFormat)

                if uploadDate >= startDate:
                    if segments[2] in studentsList:
                        studentsList[segments[2]][segments[3]] += 1
                    else:
                        lettersDict = dict(zip(letters, [0] * len(letters)))
                        lettersDict[segments[3]] = 1
                        studentsList[segments[2]] = lettersDict

fillStudentsList(imageFile)
fillStudentsList(videoFile)

stats = []
names = []
for key, value in studentsList.items():
    arr = []
    for letter, count in value.items():
        arr.append(count)
    stats.append(arr)
    names.append(key)

df = pd.DataFrame(stats, columns=letters, index=names)
df['Total'] = df.sum(axis=1)
df.to_csv(csv_file, encoding='utf-8-sig')