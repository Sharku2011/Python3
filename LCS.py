import os

def calc_cache_pos(strings, indexes):
    factor = 1
    pos = 0
    for s, i in zip(strings, indexes):
        pos += i * factor
        factor *= len(s)
        #print("p:{0},f:{1}/".format(pos,factor),end='')
    return pos

def lcs_back(strings, indexes, cache):
    if -1 in indexes:
        return ""
    match = all(strings[0][indexes[0]] == s[i]
                for s, i in zip(strings, indexes))
    if match:
        new_indexes = [i - 1 for i in indexes]
        result = lcs_back(strings, new_indexes, cache) + strings[0][indexes[0]]
    else:
        substrings = [""] * len(strings)
        #print(len(strings))
        for n in range(len(strings)):
            if indexes[n] > 0:
                new_indexes = indexes[:]
                new_indexes[n] -= 1
                cache_pos = calc_cache_pos(strings, new_indexes)
                if cache[cache_pos] is None:
                    substrings[n] = lcs_back(strings, new_indexes, cache)
                else:
                    substrings[n] = cache[cache_pos]
        result = max(substrings, key=len)
    cache[calc_cache_pos(strings, indexes)] = result
    return result

def lcs(strings):
    """
    >>> lcs(['666222054263314443712', '5432127413542377777', '6664664565464057425'])
    '54442'
    >>> lcs(['abacbdab', 'bdcaba', 'cbacaa'])
    'baa'
    """
    if len(strings) == 0:
        return ""
    elif len(strings) == 1:
        return strings[0]
    else:
        cache_size = 1
        for s in strings:
            cache_size *= len(s)
        cache = [None] * cache_size
        indexes = [len(s) - 1 for s in strings]
        output = lcs_back(strings, indexes, cache)
        print(cache)
        return output
        
print(lcs(['CGGGGCTA','TTTGAGGG','GGATGGAT']))
#print(lcs(['aac','abc','bbc']))
#print(calc_cache_pos(['CGGGGCTA','TTTGAGGG','GGATGGAT'],[7,7,7]))

os.system('pause')