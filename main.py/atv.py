import math
import random
from datetime import datetime
import requests
matematica = int(input("Digite o número referente à opção que deseja:\n1. Raiz Quadrada \n2. Potência do número\n3. Arredonde um número para cima\n4.Arredonde um número para baixo\n5. sortear um nome\n6. Para ver Localidade \n7. Para Calcular quantos dias faltam\n ------> "))

match matematica:
    case 1:
        n1= float(input("Digite um número para calcular a raiz quadrada: "))
        resultado = math.sqrt(n1)
        print(f"A raiz quadrada de {n1} é {resultado} ")
    case 2:
        n2 = float(input("Digite um número: "))
        n3= float(input("Digite outro número (potência): "))
        resul1= math.pow(n2, n3)
        print(f"O número {n2} elevado a {n3} é {resul1}")
    case 3: 
        n4 = float(input("Digite um número: "))
        n5 = float(input("Digite outro número: "))
        resul2 = math.ceil(n4/n5)
        print(f"O resultado arredondado para cima é: {resul2}")
    case 4:
        n6= float(input("Digite um número: "))
        n7= float(input("Digite outro número: "))
        resul3= math.floor(n6/n7)
        print(f"O resultado arredondado para baixo é de: {resul3}")
    case 5:
        sim = input("Deseja sortear um nome? (S/N): ").upper()
        if sim == "S":
            nome = ["Débora", "Polly", "João Fernando", "Ana Paula", "Mariana", "Maria", "Leonardo", "Evelyn", "Alice", "Matheus" ]
            resul4 = random.choice(nome)
            print(resul4)
        elif sim == "N":
            print("Fim da operação")
        else:
            print("Opção inválida! Digite S ou N")
    case 6:
        cep = input("Digite o seu cep: ")
        url = (f"https://viacep.com.br/ws/{cep}/json/")
        resposta = requests.get(url)
        dados = resposta.json()
        print(dados["logradouro"])
        print(dados["bairro"])
        print(dados["localidade"])
    case 7:
        agora = datetime.now()
        print("Data e hora atuais:", agora)
        data = input("Digite uma data (dd/mm/aaaa): ")
        data_futura = datetime.strptime(data, "%d/%m/%Y")
        dias = (data_futura - agora).days
        print("Faltam", dias, "dias.")
