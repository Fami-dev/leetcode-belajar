# ═══════════════════════════════════════════════════════════════
# Q10. ROMAN TO INTEGER (Kebalikan Q9!)
# ═══════════════════════════════════════════════════════════════

# 📖 PENJELASAN SOAL (UNTUK PEMULA)
# ═════════════════════════════════════════════════════════════════
#
# Apa itu Roman to Integer?
# → Kebalikan dari Q9! Konversi Roman numerals (I, II, III...) ke desimal (1, 2, 3...)
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
# Aturan membaca Roman:
# 1. Biasanya dari kiri ke kanan, symbol besar dulu
#    Contoh: LV = 50 + 5 = 55
#
# 2. SUBTRACTIVE FORM (pengurangan):
#    - Jika symbol KECIL ada sebelum symbol BESAR
#    - Berarti dikurangi!
#    - IV = 5 - 1 = 4 (bukan 1+5 = 6)
#    - IX = 10 - 1 = 9 (bukan 1+10 = 11)
#    - XL = 50 - 10 = 40
#    - XC = 100 - 10 = 90
#    - CD = 500 - 100 = 400
#    - CM = 1000 - 100 = 900
#
# Contoh mudah:
#   s = "LVIII"
#   L = 50
#   V = 5
#   I = 1, I = 1, I = 1
#   Total: 50 + 5 + 1 + 1 + 1 = 58
#
#   s = "MCMXCIV"
#   M = 1000
#   CM = 900 (C < M, so -100 then +1000 = 900)
#   XC = 90 (X < C, so -10 then +100 = 90)
#   IV = 4 (I < V, so -1 then +5 = 4)
#   Total: 1000 + 900 + 90 + 4 = 1994
#
# ═════════════════════════════════════════════════════════════════

# 🔢 PENJELASAN STRATEGI (CARA KERJA)
# ═════════════════════════════════════════════════════════════════
#
# Strategi: MAPPING + LEFT-TO-RIGHT ITERATION
#
# Logika:
# 1. Buat mapping roman -> value
#    Contoh: {"I": 1, "V": 5, "X": 10, ...}
#
# 2. Loop dari kiri ke kanan (i = 0 sampai len(s)-1)
#    - Ambil nilai symbol saat ini: current = mapping[s[i]]
#    - Cek apakah ada symbol berikutnya: i+1 < len(s)?
#      - Jika YES, ambil nilai symbol berikutnya: next_val = mapping[s[i+1]]
#      - Jika current < next_val:
#        → Ini subtractive form! Kurangi: result -= current
#      - Jika current >= next_val:
#        → Tambah: result += current
#      - Jika NO (tidak ada berikutnya):
#        → Tambah: result += current
#
# 3. Return result
#
# Contoh trace:
#   s = "MCMXCIV"
#
#   i=0: s[0]='M', current=1000, s[1]='C', next=100
#   1000 >= 100? YES, add 1000
#   result = 1000
#
#   i=1: s[1]='C', current=100, s[2]='M', next=1000
#   100 < 1000? YES, subtract 100 (subtractive form!)
#   result = 1000 - 100 = 900
#
#   i=2: s[2]='M', current=1000, s[3]='X', next=10
#   1000 >= 10? YES, add 1000
#   result = 900 + 1000 = 1900
#
#   i=3: s[3]='X', current=10, s[4]='C', next=100
#   10 < 100? YES, subtract 10 (subtractive form!)
#   result = 1900 - 10 = 1890
#
#   i=4: s[4]='C', current=100, s[5]='I', next=1
#   100 >= 1? YES, add 100
#   result = 1890 + 100 = 1990
#
#   i=5: s[5]='I', current=1, s[6]='V', next=5
#   1 < 5? YES, subtract 1 (subtractive form!)
#   result = 1990 - 1 = 1989
#
#   i=6: s[6]='V', current=5, i+1=7 >= len=7? NO
#   No next, add 5
#   result = 1989 + 5 = 1994
#
#   Return 1994 ✓
#
# ═════════════════════════════════════════════════════════════════


