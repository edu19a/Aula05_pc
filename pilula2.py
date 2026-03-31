def simularCrescimento(populacao, taxa, limite):
    anos = 0
    while populacao <= limite:
        populacao = populacao * (1 + taxa)
    anos += 1
    return anos

#main
p = float(input('populacao inicial: '))
t = float(input('taxa (%): '))/100
l = float(input('limite: '))

print(f'{simularCrescimento(p,t,l)} anos')