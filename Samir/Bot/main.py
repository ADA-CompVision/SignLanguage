#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import pandas as pd
from pandas.core.frame import DataFrame
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

import os
import uuid
import datetime

#date = datetime.datetime.now()
# letter = 'lt'
userList = []
idList = []
letters = ['A', 'B', 'C', 'Ç', 'D', 'E', 'Ə', 'F', 'G', 'Ğ', 'H', 'I', 'İ', 'J', 'K', 'L', 'M', 'N', 'O', 'Ö', 'P', 'Q', 'R', 'S', 'Ş', 'T', 'U', 'Ü', 'V', 'X', 'Y', 'Z']
lastCacheTime = None
cacheDuration = 3 #hours

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

# Define a few command handlers. These usually take the two arguments update and
# context. Error handlers also receive the raised TelegramError object in error.
def start(update, context):
    """Send a message when the command /start is issued."""
    update.message.reply_text('Jest Dili botu sizi Salamlayır. Azərbaycan Jest Dilinin Tanınması ideyasını həyata keçirmək üçün data toplanmasında dəstəyinizə eytihacımız var. Hər birinizdən hər bir hərf üçün nümunələrə uyğun ən azı 1 ədəd şəkil vəya video (bəzi hərflər hərəkətli olduğundan videoya ehtiyac yaranır.) çəkib göndərməyinizi sizdən xahiş edirik. Dəstəyiniz üçün öncədən təşəkkür edirik.')
    update.message.reply_text('Hazırda aşağıdakı hərflərə daha çox ehtiyacımız var: ' + getMinLetters() + '. Xahiş edirik, hərflərdən birini qeyd edərək başlayın.')

def help(update, context):
    """Send a message when the command /help is issued."""
    update.message.reply_text('Azərbaycan Jest Dilinin Tanınması ideyasını həyata keçirmək üçün data toplanmasında dəstəyinizə eytihacımız var. Hər birinizdən hər bir hərf üçün nümunələrə uyğun ən azı 1 ədəd şəkil vəya video (bəzi hərflər hərəkətli olduğundan videoya ehtiyac yaranır.) çəkib göndərməyinizi sizdən xahiş edirik. Dəstəyiniz üçün öncədən təşəkkür edirik.')    
    update.message.reply_text('Hazırda aşağıdakı hərflərə daha çox ehtiyacımız var: ' + getMinLetters() + '. Xahiş edirik, hərflərdən birini qeyd edərək başlayın.')

def showData(update, context):
    """Send a message when the command /showDate is issued."""
    strDict = ''
    letterDict = readCountCache()

    for letter in letterDict:
        strDict += letter + ' : ' + str(letterDict[letter]) + '\t' * 7

    update.message.reply_text('Hazırda yığılan şəkil və videoların hərflər üzrə sayı: \n' + strDict)

def echo(update, context):
    """Echo the user message."""
    update.message.reply_text(update.message.text) 

def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)



def getId(update, context):
	user_id = update.message.from_user.id
	user_name = update.message.from_user.name
	
	global userList
	global idList

	if {'username':user_name, 'id':user_id} not in userList:
		userList.append({'username':user_name, 'id':user_id})
		with open("userName_userId.txt", "a") as userNameIdFile:
			for item in userList:
				userNameIdFile.write("%s\n" % str(item))
		    #userNameIdFile.write(str(userList))
		    
	if user_id not in idList:
		idList.append(user_id)
		with open("userId.txt", "a") as userIdFile:
			for i in idList:
				userIdFile.write("%s\n" % str(i))

	print(userList)
	print(user_name)
	print(user_id)