class Solution(object):
    def romanToInt(self, s):
        # Input:
        #   s = Roman numeral string
        # Output:
        #   integer value
        
        # ═══════════════════════════════════════════════════════════
        # STEP 1: Buat mapping roman symbol ke nilai
        # ═══════════════════════════════════════════════════════════
        #
        # Dictionary berisi symbol : value
        #
        # Mapping:
        #   I = 1
        #   V = 5
        #   X = 10
        #   L = 50
        #   C = 100
        #   D = 500
        #   M = 1000
        #
        roman_map = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        
        # ═══════════════════════════════════════════════════════════
        # STEP 2: Inisialisasi result
        # ═══════════════════════════════════════════════════════════
        #
        # result = total value yang akan diakumulasi
        #
        result = 0
        
        # ═══════════════════════════════════════════════════════════
        # STEP 3: Loop melalui string dari kiri ke kanan
        # ═══════════════════════════════════════════════════════════
        #
        for i in range(len(s)):
            # ═════════════════════════════════════════════════════
            # STEP 3A: Ambil nilai symbol saat ini
            # ═════════════════════════════════════════════════════
            #
            # current = roman_map[s[i]]
            # Cari nilai dari symbol yang sekarang
            #
            # Contoh:
            # s = "MCMXCIV", i = 0
            # s[0] = 'M', current = 1000
            #
            current = roman_map[s[i]]
            
            # ═════════════════════════════════════════════════════
            # STEP 3B: Cek apakah ada symbol berikutnya?
            # ═════════════════════════════════════════════════════
            #
            # Kondisi: i + 1 < len(s)
            # Artinya: index berikutnya masih dalam batas string
            #
            # Contoh:
            # i = 0, len(s) = 7
            # 0 + 1 = 1 < 7? YES, ada berikutnya
            #
            if i + 1 < len(s):
                # ═════════════════════════════════════════════════
                # STEP 3C: Ambil nilai symbol berikutnya
                # ═════════════════════════════════════════════════
                #
                next_val = roman_map[s[i + 1]]
                
                # ═════════════════════════════════════════════════
                # STEP 3D: Cek apakah ini SUBTRACTIVE form
                # ═════════════════════════════════════════════════
                #
                # Subtractive form = current < next
                # Artinya symbol kecil sebelum symbol besar
                # Contoh: IV (1 < 5), IX (1 < 10), XL (10 < 50)
                #
                # Jika YES, kurangi: result -= current
                # Jika NO, tambah: result += current
                #
                # Contoh:
                # i=1: s[1]='C', current=100, s[2]='M', next=1000
                # 100 < 1000? YES, subtractive!
                # result -= 100 (nanti M akan di-add untuk dapat 900)
                #
                if current < next_val:
                    result -= current
                else:
                    result += current
            else:
                # ═════════════════════════════════════════════════
                # STEP 3E: Jika tidak ada symbol berikutnya
                # ═════════════════════════════════════════════════
                #
                # Berarti ini symbol terakhir
                # Selalu tambah nilainya
                #
                # Contoh:
                # i=6 (terakhir): s[6]='V'
                # Tidak ada s[7], tambah 5
                #
                result += current
        
        # ═══════════════════════════════════════════════════════════
        # STEP 4: Return result
        # ═══════════════════════════════════════════════════════════
        #
        return result


# ═══════════════════════════════════════════════════════════════
# TEST CASES (JALANKAN DAN LIHAT OUTPUT)
# ═══════════════════════════════════════════════════════════════

print("=" * 80)
print("TESTING Q10: Roman to Integer")
print("=" * 80 + "\n")

sol = Solution()

# TEST 1: s = "LVIII"
# ═══════════════════════════════════════════════════════════════
print("TEST 1: s = 'LVIII'")
print("-" * 80)
print("PENJELASAN:")
print("  L = 50")
print("  V = 5")
print("  I = 1, I = 1, I = 1")
print("  Total: 50 + 5 + 1 + 1 + 1 = 58")
print()
print("TRACE LEFT-TO-RIGHT:")
print()

s = "LVIII"
roman_map = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
result = 0

for i in range(len(s)):
    current = roman_map[s[i]]
    
    print(f"  i={i}: s[{i}]='{s[i]}', value={current}")
    
    if i + 1 < len(s):
        next_val = roman_map[s[i + 1]]
        print(f"        Next: s[{i+1}]='{s[i+1]}', value={next_val}")
        
        if current < next_val:
            print(f"        {current} < {next_val}? YES (subtractive)")
            print(f"        result -= {current}")
            result -= current
        else:
            print(f"        {current} >= {next_val}? YES (add)")
            print(f"        result += {current}")
            result += current
    else:
        print(f"        No next, add {current}")
        print(f"        result += {current}")
        result += current
    
    print(f"        result = {result}")
    print()

result_actual = sol.romanToInt("LVIII")
print(f"HASIL: {result_actual}")
print(f"PENJELASAN: LVIII = 50+5+1+1+1 = 58 ✓\n")

# TEST 2: s = "MCMXCIV"
# ═══════════════════════════════════════════════════════════════
print("TEST 2: s = 'MCMXCIV'")
print("-" * 80)
print("PENJELASAN:")
print("  M = 1000")
print("  CM = 900 (C < M, subtractive form)")
print("  XC = 90 (X < C, subtractive form)")
print("  IV = 4 (I < V, subtractive form)")
print("  Total: 1000 + 900 + 90 + 4 = 1994")
print()
print("TRACE LEFT-TO-RIGHT:")
print()

