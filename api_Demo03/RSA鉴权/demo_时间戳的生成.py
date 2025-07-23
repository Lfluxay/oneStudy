from time import time
from common.hand_sign import HandleSign
# 时间戳的获取
t = int(time())


# 签名的获取
"""
token的前50位 + 时间戳， 然后进行RSA加密
"""

token = "eyJhbGciOiJIUzUxMiJ9.eyJtZW1iZXJf" \
        "aWQiOjEyMzcwMDA4MTksImV4cCI6MTYzN" \
        "TE1NTQ5M30.lKAiPI8ZVuLyrHxAka29BSfkS" \
        "einFZIgb-ZIOdQjK4jLgZJqR4as4gBCY6zCh" \
        "sos68VQmYo7W4WPP0Br-M-vHQ"

data = token[:50] + str(t)
hs = HandleSign()
res = hs.encrypt(data)
print(res)

params = {"timestamp": t, "sign": res}
print(params)