def response(update, context):
    global letter
    text = str(update.message.text).upper()
    if text == 'A':
        update.message.reply_text('A hərfini seçdiniz. Bütün barmaqlar bükülü vəziyyətdə olur. Xahiş edirik aşağıdakı şəkilə uyğun foto çəkib göndərəsiniz.')
        update.message.reply_photo(open('sample_images/A1.jpg', 'rb'))
        letter = text
    elif text == 'B':
        update.message.reply_text('B hərfini seçdiniz. Son iki barmaq və baş barmaq bükülür, orta barmaq yarımbükülü və işarət barmağı açıq vəziyyətdə olur. Xahiş edirik aşağıdakı şəkillərə uyğun həm ön, həm də yandan foto çəkib göndərəsiniz.')
        update.message.reply_photo(open('sample_images/B1.jpg', 'rb'))
        update.message.reply_photo(open('sample_images/B2.png', 'rb'))
        letter = text
    elif text == 'C':
        update.message.reply_text('C hərfini seçdiniz. İşarət və orta barmaq baş barmaqla birləşir. Xahiş edirik aşağıdakı şəkillərə uyğun həm ön, həm də yandan foto çəkib göndərəsiniz.')
        update.message.reply_photo(open('sample_images/C1.png', 'rb'))
        update.message.reply_photo(open('sample_images/C2.png', 'rb'))
        letter = text
    elif text == 'Ç':
        update.message.reply_text('Ç hərfini seçdiniz. İşarət və orta barmaq baş barmaqla birləşir (C hərfi) və əl aşağıya doğru hərəkət etdirilir. Xahiş edirik aşağıdakı video nümunəyə uyğun video çəkib göndərəsiniz.')
        update.message.reply_video(open('sample_images/Ç1.mp4', 'rb'))
        letter = text
    elif text == 'D':
        update.message.reply_text('D hərfini seçdiniz. İşarət barmağı və orta barmaq birləşdirilir və sanki çevrə cızırmış kimi firladılır (yalnız qeyd edilən barmaqlar firladılır. Bütöv əl biləkdən vəya dirsəkdən fırladılarsa yanlış olar) Xahiş edirik aşağıdakı video nümunəyə uyğun video çəkib göndərəsiniz.')
        update.message.reply_video(open('sample_images/D1.mp4', 'rb'))
        letter = text
    elif text == 'E':
        update.message.reply_text('E hərfini seçdiniz. Digər dört barmaq baş barmaqla dairə formasında birləşdirilir. Xahiş edirik aşağıdakı şəkil nümunəyə uyğun foto çəkib göndərəsiniz.')
        update.message.reply_photo(open('sample_images/E1.png', 'rb'))
        letter = text
    elif text == 'Ə':
        update.message.reply_text('Ə hərfini seçdiniz. Xahiş edirik aşağıdakı şəkil nümunəyə uyğun foto çəkib göndərəsiniz.')
        update.message.reply_photo(open('sample_images/Ə1.png', 'rb'))
        letter = text
    elif text == 'F':
        update.message.reply_text('F hərfini seçdiniz. Xahiş edirik aşağıdakı şəkil nümunəyə uyğun foto çəkib göndərəsiniz.')
        update.message.reply_photo(open('sample_images/F1.png', 'rb'))
        letter = text
    elif text == 'G':
        update.message.reply_text('G hərfini seçdiniz. İşarət barmağı, orta barmaq və üzük barmağı birləşdirilir və önə atılır. Xahiş edirik aşağıdakı video nümunəyə uyğun video çəkib göndərəsiniz.')
        update.message.reply_video(open('sample_images/G1.mp4', 'rb'))
        letter = text
    elif text == 'Ğ':
        update.message.reply_text('Ğ hərfini seçdiniz. Xahiş edirik aşağıdakı şəkil nümunəyə uyğun foto çəkib göndərəsiniz.')
        update.message.reply_photo(open('sample_images/Ğ1.png', 'rb'))
        letter = text
    elif text == 'H':
        update.message.reply_text('H hərfini seçdiniz. Xahiş edirik aşağıdakı şəkil nümunəyə uyğun foto çəkib göndərəsiniz.')
        update.message.reply_photo(open('sample_images/H1.png', 'rb'))
        letter = text
    elif text == 'I':
        update.message.reply_text('I hərfini seçdiniz. İşarət barmağı və sonuncu bamaq açılır, digər barmaqlar bükülür. Xahiş edirik aşağıdakı şəkil nümunəyə uyğun foto çəkib göndərəsiniz.')
        update.message.reply_photo(open('sample_images/I1.png', 'rb'))
        update.message.reply_photo(open('sample_images/I2.png', 'rb'))
        letter = text
    elif text == 'İ':
        update.message.reply_text('İ hərfini seçdiniz. Son iki barmaq, üzük və sonuncu bamaq düz dayanır, digər barmaqlar bükülür. Xahiş edirik aşağıdakı şəkil nümunəyə uyğun foto çəkib göndərəsiniz.')
        update.message.reply_photo(open('sample_images/İ1.png', 'rb'))
        update.message.reply_photo(open('sample_images/İ2.png', 'rb'))
        letter = text
    elif text == 'J':
        update.message.reply_text('J hərfini seçdiniz. F hərfindən fərqli olaraq dört barmaq baş barmağın üzərinə yığılır. Xahiş edirik aşağıdakı şəkil nümunələrə uyğun foto çəkib göndərəsiniz.')
        update.message.reply_photo(open('sample_images/J1.png', 'rb'))
        update.message.reply_photo(open('sample_images/J2.png', 'rb'))
        letter = text
    elif text == 'K':
        update.message.reply_text('K hərfini seçdiniz. İşarət barmağı və orta barmaq birləşdirilir və önə atılır. Xahiş edirik aşağıdakı video nümunəyə uyğun video çəkib göndərəsiniz.')
        update.message.reply_video(open('sample_images/K1.mp4', 'rb'))
        letter = text
    elif text == 'L':
        update.message.reply_text('L hərfini seçdiniz. Xahiş edirik aşağıdakı şəkil nümunələrə uyğun foto çəkib göndərəsiniz.')
        update.message.reply_photo(open('sample_images/L1.png', 'rb'))
        update.message.reply_photo(open('sample_images/L2.png', 'rb'))
        letter = text
    elif text == 'M':
        update.message.reply_text('M hərfini seçdiniz. Xahiş edirik aşağıdakı şəkil nümunələrə uyğun foto çəkib göndərəsiniz.')
        update.message.reply_photo(open('sample_images/M1.png', 'rb'))
        update.message.reply_photo(open('sample_images/M2.png', 'rb'))
        letter = text
    elif text == 'N':
        update.message.reply_text('N hərfini seçdiniz. Üzük barmağı baş barmaqla birgə bükülür, digər barmaqlar açıq şəkildə olur. Xahiş edirik aşağıdakı şəkil nümunəyə uyğun foto çəkib göndərəsiniz.')
        update.message.reply_photo(open('sample_images/N1.png', 'rb'))
        update.message.reply_photo(open('sample_images/N2.png', 'rb'))
        letter = text
    elif text == 'O':
        update.message.reply_text('O hərfini seçdiniz. F hərfindən fərqli olaraq dört barmaq baş barmağın üzərinə yığılır. Xahiş edirik aşağıdakı şəkil nümunəyə uyğun foto çəkib göndərəsiniz.')
        update.message.reply_photo(open('sample_images/O1.png', 'rb'))
        letter = text
    elif text == 'Ö':
        update.message.reply_text('Ö hərfini seçdiniz. O hərfi kimi tutulur və əl aşağıya doğru hərəkət etdirilir. Xahiş edirik aşağıdakı video nümunəyə uyğun video çəkib göndərəsiniz.')
        update.message.reply_video(open('sample_images/Ö1.mp4', 'rb'))
        letter = text
    elif text == 'P':
        update.message.reply_text('P hərfini seçdiniz. H hərfinə oxşayır, lakin H hərfindən fərqli olaraq burada baş barmaq açılmır. Xahiş edirik aşağıdakı şəkil nümunəyə uyğun foto çəkib göndərəsiniz.')
        update.message.reply_photo(open('sample_images/P1.png', 'rb'))
        update.message.reply_photo(open('sample_images/P2.png', 'rb'))
        letter = text
    elif text == 'Q':
        update.message.reply_text('Q hərfini seçdiniz. baş barmaq və işarət barmağı kiril Г hərfi formasında açılır. Xahiş edirik aşağıdakı şəkil nümunəyə uyğun foto çəkib göndərəsiniz.')
        update.message.reply_photo(open('sample_images/Q1.png', 'rb'))
        letter = text
    elif text == 'R':
        update.message.reply_text('R hərfini seçdiniz. N hərfinə bənzəyir (N hərfində üzük barmağı bükülür), lakin burada orta barmaq bükülür. Xahiş edirik aşağıdakı şəkil nümunəyə uyğun foto çəkib göndərəsiniz.')
        update.message.reply_photo(open('sample_images/R1.png', 'rb'))
        letter = text
    elif text == 'S':
        update.message.reply_text('S hərfini seçdiniz. Kiril С hərfi formasında göstərilir. Xahiş edirik aşağıdakı şəkil nümunəyə uyğun foto çəkib göndərəsiniz.')
        update.message.reply_photo(open('sample_images/S1.png', 'rb'))
        letter = text
    elif text == 'Ş':
        update.message.reply_text('Ş hərfini seçdiniz. Uyğun barmaqlar birləşdirilməklə Kiril Ш hərfi formasında göstərilir. Xahiş edirik aşağıdakı şəkil nümunəyə uyğun foto çəkib göndərəsiniz.')
        update.message.reply_photo(open('sample_images/Ş1.png', 'rb'))
        letter = text
    elif text == 'T':
        update.message.reply_text('T hərfini seçdiniz. Uyğun barmaqlar birləşdirilməklə Ş hərfinə oxşar, lakin Ş hərfinin tərsi olaraq başaşağı formasında göstərilir. Xahiş edirik aşağıdakı şəkil nümunəyə uyğun foto çəkib göndərəsiniz.')
        update.message.reply_photo(open('sample_images/T1.png', 'rb'))
        update.message.reply_photo(open('sample_images/T2.png', 'rb'))
        letter = text
    elif text == 'U':
        update.message.reply_text('U hərfini seçdiniz. Baş barmaq və sonuncu barmaq açılır, qalan digər barmaqlar isə bükülür. Xahiş edirik aşağıdakı şəkil nümunəyə uyğun foto çəkib göndərəsiniz.')
        update.message.reply_photo(open('sample_images/U1.png', 'rb'))
        letter = text
    elif text == 'Ü':
        update.message.reply_text('Ü hərfini seçdiniz. U hərfi kimi tutulur və əl aşağıya doğru hərəkət etdirilir. Xahiş edirik aşağıdakı video nümunəyə uyğun video çəkib göndərəsiniz.')
        update.message.reply_video(open('sample_images/Ü1.mp4', 'rb'))
        letter = text
    elif text == 'V':
        update.message.reply_text('V hərfini seçdiniz. Xahiş edirik aşağıdakı şəkil nümunələrə uyğun həm ön, həm də yana doğru olan foto çəkib göndərəsiniz.')
        update.message.reply_photo(open('sample_images/V1.png', 'rb'))
        update.message.reply_photo(open('sample_images/V2.png', 'rb'))
        letter = text
    elif text == 'X':
        update.message.reply_text('X hərfini seçdiniz. Xahiş edirik aşağıdakı şəkil nümunəyə uyğun foto çəkib göndərəsiniz.')
        update.message.reply_photo(open('sample_images/X1.png', 'rb'))
        update.message.reply_photo(open('sample_images/X2.png', 'rb'))
        letter = text
    elif text == 'Y':
        update.message.reply_text('Y hərfini seçdiniz. Üzük barmağı və sonuncu barmaq açıq və  digər barmaqlar bükülü olmaqla əl aşağıdan yuxarıya doğru fırladılır. Xahiş edirik aşağıdakı video nümunəyə uyğun video çəkib göndərəsiniz.')
        update.message.reply_video(open('sample_images/Y1.mp4', 'rb'))
        letter = text
    elif text == 'Z':
        update.message.reply_text('Z hərfini seçdiniz. İşarət barmağı ilə sanki Z hərfi yazılır. Xahiş edirik aşağıdakı video nümunəyə uyğun video çəkib göndərəsiniz.')
        update.message.reply_video(open('sample_images/Z1.mp4', 'rb'))
        letter = text
    else:
        update.message.reply_text('Yanlış seçim etdiniz. Xahiş edirik A, B, C, Ç, D, E, Ə, F, G, Ğ, H, I, İ, J, K, L, M, N, O, Ö, P, Q, R, S, Ş, T, U, Ü V, X, Y, Z hərflərdən birini qeyd edin.')
    getId(update, context)

