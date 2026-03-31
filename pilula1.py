def validarSenha(senha):
    if len(senha) < 8:
        return 'Senha inválida, muito curta'

    temNumero = False
    temMaiuscula = False

    for c in senha:
        if c == ' ':
            return 'Senha invalida, nao pode conter espaco'
        if c >= '0' and c <= '9':
            temNumero = True
        if c >= 'A' and c <= 'Z':
            temMaiuscula = True
    
    if not temNumero:
        return 'Não tem numero'
    if not temMaiuscula:
        return 'Não tem maiuscula'
    
    return 'Senha valida'

senha = input('Digite sua senha: ')
print(validarSenha(senha))
