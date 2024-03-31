from TH1_2 import xgcd

# (ax1 + b) % m = y1
# (ax2 + b) % m = y2
# ==================
# ax1 + b = y1 + t*m (1)
# ax2 + b = y2 + t*m (2)
# ==================
# (1) - (2):
# a(x1 - x2) = y1 - y2
# => a = (y1 - y2) / (x1 - x2)
def giai_he_pt_bac_nhat_2_an(x1, y1, x2, y2):
    m = 26
    tu_so = y1 - y2
    mau_so = x1 - x2
    if mau_so == 0:
        exit()
    if mau_so < 0:
        mau_so, tu_so = - mau_so, - tu_so
    if tu_so < 0:
        tu_so = tu_so % m
    inverted_mau_so = xgcd(mau_so, m)
    a = inverted_mau_so * tu_so
    b = y1 - (a * x1)
    return a, b