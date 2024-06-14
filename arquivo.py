import pywhatkit as kit
import time

# Classe Professor
class Professor:
    def __init__(self, nome):
        self.nome = nome

    def enviar_notificacao(self, mensagem, sala, numeros):
        sala.receber_notificacao(mensagem, self)
        enviar_mensagens(numeros, mensagem)


# Classe Aluno
class Aluno:
    def __init__(self, nome):
        self.nome = nome

    def receber_notificacao(self, mensagem):
        print(f"Notificação para {self.nome}: {mensagem}")


# Classe Sala
class Sala:
    def __init__(self, nome, numero):
        self.nome = nome
        self.numero = numero

    def receber_notificacao(self, mensagem, professor):
        print(f"Notificação de {professor.nome} para {self.nome} ({self.numero}): {mensagem}")


# Função para obter o período do dia
def periodo_do_dia():
    periodo = input("Insira o período do dia (manhã ou tarde): ").lower()
    if periodo == "manhã" or periodo == "manha":
        return "manhã"
    elif periodo == "tarde":
        return "tarde"
    else:
        print("Período inválido. Por favor, insira 'manhã' ou 'tarde'.")
        return periodo_do_dia()


# Função para enviar mensagens via WhatsApp
def enviar_mensagens(contatos, mensagem):
    for numero in contatos:
        # Aguarda 5 segundos antes de abrir o WhatsApp Web
        time.sleep(5)
        # Envia a mensagem no WhatsApp
        kit.sendwhatmsg_instantly(numero, mensagem, wait_time=10, tab_close=True)
        print(f"Mensagem enviada para {numero}")
        # Aguarda alguns segundos para evitar bloqueio
        time.sleep(8)


# Função principal
def main():
    tipo_usuario = input("Você é um professor ou um aluno? ").lower()
    if tipo_usuario == "professor":
        nome = input("Insira seu nome: ")
        professor = Professor(nome)

        turmaA_manha = Sala("turmaA", input("Insira o número da sala para a turmaA : "))
        turmaB_manha = Sala("turmaB", input("Insira o número da sala para a turmaB : "))

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

        periodo = periodo_do_dia()

        if periodo == "manhã":
            turma = input("Insira a turma (turmaA ou turmaB): ")
            sala = turmaA_manha if turma.lower() == 'turmaa' else turmaB_manha
            mensagem = f"A aula na parte da manhã será na sala {sala.numero} para a  {turma}."
            numeros = turma_A if turma.lower() == 'turmaa' else turma_B
            professor.enviar_notificacao(mensagem, sala, numeros)
        else:
            turma = input("Insira a turma (turmaA ou turmaB): ")
            sala = Sala(turma.lower(), input(f"Insira o número da sala para a {turma} na parte da tarde: "))
            mensagem = f"A aula na parte da tarde será na sala {sala.numero} para a  {turma}."
            numeros = turma_A if turma.lower() == 'turmaa' else turma_B
            professor.enviar_notificacao(mensagem, sala, numeros)
    elif tipo_usuario == "aluno":
        nome = input("Insira seu nome: ")
        aluno = Aluno(nome)

        while True:
            mensagem = input("Digite sua mensagem ('sair' para encerrar): ")
            if mensagem.lower() == "sair":
                break
            else:
                aluno.receber_notificacao(mensagem)
    else:
        print("Tipo de usuário inválido. Por favor, insira 'professor' ou 'aluno'.")


if __name__ == "__main__":
    main()

