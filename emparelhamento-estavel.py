# coding: utf-8
"""
0=>key
1=>Solteiro
2=>Preferencia
3=>Casado
"""
df = {'H':[['h1', True, None, None],['h2', True, None, None]], 'M':[['m1',True,'h1', None], ['m2', True, None, None]]}
solteiro = True
casais = []
while solteiro == True:
    for i in df['H']:
        print(i[0])
    solteiro = False
