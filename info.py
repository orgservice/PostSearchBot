import os
from os import environ

API_ID       = int(environ.get("API_ID", "12549463"))
API_HASH     = environ.get("API_HASH", "fddc277f921e644b9b439a61d7f92bee")
BOT_TOKEN    = environ.get("BOT_TOKEN", "6800494318:AAEsqTZxU8wj_AaTIn1UHIYwfgHmm2o789A")
DATABASE_URI = environ.get("DATABASE_URI", "mongodb+srv://uhdprime:uhdprime@cluster0.ry5y4yk.mongodb.net/?retryWrites=true&w=majority")
LOG_CHANNEL  = int(environ.get("LOG_CHANNEL", "-1002100505904"))
ADMIN        = int(environ.get("ADMIN", "6630344997"))
CHANNEL      = environ.get("CHANNEL", "@ORGPrime")
