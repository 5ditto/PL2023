
file = open('myheart.csv','r')
content = file.readlines()
content = content[1:]
file.close()

def parse(file):
    info = []
    for linha in file:
        idade,sexo,tensao,colestrol,batimento,temDoenca = linha.split(',')
        dic = dict()
        dic['idade'] = int(idade)
        dic['sexo'] = sexo
        dic['tensao'] = int(tensao)
        dic['colestrol'] = int(colestrol)
        dic['batimento'] = int(batimento)
        dic['temDoenca'] = int(temDoenca.strip('\n'))
        info.append(dic)
    return info

def doencaSexo(info):
    dicDS = dict()
    # 'Feminino' : [Doentes, Não Doentes]
    dicDS['Feminino'] = [0,0]
    # 'Masculino' : [Doentes, Não Doentes]
    dicDS['Masculino'] = [0,0]
    # 'Outros' : [Doentes, Não Doentes]
    dicDS['Outros'] = [0,0]
    
    for i in info:
        if (i['sexo'] == 'F'):
            if(i['temDoenca'] == 1): 
                dicDS['Feminino'][0] += 1
            else:
                dicDS['Feminino'][1] += 1
        elif(i['sexo'] == 'M'):
            if(i['temDoenca'] == 1):
                dicDS['Masculino'][0] += 1
            else:
                dicDS['Masculino'][1] += 1
        elif(i['temDoenca'] == 1):
            dicDS['Outros'][0] += 1
        else:
            dicDS['Outros'][1] += 1
    return dicDS


def doencaFaixaEtaria(info):
    dicIdades = dict()
    max = idadeMax(info)
    i = 0
    while(i<=max):
        # faixa etária : [Doentes, Não Doentes]
        fe = '['+str(i) + '-' + str(i+4)+ ']'
        dicIdades[fe] = [0,0]
        i += 5
    for i in info:
        idade = i['idade']
        nivel = int(idade/5)
        fe = '['+str(int(nivel*5)) + '-' + str(int(nivel*5 + 4)) + ']'
        
        if(i['temDoenca'] == 1):
            dicIdades[fe][0] += 1
        else:
            dicIdades[fe][1] += 1
            
    return dicIdades
    

def idadeMax(info):
    max = 0
    for i in info:
        if(i['idade'] > max):
            max = i['idade']
    return max



def doencaColestrol(info):
    dicColestrol = dict()
    max = colestrolMax(info)
    min = colestrolMin(info)

    # nivelColestrol : [Doentes, Não Doentes]
    for i in range(min, max+1,10):
        fe = '['+str(i) + '-' + str(i+9)+ ']'
        dicColestrol[fe] = [0,0]

    for i in info:
        colestrol = i['colestrol']
        nivel = int(colestrol/10)
        fe = '['+str(int(nivel*10)) + '-' + str(int(nivel*10 + 9)) + ']'
        if(i['temDoenca'] == 1):
            dicColestrol[fe][0] += 1
        else:
            dicColestrol[fe][1] += 1
    return dicColestrol

def colestrolMax(info):
    max = info[0]['colestrol']
    for i in info:
        if(i['colestrol'] > max):
           max = i['colestrol']
    
    return max

def colestrolMin(info):
    min = info[0]['colestrol']
    for i in info:
        if(i['colestrol'] < min):
            min = i['colestrol']
    return min


def imprimeDistr(nome,dic):
    keys = dic.keys()
    l = 0
    for k in keys:
        if len(k) > l:
            l = len(k)
    print("\n" + nome + "\n")
    print(" " * (l+2) + "| Doentes | Não doentes |")
    for key in dic:
        d = str(dic[key][0])
        nd = str(dic[key][1])
        print(" " + key + " " * (l-len(key)) + " | " + d + " " * (8-len(d)) + "| " + nd + " " * (12 - len(nd)) + "|")
   

info = parse(content)

a = doencaSexo(info) 
idade = doencaFaixaEtaria(info)
colestrol = doencaColestrol(info)

imprimeDistr("Distribuição da Doença por Sexo", a)
imprimeDistr("Distribuição da Doença por Escalões Etários", idade)
imprimeDistr("Distribuição da Doença por Níveis de Colesterol", colestrol)


