"""Примеры с sha"""

import hashlib


# -------------------------------------sha1-----------------------------------#
hash_obj = hashlib.sha1(b'Testing sha1 func')
hex_dig_res = hash_obj.hexdigest()
print(hex_dig_res)
# d9536c477c646977dce73445a656a9c5e1c19d59

print()

# ------------------------------------sha224----------------------------------#
hash_obj = hashlib.sha224(b'Testing sha224 func')
hex_dig_res = hash_obj.hexdigest()
print(hex_dig_res)
# 0e4a2520fa80b33759be9c3ee71c9ea85a73137a2bef6af33537f197

print()

# ------------------------------------sha256----------------------------------#
hash_obj = hashlib.sha256(b'Testing sha256 func')
hex_dig_res = hash_obj.hexdigest()
print(hex_dig_res)
# 2e5bf4fb0365b2223c688e53ffe7b8866aaba5bfc1dcf42c9a6cb5e63701fe6e


print()

# -----------------------------------sha384-----------------------------------#
hash_obj = hashlib.sha384(b'Testing sha384 func')
hex_dig_res = hash_obj.hexdigest()
print(hex_dig_res)
# 367e5113f381c81e9260b530d2c8b2f062c6b1c62b44410ac95bedce1de6d7438f102a4e9c00c419c5bc22209a1541f1
print()

# ----------------------------------sha512------------------------------------#
hash_obj = hashlib.sha512(b'Testing sha512 func')
hex_dig_res = hash_obj.hexdigest()
print(hex_dig_res)
print(type(hex_dig_res))
# fab9c6c6d2fc7026210181e84cffacc471237bf58a10fbde4f5c4d942fe25846103937ff9b549f08fb921aa2e6da4f1c21f665d5ef7f83e908c4b99e41b9dcae

