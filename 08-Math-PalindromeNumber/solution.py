# ═══════════════════════════════════════════════════════════════
# Q8. PALINDROME NUMBER
# ═══════════════════════════════════════════════════════════════

# 📖 PENJELASAN SOAL (UNTUK PEMULA)
# ═════════════════════════════════════════════════════════════════
#
# Apa itu Palindrome Number?
# → Angka yang dibaca sama dari depan dan belakang
# → Contoh: 121 → 121 (sama dari depan belakang)
#
# Diberikan integer x, cek apakah x adalah palindrome
# - Return True jika palindrome
# - Return False jika bukan
#
# Penting:
#   - Angka negatif TIDAK PERNAH palindrome (ada minus di depan)
#   - Angka diakhiri 0 (kecuali 0 sendiri) TIDAK palindrome
#   - Contoh: 10 dibaca 01 dari belakang (beda)
#
# Contoh mudah:
#   x = 121
#   → Dari kiri: 121
#   → Dari kanan: 121
#   → Sama! Return True
#
#   x = -121
#   → Ada minus di depan
#   → Tidak bisa sama
#   → Return False
#
#   x = 10
#   → Dari kiri: 10
#   → Dari kanan: 01 (tanpa leading 0 = 1)
#   → Beda! Return False
#
#   x = 0
#   → Palindrome (angka tunggal)
#   → Return True
#
# ═════════════════════════════════════════════════════════════════

# 🔢 PENJELASAN STRATEGI (CARA KERJA)
# ═════════════════════════════════════════════════════════════════
#
# Strategi: REVERSE NUMBER SECARA MATHEMATICAL
#
# Tidak gunakan string! Gunakan modulo dan division
#
# Logika:
# 1. Handle edge cases:
#    - Jika x < 0 (negatif), return False
#    - Jika x > 0 dan x % 10 == 0 (berakhir 0), return False
#      Exception: x == 0 adalah palindrome
#
# 2. Reverse angka x menggunakan loop:
#    - Ambil digit terakhir: digit = x % 10
#    - Tambah ke reversed: reversed = reversed * 10 + digit
#    - Hapus digit terakhir dari x: x = x // 10
#    - Loop sampai x habis
#
# 3. Cek apakah reversed == original
#
# Contoh trace:
#   x = 121, original = 121
#
#   Step 1: digit = 121 % 10 = 1
#           reversed = 0 * 10 + 1 = 1
#           x = 121 // 10 = 12
#
#   Step 2: digit = 12 % 10 = 2
#           reversed = 1 * 10 + 2 = 12
#           x = 12 // 10 = 1
#
#   Step 3: digit = 1 % 10 = 1
#           reversed = 12 * 10 + 1 = 121
#           x = 1 // 10 = 0
#
#   Loop selesai (x == 0)
#   reversed (121) == original (121)? YES! Return True
#
# Contoh 2:
#   x = -121, original = -121
#
#   x < 0? YES! Return False (langsung)
#
# ═════════════════════════════════════════════════════════════════


