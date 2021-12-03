import hashlib


def rabin_karp_count(s: str, subs: str) -> int:
    assert len(s) > 0 and len(subs) > 0, 'string or substring cant be empty'
    assert len(s) > len(subs), 'substring should be less then string'

    count = 0
    len_sub = len(subs)
    h_sub = hashlib.sha1(subs.encode('utf-8')).hexdigest()

    for i in range(len(s) - len_sub + 1):
        h_i_sub = hashlib.sha1(s[i:i + len_sub].encode('utf-8')).hexdigest()
        if h_sub == h_i_sub:
            count += 1
    return count


s_1 = input('enter string: ')
s_2 = input('enter substring for counting its quantity in string: ')

count = rabin_karp_count(s_1, s_2)

print(f'"{s_1}" contains: {count} "{s_2}"')
