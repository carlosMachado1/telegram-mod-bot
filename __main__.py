#!/usr/bin/env python

"""

Author  : Carlos Gabriel 
email   : carlos.machado1980@yahoo.com
date    : 06/01/2024

Usage:

"""

from .log import logger
from .config import BOT_TOKEN
from .__version__ import VERSION

from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler


logger.info(f"Scraper Adder Bot is on version {VERSION}")

bot = ApplicationBuilder().token(BOT_TOKEN).build()

bot.run_polling(allowed_updates=Update.ALL_TYPES)