class Solution(object):
    def isPalindrome(self, x):
        # Input:
        #   x = integer (bisa negatif atau positif)
        # Output:
        #   True jika palindrome, False jika tidak
        
        # ═══════════════════════════════════════════════════════════
        # STEP 1: Handle edge cases
        # ═══════════════════════════════════════════════════════════
        #
        # Edge case 1: Negatif
        # Jika x < 0 (negatif), pasti bukan palindrome
        # Kenapa? Karena ada tanda "-" di depan
        # Dari belakang tidak ada "-"
        # Contoh: -121 ≠ 121-
        #
        if x < 0:
            return False
        
        # Edge case 2: Berakhir dengan 0 (kecuali 0 sendiri)
        # Jika x > 0 dan x % 10 == 0, berarti berakhir 0
        # Tapi dari belakang akan leading 0 (tidak valid)
        # Contoh: 10 dibaca 01 = 1 (beda)
        #
        # Kecuali x == 0, yang adalah palindrome
        #
        if x > 0 and x % 10 == 0:
            return False
        
        # ═══════════════════════════════════════════════════════════
        # STEP 2: Save original value
        # ═══════════════════════════════════════════════════════════
        #
        # original = angka asli yang akan dibandingkan nanti
        #
        original = x
        
        # ═══════════════════════════════════════════════════════════
        # STEP 3: Reverse angka x secara mathematical
        # ═══════════════════════════════════════════════════════════
        #
        # reversed = angka yang di-reverse
        # Mulai dari 0
        #
        reversed_num = 0
        
        # ═════════════════════════════════════════════════════════
        # STEP 3A: Loop ambil digit dari belakang (dari kanan)
        # ═════════════════════════════════════════════════════════
        #
        # Loop sampai x tidak ada digit lagi (x == 0)
        #
        while x > 0:
            # ═════════════════════════════════════════════════════
            # STEP 3B: Ambil digit terakhir dari x
            # ═════════════════════════════════════════════════════
            #
            # digit = x % 10
            # Modulo 10 mengambil sisa bagi 10
            # Sisa bagi 10 = digit terakhir
            #
            # Contoh:
            # x = 121, digit = 121 % 10 = 1 (digit terakhir)
            # x = 12, digit = 12 % 10 = 2 (digit terakhir)
            # x = 1, digit = 1 % 10 = 1 (digit terakhir)
            #
            digit = x % 10
            
            # ═════════════════════════════════════════════════════
            # STEP 3C: Tambah digit ke reversed (build dari belakang)
            # ═════════════════════════════════════════════════════
            #
            # reversed_num = reversed_num * 10 + digit
            #
            # *10 untuk shift posisi digit (geser ke kiri)
            # +digit untuk tambah digit baru di posisi terakhir
            #
            # Contoh:
            # reversed_num = 0
            # digit = 1 (dari x=121)
            # reversed_num = 0 * 10 + 1 = 0 + 1 = 1
            #
            # reversed_num = 1
            # digit = 2 (dari x=12)
            # reversed_num = 1 * 10 + 2 = 10 + 2 = 12
            #
            # reversed_num = 12
            # digit = 1 (dari x=1)
            # reversed_num = 12 * 10 + 1 = 120 + 1 = 121
            #
            reversed_num = reversed_num * 10 + digit
            
            # ═════════════════════════════════════════════════════
            # STEP 3D: Hapus digit terakhir dari x
            # ═════════════════════════════════════════════════════
            #
            # x = x // 10
            # // adalah integer division (bagi tanpa desimal)
            # Ini hapus digit terakhir
            #
            # Contoh:
            # x = 121, x // 10 = 12 (hilang angka 1)
            # x = 12, x // 10 = 1 (hilang angka 2)
            # x = 1, x // 10 = 0 (hilang angka 1, habis)
            #
            x = x // 10
        
        # ═══════════════════════════════════════════════════════════
        # STEP 4: Cek apakah reversed == original
        # ═══════════════════════════════════════════════════════════
        #
        # Jika angka original sama dengan angka yang di-reverse
        # Berarti palindrome!
        #
        # Contoh:
        # original = 121, reversed_num = 121
        # 121 == 121? YES! Return True
        #
        # Contoh 2:
        # original = 123, reversed_num = 321
        # 123 == 321? NO! Return False
        #
        return original == reversed_num


# ═══════════════════════════════════════════════════════════════
# TEST CASES (JALANKAN DAN LIHAT OUTPUT)
# ═══════════════════════════════════════════════════════════════

print("=" * 80)
print("TESTING Q8: Palindrome Number")
print("=" * 80 + "\n")

sol = Solution()

# TEST 1: x = 121
# ═══════════════════════════════════════════════════════════════
print("TEST 1: x = 121")
print("-" * 80)
print("PENJELASAN:")
print("  x = 121")
print("  Dari kiri: 121")
print("  Dari kanan: 121 (dibalik)")
print("  Sama? YES! Palindrome!")
print()
print("TRACE REVERSE NUMBER:")
print()

x = 121
original = x
reversed_num = 0
step = 1

print(f"  original = {original}")
print(f"  Mulai reverse:")
print()

while x > 0:
    digit = x % 10
    reversed_num = reversed_num * 10 + digit
    
    print(f"  Step {step}:")
    print(f"    digit = {x} % 10 = {digit}")
    print(f"    reversed_num = reversed * 10 + digit = {reversed_num}")
    x = x // 10
    print(f"    x = x // 10 = {x}")
    print()
    step += 1

print(f"  reversed_num = {reversed_num}")
print(f"  original ({original}) == reversed ({reversed_num})? {original == reversed_num}")
print()

result = sol.isPalindrome(121)
print(f"HASIL: {result}")
print(f"PENJELASAN: 121 adalah palindrome ✓\n")

