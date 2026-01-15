"""
Docstring for CPF Validator
"""

import re 

def validar_cpf():

    while True:
        cpf_usuario = input('Digite o CPF a ser validado ou [s]air: ')

        if cpf_usuario.lower() == 's':
            print('Saindo do validador de CPF.')
            break
        
        cpf_usuario = re.sub(r'[^0-9]', '', cpf_usuario) 

        if len(cpf_usuario) != 11:
            print('Erro: CPF deve conter 11 dígitos numéricos.')
            continue  
        
        entrada_sequencial = cpf_usuario == cpf_usuario[0] * len(cpf_usuario)
        
        if entrada_sequencial:
            print('Erro: CPF não pode conter números sequenciais.')
            continue  
        
        nove_digitos = cpf_usuario[:9] # Primeiros nove dígitos do CPF
        contador_regressivo_1 = 10 # Contador regressivo para o primeiro dígito
        resultado_digito1 = 0

        for digito in nove_digitos:
            resultado_digito1 += int(digito) * contador_regressivo_1
            contador_regressivo_1 -= 1
        digito_1 = (resultado_digito1 * 10) % 11
        digito_1 = digito_1 if digito_1 <= 9 else 0
            
        dez_digitos = nove_digitos + str(digito_1)
        contador_regressivo_2 = 11
        resultado_digito2 = 0

        for digito in dez_digitos:
            resultado_digito2 += int(digito) * contador_regressivo_2
            contador_regressivo_2 -= 1
        digito_2 = (resultado_digito2 * 10) % 11
        digito_2 = digito_2 if digito_2 <= 9 else 0
        cpf_calculado = f'{nove_digitos}{digito_1}{digito_2}'

        if cpf_calculado == cpf_usuario:
            print('CPF válido!')
        else:
            print('CPF inválido!')

if __name__ == '__main__':
    validar_cpf()