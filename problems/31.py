ways = 1 # one 200p coin

def get_total(a, b=0, c=0, d=0, e=0, f=0, g=0):
    return a*100 + b*50 + c*20 + d*10 + e*5 + f*2 + g

for a in range(3): # 100p
    if get_total(a) > 200: break
    for b in range(5): # 50p
        if get_total(a, b) > 200: break
        for c in range(11): # 20p
            if get_total(a, b, c) > 200: break
            for d in range(21): # 10p
                if get_total(a, b, c, d) > 200: break
                for e in range(41): # 5p
                    if get_total(a, b, c, d, e) > 200: break
                    for f in range(101): # 2p
                        if get_total(a, b, c, d, e, f) > 200: break
                        for g in range(201): # 1p
                            total = get_total(a, b, c, d, e, f, g)
                            if total > 200: break
                            if total == 200:
                                ways += 1

print('Ways to to make 2 pounds: {}'.format(ways))
