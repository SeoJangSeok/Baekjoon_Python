def solution(bin1, bin2):
    dec1, dec2 = int(bin1, 2), int(bin2, 2)
    return bin(dec1 + dec2).replace('0b', '')