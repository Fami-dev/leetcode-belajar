# ═══════════════════════════════════════════════════════════════
# Q9. INTEGER TO ROMAN
# ═══════════════════════════════════════════════════════════════

# 📖 PENJELASAN SOAL (UNTUK PEMULA)
# ═════════════════════════════════════════════════════════════════
#
# Apa itu Integer to Roman?
# → Konversi angka desimal (1, 2, 3...) ke Roman numerals (I, II, III...)
#
# Simbol Roman dan nilainya:
#   I = 1
#   V = 5
#   X = 10
#   L = 50
#   C = 100
#   D = 500
#   M = 1000
#
# Aturan Roman Numerals:
# 1. Gabung simbol dari besar ke kecil
#    Contoh: 27 = XX + V + II = XXVII
#
# 2. Subtractive form (pengurangan):
#    - IV = 4 (5-1, bukan IIII)
#    - IX = 9 (10-1, bukan VIIII)
#    - XL = 40 (50-10)
#    - XC = 90 (100-10)
#    - CD = 400 (500-100)
#    - CM = 900 (1000-100)
#
# 3. Simbol power of 10 (I, X, C, M) max 3 kali berturut-turut
#    Contoh: III = 3, bukan IIII
#            XXX = 30, bukan XXXX
#            CCC = 300, bukan CCCC
#
# Contoh mudah:
#   num = 58
#   50 = L
#   5 = V
#   3 = III
#   Result: L + V + III = LVIII
#
#   num = 1994
#   1000 = M
#   900 = CM (tidak DCCCC)
#   90 = XC (tidak LXXXX)
#   4 = IV (tidak IIII)
#   Result: M + CM + XC + IV = MCMXCIV
#
# ═════════════════════════════════════════════════════════════════

# 🔢 PENJELASAN STRATEGI (CARA KERJA)
# ═════════════════════════════════════════════════════════════════
#
# Strategi: GREEDY + MAPPING
#
# Greedy = Selalu ambil nilai TERBESAR dulu
#
# Logika:
# 1. Buat list berisi [nilai, simbol] dari BESAR ke KECIL
#    - Termasuk subtractive forms (IV, IX, XL, dll)
#    - Contoh: [1000,"M"], [900,"CM"], [500,"D"], [400,"CD"], ...
#
# 2. Loop melalui list dari besar ke kecil
#    - Cek apakah num >= nilai saat ini?
#    - Jika YES: tambah simbol ke result, kurangi num
#    - Jika NO: cek nilai berikutnya
#
# 3. Ulangi sampai num habis (num == 0)
#
# Contoh trace:
#   num = 58
#
#   Step 1: 58 >= 50? YES!
#   → Tambah "L", num = 58 - 50 = 8, result = "L"
#
#   Step 2: 8 >= 50? NO
#   → Cek nilai berikutnya (40)
#
#   Step 3: 8 >= 40? NO
#   → Cek nilai berikutnya (10)
#
#   Step 4: 8 >= 10? NO
#   → Cek nilai berikutnya (9)
#
#   Step 5: 8 >= 9? NO
#   → Cek nilai berikutnya (5)
#
#   Step 6: 8 >= 5? YES!
#   → Tambah "V", num = 8 - 5 = 3, result = "LV"
#
#   Step 7: 3 >= 5? NO
#   → Cek nilai berikutnya (4)
#
#   Step 8: 3 >= 4? NO
#   → Cek nilai berikutnya (1)
#
#   Step 9: 3 >= 1? YES!
#   → Tambah "I", num = 3 - 1 = 2, result = "LVI"
#
#   Step 10: 2 >= 1? YES!
#   → Tambah "I", num = 2 - 1 = 1, result = "LVII"
#
#   Step 11: 1 >= 1? YES!
#   → Tambah "I", num = 1 - 1 = 0, result = "LVIII"
#
#   num == 0? YES! Return "LVIII"
#
# ═════════════════════════════════════════════════════════════════


