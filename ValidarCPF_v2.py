def validacao(cpf):
    
    resultado=0
    
    #verificação funciona somando uma operação de digito a digito
    #primeiro digito x 10, segundo x 9 e assim por diante até o nono digito
    
    for i,n in enumerate(cpf[:-2]):
        resultado+=int(n)*(10-i)
    
    #resultado da soma é calculado o resto da divisão por 11,
    #e em seguida subtrai ele de 11
 
    resultado=11-(resultado%11)
    
    #se o resultado for menor que 10, verifica se o penultimo digito é igual o
    #resultado 
    
    if (resultado < 10 and resultado != int(cpf[-2])) or (0 != int(cpf[-2])):
        return False    
            

    #bloco de verificacao do ultimo digito
    '''
    mesmo processo de verificação do penultimo,
    mas a multiplicação começa no 11 e vai até o decimo digito
    '''

    resultado=0
    for i,n in enumerate(cpf[:-1]):
        resultado+=int(n)*(11-i)
    resultado=-(resultado%11)+11
    
    if (resultado < 10 and resultado != int(cpf[-1])) or 0 != int(cpf[-1]):
        return False
 
    return True



def validar_cpf(cpf): #só aceita cpf int ou str sem separadores ex:'12345678911'
    
    if type(cpf)==int:
        return validacao(f'{cpf:0>11}') #ajusta a quantidade de digitos para 11      
        
    elif type(cpf)==str and len(cpf)==11:
        return validacao(cpf)
        
    else:
        print(f'{cpf} é invalido!')
        return False
      
