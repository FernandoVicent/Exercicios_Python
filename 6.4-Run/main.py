import time
minuto = 0
metros = 0
tartaruga = 500 #1
lebre = 0 #10

while lebre <= tartaruga:
    #time.sleep(1)
    tartaruga += 1
    lebre += 10
    minuto += 1
    print(f"A tartaruga esta a {tartaruga} metros")
    print(f"A Lebre esta a {lebre} metros")
    if lebre > tartaruga:
        print(f"A lebre passou a tartaruga em {minuto} minutos")


