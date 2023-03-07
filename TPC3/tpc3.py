import re
import json

def parser(file):
    dataLines = []
    with open(file) as f:
        #f1 = re.sub(r'\n+','\n',f.read())
        #print(f1);
        for line in f:
            if(len(line.split('::')) == 7):
                pasta,data,nome,pai,mae,info,_ = line.split('::')
                dic = {}
                dic['pasta'] = pasta
                dic['data'] = data 
                dic['nome'] = nome
                dic['pai']  = pai
                dic['mae']  = mae
                dic['info'] = info
                dataLines.append(dic)
    
    return dataLines
            
def processoAno(data):
    dicAno = {}
    for line in data:
        ano = line['data'].split('-')[0]
        if ano in dicAno.keys():
            dicAno[ano] += 1
        else:
            dicAno[ano] = 1
    
    return sorted(dicAno.items(),key=lambda x:x[1],reverse = True)


def seculos(year):
    return (int(year) - 1 ) // 100 + 1

def nomesSeculo(data):
    dicSeculos = {}
    for line in data:
        ano = line['data'].split('-')[0]
        seculo = seculos(ano)
        name = re.match(r'^\w+',line['nome']).group()
        apelido = re.search(r'\w+$',line['nome']).group()
        if seculo in dicSeculos.keys():
            if name in dicSeculos[seculo]['nomes'].keys():
                dicSeculos[seculo]['nomes'][name] += 1
            else:
                dicSeculos[seculo]['nomes'][name] = 1
            if apelido in dicSeculos[seculo]['apelidos'].keys():
                dicSeculos[seculo]['apelidos'][apelido] += 1
            else:
                dicSeculos[seculo]['apelidos'][apelido] = 1
        else:
            dicSeculos[seculo] = {'nomes': {name: 1}, 'apelidos': {apelido: 1}}
    for sec in dicSeculos:
        dicSeculos[sec]['nomes'] = sorted(dicSeculos[sec]['nomes'].items(),key=lambda x:x[1],reverse = True)
        dicSeculos[sec]['apelidos'] = sorted(dicSeculos[sec]['apelidos'].items(),key=lambda x:x[1],reverse = True)
    
    dicSeculos = dict(sorted(dicSeculos.items()))
    
    return dicSeculos
# 
def relacao(data):
    dicRelacoes ={}
    for line in data:
        if line['info'] !='':
            rel = re.findall(r',([^,]+)\. Proc',line['info'])
            for i in rel:
                if i in dicRelacoes.keys():
                    dicRelacoes[i] += 1
                else:
                    dicRelacoes[i] = 1
    return dicRelacoes
            
def exD(data):
    f = open("ex.json", "w")
    
    for i in range(20):
        dictJ = {}
        dictJ['pasta'] = data[i]['pasta']
        dictJ['data'] = data[i]['data']
        dictJ['nome'] = data[i]['nome']
        dictJ['pai']  = data[i]['pai']
        dictJ['mae']  = data[i]['mae']
        dictJ['info'] = data[i]['info']
        json.dump(dictJ, f)
    f.close()


info = parser("processos.txt")
anos = processoAno(info)
nomesApelidos = nomesSeculo(info)

for sec in nomesApelidos:
    
    print('\nSéculo: ' + str(sec))
    print('\nNomes')
    for i in range(5):
        print(str(i+1) + ': ' + nomesApelidos[sec]['nomes'][i][0] + ' - ' + str(nomesApelidos[sec]['nomes'][i][1]))
    print('\nApelidos')
    for i in range(5):
        print(str(i+1) + ': ' + nomesApelidos[sec]['apelidos'][i][0] + ' - ' + str(nomesApelidos[sec]['apelidos'][i][1]))

print (relacao(info))
exD(info)
