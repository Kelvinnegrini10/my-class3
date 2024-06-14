import pywhatkit as kit
import time
import customtkinter
from PIL import Image, ImageTk

# Configuração do CustomTkinter
customtkinter.set_appearance_mode("dark") 
customtkinter.set_default_color_theme("dark-blue")

# Criação da janela
janela = customtkinter.CTk() 
janela.geometry("500x400")
janela.title("My Class") 

# Carregamento da imagem
imagem = Image.open("imagem1.png")  # Substitua "logo.png" pelo nome da sua imagem
imagem = imagem.resize((100, 100))  # Redimensiona a imagem
imagem_tk = ImageTk.PhotoImage(imagem)

# Componentes da interface
logo = customtkinter.CTkLabel(janela, image=imagem_tk, text="") 
logo.pack(padx=10, pady=10)

prof = customtkinter.CTkEntry(janela, placeholder_text="Nome do professor(a)") 
prof.pack(padx=10, pady=10)

turma = customtkinter.CTkOptionMenu(janela, values=["Turma A", "Turma B"]) 
turma.pack(padx=10, pady=10)

periodo = customtkinter.CTkOptionMenu(janela, values=["Manhã", "Tarde"]) 
periodo.pack(padx=10, pady=10)

sala = customtkinter.CTkEntry(janela, placeholder_text="Insira a sala") 
sala.pack(padx=10, pady=10)

# Função para enviar mensagem
def enviar_mensagem():
    valor_prof = prof.get()
    valor_turma = turma.get()
    valor_periodo = periodo.get()
    valor_sala = sala.get()
    
    mensagem = f"Aula do professor(a): {valor_prof}\nTurma: {valor_turma}\nPeríodo: {valor_periodo}\nSala: {valor_sala}"
    
    # Números de telefone dos alunos das turmas
    turma_A = [
        "+5516992787899", "+5519992874556", "+5516993096589", "+5511956397841", "+5516974033367", "+5516994290154",
        "+5516994290188", "+5516997500763", "+5516988156727", "+5516988016776", "+5516996151754", "+5516933008761",
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
        time.sleep(8)

# Botão para enviar mensagem
botao = customtkinter.CTkButton(janela, text="Enviar notificação", command=enviar_mensagem) 
botao.pack(padx=10, pady=10)

janela.mainloop()
