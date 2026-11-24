#Nhan hai da thuc trong truong huu han GF(2^m)
def gf_multiply(a, b, m, modulus):
  result = 0
  high_bit = 1 << m
  mask = high_bit - 1

  while b > 0:
    if b & 1:
      result ^= a #Cong bit cuoi cua b cong bang XOR
    a <<= 1

    if a & high_bit:
      a ^= modulus
    a &= mask
    b >>= 1
  return result

#GF(2^4), da thuc toi gian: x^4 + x + 1 => 0x13
def multiply_gf16(a, b):
  if not (0 <= a < 16 and 0 <= b < 16):
    raise ValueError("Phan tu GF(2^4) phai nam trong [0, 15]")
  return gf_multiply(a, b, 4, 0x13)

#GF(2^8), da thuc toi gian: x^8 + x^4 + x + 1 => 0x11B
def multiply_gf256(a, b):
  if not (0 <= a <256 and 0 <= b < 256):
    raise ValueError("Phan tu GF(2^8) phai nam trong [0, 255]")
  return gf_multiply(a, b, 8, 0x11B)

if __name__ == "__main__":
  print("PHEP NHAN GF(2^4)")
  a4, b4 = 0b1011, 0b0110
  print(f"A = {a4:04b}, B = {b4:04b}")
  print(f"A * B = {multiply_gf16(a4, b4):04b}")

  print("\nPHEP NHAN GF(2^6)")
  a8, b8 = 0x57, 0x83
  print(f"A = 0x{a8:02X}, B = 0x{b8:02X}")
  print(f"A * B = 0x{multiply_gf256(a8, b8):02X}")