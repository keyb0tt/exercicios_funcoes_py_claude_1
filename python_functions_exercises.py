"""
=============================================================================
30 EXERCÍCIOS DE FUNÇÕES EM PYTHON - ESTUDANTE DE ENGENHARIA DE SOFTWARE
=============================================================================

INSTRUÇÕES:
- Resolva cada exercício criando a função solicitada
- Teste suas funções com diferentes valores
- Compare suas soluções com as respostas no final do arquivo
- Não olhe as respostas antes de tentar!

=============================================================================
BLOCO 1: EXERCÍCIOS FÁCEIS (10 exercícios)
=============================================================================
"""

# EXERCÍCIO 1: Saudação Personalizada
# Crie uma função que receba um nome e retorne "Olá, [nome]!"
# Exemplo: saudacao("Maria") → "Olá, Maria!"

def saudacao(nome):
    saudacao = f'Olá, {nome}!'

    return saudacao

# EXERCÍCIO 2: Calculadora de Área do Retângulo
# Crie uma função que receba base e altura e retorne a área
# Exemplo: area_retangulo(5, 3) → 15

def area_retangulo(base, altura):
    area = base * altura

    return area    

# EXERCÍCIO 3: Par ou Ímpar
# Crie uma função que retorne True se o número for par, False se for ímpar
# Exemplo: eh_par(4) → True, eh_par(7) → False

def eh_par(numero):
    if numero % 2 == 0:
        return True
    else:
        return False


# EXERCÍCIO 4: Maior de Três Números
# Crie uma função que receba três números e retorne o maior deles
# Exemplo: maior_de_tres(10, 25, 15) → 25

def maior_de_tres(a, b, c):
    numeros = [a, b, c]
    
    return max(numeros)


# EXERCÍCIO 5: Conversor de Temperatura
# Crie uma função que converta Celsius para Fahrenheit
# Fórmula: F = (C * 9/5) + 32
# Exemplo: celsius_para_fahrenheit(0) → 32.0

def celsius_para_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    
    return fahrenheit

# EXERCÍCIO 6: Contador de Vogais
# Crie uma função que conte quantas vogais existem em uma string
# Exemplo: contar_vogais("python") → 1

def contar_vogais(texto):
    contador = 0
    vogais = 'aeiouAEIOU'
    
    for letra in texto:
        if letra in vogais:
            contador += 1

    return contador

# EXERCÍCIO 7: Inverter String
# Crie uma função que inverta uma string
# Exemplo: inverter("python") → "nohtyp"

def inverter(texto):
    texto_invertido = texto[::-1]

    return texto_invertido

# EXERCÍCIO 8: Calcular Média
# Crie uma função que receba uma lista de números e retorne a média
# Exemplo: calcular_media([10, 20, 30]) → 20.0

def calcular_media(numeros):
    soma_numeros = 0

    for numero in numeros:
        soma_numeros += numero
    
    media_numeros = soma_numeros / len(numeros)

    return media_numeros

# EXERCÍCIO 9: Verificar Maioridade
# Crie uma função que retorne True se idade >= 18, False caso contrário
# Exemplo: eh_maior_de_idade(20) → True

def eh_maior_de_idade(idade):
    if idade >= 18:
        return True
    else:
        return False

# EXERCÍCIO 10: Repetir String
# Crie uma função que repita uma string n vezes
# Exemplo: repetir("Ha", 3) → "HaHaHa"

def repetir(texto, n):
    pass


"""
=============================================================================
BLOCO 2: EXERCÍCIOS MÉDIOS (10 exercícios)
=============================================================================
"""

# EXERCÍCIO 11: Validador de CPF (formato básico)
# Crie uma função que valide se um CPF tem 11 dígitos (apenas numérico)
# Exemplo: validar_cpf("12345678901") → True

def validar_cpf(cpf):
    pass


# EXERCÍCIO 12: Calculadora com Operação Personalizada
# Crie uma função que receba dois números e uma operação (+, -, *, /)
# Exemplo: calculadora(10, 5, "+") → 15

def calculadora(a, b, operacao):
    pass


# EXERCÍCIO 13: Palíndromo
# Crie uma função que verifique se uma palavra é um palíndromo
# Exemplo: eh_palindromo("arara") → True

def eh_palindromo(palavra):
    pass


# EXERCÍCIO 14: Contador de Palavras
# Crie uma função que conte o número de palavras em uma frase
# Exemplo: contar_palavras("Python é incrível") → 3

def contar_palavras(frase):
    pass


# EXERCÍCIO 15: Números Primos
# Crie uma função que verifique se um número é primo
# Exemplo: eh_primo(7) → True, eh_primo(10) → False

def eh_primo(numero):
    pass


# EXERCÍCIO 16: Fatorial Iterativo
# Crie uma função que calcule o fatorial usando loop
# Exemplo: fatorial_iterativo(5) → 120

def fatorial_iterativo(n):
    pass


# EXERCÍCIO 17: Fibonacci até N
# Crie uma função que retorne todos os números de Fibonacci menores que n
# Exemplo: fibonacci_ate(10) → [0, 1, 1, 2, 3, 5, 8]

