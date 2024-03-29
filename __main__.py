#!/usr/bin/env python

"""

Author  : Carlos Gabriel Machado
github   : carlosMachado1
date    : 06/01/2024

Usage:

"""

from .log import logger
from .config import BOT_TOKEN
from .__version__ import VERSION
from .commands import (
    start,
    helper,
    invite_user,
    add_link_conv,
    add_link_group,
    get_group_name,
    validation,
)
from .utils import ConvEvents

from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    filters,
    ConversationHandler,
)


logger.info(f"Scraper Adder Bot is on version {VERSION}")

bot = ApplicationBuilder().token(BOT_TOKEN).build()
bot.add_handler(CommandHandler("start", start))
bot.add_handler(CommandHandler("help", helper))
bot.add_handler(CommandHandler("convidarUsuario", invite_user))
bot.add_handler(
    ConversationHandler(
        entry_points=[CommandHandler("cadastrarLink", add_link_conv)],
        states={
            ConvEvents.get_group_name: [
                MessageHandler(filters.TEXT & ~filters.COMMAND, get_group_name),
            ],
            ConvEvents.validation: [
                MessageHandler(filters.TEXT, validation),
            ],
            ConvEvents.bot_ask_link: [
                MessageHandler(filters.TEXT, validation),
            ],
        },
        fallbacks=[],
    )
)


bot.run_polling(allowed_updates=Update.ALL_TYPES)
