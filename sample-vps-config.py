import os
import logging

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

class Config(object):

    TG_BOT_TOKEN = "5713314297:AAEV5vDP5rQPOMdX3QUHugoCYJ4_EDe1mhY"
    APP_ID = "20869850"
    API_HASH = "b9d94e303d86df2a2b32679e50ccfb43"
    TG_USER_SESSION = "AQBPUMVJICRDJOb-oGUlTACu6CF3XbLmZ85NjcwHapyW-1bo6sozw9fKpNJ25xeEAEVlRjqCqdQsuZzFp4wYIfDkL8caLL7WlI1hFDLcybQB1aqpDZCTZNz21aBW2ClT_yhydAs1l4Lq7xU4ctjlHty2ttJdj1BurhNDjUpnp7sOE_jxyrdJ8g5E72-EPD1EOnLzREbT87394PvH-G9QRfUbIs-uZtrA1ixRBADbl6dhF1185wJX7BxaHm8wOUqVIKxHfF3br5bUOqXcLCOyBidyuWUCDsk44_p6JIe8456ADWqJb2AwalK4aJeWnoF-nQpYrF9AbAHLCBjshYxRjsG5AAAAAVLxVIIA"
    DB_URI = "mongodb+srv://CM:CM@cluster0.jfn3p38.mongodb.net/?retryWrites=true&w=majority"

def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
