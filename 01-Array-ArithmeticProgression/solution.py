# ═══════════════════════════════════════════════════════════════
# Q1. CAN MAKE ARITHMETIC PROGRESSION FROM SEQUENCE
# ═══════════════════════════════════════════════════════════════

# 📖 PENJELASAN SOAL (UNTUK PEMULA)
# ═════════════════════════════════════════════════════════════════
#
# Apa itu Arithmetic Progression?
# → Barisan angka dimana JARAK antar angka SELALU SAMA
# 
# Contoh:
#   [1, 3, 5] → Jarak 1→3 = 2, Jarak 3→5 = 2 ✓ BENAR
#   [1, 2, 4] → Jarak 1→2 = 1, Jarak 2→4 = 2 ✗ SALAH (jaraknya beda!)
# 
# TASK:
# Diberikan array, cek apakah BISA di-rearrange (diatur ulang) 
# menjadi arithmetic progression?
# 
# Jawab: True jika bisa, False jika tidak bisa
# 
# ═════════════════════════════════════════════════════════════════

# 🔢 PENJELASAN STRATEGI (CARA KERJA)
# ═════════════════════════════════════════════════════════════════
#
# Strategi 3 Langkah:
#
# LANGKAH 1: URUTKAN ARRAY
# ════════════════════════════════════════════
# Kenapa urutkan?
# → Jika barisan sudah terurut, mudah cek jaraknya
# → Jarak antar elemen berurutan akan konsisten
#
# Contoh:
#   [3, 5, 1] → diurutkan → [1, 3, 5]
#   Sekarang: 3-1=2, 5-3=2 (MUDAH DICEK!)
#
# Dibanding:
#   [3, 5, 1] tanpa urutkan
#   Cek: 5-3=2, 1-5=-4 (RIBET, JARAKNYA BEDA!)
#
# ════════════════════════════════════════════════════════════════
#
# LANGKAH 2: AMBIL JARAK ACUAN
# ════════════════════════════════════════════
# Jarak Acuan = jarak antara 2 angka PERTAMA (setelah urutkan)
#
# Rumus: jarak = arr[1] - arr[0]
#
# Contoh untuk [1, 3, 5]:
#   jarak = 3 - 1 = 2
#   Ini akan jadi "standar" untuk cek yang lain
#
# Contoh untuk [1, 2, 4]:
#   jarak = 2 - 1 = 1
#   Standar: semua jarak harus 1
#
# ════════════════════════════════════════════════════════════════
#
# LANGKAH 3: CEK SEMUA JARAK
# ════════════════════════════════════════════
# Loop untuk setiap pasang angka berturut-turut
# Hitung jaraknya
# Bandingkan dengan jarak acuan
#
# Jika ADA yang berbeda → Return False (TIDAK BISA)
# Jika SEMUA sama → Return True (BISA)
#
# Contoh [1, 3, 5]:
#   Cek 1→3: 3-1=2, sama dengan acuan (2)? IYA ✓
#   Cek 3→5: 5-3=2, sama dengan acuan (2)? IYA ✓
#   Semua sama! Return True
#
# Contoh [1, 2, 4]:
#   Cek 1→2: 2-1=1, sama dengan acuan (1)? IYA ✓
#   Cek 2→4: 4-2=2, sama dengan acuan (1)? TIDAK ✗
#   Ada yang beda! Return False
#
# ═════════════════════════════════════════════════════════════════


