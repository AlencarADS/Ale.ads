# Título: hashzap
# Criar um botão iniciar
    #popup/modal/alerta
        #Titulo: Bem vindo ao hashzap
        #botão: entrar no chat
            #sumir com o titulo e o botão iniciar
            #fechar o popup
            #criar o chat (com a msg "nome de usuario entrou no chat")
            #embaixo do chat:
             # compo do texto: digite sua msg
             # botão enviar   
                #vai aparecer a msg no chat com nome do usario
                #lira: "coe galera"

#flet -> aplicativos/site/programa de computador
#pip  install flet - cmd

# importar o flet
import flet as ft

# criar a função principal do seu sistema
def main(pagina):
        #tudo que ela vai fazer

        #criar o titulo

        titulo = ft.Text("hashzap")

        def enviar_mensagem_tunel(mensagem):
              print(mensagem)
        pagina.pubsub.subscribe(enviar_mensagem_tunel)

        titulo_janela = ft.Text("Bem vindo ao Hashzap")
        campo_nome_usuario = ft.TextField(label="Escreva seu nome no chat")

        texto_mensagem = ft.TextField(label="Digite sua mensagem")

        def enviar_mensagem(evento):
            texto = f"{campo_nome_usuario.value}: {texto_mensagem.value}"

            chat.controls.append(ft.Text(texto))

            texto_mensagem.value = ""
            pagina.pubsub.send_all(texto)
            pagina.update()
        botao_enviar = ft.ElevatedButton("Enviar", on_click=enviar_mensagem)
    
        chat = ft.Column()


        # colunas e linhas
        linha_mensagem = ft.Row([texto_mensagem, botao_enviar])
        def entrar_chat(evento):
              
              #tiar titulo da pagina
              pagina.remove(titulo)
              #tiar o botao iniciar
              pagina.remove(botão_iniciar)
              #fechar janela
              janela.open = False

              pagina.add(chat)

              pagina.add(linha_mensagem)
              #escrever msg usuario entrou no chat
              texto_entrou_chat = f"{campo_nome_usuario.value} entrou no chat"
              chat.controls.append(ft.Text(texto_entrou_chat))
              #criar o botão de enviar

              pagina.update()
        
        botao_entrar = ft.ElevatedButton("entrar no chat", on_click=entrar_chat)

        janela = ft.AlertDialog(title=titulo_janela, content=campo_nome_usuario,actions=[botao_entrar])

        
        def abrir_popup(evento):
                
            pagina.dialog = janela
            janela.open = True
            print("Clicou no botão")
            

            pagina.update()

        botão_iniciar = ft.ElevatedButton("iniciar chat", on_click=abrir_popup)


        #colocar essa coisa na pagina
        #adicionar o titulo na pagina

        pagina.add(titulo)
        pagina.add(botão_iniciar)

# executar o seu sistema

ft.app(main, view=ft.WEB_BROWSER) 





