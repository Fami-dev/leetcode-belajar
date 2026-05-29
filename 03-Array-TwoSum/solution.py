# ═══════════════════════════════════════════════════════════════
# Q3. TWO SUM
# ═══════════════════════════════════════════════════════════════

# 📖 PENJELASAN SOAL (UNTUK PEMULA)
# ═════════════════════════════════════════════════════════════════
#
# Apa itu Two Sum?
# → Cari 2 angka dari array yang JUMLAHNYA = target
# → Return INDEX (posisi) dari kedua angka tersebut
# 
# Penting:
#   - Tidak boleh pakai angka yang sama 2 kali
#   - Cuma ada 1 solusi yang benar
#   - Bisa return dalam urutan apa saja
# 
# Contoh mudah:
#   nums = [2, 7, 11, 15], target = 9
#   → Cari: 2 angka yang jumlahnya 9
#   → Jawab: 2 + 7 = 9
#   → Angka 2 di posisi 0, angka 7 di posisi 1
#   → Return: [0, 1]
#
#   nums = [3, 2, 4], target = 6
#   → Cari: 2 angka yang jumlahnya 6
#   → Jawab: 2 + 4 = 6
#   → Angka 2 di posisi 1, angka 4 di posisi 2
#   → Return: [1, 2]
#
#   nums = [3, 3], target = 6
#   → Cari: 2 angka yang jumlahnya 6
#   → Jawab: 3 + 3 = 6
#   → Angka pertama di posisi 0, angka kedua di posisi 1
#   → Return: [0, 1]
#
# ═════════════════════════════════════════════════════════════════

# 🧠 PENJELASAN STRATEGI (CARA KERJA)
# ═════════════════════════════════════════════════════════════════
#
# Ada 2 cara menyelesaikan:
#
# CARA 1: BRUTE FORCE (Mudah tapi LAMBAT)
# ════════════════════════════════════════════
# Cara: Coba semua kombinasi 2 angka
#
# Contoh: nums = [2, 7, 11, 15], target = 9
#   Coba angka 0 dengan 1: 2 + 7 = 9 ✓ COCOK! Return [0, 1]
#   (Jika tidak cocok, lanjut coba kombinasi lain)
#
# Waktu: O(n²) = LAMBAT untuk array besar
# Ruang: O(1) = Tidak perlu memory tambahan
#
# ════════════════════════════════════════════
#
# CARA 2: HASH MAP (CEPAT) ← Kita pakai ini!
# ════════════════════════════════════════════
# Cara: Gunakan dictionary untuk cek
#
# Logika:
#   Untuk setiap angka, hitung:
#   complement = target - angka_sekarang
#   
#   Tanya: Apakah complement sudah ada di dictionary?
#   - Jika IYA → Ketemu! Return posisi complement dan posisi sekarang
#   - Jika TIDAK → Simpan angka_sekarang ke dictionary
#
# Contoh: nums = [2, 7, 11, 15], target = 9
#   
#   Langkah 1: Lihat angka 2
#   - complement = 9 - 2 = 7
#   - Apakah 7 ada di dict? TIDAK
#   - Simpan: dict[2] = 0
#   - dict sekarang: {2: 0}
#   
#   Langkah 2: Lihat angka 7
#   - complement = 9 - 7 = 2
#   - Apakah 2 ada di dict? IYA! Di posisi 0
#   - KETEMU! Return [0, 1] ✓
#
# Waktu: O(n) = CEPAT!
# Ruang: O(n) = Butuh memory untuk dictionary
#
# ═════════════════════════════════════════════════════════════════


class Solution(object):
    def twoSum(self, nums, target):
        # Input: 
        #   nums = list of integers
        #   target = integer yang ditargetkan
        # Output: 
        #   list dengan 2 index [index1, index2]
        
        # ═══════════════════════════════════════════════════════════
        # STEP 1: Buat dictionary kosong
        # ═══════════════════════════════════════════════════════════
        # Dictionary ini akan menyimpan:
        # Key = angka yang sudah dilihat
        # Value = posisi (index) angka tersebut
        #
        # Contoh isi dictionary:
        # {2: 0, 7: 1, 11: 2, 15: 3}
        # Artinya: angka 2 di posisi 0, angka 7 di posisi 1, dst
        #
        seen = {}
        
        # ═══════════════════════════════════════════════════════════
        # STEP 2: Loop untuk setiap angka dalam array
        # ═══════════════════════════════════════════════════════════
        # i = 0, 1, 2, 3, ... (posisi/index)
        # num = angka di posisi i
        #
        for i, num in enumerate(nums):
            # enumerate() memberi kita dua hal:
            # - i = index/posisi (0, 1, 2, ...)
            # - num = nilai di posisi i
            #
            # Contoh: nums = [2, 7, 11, 15]
            # Loop 1: i=0, num=2
            # Loop 2: i=1, num=7
            # Loop 3: i=2, num=11
            # Loop 4: i=3, num=15
            
            # ═════════════════════════════════════════════════════════
            # STEP 2A: Hitung COMPLEMENT (angka yang kita cari)
            # ═════════════════════════════════════════════════════════
            # 
            # Rumus: complement = target - angka_sekarang
            # 
            # Kenapa?
            # Jika target = 9 dan angka_sekarang = 2
            # Maka kita cari angka berapa yang + 2 = 9?
            # Jawab: 7, karena 2 + 7 = 9
            # Jadi: complement = 9 - 2 = 7
            #
            # Contoh lengkap:
            # target=9, num=2 → complement=9-2=7
            # target=9, num=7 → complement=9-7=2
            # target=9, num=11 → complement=9-11=-2
            # target=9, num=15 → complement=9-15=-6
            #
            complement = target - num
            
            # ═════════════════════════════════════════════════════════
            # STEP 2B: Cek apakah COMPLEMENT ada di dictionary?
            # ═════════════════════════════════════════════════════════
            #
            if complement in seen:
                # KETEMU! complement sudah ada di dictionary
                # Artinya: kita sudah lihat angka ini sebelumnya
                # Dan angka itu + angka_sekarang = target
                
                # seen[complement] = posisi angka complement
                # i = posisi angka sekarang
                # Kembalikan kedua posisi tersebut
                return [seen[complement], i]
            
            # ═════════════════════════════════════════════════════════
            # STEP 2C: Simpan angka SEKARANG ke dictionary
            # ═════════════════════════════════════════════════════════
            #
            # Jika complement tidak ditemukan
            # Berarti kita perlu ingat angka ini untuk nanti
            # Simpan: dict[angka] = posisinya
            #
            # Contoh:
            # seen[2] = 0 (angka 2 di posisi 0)
            # seen[7] = 1 (angka 7 di posisi 1)
            # seen[11] = 2 (angka 11 di posisi 2)
            #
            seen[num] = i
        
        # ═════════════════════════════════════════════════════════════
        # STEP 3: Jika tidak ketemu (tidak seharusnya terjadi)
        # ═════════════════════════════════════════════════════════════
        # Soal menjamin ada 1 solusi
        # Jadi ini hanya "safety net"
        #
        return []


