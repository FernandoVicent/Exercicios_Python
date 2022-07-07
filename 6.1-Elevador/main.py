import time
def Descer():
    carga_max = 0
    q_peso = "Qual seu peso: "
    while carga_max != 500:
        pessoa = int(input(q_peso))
        carga_max += pessoa
        if(carga_max > 500):
            print("carga excedida\nElevador descendo")
            break
        if carga_max == 500:
             print("elevador descendo")

Descer()
time.sleep(4)
print('Elevador subiu: ')
Descer()