class Solution(object):
    def canMakeArithmeticProgression(self, arr):
        # Input: arr = list angka
        # Output: True atau False
        
        # ═══════════════════════════════════════════════════════════
        # STEP 1: Jika cuma 1 atau 2 angka, pasti bisa!
        # ═══════════════════════════════════════════════════════════
        # 
        # Alasan:
        # - 1 angka: Pola dengan 1 angka selalu arithmetic progression
        # - 2 angka: Pola dengan 2 angka selalu arithmetic progression
        #   (Ada jarak, tapi konsisten karena cuma 1 jarak)
        #
        # Contoh:
        # - [5] → Hanya 1 angka, pasti True
        # - [3, 7] → 2 angka, jarak 4, pasti True
        #
        if len(arr) <= 2:
            return True
        
        # ═══════════════════════════════════════════════════════════
        # STEP 2: Urutkan array dari kecil ke besar
        # ═══════════════════════════════════════════════════════════
        # 
        # Fungsi .sort():
        # - Mengubah array menjadi terurut (dari kecil ke besar)
        # - Bekerja IN-PLACE (mengubah array asli)
        #
        # Contoh:
        # [3, 5, 1].sort() → array menjadi [1, 3, 5]
        # [5, 5, 5].sort() → array tetap [5, 5, 5] (sudah urut)
        # [-3, 1, -1].sort() → array menjadi [-3, -1, 1]
        #
        # Kenapa perlu urutkan?
        # → Supaya bisa cek jarak antar elemen berurutan
        #
        arr.sort()
        
        # ═══════════════════════════════════════════════════════════
        # STEP 3: Hitung JARAK ACUAN (antara 2 angka pertama)
        # ═══════════════════════════════════════════════════════════
        # 
        # Rumus: jarak = arr[1] - arr[0]
        # 
        # Apa itu arr[0] dan arr[1]?
        # arr[0] = elemen PERTAMA di array (index 0)
        # arr[1] = elemen KEDUA di array (index 1)
        #
        # Contoh:
        # arr = [1, 3, 5]
        # arr[0] = 1
        # arr[1] = 3
        # jarak = 3 - 1 = 2
        #
        # arr = [5, 5, 5]
        # arr[0] = 5
        # arr[1] = 5
        # jarak = 5 - 5 = 0
        #
        jarak = arr[1] - arr[0]
        
        # ═══════════════════════════════════════════════════════════
        # STEP 4: Loop dari elemen ke-0 sampai ke-(n-1)
        # ═══════════════════════════════════════════════════════════
        # Cek apakah SEMUA jarak sama?
        #
        # range(len(arr) - 1) memberi i = 0, 1, 2, ..., n-2
        #
        # Contoh untuk arr = [1, 3, 5]:
        # len(arr) = 3
        # range(3 - 1) = range(2) = [0, 1]
        # Jadi i akan jadi 0 dan 1
        #
        # Mengapa sampai n-1?
        # Karena kita cek pasangan (i, i+1)
        # Jika ada 3 elemen (index 0,1,2):
        # - Cek (0, 1): arr[1] - arr[0]
        # - Cek (1, 2): arr[2] - arr[1]
        # Tidak perlu cek (2, 3) karena arr[3] tidak ada
        #
        for i in range(len(arr) - 1):
            # i = 0, 1, 2, ...
            
            # ═════════════════════════════════════════════════════
            # STEP 4A: Hitung jarak elemen sekarang dengan berikutnya
            # ═════════════════════════════════════════════════════
            # 
            # Rumus: jarak_sekarang = arr[i + 1] - arr[i]
            #
            # Contoh untuk arr = [1, 3, 5]:
            # i=0: jarak_sekarang = arr[1] - arr[0] = 3 - 1 = 2
            # i=1: jarak_sekarang = arr[2] - arr[1] = 5 - 3 = 2
            #
            # Contoh untuk arr = [1, 2, 4]:
            # i=0: jarak_sekarang = arr[1] - arr[0] = 2 - 1 = 1
            # i=1: jarak_sekarang = arr[2] - arr[1] = 4 - 2 = 2
            #
            jarak_sekarang = arr[i + 1] - arr[i]
            
            # ═════════════════════════════════════════════════════
            # STEP 4B: Bandingkan dengan jarak acuan
            # ═════════════════════════════════════════════════════
            #
            # Jika jarak_sekarang TIDAK SAMA dengan jarak acuan
            # Berarti pola TIDAK konsisten!
            #
            if jarak_sekarang != jarak:
                # Artinya tidak bisa jadi arithmetic progression!
                return False
        
        # ═══════════════════════════════════════════════════════════
        # STEP 5: Jika loop selesai tanpa return False
        # ═══════════════════════════════════════════════════════════
        # Berarti SEMUA jarak sama!
        # Ini adalah arithmetic progression!
        #
        return True


