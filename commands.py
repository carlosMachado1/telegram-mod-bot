from telegram import Update, ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import ContextTypes, CallbackContext

from .log import logger
from .utils import ConvEvents

commands = {
    "/start": "Comando usado para apresentação do bot.",
    "/help": "Comando usado para mostrar todos os comandos que podem ser utilizados.",
    "/convidarUsuario <usuario> <grupo>": "Comando usado para enviar um convite de grupo para o usuário desejado.",
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
    user_ids = ", ".join(
        str(uid) for uid in context.bot_data.setdefault("user_ids", set())
    )
    logger.info(user_ids)


async def add_link_conv(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    logger.info("Running add_link_conv function")

    await update.message.reply_text(
        "Comando utilizado para adicionar/editar o nome do grupo e link de compartilhamento\n\nSó é possivel ter 1 link de compartilhamento por enquanto."
    )

    await update.message.reply_text("Digite o nome do grupo (ou canal):")

    return ConvEvents.get_group_name


async def get_group_name(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    logger.info("Running get_group_name function")

    user_group_name = update.message.text

    logger.info(f"Grupo (ou Canal): {user_group_name}")

    await update.message.reply_text(
        text=f"Grupo: {user_group_name}\n\nEstá correto?",
        reply_markup=ReplyKeyboardMarkup(
            [["Sim", "Não"]],
            one_time_keyboard=True,
            input_field_placeholder="Está correto?",
        ),
    )

    return ConvEvents.validation


async def add_link_group(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    logger.info("Running add_link_group function")


async def validation(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    logger.info("Running validation function")

    ans = update.message.text
    if ans == "Sim":
        await update.message.reply_text("Qual o link para o grupo")
        return ConvEvents.bot_ask_link
    return ConvEvents.get_group_name


async def bot_ask_link(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    logger.info("Running bot_ask_link function")

    group_link = update.message.text

    logger.info(f"Link do Grupo: {group_link}")