def receive_file(update, context, fileType):
    global letter
    date = datetime.datetime.now()
    user_id = update.message.from_user.id
    fileName = 'ID--' + str(user_id) + '--__' + str(uuid.uuid4())
    # user_name = update.message.from_user.name

    if fileType == 0: # 0 image, 1 video
        fileName += '.jpg'
        rootFolder = './downloaded_images/'
        file_id = update.message.photo[-1]
        logFile = 'receive_image_logs.txt'
    else:
        fileName += '.mp4'
        rootFolder = './downloaded_videos/'
        file_id = update.message.video.file_id
        logFile = 'receive_video_logs.txt'

    folderName = rootFolder + date.strftime("%d.%m.%Y") + '/' + letter
    if not os.path.exists(folderName):
        os.makedirs(folderName)
        
    file = context.bot.getFile(file_id)
    file.download(folderName + '/' + fileName)

    print("\n" + date.strftime("%d.%m.%Y, %H:%M:%S") + ": User with Id %d saved the file" % (user_id), file=open(logFile, 'a'))
    update.message.reply_text("Fayl serverimizə yükləndi. Təşəkkür edirik.")
    update.message.reply_text("Əlavə məlumat üçün '/help' qeyd edin.")
    update.message.reply_text("Davam etmək üçün xahiş edirik "+ getMinLetters() +" hərflərdən birini qeyd edin.")