class Solution(object):
    def intToRoman(self, num):
        # Input:
        #   num = integer (1 sampai 3999)
        # Output:
        #   Roman numeral sebagai string
        
        # ═══════════════════════════════════════════════════════════
        # STEP 1: Buat mapping nilai dan simbol
        # ═══════════════════════════════════════════════════════════
        #
        # List berisi tuple (nilai, simbol)
        # Urutan: BESAR ke KECIL
        # PENTING: Termasuk subtractive forms (IV, IX, XL, dll)
        #
        # Kenapa subtractive forms diperlukan?
        # → Agar tidak perlu loop berkali-kali
        # → Contoh: 900 = CM langsung, bukan C+C+C+C+D+C
        #
        # Mapping lengkap:
        #   1000 = M
        #   900 = CM (1000-100)
        #   500 = D
        #   400 = CD (500-100)
        #   100 = C
        #   90 = XC (100-10)
        #   50 = L
        #   40 = XL (50-10)
        #   10 = X
        #   9 = IX (10-1)
        #   5 = V
        #   4 = IV (5-1)
        #   1 = I
        #
        values = [
            (1000, "M"),
            (900, "CM"),
            (500, "D"),
            (400, "CD"),
            (100, "C"),
            (90, "XC"),
            (50, "L"),
            (40, "XL"),
            (10, "X"),
            (9, "IX"),
            (5, "V"),
            (4, "IV"),
            (1, "I")
        ]
        
        # ═══════════════════════════════════════════════════════════
        # STEP 2: Inisialisasi result string
        # ═══════════════════════════════════════════════════════════
        #
        # result = string yang akan diisi simbol-simbol
        # Mulai kosong, nanti akan ditambahi
        #
        result = ""
        
        # ═══════════════════════════════════════════════════════════
        # STEP 3: Loop melalui mapping (greedy approach)
        # ═══════════════════════════════════════════════════════════
        #
        for value, symbol in values:
            # ═════════════════════════════════════════════════════
            # STEP 3A: Cek apakah num >= value saat ini?
            # ═════════════════════════════════════════════════════
            #
            # Jika YES, berarti simbol ini bisa digunakan
            # Mungkin berkali-kali!
            # Contoh: 300 = CCC (100+100+100)
            #
            while num >= value:
                # ═════════════════════════════════════════════════
                # STEP 3B: Tambah simbol ke result
                # ═════════════════════════════════════════════════
                #
                # result += symbol
                # Artinya: gabung symbol ke result
                # Contoh: "L" + "V" = "LV"
                #
                result += symbol
                
                # ═════════════════════════════════════════════════
                # STEP 3C: Kurangi num dengan value yang baru saja dipakai
                # ═════════════════════════════════════════════════
                #
                # num -= value
                # Artinya: sisa yang perlu dikonversi berkurang
                # Contoh: 58 - 50 = 8 (masih ada 8 yang perlu dikonversi)
                #
                num -= value
        
        # ═══════════════════════════════════════════════════════════
        # STEP 4: Return result
        # ═══════════════════════════════════════════════════════════
        #
        # Loop sudah selesai, result sudah lengkap
        #
        return result


# ═══════════════════════════════════════════════════════════════
# TEST CASES (JALANKAN DAN LIHAT OUTPUT)
# ═══════════════════════════════════════════════════════════════

print("=" * 80)
print("TESTING Q9: Integer to Roman")
print("=" * 80 + "\n")

sol = Solution()

# TEST 1: num = 58
# ═══════════════════════════════════════════════════════════════
print("TEST 1: num = 58")
print("-" * 80)
print("PENJELASAN:")
print("  58 = 50 + 5 + 3")
print("  50 = L")
print("  5 = V")
print("  3 = I + I + I = III")
print("  Result: L + V + III = LVIII")
print()
print("TRACE GREEDY ALGORITHM:")
print()

