# ═══════════════════════════════════════════════════════════════
# Q6. APPLE REDISTRIBUTION INTO BOXES
# ═══════════════════════════════════════════════════════════════

# 📖 PENJELASAN SOAL (UNTUK PEMULA)
# ═════════════════════════════════════════════════════════════════
#
# Apa itu Apple Redistribution into Boxes?
# → Ada n "packs" berisi apples
# → Ada m "boxes" dengan kapasitas berbeda
# → Perlu distribute SEMUA apples dari packs ke boxes
# → Cari: minimum boxes yang PERLU digunakan
#
# Penting:
#   - Hitung TOTAL apples dari semua packs
#   - Hitung capacity dari masing-masing box
#   - Ambil boxes dengan kapasitas TERBESAR dulu
#   - Terus ambil boxes sampai total capacity >= total apples
#   - Return berapa banyak boxes yang diambil
#
# Contoh mudah:
#   apple = [1, 3, 2], capacity = [4, 3, 1, 5, 2]
#   → Total apples: 1 + 3 + 2 = 6
#   → Sorted capacity (besar ke kecil): [5, 4, 3, 2, 1]
#   → Ambil box capacity 5: total = 5, masih kurang (5 < 6)
#   → Ambil box capacity 4: total = 5 + 4 = 9, cukup! (9 >= 6)
#   → Boxes yang digunakan: 2 ✓
#
#   apple = [5, 5, 5], capacity = [2, 4, 2, 7]
#   → Total apples: 5 + 5 + 5 = 15
#   → Sorted capacity (besar ke kecil): [7, 4, 2, 2]
#   → Ambil box capacity 7: total = 7 (7 < 15)
#   → Ambil box capacity 4: total = 7 + 4 = 11 (11 < 15)
#   → Ambil box capacity 2: total = 11 + 2 = 13 (13 < 15)
#   → Ambil box capacity 2: total = 13 + 2 = 15 (15 >= 15) ✓
#   → Boxes yang digunakan: 4 ✓
#
# ═════════════════════════════════════════════════════════════════

# 🔢 PENJELASAN STRATEGI (CARA KERJA)
# ═════════════════════════════════════════════════════════════════
#
# Strategi: GREEDY + SORTING (Ambil yang terbaik dulu!)
#
# Greedy = Selalu ambil pilihan TERBAIK di setiap step
#
# Logika:
# 1. Hitung total_apples (jumlah apples dari semua packs)
#
# 2. Sort capacity dari BESAR ke KECIL
#    Kenapa? Pakai box yang besar dulu, lebih cepat penuh!
#
# 3. Loop melalui capacity yang sudah sorted
#    - Total box_capacity += capacity[i]
#    - Cek apakah total_capacity sudah >= total_apples
#    - Jika YA, return count boxes
#
# 4. Return jumlah boxes yang digunakan
#
# Mengapa cara ini optimal?
# → Dengan mengambil boxes terbesar dulu, minimum boxes terpakai
# → Jika ambil random, bisa jadi perlu lebih banyak boxes
#
# Contoh trace:
#   apple = [1, 3, 2], capacity = [4, 3, 1, 5, 2]
#   
#   Step 1: total_apples = 1 + 3 + 2 = 6
#   
#   Step 2: Sort capacity descending = [5, 4, 3, 2, 1]
#   
#   Step 3: Ambil boxes satu-satu
#     - Ambil box[0] capacity 5: total_capacity = 5, count = 1
#       5 >= 6? NO, lanjut
#     - Ambil box[1] capacity 4: total_capacity = 9, count = 2
#       9 >= 6? YES! Return 2
#
# ═════════════════════════════════════════════════════════════════