def receive_image(update, context):
    receive_file(update, context, 0)

def receive_video(update, context):
    receive_file(update, context, 1)
	
def genCountByLetter():
    folders = ['./downloaded_images', './downloaded_videos']
    letterDict = {letter : 0 for letter in letters}

    for folder in folders:
        for day in os.listdir(folder):
            dayPath = os.path.join(folder, day)
            if os.path.isdir(dayPath):
                for letter in letters:
                    letterPath = os.path.join(dayPath, letter)
                    if os.path.isdir(letterPath):
                        letterCount = len([f for f in os.listdir(letterPath) if os.path.isfile(os.path.join(letterPath, f))])
                        letterDict[letter] += letterCount

    return letterDict

def readCountCache():
    global lastCacheTime

    if not lastCacheTime or (datetime.datetime.now() - lastCacheTime).seconds/60/60 > cacheDuration:
       letterDict = genCountByLetter()
       sortedDict = dict(sorted(letterDict.items(), key=lambda x:x[1]))
       saveCountCache(sortedDict)
       lastCacheTime = datetime.datetime.now()
       return sortedDict

    return pd.read_csv('count_cache.csv', index_col=0, header=None, squeeze=True).to_dict()

def saveCountCache(sortedDict):
    df = DataFrame(sortedDict.items())
    df.to_csv('count_cache.csv', header=None, index = None, encoding="utf-8-sig")


def getMinLetters():
    letterDict = readCountCache()
    minCountLetters = ''
    i = 0
    for key in letterDict:
        if i == 10:
            break
        minCountLetters += key
        if i < 9:
            minCountLetters += ', '
        i+=1
    return minCountLetters

def main():
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater("1965719456:AAHY7PfVGemghSldKj87GLP4yqPCvtH5_Hs", use_context=True) #asl_test_bot

    # Get the dispatcher to register handlers
    dp = updater.dispatcher
    
    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("showData", showData))

    # on message - above defined response messages on Telegram
    dp.add_handler(MessageHandler(Filters.text, response))
    
    # on received image file by users - downloading the image
    dp.add_handler(MessageHandler(Filters.photo, receive_image))
    
    # on received video file by users - downloading the video
    dp.add_handler(MessageHandler(Filters.video, receive_video))

    # on received any message capturing and saving username and userid
#    dp.add_handler(MessageHandler(Filters.text, getId))


    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()



if __name__ == '__main__':
    main()
