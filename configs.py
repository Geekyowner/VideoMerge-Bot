# (c) @AbirHasan2005

import os


class Config(object):
    API_ID = os.environ.get("API_ID", 21257327)
    API_HASH = os.environ.get("API_HASH", 1235c1fe45ebc4968d9e23bc93440549)
    BOT_TOKEN = os.environ.get("BOT_TOKEN"), 7405223456:AAGltTbvARClRS0CcKPzueSPs-RQ26uJO2M
    SESSION_NAME = os.environ.get("SESSION_NAME", "Video-Merge-Bot")
    UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", -1002115299028)
    LOG_CHANNEL = os.environ.get("LOG_CHANNEL", -1002115299028)
    DOWN_PATH = os.environ.get("DOWN_PATH", "./downloads")
    TIME_GAP = int(os.environ.get("TIME_GAP", 5))
    MAX_VIDEOS = int(os.environ.get("MAX_VIDEOS", 5))
    STREAMTAPE_API_USERNAME = os.environ.get("STREAMTAPE_API_USERNAME")
    STREAMTAPE_API_PASS = os.environ.get("STREAMTAPE_API_PASS")
    MONGODB_URI = os.environ.get("MONGODB_URI", mongodb+srv://ytviralverse:2VPjBQ95DDnmVFu8@streamify.dvncffo.mongodb.net/?retryWrites=true&w=majority&appName=streamify)
    BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", False))
    BOT_OWNER = int(os.environ.get("BOT_OWNER", 5192808332))

    START_TEXT = """
Hi Unkil, I am Video Merge Bot!
I can Merge Multiple Videos in One Video. Video Formats should be same.

Made by @AbirHasan2005
"""
    CAPTION = "Video Merged by @{}\n\nMade by @AbirHasan2005"
    PROGRESS = """
Percentage : {0}%
Done: {1}
Total: {2}
Speed: {3}/s
ETA: {4}
"""
