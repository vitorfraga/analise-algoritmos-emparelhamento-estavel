# coding: utf-8
import random


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


df = get_dataset(1,10)
mans = list(df['H'].keys())
womans = list(df['M'].keys())
manschoice = df['H']
womanschoice = df['M']

engaged = tinder(mans=mans, manschoice=manschoice, womans=womans, womanschoice=womanschoice)

print(engaged)
