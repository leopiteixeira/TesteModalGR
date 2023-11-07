#imports
from datetime import date

#Funções criadas
def somatorioNotas(emprest, nVal):
    ntotal = 0
    while(emprest >= nVal):
        ntotal += 1
        emprest -= nVal

    return ntotal, emprest


def notasMenores(emprest):
    n20, emprest = somatorioNotas(emprest, 20)
    n10, emprest = somatorioNotas(emprest, 10)
    n5, emprest = somatorioNotas(emprest, 5)
    n2, emprest = somatorioNotas(emprest, 2)
    return [n20, n10, n5, n2]

def notasMaiores(emprest):
    n100, emprest = somatorioNotas(emprest, 100)
    n50, emprest = somatorioNotas(emprest, 50)
    n20, n10, n5, n2 = notasMenores(emprest)
    return [n100, n50, n20, n10, n5, n2]

def notasMedias(emprest):
    n100, n50, n20Mai, n10Mai, n5Mai, n2Mai = notasMaiores(emprest / 2)
    n20Men, n10Men, n5Men, n2Men = notasMenores(emprest / 2)
    return n100, n50, n20Mai + n20Men, n10Mai + n10Men, n5Men + n5Mai, n2Men + n2Mai

#Corpo do código
nome = input("Qual seu nome?")
dia = int(input("Qual foi o dia da sua admissão"))
mes = int(input("Em qual mês você foi admitido?"))
ano = int(input("De qual ano?"))
salario = float(input("Qual seu salário atual?"))
emprestimo = int(input("Qual o valor do empréstimo solicitado?"))

anosEmpresa = date.today().year - ano

if(anosEmpresa < 5):
    print("Agradecemos seu interesse, mas você não atende os requisitos mínimos do programa")
    exit()
elif(anosEmpresa == 5):
    if(date.today().month < mes):
        print("Agradecemos seu interesse, mas você não atende os requisitos mínimos do programa")
        exit()
    elif(date.today().month == mes):
        if(date.today().day < dia):
            print("Agradecemos seu interesse, mas você não atende os requisitos mínimos do programa")
            exit()

if(emprestimo > salario*2):
    print("Agradecemos seu interesse, mas você não atende os requisitos mínimos do programa")
    exit()

while(emprestimo % 2 == 1):
    print("valor de emprestimo invalido! coloque um valor multiplo de 2")
    emprestimo = int(input())


print("\nNotas menores:")
n20, n10, n5, n2 = notasMenores(emprestimo)
print(f"Notas de 20: {n20}\n"
      f"Notas de 10: {n10}\n"
      f"Notas de 5: {n5}\n"
      f"Notas de 2: {n2}\n")

print("\n--------------------------\n")

print("Notas maiores:")
n100, n50, n20, n10, n5, n2 = notasMaiores(emprestimo)
print(f"Notas de 100: {n100}\n"
      f"Notas de 50: {n50}\n"
      f"Notas de 20: {n20}\n"
      f"Notas de 10: {n10}\n"
      f"Notas de 5: {n5}\n"
      f"Notas de 2: {n2}\n")

print("\n--------------------------\n")

print("Notas meio a meio:")
n100, n50, n20, n10, n5, n2 = notasMedias(emprestimo)
print(f"Notas de 100: {n100}\n"
      f"Notas de 50: {n50}\n"
      f"Notas de 20: {n20}\n"
      f"Notas de 10: {n10}\n"
      f"Notas de 5: {n5}\n"
      f"Notas de 2: {n2}\n")
