import re, sys

saldo = 0
estado = 'POUSAR'
er_cents = re.compile(r'(\d+)c')
er_euros = re.compile(r'(\d+)e')

def atualizaSaldo():
    global saldo
    euro = int(saldo/100)
    cent = saldo%100
    sSaldo = str(euro) + 'e' + str(cent) + 'c'
    return sSaldo

def verificaContacto(contacto):
    print('ola')
    global saldo
    if(not (len(contacto) == 9)):
        print('maq: \"Número inválido. Disque um novo número!\"')
    elif(contacto[:3] == '601' or contacto[:3] == '641'):
        print('maq: \"Esse número não é permitido neste telefone. Queira discar novo número!\"')
    elif(contacto[:3] == '800'):
        print('maq: \"saldo = ' + atualizaSaldo() + '\"')
    elif(contacto[:3] == '808'):
        if(saldo > 10):
            saldo -= 10
            print('maq: \"saldo = ' + atualizaSaldo() + '\"')
        else:
            print('maq: \"Saldo Insuficiente\"')
    elif(contacto[:2] == '00'):
        if(saldo > 150):
            saldo -= 150
            print('maq: \"saldo = ' + atualizaSaldo() + '\"')
        else:
            print('maq: \"Saldo Insuficiente\"')
    elif(contacto[0] == '2'):
        if(saldo > 25):
            saldo -= 25
            print('maq: \"saldo = ' + atualizaSaldo() + '\"')
        else:
            print('maq: \"Saldo Insuficiente\"')

def interpretaMoedas(moedas):
    global saldo
    erro =''
    for m in moedas:
        if (x := re.search(er_cents,m)):
            if(int(x.group(1)) in [1,2,5,10,20,50]):
                saldo += int(x.group(1))
            else:
                erro += x.group(1)+ 'c - moeda inválida; '
        elif(y := re.search(er_euros,m)):
            if(int(y.group(1)) in [1,2]):
                saldo += int(y.group(1)) * 100
            else:
                erro += y.group(1)+ 'e - moeda inválida; '
            
    print(erro + 'saldo = ' + atualizaSaldo())

def main():
    global saldo
    global estado

    for linha in sys.stdin:
        if(len(linha) == 0):
            continue
        
        linha = linha.strip('\n')
        if '=' in linha:
            token,num = linha.split('=')
            if(token == 'T'):
                verificaContacto(num)
        else:
            l = linha.split(' ')
            token = l[0]
            linha = ''.join(l[1::])

            if(estado == 'POUSAR'):
                if(token == 'LEVANTAR'): 
                    print('maq: \"Introduza moedas.\"')
                    estado = token
                else:
                    print('Operação inválida')
                    return 1
            else:
                if (token == 'ABORTAR' or token == 'POUSAR' ):
                    print('maq: \"troco=' + atualizaSaldo() + '; Volte sempre!\"')
                    estado = token
                    saldo = 0
                    return 1
                elif(token == "MOEDA"):
                    interpretaMoedas(linha.split(','))
                else:
                    print('Operação inválida1')
                    return 1
main()
