
# ============================================================
# DES - DATA ENCRYPTION STANDARD
# Full implementation: Encrypt + Decrypt + Key Schedule
# Không sử dụng thư viện mã hóa có sẵn.
# ============================================================

# -------------------- 1. BANG IP ----------------------------

IP = [
    58, 50, 42, 34, 26, 18, 10, 2,
    60, 52, 44, 36, 28, 20, 12, 4,
    62, 54, 46, 38, 30, 22, 14, 6,
    64, 56, 48, 40, 32, 24, 16, 8,
    57, 49, 41, 33, 25, 17, 9, 1,
    59, 51, 43, 35, 27, 19, 11, 3,
    61, 53, 45, 37, 29, 21, 13, 5,
    63, 55, 47, 39, 31, 23, 15, 7
]

# -------------------- 2. BANG IP NGUOC ----------------------

FP = [
    40, 8, 48, 16, 56, 24, 64, 32,
    39, 7, 47, 15, 55, 23, 63, 31,
    38, 6, 46, 14, 54, 22, 62, 30,
    37, 5, 45, 13, 53, 21, 61, 29,
    36, 4, 44, 12, 52, 20, 60, 28,
    35, 3, 43, 11, 51, 19, 59, 27,
    34, 2, 42, 10, 50, 18, 58, 26,
    33, 1, 41, 9, 49, 17, 57, 25
]

# -------------------- 3. BANG MO RONG E ---------------------

E = [
    32, 1, 2, 3, 4, 5,
    4, 5, 6, 7, 8, 9,
    8, 9, 10, 11, 12, 13,
    12, 13, 14, 15, 16, 17,
    16, 17, 18, 19, 20, 21,
    20, 21, 22, 23, 24, 25,
    24, 25, 26, 27, 28, 29,
    28, 29, 30, 31, 32, 1
]

# -------------------- 4. BANG P -----------------------------

P = [
    16, 7, 20, 21, 29, 12, 28, 17,
    1, 15, 23, 26, 5, 18, 31, 10,
    2, 8, 24, 14, 32, 27, 3, 9,
    19, 13, 30, 6, 22, 11, 4, 25
]

# -------------------- 5. CAC S-BOX --------------------------

S_BOX = [
[
[14,4,13,1,2,15,11,8,3,10,6,12,5,9,0,7],
[0,15,7,4,14,2,13,1,10,6,12,11,9,5,3,8],
[4,1,14,8,13,6,2,11,15,12,9,7,3,10,5,0],
[15,12,8,2,4,9,1,7,5,11,3,14,10,0,6,13]
],
[
[15,1,8,14,6,11,3,4,9,7,2,13,12,0,5,10],
[3,13,4,7,15,2,8,14,12,0,1,10,6,9,11,5],
[0,14,7,11,10,4,13,1,5,8,12,6,9,3,2,15],
[13,8,10,1,3,15,4,2,11,6,7,12,0,5,14,9]
],
[
[10,0,9,14,6,3,15,5,1,13,12,7,11,4,2,8],
[13,7,0,9,3,4,6,10,2,8,5,14,12,11,15,1],
[13,6,4,9,8,15,3,0,11,1,2,12,5,10,14,7],
[1,10,13,0,6,9,8,7,4,15,14,3,11,5,2,12]
],
[
[7,13,14,3,0,6,9,10,1,2,8,5,11,12,4,15],
[13,8,11,5,6,15,0,3,4,7,2,12,1,10,14,9],
[10,6,9,0,12,11,7,13,15,1,3,14,5,2,8,4],
[3,15,0,6,10,1,13,8,9,4,5,11,12,7,2,14]
],
[
[2,12,4,1,7,10,11,6,8,5,3,15,13,0,14,9],
[14,11,2,12,4,7,13,1,5,0,15,10,3,9,8,6],
[4,2,1,11,10,13,7,8,15,9,12,5,6,3,0,14],
[11,8,12,7,1,14,2,13,6,15,0,9,10,4,5,3]
],
[
[12,1,10,15,9,2,6,8,0,13,3,4,14,7,5,11],
[10,15,4,2,7,12,9,5,6,1,13,14,0,11,3,8],
[9,14,15,5,2,8,12,3,7,0,4,10,1,13,11,6],
[4,3,2,12,9,5,15,10,11,14,1,7,6,0,8,13]
],
[
[4,11,2,14,15,0,8,13,3,12,9,7,5,10,6,1],
[13,0,11,7,4,9,1,10,14,3,5,12,2,15,8,6],
[1,4,11,13,12,3,7,14,10,15,6,8,0,5,9,2],
[6,11,13,8,1,4,10,7,9,5,0,15,14,2,3,12]
],
[
[13,2,8,4,6,15,11,1,10,9,3,14,5,0,12,7],
[1,15,13,8,10,3,7,4,12,5,6,11,0,14,9,2],
[7,11,4,1,9,12,14,2,0,6,10,13,15,3,5,8],
[2,1,14,7,4,10,8,13,15,12,9,0,3,5,6,11]
]
]

# -------------------- 6. KEY SCHEDULE -----------------------

PC1 = [
    57,49,41,33,25,17,9,
    1,58,50,42,34,26,18,
    10,2,59,51,43,35,27,
    19,11,3,60,52,44,36,
    63,55,47,39,31,23,15,
    7,62,54,46,38,30,22,
    14,6,61,53,45,37,29,
    21,13,5,28,20,12,4
]

