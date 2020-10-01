# coding: utf-8
import random
import time 
import sys
import numpy as np
from matplotlib import pyplot as plt
from pathlib import Path
import warnings
from numba import jit
#This is to ignore NumbaWarnings and NumbaDeprecationWarnings issued by @jit
warnings.filterwarnings("ignore", category=Warning)
warnings.filterwarnings("ignore", category=DeprecationWarning)

#https://cse.buffalo.edu/~hartloff/CSE331-Summer2015/GaleShapley.pdf
def tinder(mans, manschoice, womans, womanschoice):
    matchs  = {}

    while mans: #Enquanto existe ao menos um homem solteiro que ainda não propôs namoro para uma mulher
        man = mans.pop(0) #Pega um homem da lista de homens
        guys_list = manschoice[man] #Pega as pretendentes desse homem
        woman = guys_list.pop(0) #Pega a primeira mulher dessa lista
        actual = matchs.get(woman) #Pergunta pra ela se ela quer namora e ja tem namorado
        
        if not actual: #Se m esta disponível (não tem atual)
            matchs[woman] = man #Ela é solteira e aceita o namoro
           
        else: #Se m não esta disponível (tem atual)
            womans_list = womanschoice[woman] #Procuramos os pretendentes da mulher
            if womans_list.index(actual) > womans_list.index(man): #Se ela prefere o novo homem
                mans.append(actual) #atual vira ex e vai procurar outra
                matchs[woman] = man #ela começa a namorar quem fez o pedido
            else: #Se ela prefere o atual ao invés que o novo homem
                mans.append(man) #Novo homem continua solteiro

    return matchs

@jit
def get_dataset(start = None, end = None):
    
    h = {}
    m = {}
    
    i, j = start,  end   
    while i <= j:
        h['h'+str(i)] = []
        m['m'+str(i)] = []
        i = i + 1
    
    k,v = start, end       
    while k <= j:
        h_keys  = list(h.keys())
        m_keys = list(m.keys())
        random.shuffle(h_keys)
        random.shuffle(m_keys)        
        h['h'+str(k)] = m_keys
        m['m'+str(k)] = h_keys
        k = k + 1
    f = {'H':h,'M':m }
    
    
    return f

# Create output folder
Path("output").mkdir(parents=True, exist_ok=True)

# Initial prepare
list_people = list(range(1,100,1))#[10,50,100,1000,2000,3000,5000,10000]
list_people.extend(range(100,1000,10))
list_people.extend(range(1000,4000,100))
list_people.extend(range(4000,10000,1000))
list_people.extend(range(10000,20000,2000))

times_to_mean = 5
list_times_tinder = []
list_times_dataset = []
for people in list_people:
    _list_times_tinder = []
    _list_times_dataset = []
    for change in range(times_to_mean):
        ##Create and Open output file
        f = open(f'output/Log_{people}_{change}.txt', 'w')
        sys.stdout = f

        ##Dataset Creation
        ###Start counting time for dataset
        start_time = time.time()
        ###Create Dataset
        df = get_dataset(1,people)
        ###Create List of mans and choices
        mans = list(df['H'].keys())
        womans = list(df['M'].keys())
        manschoice = df['H']
        womanschoice = df['M']
        ###Finish counting time for dataset
        end_time = time.time()
        print(f"Create Dataset time: {end_time - start_time}")
        _list_times_dataset.append(end_time - start_time)

        ##Tinder Alg
        ###Start counting time for Tinder
        start_time = time.time()
        ###Do Tinder
        engaged = tinder(mans=mans, manschoice=manschoice, womans=womans, womanschoice=womanschoice)
        ###Finish counting time for Tinder
        end_time = time.time()
        print(f"Tinder time: {end_time - start_time}")
        _list_times_tinder.append(end_time - start_time)
        print(f'Casamentos: {engaged}')
        ###Close File
        f.close()

    f = open(f'output/_Log_mean_time.txt', 'w')
    sys.stdout = f
    list_times_tinder.append(np.mean(_list_times_tinder))
    list_times_dataset.append(np.mean(_list_times_dataset))
    print(list_times_tinder)
    print(list_times_dataset)
    ###Close File
    f.close()

    ##Create every time because sometimes shit happen
    ##Create Im Tinder
    plt.figure()
    plt.plot(list_people[0:len(list_times_dataset)],list_times_dataset)
    plt.savefig(f'out_dataset/dataset_run{len(list_times_dataset)}.png')
    plt.close()

    ##Create Img Dataset
    plt.figure()
    plt.plot(list_people[0:len(list_times_tinder)],list_times_tinder)
    plt.savefig(f'out_tinder/Tinder_run{len(list_times_dataset)}.png')
    plt.close()
