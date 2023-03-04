#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) @Bae_wafaaa

import os
import logging

class Config:
  
#Your API HASH from my.telegram.org    
    API_ID = int(os.environ.get("API_ID", "29409646"))
#Your API HASH from my.telegram.org      
    API_HASH = os.environ.get("API_HASH", "a69d0340a520c1913c517bea143a3de7")
#BOT TOKEN: @Botfather on telegram    
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5682083705:AAHHEc78t-XJUKPMba4CIRc4C1by-GH9lxE")
#Public channel username without '@'. Don't forget to add bot in channel as administrator.    
    FORCESUB = os.environ.get("FORCESUB", "SK_MoviesOffl") 
#Owner user id   
    AUTH  = os.environ.get("OWNER_ID", "5143506371")
#Pyrogram string session using (https://replit.com/@KindKobra/Pyrogram-String-Gen?v=1)
    SESSION = os.environ.get("SESSION", "AQAYE4IFXO0SjiKDKlwhmYLaTIFCkNq1LHENlT8DExAIphz0ibtjpupxNTKqVNei10_Z4OsHpSJinRPaq4dGTDmEqzPyV1l78jBNKgu1Yv5wd-VddiczExq8TQqfgO3K4pn8zf8PSbItUAkmNSsYN9daJeQW3xW1H_Q9S22SIgvXu902r4WyeYo96GNMyz8A4MGO1prt0V6PwnANctf94_YQTp95Xz2JkQ6J4peJNic8pKZG5qbt1ln3QoRFVVkELyJDZBZXx2iWZmDul-gyVsTPDZufqmEKvZmWl4tYxnybZPRBIvsjBd22k4ifQfScHs19mgrBhiNHooXMVrJUk5QaAAAAAV6vDl0A")
  
def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
