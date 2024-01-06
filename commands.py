from telegram import Update
from telegram.ext import ContextTypes

from .log import logger

commands = {
    "/start": "Comando usado para apresentação do bot.",
    "/help": "Comando usado para mostrar todos os comandos que podem ser utilizados.",
    "/convidarUsuario <usuario> <grupo>": "Comando usado para enviar um convite de grupo para o usuário desejado.",
    "/convidarUsuarios <grupo>": "Comando usado para enviar um convite de grupo para todos os usuários dentro do grupo.",
}


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    logger.info("Running start function")

    await update.message.reply_text(
        "Olá, eu sou o bot Spider para poder utilizar meus serviços me adicione no seu grupo."
    )

    await update.message.reply_text(
        "Esses são os comandos que você pode fazer uso até então."
    )

    for command, desc in commands.items():
        await update.message.reply_text(f"{command} ==> {desc}")


async def helper(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    logger.info("Running helper function")
    for command, desc in commands.items():
        if command != "/help":
            await update.message.reply_text(f"{command} ==> {desc}")


async def invite_user(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    logger.info("Running invite_user function")


async def invite_users(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    logger.info("Running invite_user function")