# ═══════════════════════════════════════════════════════════════
# TEST CASES (JALANKAN DAN LIHAT OUTPUT)
# ═══════════════════════════════════════════════════════════════

print("=" * 70)
print("TESTING Q3: Two Sum")
print("=" * 70 + "\n")

sol = Solution()

# TEST 1: nums = [2, 7, 11, 15], target = 9
# ═══════════════════════════════════════════════════════════════
print("TEST 1: nums = [2, 7, 11, 15], target = 9")
print("-" * 70)
print("PENJELASAN STRATEGI:")
print("  Cari 2 angka yang jumlahnya 9")
print()
print("TRACE EXECUTION:")
print()

nums = [2, 7, 11, 15]
target = 9
seen = {}

for i, num in enumerate(nums):
    complement = target - num
    print(f"  Step {i+1}: num={num} (posisi {i})")
    print(f"    complement = {target} - {num} = {complement}")
    
    if complement in seen:
        print(f"    ✓ KETEMU! {complement} ada di posisi {seen[complement]}")
        print(f"    RETURN: [{seen[complement]}, {i}]")
        break
    else:
        print(f"    ✗ {complement} belum ada di dictionary")
        print(f"    Simpan: seen[{num}] = {i}")
        seen[num] = i
    
    print(f"    Dictionary sekarang: {seen}")
    print()

result = sol.twoSum(nums, target)
print(f"HASIL: {result}")
print(f"VERIFIKASI: nums[{result[0]}] + nums[{result[1]}] = {nums[result[0]]} + {nums[result[1]]} = {nums[result[0]] + nums[result[1]]}")
print()

# TEST 2: nums = [3, 2, 4], target = 6
# ═══════════════════════════════════════════════════════════════
print("TEST 2: nums = [3, 2, 4], target = 6")
print("-" * 70)
print("PENJELASAN STRATEGI:")
print("  Cari 2 angka yang jumlahnya 6")
print()
print("TRACE EXECUTION:")
print()

nums = [3, 2, 4]
target = 6
seen = {}

for i, num in enumerate(nums):
    complement = target - num
    print(f"  Step {i+1}: num={num} (posisi {i})")
    print(f"    complement = {target} - {num} = {complement}")
    
    if complement in seen:
        print(f"    ✓ KETEMU! {complement} ada di posisi {seen[complement]}")
        print(f"    RETURN: [{seen[complement]}, {i}]")
        break
    else:
        print(f"    ✗ {complement} belum ada di dictionary")
        print(f"    Simpan: seen[{num}] = {i}")
        seen[num] = i
    
    print(f"    Dictionary sekarang: {seen}")
    print()

result = sol.twoSum(nums, target)
print(f"HASIL: {result}")
print(f"VERIFIKASI: nums[{result[0]}] + nums[{result[1]}] = {nums[result[0]]} + {nums[result[1]]} = {nums[result[0]] + nums[result[1]]}")
print()

# TEST 3: nums = [3, 3], target = 6
# ═══════════════════════════════════════════════════════════════
print("TEST 3: nums = [3, 3], target = 6")
print("-" * 70)
print("PENJELASAN STRATEGI:")
print("  Cari 2 angka yang jumlahnya 6 (BOLEH pakai angka yang sama asal index beda)")
print()
print("TRACE EXECUTION:")
print()

nums = [3, 3]
target = 6
seen = {}

for i, num in enumerate(nums):
    complement = target - num
    print(f"  Step {i+1}: num={num} (posisi {i})")
    print(f"    complement = {target} - {num} = {complement}")
    
    if complement in seen:
        print(f"    ✓ KETEMU! {complement} ada di posisi {seen[complement]}")
        print(f"    RETURN: [{seen[complement]}, {i}]")
        break
    else:
        print(f"    ✗ {complement} belum ada di dictionary")
        print(f"    Simpan: seen[{num}] = {i}")
        seen[num] = i
    
    print(f"    Dictionary sekarang: {seen}")
    print()

result = sol.twoSum(nums, target)
print(f"HASIL: {result}")
print(f"VERIFIKASI: nums[{result[0]}] + nums[{result[1]}] = {nums[result[0]]} + {nums[result[1]]} = {nums[result[0]] + nums[result[1]]}")
print()
