# def capsule(shirt, pants, cardigans, shoes, socks, hats):
#     return shirt * pants * cardigans * shoes * socks * hats

def capsule(*clothes):
    result = 1
    for garment in clothes:
        result *= garment
    return result