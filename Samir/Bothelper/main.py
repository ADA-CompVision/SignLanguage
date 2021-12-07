import re
import pandas as pd
from datetime import datetime

# WARNING! CHANGE STARTDATE
startDate = '01.11.2021'

dateFormat = "%d.%m.%Y"
startDate = datetime.strptime(startDate, dateFormat)
imageFile = 'files/receive_image_logs.txt'
imageFileOld = 'files/receive_image_logs_old.txt'
videoFile = 'files/receive_video_logs.txt'
videoFileOld = 'files/receive_video_logs_old.txt'
usernameFile = 'files/userName_userId.txt'
csv_file = f'result_{datetime.now().strftime(dateFormat)}.csv'
studentsList = dict()
usernameIdMap = dict()
regex = "(\d{2}\.\d{2}\.\d{4}), (\d{2}:\d{2}:\d{2}):\s*(.*?) saved.*?2021/(\w)"
regexUsernameId = "{'username': '(.*?)', 'id': (.*?)}"
regexUsernameUpload = "(\d{2}\.\d{2}\.\d{4}), (\d{2}:\d{2}:\d{2}): User with Id (.*?) saved the file"
letters = ['A', 'B', 'C', 'Ç', 'D', 'E', 'Ə', 'F', 'G', 'Ğ', 'H', 'I', 'İ', 'J', 'K',
           'L', 'M', 'N', 'O', 'Ö', 'P', 'Q', 'R', 'S', 'Ş', 'T', 'U', 'Ü', 'V', 'X', 'Y', 'Z', 'NA']

def createUsernameIdMap(file):
    with open(file, 'r') as lines:
        for line in lines:
            z = re.match(regexUsernameId, line)
            if z:
                segments = z.groups()
                username = segments[0]
                userId = segments[1]

                if userId not in usernameIdMap:
                    usernameIdMap[userId] = username

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
            else:
                # username is not available, parse the id, find in the id-username map
                z = re.match(regexUsernameUpload, log)

                if z:
                    segments = z.groups()
                    uploadDate = datetime.strptime(segments[0], dateFormat)

                    if uploadDate >= startDate:
                        # if username is not found, make username the userId
                        username = segments[2]
                        if segments[2] in usernameIdMap:
                            username = usernameIdMap[segments[2]]

                        if username in studentsList:
                            studentsList[username]['NA'] += 1
                        else:
                            lettersDict = dict(zip(letters, [0] * len(letters)))
                            lettersDict['NA'] = 1
                            studentsList[username] = lettersDict

createUsernameIdMap(usernameFile)
fillStudentsList(imageFile)
fillStudentsList(imageFileOld)
fillStudentsList(videoFile)
fillStudentsList(videoFileOld)

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