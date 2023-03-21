import json
import re

def parse_firstLine(line):
    campos = line.split(',')
    return campos

def ex1(file):
    info = []
    with open(file,'r',encoding='utf-8') as f:
        data = f.readlines()
        first_line = data[0]
        campos = parse_firstLine(first_line)
        content = data[1:]
        for line in content:
            fields = line.split(',')
            dic = {}
            for i in range(len(campos)):
                dic[campos[i]] = fields[i]
            info.append(dic)
    
    return info

def ex2(file):
    info = []
    with open(file,'r',encoding='utf-8') as f:
        data = f.readlines()
        first_line = data[0]
        campos = parse_firstLine(first_line)
        content = data[1:]
        n_grades = re.search(r'Notas{(\d+)}',first_line).group(1)
        for line in content:
            fields = line.split(',')
            dic = {}
            for i in range(3):
                dic[campos[i]] = fields[i]
            grades = []
            for i in range(3,int(n_grades) + 3):
                grades.append(int(fields[i]))
            dic['Notas'] = grades
            info.append(dic)
    
    return info

def ex3(file):
    info = []
    with open(file,'r',encoding='utf-8') as f:
        data = f.readlines()
        first_line = data[0]
        campos = parse_firstLine(first_line)
        content = data[1:]
        n_grades = re.search(r'Notas{(\d+),(\d+)}',first_line)
        min_grades = n_grades.group(1)
        max_grades = n_grades.group(2)
        for line in content:
            fields = line.split(',')
            dic = {}
            for i in range(3):
                dic[campos[i]] = fields[i]
            grades = []
            for i in range(3,int(max_grades) + 3):
                if fields[i] not in ['','\n']:
                    grades.append(int(fields[i]))
            dic['Notas'] = grades
            info.append(dic)
    return info

def ex4(file):
    info = []
    with open(file,'r',encoding='utf-8') as f:
        data = f.readlines()
        first_line = data[0]
        campos = parse_firstLine(first_line)
        content = data[1:]
        n_grades = re.search(r'Notas{(\d+),(\d+)}::(\w+)',first_line)
        min_grades = n_grades.group(1)
        max_grades = n_grades.group(2)
        func = n_grades.group(3)
        for line in content:
            fields = line.split(',')
            dic = {}
            for i in range(3):
                dic[campos[i]] = fields[i]
            grades = []
            for i in range(3,int(max_grades) + 3):
                if fields[i] not in ['','\n']:
                    grades.append(int(fields[i]))

            if func == "sum":
                dic[func] = sum(grades)
            elif func == "media":
                dic[func] = sum(grades) / len(grades)
            else:
                pass
            info.append(dic)
    return info

def json_format(file,data):
    with open(file, "w",encoding='utf8') as f:
        json.dump(data,f,indent=2)
            


def main():
    print("\n------------------ Menu Principal ------------------")
    print("1. Sem extensão")
    print("2. Com listas")
    print("3. Com listas com intervalo de tamanho")
    print("4. Com funções de agregação")
    print("0. Sair")
    print("----------------------------------------------------\n")

    escolha = input('Opção: ')
    if escolha == '0':
        print('Programa Terminado')
        return
    elif (escolha == '1'):
        info = ex1("./input/input1.csv")
        json_format("./output/ex_1.json",info)
    elif (escolha == '2'):
        info = ex2("./input/input2.csv")
        json_format("./output/ex_2.json",info)
    elif (escolha == '3'):
        info = ex3("./input/input3.csv")
        json_format("./output/ex_3.json",info)
    elif (escolha == '4'):
        info = ex4("./input/input4.csv")
        json_format("./output/ex_4.json",info)
        info = ex4("./input/input5.csv")
        json_format("./output/ex_5.json",info)
    else:
        print("Opção inválida!")

main()