s = "MCMXCIV"
roman_map = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
result = 0

for i in range(len(s)):
    current = roman_map[s[i]]
    
    print(f"  i={i}: s[{i}]='{s[i]}', value={current}")
    
    if i + 1 < len(s):
        next_val = roman_map[s[i + 1]]
        print(f"        Next: s[{i+1}]='{s[i+1]}', value={next_val}")
        
        if current < next_val:
            print(f"        {current} < {next_val}? YES (subtractive!)")
            print(f"        result -= {current}")
            result -= current
        else:
            print(f"        {current} >= {next_val}? YES (add)")
            print(f"        result += {current}")
            result += current
    else:
        print(f"        No next, add {current}")
        print(f"        result += {current}")
        result += current
    
    print(f"        result = {result}")
    print()

result_actual = sol.romanToInt("MCMXCIV")
print(f"HASIL: {result_actual}")
print(f"PENJELASAN: MCMXCIV = 1000+900+90+4 = 1994 ✓\n")

# TEST 3: s = "IX"
# ═══════════════════════════════════════════════════════════════
print("TEST 3: s = 'IX' (Subtractive form)")
print("-" * 80)
print("PENJELASAN:")
print("  I = 1")
print("  X = 10")
print("  I < X? YES (subtractive form!)")
print("  IX = 10 - 1 = 9")
print()
print("TRACE:")
print()

s = "IX"
roman_map = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
result = 0

for i in range(len(s)):
    current = roman_map[s[i]]
    print(f"  i={i}: s[{i}]='{s[i]}', value={current}")
    
    if i + 1 < len(s):
        next_val = roman_map[s[i + 1]]
        print(f"        Next: s[{i+1}]='{s[i+1]}', value={next_val}")
        
        if current < next_val:
            print(f"        {current} < {next_val}? YES (subtractive!)")
            print(f"        result -= {current} = {result - current}")
            result -= current
        else:
            result += current
    else:
        print(f"        No next, add {current}")
        result += current
    
    print(f"        result = {result}")
    print()

result_actual = sol.romanToInt("IX")
print(f"HASIL: {result_actual}")
print(f"PENJELASAN: IX = 10-1 = 9 ✓\n")

# TEST 4: s = "III"
# ═══════════════════════════════════════════════════════════════
print("TEST 4: s = 'III' (Simple case)")
print("-" * 80)
print("PENJELASAN:")
print("  I = 1, I = 1, I = 1")
print("  Total: 1 + 1 + 1 = 3")
print()
print("TRACE:")
print()

s = "III"
roman_map = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
result = 0

for i in range(len(s)):
    current = roman_map[s[i]]
    print(f"  i={i}: s[{i}]='{s[i]}', value={current}")
    
    if i + 1 < len(s):
        next_val = roman_map[s[i + 1]]
        print(f"        Next: s[{i+1}]='{s[i+1]}', value={next_val}")
        
        if current < next_val:
            print(f"        {current} < {next_val}? subtractive")
            result -= current
        else:
            print(f"        {current} >= {next_val}? add")
            result += current
    else:
        print(f"        No next, add {current}")
        result += current
    
    print(f"        result = {result}")
    print()

result_actual = sol.romanToInt("III")
print(f"HASIL: {result_actual}")
print(f"PENJELASAN: III = 1+1+1 = 3 ✓\n")

# TEST 5: s = "XXVII"
# ═══════════════════════════════════════════════════════════════
print("TEST 5: s = 'XXVII'")
print("-" * 80)
print("PENJELASAN:")
print("  X = 10, X = 10, V = 5, I = 1, I = 1")
print("  Total: 10 + 10 + 5 + 1 + 1 = 27")
print()
print("TRACE:")
print()

s = "XXVII"
roman_map = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
result = 0

for i in range(len(s)):
    current = roman_map[s[i]]
    print(f"  i={i}: s[{i}]='{s[i]}', value={current}")
    
    if i + 1 < len(s):
        next_val = roman_map[s[i + 1]]
        print(f"        Next: s[{i+1}]='{s[i+1]}', value={next_val}")
        
        if current < next_val:
            result -= current
        else:
            print(f"        {current} >= {next_val}? add")
            result += current
    else:
        print(f"        No next, add {current}")
        result += current
    
    print(f"        result = {result}")
    print()

result_actual = sol.romanToInt("XXVII")
print(f"HASIL: {result_actual}")
print(f"PENJELASAN: XXVII = 10+10+5+1+1 = 27 ✓\n")
