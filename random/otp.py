import secrets


def generatePassword(length):
    chars = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%&*?"
    otp = ""
    i = 0
    while i < length:
        otp = otp + secrets.choice(chars)
        i += 1
    return otp


print(generatePassword(6))
