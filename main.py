#fiz a importaçao dessa bibioteca no python para o programa nao aceitar numeros,
#apenas letras, toda vez que o usuario digitar um numero,ele vai ser removido
from string import digits
string=input('digite alguma coisa').strip()#vai eliminar os espaços que o usuario digiter
table=str.maketrans('','', digits)#vai fazer a remoçao dos numeros
newstring= string.translate(table)

v='aeiou-AEIOU'#criaçao de duas variaveis para serem comparadas
c='bcdfghjklmnpqrstvwxyz-BCDFGHJKLMNPQRSTSVWXYZ'

for letra in string :#processo para deixar letras maiusculas e outras minusculas
    if letra in v:#se for uma  vogal vai sair maiuscula
      print(letra.upper(), end='')
    elif letra in c:# se a letra for uma consoante vai sair minuscula,caso o usuario digite maiuscula,vai ficar maiuscula
       print(letra, end='')
