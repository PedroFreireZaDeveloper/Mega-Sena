import random
print("Programa para fornecer números aleatórios para se jogar na Mega-Sena\nOs números são:\n")
R = "S"
while(R == "S"):
    A = 1
    B = 1
    C = 1
    D = 1
    E = 1
    F = 1
    while(A == B or A == C or A == D or A == E or A == F or B == C or B == D or B == E or B == F or C == D or C == E or C == F or D == E or D == F or E == F):
        A = random.randint(1,60)
        B = random.randint(1,60)
        C = random.randint(1,60)
        D = random.randint(1,60)
        E = random.randint(1,60)
        F = random.randint(1,60)
    Num = [A,B,C,D,E,F]
    print(sorted(Num))
    R = input("\nDigite S para novos números, ou digite N para sair.\n=====> ").upper()
    