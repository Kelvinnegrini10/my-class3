import pywhatkit as kit
import time
import customtkinter
from PIL import Image, ImageTk

# Configuração do CustomTkinter
customtkinter.set_appearance_mode("dark") 
customtkinter.set_default_color_theme("dark-blue")

# Criação da janela
janela = customtkinter.CTk() 
janela.state("zoomed")  # Deixa a janela em tela cheia
janela.title("My Class") 

# Carregamento da imagem
imagem = Image.open("imagem1.png")  # Substitua "logo.png" pelo nome da sua imagem
imagem = imagem.resize((200, 200))  # Redimensiona a imagem para um tamanho maior
imagem_tk = ImageTk.PhotoImage(imagem)

# Componentes da interface
logo = customtkinter.CTkLabel(janela, image=imagem_tk, text="", font=("Arial", 24))  # Aumenta o tamanho da fonte
logo.pack(padx=20, pady=20)

prof = customtkinter.CTkEntry(janela, placeholder_text="Nome do professor(a)", width=400, height=40, font=("Arial", 24))  # Aumenta o tamanho da entrada de texto
prof.pack(padx=20, pady=20)

turma = customtkinter.CTkOptionMenu(janela, values=["Turma A", "Turma B"], width=400, height=40, font=("Arial", 24))  # Aumenta o tamanho do menu de opções
turma.pack(padx=20, pady=20)

periodo = customtkinter.CTkOptionMenu(janela, values=["Manhã", "Tarde"], width=400, height=40, font=("Arial", 24))  # Aumenta o tamanho do menu de opções
periodo.pack(padx=20, pady=20)

sala = customtkinter.CTkEntry(janela, placeholder_text="Insira a sala", width=400, height=40, font=("Arial", 24))  # Aumenta o tamanho da entrada de texto
sala.pack(padx=20, pady=20)

# Função para enviar mensagem
def enviar_mensagem():
    valor_prof = prof.get()
    valor_turma = turma.get()
    valor_periodo = periodo.get()
    valor_sala = sala.get()
    
    mensagem = f"Aula do professor(a): {valor_prof}\nTurma: {valor_turma}\nPeríodo: {valor_periodo}\nSala: {valor_sala}"
    
    # Números de telefone dos alunos das turmas
    turma_A = [
        "+5516994290188", "+5516992787899", "+5519992874556", "+5516993096589", "+5511956397841", "+5516974033367", "+5516994290154",
        "+5516997500763", "+5516988156727", "+5516988016776", "+5516996151754", "+5516933008761",
        "+5519981436632", "+5516996077586", "+5516992655132", "+5516996207149"
    ]

    turma_B = [
        "+5516997733571", "+5516994073634", "+5519983531961", "+5516991002280", "+5516996046548", "+5516991862497",
        "+5516997504977", "+5516993043528", "+5516993527040", "+5516997032486", "+5516996378308", "+5516992890222",
        "+5516988184175", "+5516997614041"
    ]

    # Definindo os números de telefone de acordo com a turma selecionada
    numeros = turma_A if valor_turma == "Turma A" else turma_B
    
    # Envio da mensagem para cada número
    for numero in numeros:
        kit.sendwhatmsg_instantly(numero, mensagem, wait_time=10, tab_close=True)
        print(f"Mensagem enviada para {numero}")
        # Aguarda alguns segundos para evitar bloqueio
        time.sleep(3)

# Botão para enviar mensagem
botao = customtkinter.CTkButton(janela, text="Enviar notificação", command=enviar_mensagem, width=400, height=40, font=("Arial", 24))  # Aumenta o tamanho do botão
botao.pack(padx=20, pady=20)

janela.mainloop()
