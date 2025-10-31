# 🐍 Exercícios de Funções em Python

![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Status](https://img.shields.io/badge/status-em%20desenvolvimento-yellow.svg)

> Repositório de estudos com 30 exercícios práticos para dominar funções em Python, desde o básico até recursão avançada.

---

## 📋 Sobre o Projeto

Este repositório contém uma coleção de **30 exercícios progressivos** focados em funções Python, desenvolvido como material de estudo para estudantes de **Engenharia de Software** que estão iniciando sua jornada com Python.

### 🎯 Objetivo

Desenvolver habilidades sólidas em:
- Definição e uso de funções
- Parâmetros e valores de retorno
- Escopo de variáveis
- Recursão e casos base
- Boas práticas de programação

---

## 📚 Estrutura dos Exercícios

O repositório está organizado em **três blocos progressivos**:

### 🟢 Bloco 1: Exercícios Fáceis (1-10)
Fundamentos de funções, incluindo:
- Funções simples com retorno
- Manipulação de strings
- Operações matemáticas básicas
- Estruturas condicionais em funções

### 🟡 Bloco 2: Exercícios Médios (11-20)
Conceitos intermediários:
- Validação de dados
- Manipulação de listas e dicionários
- Algoritmos clássicos (palíndromos, números primos)
- Iteração e estruturas de dados

### 🔴 Bloco 3: Exercícios de Recursão (21-30)
Recursão do básico ao avançado:
- Casos base e recursivos
- Algoritmos recursivos clássicos (Fibonacci, Fatorial)
- Torres de Hanói
- Algoritmo de Euclides (MDC)

---

## 🚀 Como Usar Este Repositório

### Pré-requisitos

- Python 3.8 ou superior instalado
- Editor de código (VS Code, PyCharm, etc.)
- Conhecimentos básicos de programação

### Instalação

```bash
# Clone o repositório
git clone https://github.com/seu-usuario/exercicios-funcoes-python.git

# Entre no diretório
cd exercicios-funcoes-python

# Execute o arquivo de exercícios
python exercicios_funcoes.py
```

### Metodologia de Estudo Recomendada

1. **Leia o enunciado** do exercício com atenção
2. **Tente resolver** sem olhar a solução (use `pass` como placeholder)
3. **Teste sua função** com diferentes valores
4. **Compare** sua solução com o gabarito apenas depois de tentar
5. **Refatore** seu código se encontrar uma solução melhor
6. **Documente** o que aprendeu em comentários

```python
# ✅ Exemplo de como trabalhar:
def minha_funcao(parametro):
    """
    Documentação: o que a função faz
    """
    # Sua solução aqui
    pass

# Teste sua função
print(minha_funcao(valor_teste))
```

---

## 📖 Recursos de Aprendizado

### Documentação Oficial
- [Python.org - Tutorial de Funções](https://docs.python.org/pt-br/3/tutorial/controlflow.html#defining-functions)
- [Python.org - Documentação Completa](https://docs.python.org/pt-br/3/)

### Tutoriais Recomendados
- [Real Python - Defining Functions](https://realpython.com/defining-your-own-python-function/)
- [W3Schools Python Functions](https://www.w3schools.com/python/python_functions.asp)
- [Curso em Vídeo - Python (Gustavo Guanabara)](https://www.cursoemvideo.com/curso/python-3-mundo-1/)

### Livros
- 📕 **Python Crash Course** - Eric Matthes
- 📗 **Automate the Boring Stuff with Python** - Al Sweigart
- 📘 **Fluent Python** - Luciano Ramalho (avançado)

### Plataformas de Prática
- [LeetCode](https://leetcode.com/) - Problemas de algoritmos
- [HackerRank](https://www.hackerrank.com/domains/python) - Python track
- [Exercism](https://exercism.org/tracks/python) - Mentoria gratuita
- [Project Euler](https://projecteuler.net/) - Problemas matemáticos

---

## 🗂️ Estrutura do Repositório

```
exercicios-funcoes-python/
│
├── README.md                    # Este arquivo
├── exercicios_funcoes.py       # Arquivo principal com todos os exercícios
├── LICENSE                      # Licença do projeto
│
├── solucoes/                    # (Opcional) Soluções separadas
│   ├── bloco1_faceis.py
│   ├── bloco2_medios.py
│   └── bloco3_recursao.py
│
└── testes/                      # (Opcional) Testes unitários
    └── test_funcoes.py
```

---

## 💡 Conceitos-Chave Abordados

### Funções Básicas
```python
def saudar(nome):
    """Função simples com parâmetro e retorno"""
    return f"Olá, {nome}!"
```

### Funções com Múltiplos Parâmetros
```python
def calcular_area(base, altura):
    """Função com dois parâmetros"""
    return base * altura
```

### Recursão
```python
def fatorial(n):
    """Função recursiva com caso base"""
    if n <= 1:  # Caso base
        return 1
    return n * fatorial(n - 1)  # Caso recursivo
```

---

## 📊 Progresso dos Exercícios

Marque com ✅ conforme for completando:

### Bloco 1: Fáceis
- [ ] Exercício 1 - Saudação Personalizada
- [ ] Exercício 2 - Área do Retângulo
- [ ] Exercício 3 - Par ou Ímpar
- [ ] Exercício 4 - Maior de Três
- [ ] Exercício 5 - Conversor de Temperatura
- [ ] Exercício 6 - Contador de Vogais
- [ ] Exercício 7 - Inverter String
- [ ] Exercício 8 - Calcular Média
- [ ] Exercício 9 - Verificar Maioridade
- [ ] Exercício 10 - Repetir String

### Bloco 2: Médios
- [ ] Exercício 11 - Validador de CPF
- [ ] Exercício 12 - Calculadora Personalizada
- [ ] Exercício 13 - Palíndromo
- [ ] Exercício 14 - Contador de Palavras
- [ ] Exercício 15 - Números Primos
- [ ] Exercício 16 - Fatorial Iterativo
- [ ] Exercício 17 - Fibonacci até N
- [ ] Exercício 18 - Remover Duplicatas
- [ ] Exercício 19 - Ordenar Dicionário
- [ ] Exercício 20 - Validador de Email

### Bloco 3: Recursão
- [ ] Exercício 21 - Contagem Regressiva
- [ ] Exercício 22 - Soma até N
- [ ] Exercício 23 - Fatorial Recursivo
- [ ] Exercício 24 - Potência Recursiva
- [ ] Exercício 25 - Fibonacci Recursivo
- [ ] Exercício 26 - Inverter String Recursivamente
- [ ] Exercício 27 - Soma de Dígitos
- [ ] Exercício 28 - MDC (Algoritmo de Euclides)
- [ ] Exercício 29 - Palíndromo Recursivo
- [ ] Exercício 30 - Torres de Hanói

---

## 🤝 Como Contribuir

Contribuições são bem-vindas! Se você tem sugestões de novos exercícios ou melhorias:

1. Faça um **Fork** do projeto
2. Crie uma **Branch** para sua feature (`git checkout -b feature/NovoExercicio`)
3. **Commit** suas mudanças (`git commit -m 'Adiciona novo exercício sobre X'`)
4. **Push** para a Branch (`git push origin feature/NovoExercicio`)
5. Abra um **Pull Request**

### Sugestões de Contribuição
- 📝 Adicionar mais exercícios
- 🧪 Criar testes unitários
- 📚 Melhorar documentação
- 🐛 Reportar ou corrigir bugs
- 🌍 Traduzir para outros idiomas

---

## 📝 Notas do Desenvolvedor

Este repositório foi criado como parte dos meus estudos no **primeiro ano de Engenharia de Software**. Venho de uma base em **linguagem C** e estou expandindo meus conhecimentos para Python.

### Minha Jornada
- ✅ Concluído: Variáveis, loops, condicionais (C)
- ✅ Concluído: Funções básicas (C)
- ✅ Concluído: Ponteiros e alocação de memória básica (C)
- 🔄 Em progresso: Funções e recursão (Python)
- 📅 Próximo: POO em Python

---

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

```
MIT License

Copyright (c) 2025 [Seu Nome]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files...
```

---

## 📞 Contato

- **GitHub**: [@keyb0tt](https://github.com/keyb0tt)
- **LinkedIn**: [Seu Nome](https://linkedin.com/in/seu-perfil)
- **Email**: seu.email@exemplo.com

---

## 🌟 Agradecimentos

- Comunidade Python Brasil
- Professores e colegas de Engenharia de Software
- Criadores de conteúdo educacional em Python
- Todos que contribuíram com sugestões e melhorias

---

<div align="center">

**[⬆ Voltar ao topo](#-exercícios-de-funções-em-python)**

Feito com ❤️ e ☕ por um estudante de Engenharia de Software

⭐ Se este repositório te ajudou, considere dar uma estrela!

</div>