commands = {
    "/start": "Comando usado para apresentação do bot.",
    "/help": "Comando usado para mostrar todos os comandos que podem ser utilizados.",
    "/convidarUsuario <usuario> <grupo>": "Comando usado para enviar um convite de grupo para o usuário desejado.",
    "/convidarUsuarios <grupo>": "Comando usado para enviar um convite de grupo para todos os usuários dentro do grupo.",
}

for command, desc in commands.items():
    print(f"{command} ==> {desc}")
