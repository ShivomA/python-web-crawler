from datetime import timedelta

Config = {
    "Start_Link": "https://flinkhub.com/",

    "User_Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",

    "Crawling_Time": timedelta(days=1, hours=0, minutes=0),

    "Links_Limit": 5000,

    "Parallel_Threads": 5,

    "Wait_Time": 5
}
