import os
from os import environ

API_ID       = int(environ.get("API_ID", "20778875"))
API_HASH     = environ.get("API_HASH", "c49ecc77f2abfaedb1bd6bca14559702")
BOT_TOKEN    = environ.get("BOT_TOKEN", "7154196481:AAHNIxoqSvIUOwc9Aq3U0M7DO7JKM15mn54")
DATABASE_URI = environ.get("DATABASE_URI", "mongodb+srv://clone:clone@clone.omngv.mongodb.net/?retryWrites=true&w=majority&appName=clone")
LOG_CHANNEL  = int(environ.get("LOG_CHANNEL", "-1002319541032"))
ADMIN        = int(environ.get("ADMIN", "6924461727"))
CHANNEL      = environ.get("CHANNEL", "@ORGPrime")
