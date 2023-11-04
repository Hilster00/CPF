from ValidarCPF.py import validar_cpf 

#percorrer todo o intervalo de cpf 000.000.000-00 a 999.999.999-99
print('Lista de cpf válidos')
quantidade=0
for cpf in range(100000000000):
    if validar_cpf(cpf) == True:
        cpf_p=f'{cpf:0>11}'
        print(f'{cpf_p[:3]}.{cpf_p[3:6]}.{cpf_p[6:9]}-{cpf_p[9:11]}')
        quantidade+=1
print(f'A quantidade de cpf validos são {quantidade}')
    
