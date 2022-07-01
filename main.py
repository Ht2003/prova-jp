#criaçao da funcao nome bibliografico
#transformei o nome em uma lista para usar os comandos de decisao para aceitar ate 3 nomes
# e depois inverti as posiçoes no print,se a lista tiver 3 elementos,2 ou 1 ela vai sair com as
# posiçoes invertidas
#chemei a funçao e pedi pra ela retornar o nome bibliografico
#usei o upper para deixar o nome maiusculo
def nome_bibliografico(Nome):
    if len(Nome) == 2:
       print(Nome[-1].upper(),',',Nome[0])
    elif len(Nome) == 3:
       print(Nome[-1].upper(),',',Nome[0],Nome[-2])
    elif len(Nome) == 1:
        print(Nome[-0].upper())

Nome=input('digite o nome').split()
nome_bibliografico(Nome)
titulo=input('digite o titulo do livro')
nume=input('digite o numero do exemplar:')
endereco=input('digite o enderço')
editora=input('digite o nome da editora')
ano=input('digite o ano de publicaçao do livro')
print(f'{nome_bibliografico},{titulo},{nume},{editora},{ano}')







