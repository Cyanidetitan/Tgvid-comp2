#    Copyright (c) 2021 Danish_00
#    Improved By @Zylern

from decouple import config

try:
    APP_ID = "10247139"
    API_HASH = "96b46175824223a33737657ab943fd6a"
    BOT_TOKEN = "5970291834:AAEL13_b8CTAnJ93ALGK18EQfA6Jn967IsM"
    DEV = 1664850827
    OWNER = "5700625607"
    ffmpegcode = ["""-c:v copy -metadata:s:v:0 title="t.me/animxt" -c:a copy -c:s copy -map 0"""]
    THUMBNAIL = config("THUMBNAIL", default="https://telegra.ph/file/f9e5d783542906418412d.jpg")
except Exception as e:
    print("Environment vars Missing! Exiting App.")
    print(str(e))
    exit(1)