# ═══════════════════════════════════════════════════════════════
# TEST CASES (JALANKAN DAN LIHAT OUTPUT)
# ═══════════════════════════════════════════════════════════════

print("=" * 70)
print("TESTING Q1: Can Make Arithmetic Progression")
print("=" * 70 + "\n")

sol = Solution()

# TEST 1: [3, 5, 1]
# ═══════════════════════════════════════════════════════════════
print("TEST 1: [3, 5, 1]")
print("-" * 70)
print("PENJELASAN STRATEGI:")
print("  Input: [3, 5, 1]")
print("  Urutkan: [1, 3, 5]")
print("  Jarak acuan: 3 - 1 = 2")
print()
print("TRACE EXECUTION:")
print()

arr = [3, 5, 1]
arr.sort()
jarak = arr[1] - arr[0]
print(f"  Setelah sort: {arr}")
print(f"  Jarak acuan: {jarak}")
print()

for i in range(len(arr) - 1):
    jarak_sekarang = arr[i + 1] - arr[i]
    match = "✓ SAMA" if jarak_sekarang == jarak else "✗ BEDA"
    print(f"  Step {i+1}: arr[{i+1}] - arr[{i}] = {arr[i+1]} - {arr[i]} = {jarak_sekarang} {match}")

print()
result = sol.canMakeArithmeticProgression([3, 5, 1])
print(f"HASIL: {result}")
print(f"PENJELASAN: Semua jarak sama (2, 2), jadi True ✓\n")

# TEST 2: [1, 2, 4]
# ═══════════════════════════════════════════════════════════════
print("TEST 2: [1, 2, 4]")
print("-" * 70)
print("PENJELASAN STRATEGI:")
print("  Input: [1, 2, 4]")
print("  Urutkan: [1, 2, 4]")
print("  Jarak acuan: 2 - 1 = 1")
print()
print("TRACE EXECUTION:")
print()

arr = [1, 2, 4]
arr.sort()
jarak = arr[1] - arr[0]
print(f"  Setelah sort: {arr}")
print(f"  Jarak acuan: {jarak}")
print()

for i in range(len(arr) - 1):
    jarak_sekarang = arr[i + 1] - arr[i]
    match = "✓ SAMA" if jarak_sekarang == jarak else "✗ BEDA"
    print(f"  Step {i+1}: arr[{i+1}] - arr[{i}] = {arr[i+1]} - {arr[i]} = {jarak_sekarang} {match}")

print()
result = sol.canMakeArithmeticProgression([1, 2, 4])
print(f"HASIL: {result}")
print(f"PENJELASAN: Ada jarak beda (1, 2), jadi False ✗\n")

# TEST 3: [5, 5, 5]
# ═══════════════════════════════════════════════════════════════
print("TEST 3: [5, 5, 5]")
print("-" * 70)
print("PENJELASAN STRATEGI:")
print("  Input: [5, 5, 5]")
print("  Urutkan: [5, 5, 5]")
print("  Jarak acuan: 5 - 5 = 0")
print()
print("TRACE EXECUTION:")
print()

arr = [5, 5, 5]
arr.sort()
jarak = arr[1] - arr[0]
print(f"  Setelah sort: {arr}")
print(f"  Jarak acuan: {jarak}")
print()

for i in range(len(arr) - 1):
    jarak_sekarang = arr[i + 1] - arr[i]
    match = "✓ SAMA" if jarak_sekarang == jarak else "✗ BEDA"
    print(f"  Step {i+1}: arr[{i+1}] - arr[{i}] = {arr[i+1]} - {arr[i]} = {jarak_sekarang} {match}")

print()
result = sol.canMakeArithmeticProgression([5, 5, 5])
print(f"HASIL: {result}")
print(f"PENJELASAN: Semua jarak sama (0, 0), jadi True ✓\n")
