# 3. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.



import os.path

def lineCountInFile(path):
    file=open(path,'r')
    lines=0
    for line in file:
        if line != "\n":
            lines+=1
    file.close()
    return lines

def printFromFile(path):
    file=open(path,'r')
    print("Содержимое файла (",path,"):")
    for i in range(lineCountInFile(path)):
        print(file.readline())
    file.close()

def readWriteFile(code,fromFile,toFile):
    source=open(fromFile,'r')
    with open(toFile,'w') as moded:
        if code:
            for i in range(lineCountInFile(fromFile)):
                moded.write(encode(source.readline()))
        else:
            for i in range(lineCountInFile(fromFile)):
                moded.write(decode(source.readline()))
    source.close()

def encode(line):
    result=char=''
    count=0
    for i in line:
        if i==char:
            count+=1
        else:
            if char:
                result+=str(count)+char
            count=1
            char=i
    result+=str(count)+char
    return result

def decode(line):
    result=count=''
    for i in line:
        if i.isdigit():
            count+=i
        else:
            result+=i*int(count)
            count=''
    return result

def getPath():
    path=''
    while not os.path.exists(path):
        path=input('введите имя файла ')
    return path

print('Исходные данные', end=',')
sourcePath=getPath()
print('Кодированиe', end=',')
codedPath=getPath()
print('Декодирование', end=',')
decodedPath=getPath()
readWriteFile(1,sourcePath,codedPath)
readWriteFile(0,codedPath,decodedPath)
printFromFile(sourcePath)
printFromFile(codedPath)
printFromFile(decodedPath)