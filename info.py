import os
from os import environ

API_ID       = int(environ.get("API_ID", "12549463"))
API_HASH     = environ.get("API_HASH", "fddc277f921e644b9b439a61d7f92bee")
BOT_TOKEN    = environ.get("BOT_TOKEN", "7300724040:AAEXGd9h1YvxsekoQoDCHX2hF1MSro8Zi1U")
DATABASE_URI = environ.get("DATABASE_URI", "mongodb+srv://uhdprime:uhdprime@cluster0.ry5y4yk.mongodb.net/?retryWrites=true&w=majority")
LOG_CHANNEL  = int(environ.get("LOG_CHANNEL", "-1002100505904"))
ADMIN        = int(environ.get("ADMIN", "1925422909"))
CHANNEL      = environ.get("CHANNEL", "@ORGPrime")