class Solution(object):
    def minimumBoxes(self, apple, capacity):
        # Input:
        #   apple = array berisi jumlah apples di setiap pack
        #   capacity = array berisi kapasitas setiap box
        # Output:
        #   minimum boxes yang perlu dipilih
        
        # ═══════════════════════════════════════════════════════════
        # STEP 1: Hitung total_apples (jumlah semua apples)
        # ═══════════════════════════════════════════════════════════
        #
        # Gunakan sum() untuk menjumlah semua elemen di array apple
        #
        # Contoh:
        # apple = [1, 3, 2]
        # total_apples = 1 + 3 + 2 = 6
        #
        total_apples = sum(apple)
        
        # ═══════════════════════════════════════════════════════════
        # STEP 2: Sort capacity dari BESAR ke KECIL
        # ═══════════════════════════════════════════════════════════
        #
        # .sort(reverse=True) = sort descending (besar ke kecil)
        # Kenapa? Ambil boxes besar dulu, lebih efisien!
        #
        # Contoh:
        # capacity = [4, 3, 1, 5, 2]
        # Setelah sort: [5, 4, 3, 2, 1]
        #
        capacity.sort(reverse=True)
        
        # ═══════════════════════════════════════════════════════════
        # STEP 3: Loop ambil boxes sampai cukup (Greedy approach)
        # ═══════════════════════════════════════════════════════════
        #
        # Variabel:
        #   total_capacity = total capacity boxes yang sudah diambil
        #   count = berapa boxes yang sudah diambil
        #
        total_capacity = 0
        count = 0
        
        # ═════════════════════════════════════════════════════════
        # STEP 3A: Loop melalui setiap box (sudah sorted besar dulu)
        # ═════════════════════════════════════════════════════════
        #
        for cap in capacity:
            # ═════════════════════════════════════════════════════
            # STEP 3B: Tambah capacity dari box ini
            # ═════════════════════════════════════════════════════
            #
            # total_capacity += cap
            # Artinya: total_capacity = total_capacity + cap
            #
            total_capacity += cap
            
            # ═════════════════════════════════════════════════════
            # STEP 3C: Tambah jumlah boxes yang diambil
            # ═════════════════════════════════════════════════════
            #
            count += 1
            
            # ═════════════════════════════════════════════════════
            # STEP 3D: Cek apakah capacity sudah cukup
            # ═════════════════════════════════════════════════════
            #
            # Jika total_capacity >= total_apples
            # Berarti semua apples bisa dimasukkan!
            # Return count (berapa boxes yang digunakan)
            #
            # Contoh:
            # total_apples = 6
            # total_capacity = 9
            # 9 >= 6? YES! Return count
            #
            if total_capacity >= total_apples:
                return count
        
        # ═══════════════════════════════════════════════════════════
        # STEP 4: Safety return (seharusnya tidak sampai sini)
        # ═══════════════════════════════════════════════════════════
        #
        # Jika loop selesai dan tidak return, berarti ada bug
        # Return -1 atau return count (should be len(capacity))
        #
        return count


# ═══════════════════════════════════════════════════════════════
# TEST CASES (JALANKAN DAN LIHAT OUTPUT)
# ═══════════════════════════════════════════════════════════════

print("=" * 80)
print("TESTING Q6: Apple Redistribution into Boxes")
print("=" * 80 + "\n")

sol = Solution()

# TEST 1: apple = [1,3,2], capacity = [4,3,1,5,2]
# ═══════════════════════════════════════════════════════════════
print("TEST 1: apple = [1,3,2], capacity = [4,3,1,5,2]")
print("-" * 80)
print("PENJELASAN:")
print("  apple = [1,3,2]")
print("  capacity = [4,3,1,5,2]")
print("  Total apples: 1 + 3 + 2 = 6")
print()
print("TRACE GREEDY ALGORITHM:")
print()

apple = [1, 3, 2]
capacity = [4, 3, 1, 5, 2]
total_apples = sum(apple)
print(f"  Total apples needed: {total_apples}")
print()

capacity_copy = capacity.copy()
capacity_copy.sort(reverse=True)
print(f"  Sorted capacity (besar ke kecil): {capacity_copy}")
print()

total_capacity = 0
count = 0
for i, cap in enumerate(capacity_copy):
    total_capacity += cap
    count += 1
    
    print(f"  Step {count}: Ambil box capacity {cap}")
    print(f"    Total capacity sekarang: {total_capacity}")
    print(f"    {total_capacity} >= {total_apples}? ", end="")
    
    if total_capacity >= total_apples:
        print("YES! ✓")
        print(f"    RETURN: {count} boxes")
        break
    else:
        print("NO, lanjut")
    
    print()

result = sol.minimumBoxes([1, 3, 2], [4, 3, 1, 5, 2])
print(f"\nHASIL: {result}")
print(f"PENJELASAN: Gunakan 2 boxes (capacity 5 dan 4), cukup untuk 6 apples ✓\n")

