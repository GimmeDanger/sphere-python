import mmh3

def hashing_trick (input_dict, bits=13):
    bits = min (max (bits, 1), 32)
    N = 2**bits
    res = {}
    for k, v in dct.iteritems():
        try:
            f = str(k) + ':' + str(v)
        except:
            continue
        h = mmh3.hash(f) % N
        if h in res:
            res[h] += 1
        else:
            res[h] = 1
    return res

dct = {None:1, (1, 2, 3, 4, 5):2, 'three':3}
print hashing_trick(dct, 19239921391)
