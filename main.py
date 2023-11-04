from ValidarCpf import validar_cpf 

while True:
    try:
        cpf=input("Digite um cpf:")
        if cpf.lower()=="sair":
            break
        cpf=int(cpf)
        print(f'{cpf:0>11}',end='')
        if validar_cpf(cpf)==True:
            print(' valido!')
        else:
            print(' invalido!')
    except:
        print(f'{cpf} não é um valor aceito')
        