num = 58
values = [
    (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
    (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
    (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")
]
result = ""
step = 1

for value, symbol in values:
    while num >= value:
        result += symbol
        num -= value
        
        print(f"  Step {step}: {num+value} >= {value}? YES")
        print(f"    Tambah '{symbol}', result = '{result}'")
        print(f"    num = {num}")
        print()
        step += 1
    
    if num == 0:
        break

result_actual = sol.intToRoman(58)
print(f"HASIL: {result_actual}")
print(f"PENJELASAN: 50+5+3 = L+V+III = LVIII ✓\n")

# TEST 2: num = 3749
# ═══════════════════════════════════════════════════════════════
print("TEST 2: num = 3749")
print("-" * 80)
print("PENJELASAN:")
print("  3749 = 3000 + 700 + 40 + 9")
print("  3000 = M + M + M = MMM (1000*3)")
print("  700 = D + C + C = DCC (500+100+100)")
print("  40 = XL (50-10)")
print("  9 = IX (10-1)")
print("  Result: MMM + DCC + XL + IX = MMMCDXLIX")
print()
print("  Note: 700 = DCC (tidak DCCCC), 40 = XL (tidak XXXX)")
print()
print("TRACE GREEDY ALGORITHM:")
print()

num = 3749
values = [
    (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
    (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
    (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")
]
result = ""
step = 1

for value, symbol in values:
    count = 0
    while num >= value:
        result += symbol
        num -= value
        count += 1
    
    if count > 0:
        print(f"  Step {step}: Simbol '{symbol}' (value={value}) digunakan {count}x")
        print(f"    result = '{result}'")
        print(f"    num sisa = {num}")
        print()
        step += 1
    
    if num == 0:
        break

result_actual = sol.intToRoman(3749)
print(f"HASIL: {result_actual}")
print(f"PENJELASAN: 3000+700+40+9 = MMM+DCC+XL+IX = MMMCDXLIX ✓\n")

# TEST 3: num = 1994
# ═══════════════════════════════════════════════════════════════
print("TEST 3: num = 1994")
print("-" * 80)
print("PENJELASAN:")
print("  1994 = 1000 + 900 + 90 + 4")
print("  1000 = M")
print("  900 = CM (1000-100, subtractive form)")
print("  90 = XC (100-10, subtractive form)")
print("  4 = IV (5-1, subtractive form)")
print("  Result: M + CM + XC + IV = MCMXCIV")
print()
print("  Note: Subtractive forms membuat lebih efisien!")
print()
print("TRACE GREEDY ALGORITHM:")
print()

num = 1994
values = [
    (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
    (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
    (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")
]
result = ""
step = 1

for value, symbol in values:
    count = 0
    while num >= value:
        result += symbol
        num -= value
        count += 1
    
    if count > 0:
        print(f"  Step {step}: Simbol '{symbol}' (value={value}) digunakan {count}x")
        print(f"    result = '{result}'")
        print(f"    num sisa = {num}")
        print()
        step += 1
    
    if num == 0:
        break

result_actual = sol.intToRoman(1994)
print(f"HASIL: {result_actual}")
print(f"PENJELASAN: 1000+900+90+4 = M+CM+XC+IV = MCMXCIV ✓\n")

# TEST 4: num = 9 (Subtractive form test)
# ═══════════════════════════════════════════════════════════════
print("TEST 4: num = 9 (Subtractive form)")
print("-" * 80)
print("PENJELASAN:")
print("  num = 9")
print("  9 = IX (10-1, subtractive form)")
print("  BUKAN: VIIII (5+1+1+1+1, salah!)")
print()
print("TRACE:")
print()

num = 9
values = [
    (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
    (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
    (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")
]
result = ""

for value, symbol in values:
    if num >= value:
        print(f"  {num} >= {value}? YES")
        print(f"  Simbol '{symbol}' digunakan")
        result += symbol
        num -= value
        print(f"  result = '{result}'")
        break
    else:
        print(f"  {num} >= {value}? NO, lanjut")

result_actual = sol.intToRoman(9)
print(f"\nHASIL: {result_actual}")
print(f"PENJELASAN: 9 = IX (bukan VIIII) ✓\n")

# TEST 5: num = 3 (Simple case)
# ═══════════════════════════════════════════════════════════════
print("TEST 5: num = 3 (Simple case)")
print("-" * 80)
print("PENJELASAN:")
print("  num = 3")
print("  3 = I + I + I = III")
print()
print("TRACE:")
print()

num = 3
values = [
    (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
    (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
    (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")
]
result = ""
step = 1

for value, symbol in values:
    count = 0
    while num >= value:
        result += symbol
        num -= value
        count += 1
        step += 1
    
    if count > 0:
        print(f"  Step 1-{count}: Simbol '{symbol}' digunakan {count}x")
        print(f"    result = '{result}'")
        print()

result_actual = sol.intToRoman(3)
print(f"HASIL: {result_actual}")
print(f"PENJELASAN: 3 = III ✓\n")
