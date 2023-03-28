import ply.lex as lex
import re

tokens = [
          'COMENTARIO',
          'VARIAVEL',
          'FUNCAO',
          'TIPO_DADOS',
          'CICLO',
          'PARENT_INI',
          'PARENT_FIM',
          'CHAVETA_INI',
          'CHAVETA_FIM',
          'OPERADOR',
          'TAMANHO',
          'INTERVALO',
          'PROGRAMA',
          'CONDICIONAL',
          'FIM_FRASE',
          'NUMERO'
]

def t_NUMERO(t):
    r'\d+'
    return t
def t_COMENTARIO(t):
     r'\/\/.*|\/\*(.|\n)*\*\/ '
     return t
def t_TIPO_DADOS(t):
    r'int'
    result = re.match(r'(int)',t.value)
    t.value = result.group(1)
    return t

def t_CONDICIONAL(t):
    r'if |else |in '
    return t

def t_FUNCAO(t):
    r'(function\s)?\w+(?=\()'
    return t

def t_CICLO(t):
    r'(while|for)'
    return t
def t_PROGRAMA(t):
    r'program\s\w+'
    #result = re.match(r'program\s\w+',t.value)
    #t.value = result
    return t
def t_VARIAVEL(t):
    r'(int\s)?\w+'
    return t


def t_OPERADOR(t):
    r'\+|-|\*|%|>|=|<|\,'
    return t

def t_TAMANHO(t):
    r'\[\w+\]'
    return  t

def t_PARENT_INI(t):
    r'\('
    return t

def t_PARENT_FIM(t):
    r'\)'
    return t

def t_CHAVETA_INI(t):
    r'\{'
    return t

def t_CHAVETA_FIM(t):
    r'\}'
    return t

def t_INTERVALO(t):
    r'\[\d+\.\.\d+\]'
    return t

def t_FIM_FRASE(t):
    r';'
    return t

def t_whitespace(t):
    r'\s+'
    pass

def t_error(t):
    print('Illegal character: ' + str(t.value[0]))
    t.lexer.skip(1)

t_ignore = ' \t\n'

lexer = lex.lex(debug=True)
f = open('max.p','r')
source = ''
for linha in f.readlines(): 
    source += linha

lexer.input(source)
for token in lexer:
    print (token)