def validacao(cpf):
    cpf_valido=True
    
    #laco para verificar o penultimo digito
    i=10
    resultado=0
    
    #verificação funciona somando uma operação de digito a digito
    #primeiro digito x 10, segundo x 9 e assim por diante até o nono digito
    
    for n in cpf[:-2]:
            resultado+=int(n)*i
            i-=1
    
    #resultado da soma é calculado o resto da divisão por 11,
    #e em seguida subtrai ele de 11
    
    resultado=resultado%11
    resultado=11-resultado
    
    #se o resultado for menor que 10, verifica se o penultimo digito é igual o
    #resultado 
    
    if resultado < 10:
        if resultado != int(cpf[-2]):
            cpf_valido=False    
    #para resultado maior que 9 verifica se o penultimo digito é igual a 0   
    else:
        if 0 != int(cpf[-2]):
            cpf_valido=False



    #bloco de verificacao do ultimo digito
    '''
    mesmo processo de verificação do penultimo,
    mas a multiplicação começa no 11 e vai até o decimo digito
    '''
    i=11
    resultado=0
    for n in cpf[:-1]:
        resultado+=int(n)*i
        i-=1
    resultado=resultado%11
    resultado=-resultado+11
    if resultado < 10:
        if resultado != int(cpf[-1]):
            cpf_valido=False
    else:
        if 0 != int(cpf[-1]):
            cpf_valido=False
    return cpf_valido



def validar_cpf(cpf): #só aceita cpf int ou str sem separadores ex:'12345678911'
    cpf_valido=True
    
    if type(cpf)==int:  
        cpf=f'{cpf:0>11}' #ajusta a quantidade de digitos para 11       
        cpf_valido=validacao(cpf)       
    elif type(cpf)==str and len(cpf)==11:
        cpf_valido=validacao(cpf)
    else:
        print(f'{cpf} é invalido!')
    return cpf_valido
    
