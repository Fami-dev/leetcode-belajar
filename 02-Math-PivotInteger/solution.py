# ═══════════════════════════════════════════════════════════════
# Q2. FIND THE PIVOT INTEGER
# ═══════════════════════════════════════════════════════════════

# 📖 PENJELASAN SOAL (UNTUK PEMULA)
# ═════════════════════════════════════════════════════════════════
#
# Apa itu Pivot Integer?
# → Angka x dimana: Jumlah(1 sampai x) = Jumlah(x sampai n)
# 
# Contoh mudah:
#   n = 8, cari x?
#   → Jumlah(1 sampai x) = Jumlah(x sampai 8)
#   → Kalau x=6: Jumlah(1-6)=21, Jumlah(6-8)=21 ✓ SAMA!
#   → Jawab: x = 6
#
#   n = 1, cari x?
#   → x=1: Jumlah(1-1)=1, Jumlah(1-1)=1 ✓ SAMA!
#   → Jawab: x = 1
#
#   n = 4, cari x?
#   → Tidak ada x yang memenuhi syarat
#   → Jawab: -1 (tidak ada)
#
# TASK:
# Diberikan n, cari angka x yang memenuhi syarat
# Jika tidak ada, return -1
#
# ═════════════════════════════════════════════════════════════════

# 🔢 PENJELASAN RUMUS (PENTING!)
# ═════════════════════════════════════════════════════════════════
#
# RUMUS 1: Jumlah dari 1 sampai k
# ════════════════════════════════
# Formula: k * (k + 1) / 2
#
# Cara kerja:
#   Jumlah(1 sampai 1) = 1 * 2 / 2 = 1
#   Jumlah(1 sampai 2) = 2 * 3 / 2 = 3 (yaitu 1+2)
#   Jumlah(1 sampai 3) = 3 * 4 / 2 = 6 (yaitu 1+2+3)
#   Jumlah(1 sampai 4) = 4 * 5 / 2 = 10 (yaitu 1+2+3+4)
#   Jumlah(1 sampai 5) = 5 * 6 / 2 = 15 (yaitu 1+2+3+4+5)
#   Jumlah(1 sampai 6) = 6 * 7 / 2 = 21 (yaitu 1+2+3+4+5+6)
#
# ════════════════════════════════════════════════════════════════
#
# RUMUS 2: Jumlah dari x sampai n
# ════════════════════════════════
# Formula: Jumlah(1 sampai n) - Jumlah(1 sampai x-1)
#
# Contoh: Jumlah dari 6 sampai 8
#   = Jumlah(1-8) - Jumlah(1-5)
#   = 36 - 15
#   = 21 (yaitu 6+7+8)
#
# Atau menggunakan rumus:
#   Jumlah(x sampai n) = n*(n+1)/2 - (x-1)*x/2
#
# ════════════════════════════════════════════════════════════════
#
# RUMUS 3: Mencari Pivot
# ════════════════════════════════
# Kita cari x dimana:
#   Jumlah(1 sampai x) = Jumlah(x sampai n)
#
# Menggunakan rumus:
#   x*(x+1)/2 = n*(n+1)/2 - (x-1)*x/2
#
# Disederhanakan:
#   x*(x+1)/2 + (x-1)*x/2 = n*(n+1)/2
#   x*(x+1)/2 + x*(x-1)/2 = n*(n+1)/2
#   x*[(x+1) + (x-1)]/2 = n*(n+1)/2
#   x*[2x]/2 = n*(n+1)/2
#   x² = n*(n+1)/2
#   x = sqrt(n*(n+1)/2)
#
# Jadi tinggal cek: apakah hasil sqrt ini integer?
# Kalau integer, itu jawabannya!
# Kalau bukan, return -1
#
# ════════════════════════════════════════════════════════════════
#
# IMPLEMENTASI di kode:
# Kita tidak perlu rumus sqrt yang kompleks
# Cukup loop x dari 1 sampai n
# Hitung left_sum dan right_sum
# Kalau sama, ketemu pivot!
#
# ═════════════════════════════════════════════════════════════════


