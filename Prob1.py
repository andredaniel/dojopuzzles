"""
Um determinado ano é bissexto se:
O ano for divisível por 4, mas não divisível por 100, exceto se ele for também divisível por 400.

Escreva uma função que determina se um determinado ano informado é bissexto ou não.
"""

ano = int(input("Digite um ano: "))

divisivelPorCem = ano % 100 == 0
divisivelPorQuatro = ano % 4 == 0
divisivelPorQuatrocentos = ano % 400 == 0

if divisivelPorQuatro:
    if divisivelPorCem:
        if divisivelPorQuatrocentos:
            print(f'O ano {ano} é bissexto!')

        else:
            print(f'O ano {ano} não é bissexto!')

    else:
        print(f'O ano {ano} é bissexto!')

else:
    print(f'O ano {ano} não é bissexto!')
