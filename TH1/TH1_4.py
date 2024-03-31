# Họ và tên: Trần Hải Đăng
# MSSV: B2016956
# STT: 13

from TH1_2 import decryptAF, Char2Num, Num2Char
from utils import giai_he_pt_bac_nhat_2_an

encrypted_txt = "LOLYLTQOLTHDZTDC"
part_plain_txt = "LAMUOI"

# Brute-Force approach:
flag = False
for a in range(0, 20):
    for b in range(0, 20):
        original_txt = decryptAF(encrypted_txt, a, b)
        x = original_txt.find(part_plain_txt)
        if x != -1:
            flag = True
            break
    if flag:
        break

print("Original text found with a = {} and b = {}: {}".format(str(a), str(b), original_txt))