# TEST 2: x = -121
# ═══════════════════════════════════════════════════════════════
print("TEST 2: x = -121")
print("-" * 80)
print("PENJELASAN:")
print("  x = -121")
print("  x < 0? YES (negatif)")
print("  Angka negatif tidak bisa palindrome (ada minus di depan)")
print()
print("TRACE:")
print()

x = -121
print(f"  x = {x}")
print(f"  x < 0? {x < 0} → Return False (langsung!)")
print()

result = sol.isPalindrome(-121)
print(f"HASIL: {result}")
print(f"PENJELASAN: Negatif tidak palindrome ✓\n")

# TEST 3: x = 10
# ═══════════════════════════════════════════════════════════════
print("TEST 3: x = 10")
print("-" * 80)
print("PENJELASAN:")
print("  x = 10")
print("  x > 0 dan x % 10 == 0? YES (berakhir 0)")
print("  Angka berakhir 0 tidak bisa palindrome (leading 0 di belakang)")
print("  Contoh: 10 dibaca 01 dari belakang = 1 (beda)")
print()
print("TRACE:")
print()

x = 10
print(f"  x = {x}")
print(f"  x > 0? {x > 0}")
print(f"  x % 10 = {x % 10}")
print(f"  x > 0 and x % 10 == 0? True → Return False (langsung!)")
print()

result = sol.isPalindrome(10)
print(f"HASIL: {result}")
print(f"PENJELASAN: Berakhir 0 tidak palindrome ✓\n")

# TEST 4: x = 0
# ═══════════════════════════════════════════════════════════════
print("TEST 4: x = 0")
print("-" * 80)
print("PENJELASAN:")
print("  x = 0")
print("  Angka tunggal")
print("  Dibaca sama dari depan dan belakang")
print()
print("TRACE REVERSE NUMBER:")
print()

x = 0
original = x
reversed_num = 0
step = 1

print(f"  original = {original}")
print(f"  x > 0? {x > 0} → Loop tidak jalan (x sudah 0)")
print(f"  reversed_num tetap = 0")
print()
print(f"  original ({original}) == reversed ({reversed_num})? {original == reversed_num}")
print()

result = sol.isPalindrome(0)
print(f"HASIL: {result}")
print(f"PENJELASAN: 0 adalah palindrome ✓\n")

# TEST 5: x = 12321
# ═══════════════════════════════════════════════════════════════
print("TEST 5: x = 12321")
print("-" * 80)
print("PENJELASAN:")
print("  x = 12321")
print("  Dari kiri: 12321")
print("  Dari kanan: 12321 (dibalik)")
print("  Sama? YES! Palindrome!")
print()
print("TRACE REVERSE NUMBER:")
print()

x = 12321
original = x
reversed_num = 0
step = 1

print(f"  original = {original}")
print(f"  Mulai reverse:")
print()

while x > 0:
    digit = x % 10
    reversed_num = reversed_num * 10 + digit
    
    print(f"  Step {step}:")
    print(f"    digit = {x} % 10 = {digit}")
    print(f"    reversed_num = {reversed_num}")
    x = x // 10
    print(f"    x = {x}")
    print()
    step += 1

print(f"  reversed_num = {reversed_num}")
print(f"  original ({original}) == reversed ({reversed_num})? {original == reversed_num}")
print()

result = sol.isPalindrome(12321)
print(f"HASIL: {result}")
print(f"PENJELASAN: 12321 adalah palindrome ✓\n")

# TEST 6: x = 123
# ═══════════════════════════════════════════════════════════════
print("TEST 6: x = 123")
print("-" * 80)
print("PENJELASAN:")
print("  x = 123")
print("  Dari kiri: 123")
print("  Dari kanan: 321 (dibalik)")
print("  Sama? NO! Bukan palindrome")
print()
print("TRACE REVERSE NUMBER:")
print()

x = 123
original = x
reversed_num = 0
step = 1

print(f"  original = {original}")
print(f"  Mulai reverse:")
print()

while x > 0:
    digit = x % 10
    reversed_num = reversed_num * 10 + digit
    
    print(f"  Step {step}:")
    print(f"    digit = {x} % 10 = {digit}")
    print(f"    reversed_num = {reversed_num}")
    x = x // 10
    print(f"    x = {x}")
    print()
    step += 1

print(f"  reversed_num = {reversed_num}")
print(f"  original ({original}) == reversed ({reversed_num})? {original == reversed_num}")
print()

result = sol.isPalindrome(123)
print(f"HASIL: {result}")
print(f"PENJELASAN: 123 bukan palindrome ✓\n")
