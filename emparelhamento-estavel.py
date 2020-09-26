# coding: utf-8
# %load emparelhamento-estavel.py
import random

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
        
    return h, m
referencia = "http://rosettacode.org/wiki/Stable_marriage_problem#Python"