def fibonacci_ate(n):
    pass


# EXERCÍCIO 18: Remover Duplicatas
# Crie uma função que remova elementos duplicados de uma lista
# Exemplo: remover_duplicatas([1, 2, 2, 3, 1]) → [1, 2, 3]

def remover_duplicatas(lista):
    pass


# EXERCÍCIO 19: Ordenar Dicionário por Valor
# Crie uma função que ordene um dicionário pelos valores
# Exemplo: ordenar_dict({"a": 3, "b": 1, "c": 2}) → {"b": 1, "c": 2, "a": 3}

def ordenar_dict(dicionario):
    pass


# EXERCÍCIO 20: Validador de Email Simples
# Crie uma função que verifique se um email é válido (contém @ e .)
# Exemplo: validar_email("user@example.com") → True

def validar_email(email):
    pass


"""
=============================================================================
BLOCO 3: EXERCÍCIOS DE RECURSÃO (10 exercícios)
=============================================================================

CONCEITO DE RECURSÃO:
Uma função recursiva é aquela que chama a si mesma para resolver um problema.
Toda recursão precisa de:
1. CASO BASE: condição de parada (evita loop infinito)
2. CASO RECURSIVO: chamada da própria função com parâmetros modificados

Estrutura básica:
def funcao_recursiva(parametro):
    if condicao_de_parada:  # CASO BASE
        return valor_simples
    else:  # CASO RECURSIVO
        return funcao_recursiva(parametro_modificado)
"""

# EXERCÍCIO 21: Contagem Regressiva
# Crie uma função recursiva que imprima números de n até 0
# Exemplo: contagem_regressiva(3) → imprime 3, 2, 1, 0

def contagem_regressiva(n):
    pass


# EXERCÍCIO 22: Soma até N
# Crie uma função recursiva que some todos os números de 1 até n
# Exemplo: soma_ate_n(5) → 15 (1+2+3+4+5)

def soma_ate_n(n):
    pass


# EXERCÍCIO 23: Fatorial Recursivo
# Crie uma função recursiva que calcule o fatorial
# Exemplo: fatorial(5) → 120

def fatorial(n):
    pass


# EXERCÍCIO 24: Potência Recursiva
# Crie uma função recursiva que calcule base^expoente
# Exemplo: potencia(2, 3) → 8

def potencia(base, expoente):
    pass


# EXERCÍCIO 25: Fibonacci Recursivo
# Crie uma função recursiva que retorne o n-ésimo número de Fibonacci
# Exemplo: fibonacci(6) → 8 (sequência: 0,1,1,2,3,5,8)

def fibonacci(n):
    pass


# EXERCÍCIO 26: Inverter String Recursivamente
# Crie uma função recursiva que inverta uma string
# Exemplo: inverter_recursivo("hello") → "olleh"

def inverter_recursivo(texto):
    pass


# EXERCÍCIO 27: Soma de Dígitos
# Crie uma função recursiva que some todos os dígitos de um número
# Exemplo: soma_digitos(123) → 6 (1+2+3)

def soma_digitos(numero):
    pass


# EXERCÍCIO 28: Máximo Divisor Comum (MDC)
# Crie uma função recursiva que calcule o MDC usando o algoritmo de Euclides
# Exemplo: mdc(48, 18) → 6

def mdc(a, b):
    pass


# EXERCÍCIO 29: Verificar Palíndromo Recursivamente
# Crie uma função recursiva que verifique se uma string é palíndromo
# Exemplo: palindromo_recursivo("arara") → True

def palindromo_recursivo(texto):
    pass


# EXERCÍCIO 30: Torres de Hanói
# Crie uma função recursiva que resolva o problema das Torres de Hanói
# Imprima os movimentos necessários para mover n discos de A para C usando B
# Exemplo: hanoi(2, "A", "C", "B") → Move disco de A para B, Move disco de A para C...

def hanoi(n, origem, destino, auxiliar):
    pass


"""
=============================================================================
GABARITO - NÃO OLHE ANTES DE TENTAR!
=============================================================================
"""

# ============= SOLUÇÕES BLOCO 1: FÁCEIS =============

def saudacao_solucao(nome):
    return f"Olá, {nome}!"


def area_retangulo_solucao(base, altura):
    return base * altura


def eh_par_solucao(numero):
    return numero % 2 == 0


def maior_de_tres_solucao(a, b, c):
    return max(a, b, c)
    # Alternativa sem max(): 
    # if a >= b and a >= c:
    #     return a
    # elif b >= c:
    #     return b
    # else:
    #     return c


def celsius_para_fahrenheit_solucao(celsius):
    return (celsius * 9/5) + 32


def contar_vogais_solucao(texto):
    vogais = "aeiouAEIOU"
    contador = 0
    for letra in texto:
        if letra in vogais:
            contador += 1
    return contador


def inverter_solucao(texto):
    return texto[::-1]


