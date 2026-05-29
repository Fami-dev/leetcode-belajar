# ═══════════════════════════════════════════════════════════════
# Q5. MINIMUM COMMON VALUE
# ═══════════════════════════════════════════════════════════════

# 📖 PENJELASAN SOAL (UNTUK PEMULA)
# ═════════════════════════════════════════════════════════════════
#
# Apa itu Minimum Common Value?
# → Cari angka terkecil yang ada di KEDUA array
# → Array sudah terurut (sorted) dari kecil ke besar
#
# Penting:
#   - Angka harus ada di nums1 DAN nums2
#   - Minimal 1 kemunculan di masing-masing
#   - Cari yang PALING KECIL
#   - Jika tidak ada, return -1
#
# Contoh mudah:
#   nums1 = [1, 2, 3], nums2 = [2, 4]
#   → Common: 2 (ada di kedua array)
#   → Minimum: 2 (cuma ada satu)
#   → Return: 2
#
#   nums1 = [1, 2, 3, 6], nums2 = [2, 3, 4, 5]
#   → Common: 2, 3 (ada di kedua array)
#   → Minimum: 2 (paling kecil)
#   → Return: 2
#
#   nums1 = [1, 3], nums2 = [2, 4]
#   → Common: TIDAK ADA
#   → Return: -1
#
# ═════════════════════════════════════════════════════════════════

# 🔢 PENJELASAN STRATEGI (CARA KERJA)
# ═════════════════════════════════════════════════════════════════
#
# Strategi: TWO POINTER (Dua pointer bergerak)
#
# Kenapa two pointer?
# → Array sudah sorted!
# → Bisa gunakan ini untuk pencarian efisien
# → Cuma perlu 1 kali loop (O(n))
#
# Logika:
# - Pointer 1 di awal nums1 (posisi 0)
# - Pointer 2 di awal nums2 (posisi 0)
#
# - Jika nums1[p1] == nums2[p2]
#   → KETEMU! Return angka itu (paling kecil)
#
# - Jika nums1[p1] < nums2[p2]
#   → nums1 lebih kecil, gerak pointer 1 ke kanan
#
# - Jika nums1[p1] > nums2[p2]
#   → nums2 lebih kecil, gerak pointer 2 ke kanan
#
# Contoh trace:
#   nums1 = [1, 2, 3, 6]
#   nums2 = [2, 3, 4, 5]
#
#   Step 1: p1=0, p2=0
#   nums1[0]=1, nums2[0]=2
#   1 < 2, gerak p1 →
#
#   Step 2: p1=1, p2=0
#   nums1[1]=2, nums2[0]=2
#   2 == 2, KETEMU! Return 2
#
# ═════════════════════════════════════════════════════════════════


class Solution(object):
    def getCommon(self, nums1, nums2):
        # Input:
        #   nums1 = array sorted, angka tidak ada duplikat
        #   nums2 = array sorted, angka tidak ada duplikat
        # Output:
        #   minimum angka yang ada di kedua array, atau -1
        
        # ═══════════════════════════════════════════════════════════
        # STEP 1: Inisialisasi dua pointer
        # ═══════════════════════════════════════════════════════════
        #
        # p1 = pointer untuk nums1, mulai dari posisi 0 (awal)
        # p2 = pointer untuk nums2, mulai dari posisi 0 (awal)
        #
        # Contoh:
        # nums1 = [1, 2, 3, 6]
        # nums2 = [2, 3, 4, 5]
        # p1 = 0 → nums1[0] = 1
        # p2 = 0 → nums2[0] = 2
        #
        p1 = 0
        p2 = 0
        
        # ═══════════════════════════════════════════════════════════
        # STEP 2: Loop sampai salah satu pointer mencapai akhir array
        # ═══════════════════════════════════════════════════════════
        #
        # Kondisi: while p1 < len(nums1) and p2 < len(nums2)
        #
        # Artinya: terus loop SELAMA:
        # - p1 belum sampai akhir nums1
        # - DAN p2 belum sampai akhir nums2
        #
        # Jika salah satu sampai akhir, berarti tidak ada common value
        #
        # Contoh:
        # nums1 length = 4 (index 0, 1, 2, 3)
        # nums2 length = 4 (index 0, 1, 2, 3)
        # Loop saat p1 < 4 dan p2 < 4
        #
        while p1 < len(nums1) and p2 < len(nums2):
            # ═════════════════════════════════════════════════════
            # STEP 2A: Ambil nilai dari kedua array di posisi pointer
            # ═════════════════════════════════════════════════════
            #
            val1 = nums1[p1]
            val2 = nums2[p2]
            
            # ═════════════════════════════════════════════════════
            # STEP 2B: Cek apakah nilai sama
            # ═════════════════════════════════════════════════════
            #
            # Jika val1 == val2, berarti ada angka yang sama
            # Karena array sorted dan kita mulai dari awal,
            # ini adalah angka MINIMUM yang common!
            #
            if val1 == val2:
                return val1
            
            # ═════════════════════════════════════════════════════
            # STEP 2C: Gerak pointer sesuai nilai mana yang lebih kecil
            # ═════════════════════════════════════════════════════
            #
            # Jika val1 < val2:
            # - val1 lebih kecil dari val2
            # - Gerak p1 ke kanan (p1 += 1)
            # - Coba cari angka yang lebih besar di nums1
            # - Mungkin angka berikutnya akan sama dengan val2
            #
            # Jika val1 > val2:
            # - val2 lebih kecil dari val1
            # - Gerak p2 ke kanan (p2 += 1)
            # - Coba cari angka yang lebih besar di nums2
            # - Mungkin angka berikutnya akan sama dengan val1
            #
            if val1 < val2:
                p1 += 1
            else:
                p2 += 1
        
        # ═══════════════════════════════════════════════════════════
        # STEP 3: Jika loop selesai tanpa return
        # ═══════════════════════════════════════════════════════════
        #
        # Berarti tidak ada angka yang sama di kedua array
        # Return -1 (standard untuk "tidak ada")
        #
        return -1