PC2 = [
    14,17,11,24,1,5,
    3,28,15,6,21,10,
    23,19,12,4,26,8,
    16,7,27,20,13,2,
    41,52,31,37,47,55,
    30,40,51,45,33,48,
    44,49,39,56,34,53,
    46,42,50,36,29,32
]

SHIFTS = [
    1, 1, 2, 2, 2, 2, 2, 2,
    1, 2, 2, 2, 2, 2, 2, 1
]

# -------------------- 7. HAM HOAN VI ------------------------

def permute(data, table, input_size):
    """
    Hoan vi chuoi bit theo bang table.
    Bang DES su dung chi so bat dau tu 1.
    """
    result = 0

    for position in table:
        bit = (data >> (input_size - position)) & 1
        result = (result << 1) | bit

    return result


def left_shift_28(value, shift):
    """Dich vong trai 28 bit."""
    return ((value << shift) | (value >> (28 - shift))) & 0x0FFFFFFF


# -------------------- 8. SINH 16 KHOA CON -------------------

def generate_subkeys(key):
    """
    Input: khoa 64 bit
    Output: 16 khoa con, moi khoa 48 bit
    """

    # Loai bo 8 bit parity
    key56 = permute(key, PC1, 64)

    C = (key56 >> 28) & 0x0FFFFFFF
    D = key56 & 0x0FFFFFFF

    subkeys = []

    for shift in SHIFTS:
        C = left_shift_28(C, shift)
        D = left_shift_28(D, shift)

        combined = (C << 28) | D

        Ki = permute(combined, PC2, 56)

        subkeys.append(Ki)

    return subkeys


# -------------------- 9. HAM F CUA DES ----------------------

def feistel(R, subkey):

    # Buoc 1: Mo rong 32 bit thanh 48 bit
    expanded = permute(R, E, 32)

    # Buoc 2: XOR voi khoa con
    mixed = expanded ^ subkey

    # Buoc 3: Chia thanh 8 nhom, moi nhom 6 bit
    output = 0

    for i in range(8):

        block = (mixed >> (42 - 6 * i)) & 0x3F

        # Bit dau va bit cuoi tao thanh hang
        row = ((block & 0x20) >> 4) | (block & 1)

        # Bon bit giua tao thanh cot
        col = (block >> 1) & 0x0F

        value = S_BOX[i][row][col]

        output = (output << 4) | value

    # Buoc 4: Hoan vi P
    return permute(output, P, 32)


# -------------------- 10. MA HOA DES -----------------------

def des_encrypt(plaintext, key):

    if not (0 <= plaintext < (1 << 64)):
        raise ValueError("Plaintext phai co dung 64 bit")

    if not (0 <= key < (1 << 64)):
        raise ValueError("Key phai co dung 64 bit")

    # Hoan vi ban dau
    data = permute(plaintext, IP, 64)

    L = (data >> 32) & 0xFFFFFFFF
    R = data & 0xFFFFFFFF

    subkeys = generate_subkeys(key)

    # 16 vong Feistel
    for i in range(16):

        new_L = R
        new_R = L ^ feistel(R, subkeys[i])

        L = new_L
        R = new_R

    # Dao vi tri hai nua
    combined = (R << 32) | L

    # Hoan vi cuoi
    ciphertext = permute(combined, FP, 64)

    return ciphertext


# -------------------- 11. GIAI MA DES -----------------------

def des_decrypt(ciphertext, key):

    if not (0 <= ciphertext < (1 << 64)):
        raise ValueError("Ciphertext phai co dung 64 bit")

    if not (0 <= key < (1 << 64)):
        raise ValueError("Key phai co dung 64 bit")

    data = permute(ciphertext, IP, 64)

    L = (data >> 32) & 0xFFFFFFFF
    R = data & 0xFFFFFFFF

    subkeys = generate_subkeys(key)

    # Giai ma: su dung khoa con theo thu tu nguoc
    for Ki in reversed(subkeys):

        new_L = R
        new_R = L ^ feistel(R, Ki)

        L = new_L
        R = new_R

    combined = (R << 32) | L

    plaintext = permute(combined, FP, 64)

    return plaintext


# -------------------- 12. KIEM THU TEST VECTOR --------------

def main():

    # Test vector DES chuan
    plaintext = 0x0123456789ABCDEF
    key = 0x133457799BBCDFF1

    expected = 0x85E813540F0AB405

    print("========== DES TEST VECTOR ==========")

    print(f"Plaintext : {plaintext:016X}")
    print(f"Key       : {key:016X}")

    # Sinh khoa con
    subkeys = generate_subkeys(key)

    print("\n========== 16 SUBKEYS ===============")

    for i, Ki in enumerate(subkeys):
        print(f"K{i+1:02d} = {Ki:012X}")

    # Ma hoa
    ciphertext = des_encrypt(plaintext, key)

    print("\n========== ENCRYPTION ===============")

    print(f"Ciphertext : {ciphertext:016X}")
    print(f"Expected   : {expected:016X}")

    if ciphertext == expected:
        print("ENCRYPTION TEST: PASS")
    else:
        print("ENCRYPTION TEST: FAIL")

    # Giai ma
    recovered = des_decrypt(ciphertext, key)

    print("\n========== DECRYPTION ===============")

    print(f"Recovered  : {recovered:016X}")
    print(f"Original   : {plaintext:016X}")

    if recovered == plaintext:
        print("DECRYPTION TEST: PASS")
    else:
        print("DECRYPTION TEST: FAIL")


if __name__ == "__main__":
    main()
