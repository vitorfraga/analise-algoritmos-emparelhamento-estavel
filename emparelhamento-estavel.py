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


 # Função tinder inspirada em matchmaker  "http://rosettacode.org/wiki/Stable_marriage_problem#Python"

def tinder(mans, manschoice, womans, womanschoice):

    guysfree = mans
    engaged  = {}
    guyprefers2 = manschoice
    galprefers2 = womanschoice

    while guysfree:

        guy = guysfree.pop(0)
        guyslist = guyprefers2[guy]
        gal = guyslist.pop(0)
        intended = engaged.get(gal)

        if not intended:
            # She's free
            engaged[gal] = guy
           
        else:
            # The bounder proposes to an engaged lass!
            galslist = galprefers2[gal]

            if galslist.index(intended) > galslist.index(guy):
                # She prefers new guy
                engaged[gal] = guy
               
                if guyprefers2[intended]:
                    # Ex has more girls to try
                    guysfree.append(intended)
            else:
                # She is faithful to old intended
                if guyslist:
                    # Look again
                    guysfree.append(guy)
    return engaged


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



##Create Im Tinder
plt.figure()
plt.plot(list_people,list_times_dataset)
plt.savefig('dataset_run.png')

##Create Img Dataset
plt.figure()
plt.plot(list_people,list_times_tinder)
plt.savefig('Tinder_run.png')