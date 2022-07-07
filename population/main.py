ano = 2017
springfield = 100000
shelbyville = 30000
c_spring = 1.01
c_shelby = 1.03

while springfield >= shelbyville:
    springfield *= c_spring
    shelbyville *= c_shelby
    ano += 1
print(f"em {ano} a população de springfield sera de {round(springfield)} e a de shelbyville sera de: {round(shelbyville)}")