def calcular_media_solucao(numeros):
    if len(numeros) == 0:
        return 0
    return sum(numeros) / len(numeros)


def eh_maior_de_idade_solucao(idade):
    return idade >= 18


def repetir_solucao(texto, n):
    return texto * n


# ============= SOLUÇÕES BLOCO 2: MÉDIOS =============

def validar_cpf_solucao(cpf):
    return cpf.isdigit() and len(cpf) == 11


def calculadora_solucao(a, b, operacao):
    if operacao == "+":
        return a + b
    elif operacao == "-":
        return a - b
    elif operacao == "*":
        return a * b
    elif operacao == "/":
        if b != 0:
            return a / b
        else:
            return "Erro: divisão por zero"
    else:
        return "Operação inválida"


def eh_palindromo_solucao(palavra):
    palavra_limpa = palavra.lower().replace(" ", "")
    return palavra_limpa == palavra_limpa[::-1]


def contar_palavras_solucao(frase):
    return len(frase.split())


def eh_primo_solucao(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True


def fatorial_iterativo_solucao(n):
    if n < 0:
        return None
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado


def fibonacci_ate_solucao(n):
    fib = [0, 1]
    while fib[-1] + fib[-2] < n:
        fib.append(fib[-1] + fib[-2])
    return fib


def remover_duplicatas_solucao(lista):
    return list(dict.fromkeys(lista))
    # Alternativa: return list(set(lista)) - mas não mantém ordem


def ordenar_dict_solucao(dicionario):
    return dict(sorted(dicionario.items(), key=lambda item: item[1]))


def validar_email_solucao(email):
    return "@" in email and "." in email.split("@")[-1]


# ============= SOLUÇÕES BLOCO 3: RECURSÃO =============

def contagem_regressiva_solucao(n):
    if n < 0:  # Caso base
        return
    print(n)
    contagem_regressiva_solucao(n - 1)  # Caso recursivo


def soma_ate_n_solucao(n):
    if n <= 0:  # Caso base
        return 0
    return n + soma_ate_n_solucao(n - 1)  # Caso recursivo


def fatorial_solucao(n):
    if n <= 1:  # Caso base
        return 1
    return n * fatorial_solucao(n - 1)  # Caso recursivo


def potencia_solucao(base, expoente):
    if expoente == 0:  # Caso base
        return 1
    return base * potencia_solucao(base, expoente - 1)  # Caso recursivo


def fibonacci_solucao(n):
    if n <= 1:  # Caso base
        return n
    return fibonacci_solucao(n - 1) + fibonacci_solucao(n - 2)  # Caso recursivo


def inverter_recursivo_solucao(texto):
    if len(texto) <= 1:  # Caso base
        return texto
    return texto[-1] + inverter_recursivo_solucao(texto[:-1])  # Caso recursivo


def soma_digitos_solucao(numero):
    if numero < 10:  # Caso base
        return numero
    return (numero % 10) + soma_digitos_solucao(numero // 10)  # Caso recursivo


def mdc_solucao(a, b):
    if b == 0:  # Caso base
        return a
    return mdc_solucao(b, a % b)  # Caso recursivo


def palindromo_recursivo_solucao(texto):
    texto = texto.lower().replace(" ", "")
    if len(texto) <= 1:  # Caso base
        return True
    if texto[0] != texto[-1]:  # Verifica extremos
        return False
    return palindromo_recursivo_solucao(texto[1:-1])  # Caso recursivo


def hanoi_solucao(n, origem, destino, auxiliar):
    if n == 1:  # Caso base
        print(f"Move disco de {origem} para {destino}")
        return
    # Caso recursivo
    hanoi_solucao(n - 1, origem, auxiliar, destino)
    print(f"Move disco de {origem} para {destino}")
    hanoi_solucao(n - 1, auxiliar, destino, origem)


"""
=============================================================================
TESTES - Execute para verificar suas soluções
=============================================================================
"""

if __name__ == "__main__":
    print("=" * 60)
    print("TESTANDO SUAS SOLUÇÕES")
    print("=" * 60)
    
    # Teste suas funções aqui!
    print("Teste Exercício 1:", saudacao("Kaique"))
    print("Teste Exercício 2:", area_retangulo(5, 10))
    print("Teste Exercício 3:", eh_par(12))
    print("Teste Exercício 4:", maior_de_tres(2, 10, 6))
    print("Teste Exercício 5:", celsius_para_fahrenheit(42))
    print("Teste Exercício 6:", contar_vogais('Vogaisteste'))
    print("Teste Exercício 7:", inverter('Teste'))
    print("Teste Exercício 8:", calcular_media([10, 20, 30]))
    print("Teste Exercício 9:", eh_maior_de_idade(21))
    
    # print("Compare seus resultados com as funções *_solucao")
    
    # Exemplo de teste com solução:
    # print("\n--- Exemplo de teste com solução ---")
    # print("Exercício 1:", saudacao_solucao("Maria"))
    # print("Exercício 23:", fatorial_solucao(5))
    # print("Exercício 30:")
    # hanoi_solucao(3, "A", "C", "B")
