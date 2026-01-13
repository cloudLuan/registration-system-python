print("Olá, seja bem-vindo!")


# CADASTRO SISTEMA

nome = input("Qual o nome para o cadastro?")
idade = int(input("Qual a sua idade:"))

email = input("informe o e-mail para cadastrar em nosso sistema:")
confirmaçao_email = input("Voce confirma esse email mesmo? (S/N): ").upper()

while confirmaçao_email != "S":
    print("Voce precisa confirmar o e-mail para continuar.")
    email = input("Informe o e-mail novamente: ")
    confirmaçao_email = input("Confirma esse e-mail? (S/N): ").upper


senha = input("Crie uma senha:")
confirmaçao_senha = input("voce confirma essa senha? (S/N): ").upper()

while confirmaçao_senha != "S":
    print("Voce precisa confirmar essa senha para continuar:")
    senha = input("Informe novamente a senha: ")
    confirmaçao_senha = input("Confirmar essa senha?: ").upper


print("Muito bem", nome, ",seu cadastro ja esta em nosso sistema!")