# TEST 2: apple = [5,5,5], capacity = [2,4,2,7]
# ═══════════════════════════════════════════════════════════════
print("TEST 2: apple = [5,5,5], capacity = [2,4,2,7]")
print("-" * 80)
print("PENJELASAN:")
print("  apple = [5,5,5]")
print("  capacity = [2,4,2,7]")
print("  Total apples: 5 + 5 + 5 = 15")
print()
print("TRACE GREEDY ALGORITHM:")
print()

apple = [5, 5, 5]
capacity = [2, 4, 2, 7]
total_apples = sum(apple)
print(f"  Total apples needed: {total_apples}")
print()

capacity_copy = capacity.copy()
capacity_copy.sort(reverse=True)
print(f"  Sorted capacity (besar ke kecil): {capacity_copy}")
print()

total_capacity = 0
count = 0
for i, cap in enumerate(capacity_copy):
    total_capacity += cap
    count += 1
    
    print(f"  Step {count}: Ambil box capacity {cap}")
    print(f"    Total capacity sekarang: {total_capacity}")
    print(f"    {total_capacity} >= {total_apples}? ", end="")
    
    if total_capacity >= total_apples:
        print("YES! ✓")
        print(f"    RETURN: {count} boxes")
        break
    else:
        print("NO, lanjut")
    
    print()

result = sol.minimumBoxes([5, 5, 5], [2, 4, 2, 7])
print(f"HASIL: {result}")
print(f"PENJELASAN: Gunakan 4 boxes (semua), capacity total = 15 = apples total ✓\n")

# TEST 3: apple = [1], capacity = [1]
# ═══════════════════════════════════════════════════════════════
print("TEST 3: apple = [1], capacity = [1]")
print("-" * 80)
print("PENJELASAN:")
print("  apple = [1]")
print("  capacity = [1]")
print("  Total apples: 1")
print()
print("TRACE GREEDY ALGORITHM:")
print()

apple = [1]
capacity = [1]
total_apples = sum(apple)
print(f"  Total apples needed: {total_apples}")
print()

capacity_copy = capacity.copy()
capacity_copy.sort(reverse=True)
print(f"  Sorted capacity (besar ke kecil): {capacity_copy}")
print()

total_capacity = 0
count = 0
for i, cap in enumerate(capacity_copy):
    total_capacity += cap
    count += 1
    
    print(f"  Step {count}: Ambil box capacity {cap}")
    print(f"    Total capacity sekarang: {total_capacity}")
    print(f"    {total_capacity} >= {total_apples}? ", end="")
    
    if total_capacity >= total_apples:
        print("YES! ✓")
        print(f"    RETURN: {count} boxes")
        break
    else:
        print("NO, lanjut")
    
    print()

result = sol.minimumBoxes([1], [1])
print(f"HASIL: {result}")
print(f"PENJELASAN: Gunakan 1 box, capacity 1 = apples 1 ✓\n")

# TEST 4: apple = [1,1,1,1,1,1,1,1,1], capacity = [5,10]
# ═══════════════════════════════════════════════════════════════
print("TEST 4: apple = [1,1,1,1,1,1,1,1,1], capacity = [5,10]")
print("-" * 80)
print("PENJELASAN:")
print("  apple = [1,1,1,1,1,1,1,1,1]")
print("  capacity = [5,10]")
print("  Total apples: 9")
print()
print("TRACE GREEDY ALGORITHM:")
print()

apple = [1, 1, 1, 1, 1, 1, 1, 1, 1]
capacity = [5, 10]
total_apples = sum(apple)
print(f"  Total apples needed: {total_apples}")
print()

capacity_copy = capacity.copy()
capacity_copy.sort(reverse=True)
print(f"  Sorted capacity (besar ke kecil): {capacity_copy}")
print()

total_capacity = 0
count = 0
for i, cap in enumerate(capacity_copy):
    total_capacity += cap
    count += 1
    
    print(f"  Step {count}: Ambil box capacity {cap}")
    print(f"    Total capacity sekarang: {total_capacity}")
    print(f"    {total_capacity} >= {total_apples}? ", end="")
    
    if total_capacity >= total_apples:
        print("YES! ✓")
        print(f"    RETURN: {count} boxes")
        break
    else:
        print("NO, lanjut")
    
    print()

result = sol.minimumBoxes([1, 1, 1, 1, 1, 1, 1, 1, 1], [5, 10])
print(f"HASIL: {result}")
print(f"PENJELASAN: Gunakan 1 box saja (capacity 10), cukup untuk 9 apples ✓\n")