class Solution(object):
    def pivotInteger(self, n):
        # Input: n = angka (positif)
        # Output: x (angka pivot) atau -1 (tidak ada)
        
        # ═══════════════════════════════════════════════════════════
        # STEP 1: Hitung TOTAL jumlah dari 1 sampai n
        # ═══════════════════════════════════════════════════════════
        # 
        # Rumus: total_sum = n * (n + 1) / 2
        # 
        # Contoh untuk n=8:
        #   total_sum = 8 * 9 / 2 = 36
        #   (yaitu jumlah 1+2+3+4+5+6+7+8 = 36)
        #
        # Kenapa rumus ini?
        # Ini adalah rumus penjumlahan deret aritmatika
        # Sudah terbukti di matematika
        # 
        # Pengecakan:
        #   n=1: 1*2/2 = 1 ✓ (1)
        #   n=2: 2*3/2 = 3 ✓ (1+2)
        #   n=3: 3*4/2 = 6 ✓ (1+2+3)
        #   n=4: 4*5/2 = 10 ✓ (1+2+3+4)
        # 
        total_sum = n * (n + 1) // 2
        
        # ═══════════════════════════════════════════════════════════
        # STEP 2: Loop untuk setiap x dari 1 sampai n
        # ═══════════════════════════════════════════════════════════
        # Coba setiap angka x untuk lihat apakah cocok
        #
        for x in range(1, n + 1):
            # x=1, 2, 3, 4, 5, ... sampai n
            
            # ═══════════════════════════════════════════════════════
            # STEP 2A: Hitung Jumlah dari 1 sampai x (LEFT SIDE)
            # ═══════════════════════════════════════════════════════
            # 
            # Rumus: left_sum = x * (x + 1) / 2
            # 
            # Ini adalah jumlah dari 1 sampai x
            # Contoh untuk x=6:
            #   left_sum = 6 * 7 / 2 = 21
            #   (yaitu jumlah 1+2+3+4+5+6 = 21)
            #
            # Contoh perhitungan step-by-step:
            # Kalau n=8 dan kita coba x=6:
            #   left_sum = 6 * 7 / 2
            #           = 42 / 2
            #           = 21
            #
            left_sum = x * (x + 1) // 2
            
            # ═══════════════════════════════════════════════════════
            # STEP 2B: Hitung Jumlah dari x sampai n (RIGHT SIDE)
            # ═══════════════════════════════════════════════════════
            # 
            # Cara: total_sum - jumlah(1 sampai x-1)
            # 
            # Rumus jumlah(1 sampai x-1) = (x-1) * x / 2
            # 
            # Contoh untuk x=6, n=8:
            #   right_sum = total_sum - (x-1)*x/2
            #            = 36 - 5*6/2
            #            = 36 - 30/2
            #            = 36 - 15
            #            = 21
            #            (yaitu jumlah 6+7+8 = 21)
            #
            # Pengecekan: 6+7+8 = 21 ✓
            #
            right_sum = total_sum - (x - 1) * x // 2
            
            # ═══════════════════════════════════════════════════════
            # STEP 3: Cek apakah left_sum == right_sum?
            # ═══════════════════════════════════════════════════════
            # 
            if left_sum == right_sum:
                # Ketemu! Angka x ini adalah pivot integer
                # Jumlah dari 1 sampai x = Jumlah dari x sampai n
                return x
        
        # ═══════════════════════════════════════════════════════════
        # STEP 4: Jika loop habis dan tidak ada yang cocok
        # ═══════════════════════════════════════════════════════════
        # Return -1 berarti tidak ada pivot integer
        #
        return -1


# ═══════════════════════════════════════════════════════════════
# TEST CASES (JALANKAN DAN LIHAT OUTPUT)
# ═══════════════════════════════════════════════════════════════

print("=" * 60)
print("TESTING Q2: Find The Pivot Integer")
print("=" * 60 + "\n")

sol = Solution()

# TEST 1: n=8 (ADA SOLUSI)
# ═══════════════════════════════════════════════════════════════
print("TEST 1: n = 8")
print("-" * 60)
print("PENJELASAN RUMUS:")
print("  Total jumlah 1-8: n*(n+1)/2 = 8*9/2 = 36")
print()
print("CARI x: Jumlah(1-x) = Jumlah(x-8)")
print()
print("TRACE untuk setiap x:")
print()

# Manual trace
for x in range(1, 9):
    left = x * (x + 1) // 2
    total = 8 * 9 // 2
    right = total - (x - 1) * x // 2
    match = "✓ COCOK!" if left == right else "✗"
    print(f"  x={x}: left={left:2d}, right={right:2d} {match}")

print()
result = sol.pivotInteger(8)
print(f"HASIL: {result}")
print("PENJELASAN: x=6 karena Jumlah(1-6)=21 dan Jumlah(6-8)=21\n")

# TEST 2: n=1 (ADA SOLUSI)
# ═══════════════════════════════════════════════════════════════
print("TEST 2: n = 1")
print("-" * 60)
print("PENJELASAN RUMUS:")
print("  Total jumlah 1-1: n*(n+1)/2 = 1*2/2 = 1")
print()
print("CARI x: Jumlah(1-x) = Jumlah(x-1)")
print()
print("TRACE untuk setiap x:")
print()

for x in range(1, 2):
    left = x * (x + 1) // 2
    total = 1 * 2 // 2
    right = total - (x - 1) * x // 2
    match = "✓ COCOK!" if left == right else "✗"
    print(f"  x={x}: left={left:2d}, right={right:2d} {match}")

print()
result = sol.pivotInteger(1)
print(f"HASIL: {result}")
print("PENJELASAN: x=1 karena Jumlah(1-1)=1 dan Jumlah(1-1)=1\n")

# TEST 3: n=4 (TIDAK ADA SOLUSI)
# ═══════════════════════════════════════════════════════════════
print("TEST 3: n = 4")
print("-" * 60)
print("PENJELASAN RUMUS:")
print("  Total jumlah 1-4: n*(n+1)/2 = 4*5/2 = 10")
print()
print("CARI x: Jumlah(1-x) = Jumlah(x-4)")
print()
print("TRACE untuk setiap x:")
print()

for x in range(1, 5):
    left = x * (x + 1) // 2
    total = 4 * 5 // 2
    right = total - (x - 1) * x // 2
    match = "✓ COCOK!" if left == right else "✗"
    print(f"  x={x}: left={left:2d}, right={right:2d} {match}")

print()
result = sol.pivotInteger(4)
print(f"HASIL: {result}")
print("PENJELASAN: Tidak ada x yang cocok, jadi return -1\n")