# ═══════════════════════════════════════════════════════════════
# TEST CASES (JALANKAN DAN LIHAT OUTPUT)
# ═══════════════════════════════════════════════════════════════

print("=" * 80)
print("TESTING Q5: Minimum Common Value")
print("=" * 80 + "\n")

sol = Solution()

# TEST 1: nums1 = [1,2,3], nums2 = [2,4]
# ═══════════════════════════════════════════════════════════════
print("TEST 1: nums1 = [1,2,3], nums2 = [2,4]")
print("-" * 80)
print("PENJELASAN:")
print("  nums1 = [1,2,3] (sorted)")
print("  nums2 = [2,4] (sorted)")
print("  Common: 2 (ada di kedua array)")
print("  Minimum: 2 (cuma ada satu)")
print()
print("TRACE TWO POINTER:")
print()

nums1 = [1, 2, 3]
nums2 = [2, 4]
p1, p2 = 0, 0
step = 1

while p1 < len(nums1) and p2 < len(nums2):
    val1 = nums1[p1]
    val2 = nums2[p2]
    
    print(f"  Step {step}: p1={p1}, p2={p2}")
    print(f"    nums1[{p1}]={val1}, nums2[{p2}]={val2}")
    
    if val1 == val2:
        print(f"    ✓ KETEMU! {val1} == {val2}")
        print(f"    RETURN: {val1}")
        break
    elif val1 < val2:
        print(f"    {val1} < {val2}, gerak p1 →")
        p1 += 1
    else:
        print(f"    {val1} > {val2}, gerak p2 →")
        p2 += 1
    
    print()
    step += 1

result = sol.getCommon(nums1, nums2)
print(f"HASIL: {result}")
print(f"PENJELASAN: Angka 2 adalah common value terkecil ✓\n")

# TEST 2: nums1 = [1,2,3,6], nums2 = [2,3,4,5]
# ═══════════════════════════════════════════════════════════════
print("TEST 2: nums1 = [1,2,3,6], nums2 = [2,3,4,5]")
print("-" * 80)
print("PENJELASAN:")
print("  nums1 = [1,2,3,6] (sorted)")
print("  nums2 = [2,3,4,5] (sorted)")
print("  Common: 2, 3 (ada di kedua array)")
print("  Minimum: 2 (paling kecil)")
print()
print("TRACE TWO POINTER:")
print()

nums1 = [1, 2, 3, 6]
nums2 = [2, 3, 4, 5]
p1, p2 = 0, 0
step = 1

while p1 < len(nums1) and p2 < len(nums2):
    val1 = nums1[p1]
    val2 = nums2[p2]
    
    print(f"  Step {step}: p1={p1}, p2={p2}")
    print(f"    nums1[{p1}]={val1}, nums2[{p2}]={val2}")
    
    if val1 == val2:
        print(f"    ✓ KETEMU! {val1} == {val2}")
        print(f"    RETURN: {val1}")
        break
    elif val1 < val2:
        print(f"    {val1} < {val2}, gerak p1 →")
        p1 += 1
    else:
        print(f"    {val1} > {val2}, gerak p2 →")
        p2 += 1
    
    print()
    step += 1

result = sol.getCommon(nums1, nums2)
print(f"HASIL: {result}")
print(f"PENJELASAN: Angka 2 adalah minimum common value ✓\n")

# TEST 3: nums1 = [1,3], nums2 = [2,4]
# ═══════════════════════════════════════════════════════════════
print("TEST 3: nums1 = [1,3], nums2 = [2,4]")
print("-" * 80)
print("PENJELASAN:")
print("  nums1 = [1,3] (sorted)")
print("  nums2 = [2,4] (sorted)")
print("  Common: TIDAK ADA")
print("  Return: -1 (standard untuk tidak ada)")
print()
print("TRACE TWO POINTER:")
print()

nums1 = [1, 3]
nums2 = [2, 4]
p1, p2 = 0, 0
step = 1

while p1 < len(nums1) and p2 < len(nums2):
    val1 = nums1[p1]
    val2 = nums2[p2]
    
    print(f"  Step {step}: p1={p1}, p2={p2}")
    print(f"    nums1[{p1}]={val1}, nums2[{p2}]={val2}")
    
    if val1 == val2:
        print(f"    ✓ KETEMU! {val1} == {val2}")
        print(f"    RETURN: {val1}")
        break
    elif val1 < val2:
        print(f"    {val1} < {val2}, gerak p1 →")
        p1 += 1
    else:
        print(f"    {val1} > {val2}, gerak p2 →")
        p2 += 1
    
    print()
    step += 1

print(f"  Loop selesai, tidak ada yang cocok")
print()

result = sol.getCommon(nums1, nums2)
print(f"HASIL: {result}")
print(f"PENJELASAN: Tidak ada angka common, return -1 ✓\n")
