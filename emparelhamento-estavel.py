# coding: utf-8
# %load emparelhamento-estavel.py
import random


# Funcao que retorna o dataset

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
        
    return h,m

 # Referencia do matchmaker  "http://rosettacode.org/wiki/Stable_marriage_problem#Python"

def matchmaker():
    guysfree = guys[:]
    engaged  = {}
    guyprefers2 = copy.deepcopy(guyprefers)
    galprefers2 = copy.deepcopy(galprefers)
    while guysfree:
        guy = guysfree.pop(0)
        guyslist = guyprefers2[guy]
        gal = guyslist.pop(0)
        fiance = engaged.get(gal)
        if not fiance:
            # She's free
            engaged[gal] = guy
            print("  %s and %s" % (guy, gal))
        else:
            # The bounder proposes to an engaged lass!
            galslist = galprefers2[gal]
            if galslist.index(fiance) > galslist.index(guy):
                # She prefers new guy
                engaged[gal] = guy
                print("  %s dumped %s for %s" % (gal, fiance, guy))
                if guyprefers2[fiance]:
                    # Ex has more girls to try
                    guysfree.append(fiance)
            else:
                # She is faithful to old fiance
                if guyslist:
                    # Look again
                    guysfree.append(guy)
    return engaged


