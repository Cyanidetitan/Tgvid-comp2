#    Copyright (c) 2021 Danish_00
#    Improved By @Zylern

from decouple import config

try:
    APP_ID = "10247139"
    API_HASH = "96b46175824223a33737657ab943fd6a"
    BOT_TOKEN = "5210009358:AAESvuzGgAhRITt0BZxgrMjnRqlq2yDf18Q"
    DEV = 1664850827
    OWNER = "1443454117"
    ffmpegcode = ["""-preset medium -c:v copy -metadata:s:v:0 title="t.me/animxt" -c:a copy -c:s copy -map 0"""]
    THUMBNAIL = config("THUMBNAIL", default="https://telegra.ph/file/f9e5d783542906418412d.jpg")
except Exception as e:
    print("Environment vars Missing! Exiting App.")
    print(str(e))
    exit(1)
