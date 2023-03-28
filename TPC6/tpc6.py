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
          'FIM_FRASE'
]

t_COMENTARIO = r'\/\/.|\/\*(.|\n)*\*\/ '
t_VARIAVEL = r'\w+'
t_FUNCAO = r'(function\s)?\w+(?=\()'
t_TIPO_DADOS = r'int'
t_CICLO = r'(while|for)'
t_OPERADOR = r'\+|-|\*|%|>|=|<|\,'
t_TAMANHO = r'\[\w+\]'
t_PARENT_INI = r'\('
t_PARENT_FIM = r'\)'
t_CHAVETA_INI = r'\{'
t_CHAVETA_FIM = r'\}'
t_INTERVALO = r'\[\d+\.\.\d+\]'

def t_PROGRAMA(t):
    r'(program\s)?\w+'
    result = re.match(r'(program\s)?\w+',t.value)
    t.value = result.group(1)
    return t

t_CONDICIONAL = r'if|else|in'
t_FIM_FRASE = r';'

def t_whitespace(t):
    r'\s+'
    pass

def t_error(t):
    print('Illegal character: ' + str(t.value[0]))
    t.lexer.skip(1)

t_ignore = ' \t\n'

lexer = lex.lex(debug=True)
f = open('factorial.p','r')
source = ''
for linha in f.readlines(): 
    source += linha

lexer.input(source)
for token in lexer:
    print (token)