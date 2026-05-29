# ═══════════════════════════════════════════════════════════════
# Q7. COUNT NEGATIVE NUMBERS IN A SORTED MATRIX
# ═══════════════════════════════════════════════════════════════

# 📖 PENJELASAN SOAL (UNTUK PEMULA)
# ═════════════════════════════════════════════════════════════════
#
# Apa itu Count Negative Numbers in a Sorted Matrix?
# → Diberikan matrix (tabel 2D) yang sudah SORTED (terurut)
# → Sorted: dari besar ke kecil (non-increasing) di setiap row
# → Sorted: dari besar ke kecil (non-increasing) di setiap column
# → Hitung berapa banyak angka NEGATIF (< 0)
#
# Apa itu Matrix?
# → Array 2D (baris dan kolom)
# → Contoh:
#    grid = [[4, 3, 2, -1],
#            [3, 2, 1, -1],
#            [1, 1, -1, -2],
#            [-1, -1, -2, -3]]
#
# Penting:
#   - Matrix SORTED (besar ke kecil di baris dan kolom)
#   - Cari TOTAL negative numbers
#   - Bisa gunakan trick karena sorted
#
# Contoh mudah:
#   grid = [[4, 3, 2, -1],
#           [3, 2, 1, -1],
#           [1, 1, -1, -2],
#           [-1, -1, -2, -3]]
#
#   Visually:
#   4    3    2    -1  ← Row 0
#   3    2    1    -1  ← Row 1
#   1    1   -1    -2  ← Row 2
#  -1   -1   -2    -3  ← Row 3
#
#   Negatives: -1, -1, -1, -1, -2, -2, -2, -3 = 8 total
#   Return: 8
#
#   grid = [[3, 2],
#           [1, 0]]
#
#   Negatives: TIDAK ADA
#   Return: 0
#
# ═════════════════════════════════════════════════════════════════

# 🔢 PENJELASAN STRATEGI (CARA KERJA)
# ═════════════════════════════════════════════════════════════════
#
# Strategi: TWO POINTER dari SUDUT KIRI BAWAH
#
# Kenapa TWO POINTER dari SUDUT KIRI BAWAH?
# → Matrix sorted decreasing per baris dan kolom
# → Mulai dari kiri bawah [m-1][0] sangat efisien!
# → Gunakan property sorted untuk berjalan efisien
#
# Logika (Start from Bottom-Left):
# 1. Mulai di posisi [m-1, 0] (baris terakhir, kolom pertama)
# 2. Cek nilai di posisi ini
#
# 3. Jika nilai NEGATIVE:
#    - Row ini DECREASING, jadi col ke col+1...n-1 semuanya NEGATIVE
#    - Semua dari index col sampai n-1 di row ini negatif
#    - Tambah count = n - col (negatives dari col ke akhir)
#    - Gerak ROW naik (row--)
#    - Col TETAP sama untuk row berikutnya
#
# 4. Jika nilai POSITIF/NOL:
#    - Kemungkinan ada negative di kolom sebelah kanan
#    - Gerak COL ke kanan (col++)
#
# 5. Loop sampai row keluar batas atas atau col keluar batas kanan
#
# Contoh trace:
#   grid = [[4, 3, 2, -1],       ← Row 0
#           [3, 2, 1, -1],       ← Row 1
#           [1, 1, -1, -2],      ← Row 2
#           [-1, -1, -2, -3]]    ← Row 3 (mulai dari sini)
#
#   Step 1: [3][0] = -1 (negative!)
#   → Dari col 0 ke end (-1,-1,-2,-3) semuanya negative
#   → Count += 4 - 0 = 4, row--
#
#   Step 2: [2][0] = 1 (positif)
#   → Mungkin ada negative di kolom sebelah kanan
#   → col++
#
#   Step 3: [2][1] = 1 (positif)
#   → col++
#
#   Step 4: [2][2] = -1 (negative!)
#   → Dari col 2 ke end (-1,-2) semuanya negative
#   → Count += 4 - 2 = 2, row--
#
#   ... dst sampai row<0
#
# ═════════════════════════════════════════════════════════════════


class Solution(object):
    def countNegatives(self, grid):
        # Input:
        #   grid = 2D array, sorted non-increasing per row & column
        # Output:
        #   total count of negative numbers
        
        # ═══════════════════════════════════════════════════════════
        # STEP 1: Inisialisasi row dan column pointers
        # ═══════════════════════════════════════════════════════════
        #
        # Start dari BOTTOM-LEFT corner (kiri bawah)
        # - row = len(grid) - 1 (baris terakhir)
        # - col = 0 (kolom pertama)
        #
        # Contoh untuk grid 4x4:
        # row = 3 (index 0,1,2,3)
        # col = 0
        #
        row = len(grid) - 1
        col = 0
        
        # ═══════════════════════════════════════════════════════════
        # STEP 2: Inisialisasi counter untuk negatif
        # ═══════════════════════════════════════════════════════════
        #
        # count = jumlah angka negatif yang ditemukan
        #
        count = 0
        
        # ═══════════════════════════════════════════════════════════
        # STEP 3: Loop sampai row keluar batas atas atau col keluar batas kanan
        # ═══════════════════════════════════════════════════════════
        #
        # Kondisi: while row >= 0 and col < len(grid[0])
        #
        # Artinya loop SELAMA:
        # - row masih dalam batas (>= 0)
        # - DAN col masih dalam batas (< n)
        #
        while row >= 0 and col < len(grid[0]):
            # ═════════════════════════════════════════════════════
            # STEP 3A: Ambil nilai di posisi [row, col]
            # ═════════════════════════════════════════════════════
            #
            val = grid[row][col]
            
            # ═════════════════════════════════════════════════════
            # STEP 3B: Cek apakah nilai NEGATIF
            # ═════════════════════════════════════════════════════
            #
            # Jika val < 0 (negatif):
            # - Row ini DECREASING (sorted non-increasing)
            # - grid[row][col] = negatif
            # - grid[row][col+1], grid[row][col+2], ... juga negatif (lebih kecil)
            # - Jadi dari col ke akhir (n-1), semuanya negatif
            # - Total negatif di row ini dari col: (n - col) angka
            #   - Misal n=4, col=2: angka di index 2,3 = 4-2=2 angka

            # Contoh:
            # grid[2] = [1, 1, -1, -2]
            # Posisi [2][2]: val = -1 (negatif)
            # Dari col 2 ke end: grid[2][2]=-1, grid[2][3]=-2
            # Count: 4 - 2 = 2 negatives di row 2
            #
            if val < 0:
                count += len(grid[0]) - col
                # ═════════════════════════════════════════════════
                # Setelah count, gerak ke row sebelumnya (naik)
                # ═════════════════════════════════════════════════
                # - row-- (naik 1 baris)
                # - tetap di column yang sama (col tidak berubah)
                # - Untuk row berikutnya, check posisi yang sama
                #
                row -= 1
            else:
                # ═════════════════════════════════════════════════
                # STEP 3C: Jika nilai BUKAN negatif (>= 0)
                # ═════════════════════════════════════════════════
                #
                # Nilai >= 0 (positif atau 0)
                # Tapi row adalah decreasing, jadi ke kanan ada nilai lebih kecil
                # Mungkin di kolom sebelah kanan ada negative
                # Geser ke kolom sebelah kanan
                # col++ (geser ke kanan)
                #
                col += 1
        
        # ═══════════════════════════════════════════════════════════
        # STEP 4: Return total count
        # ═══════════════════════════════════════════════════════════
        #
        return count


# ═══════════════════════════════════════════════════════════════
# TEST CASES (JALANKAN DAN LIHAT OUTPUT)
# ═══════════════════════════════════════════════════════════════

print("=" * 80)
print("TESTING Q7: Count Negative Numbers in a Sorted Matrix")
print("=" * 80 + "\n")

sol = Solution()

# TEST 1: [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
# ═══════════════════════════════════════════════════════════════
print("TEST 1: grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]")
print("-" * 80)
print("PENJELASAN:")
print("  Grid:")
print("    [4,  3,  2, -1]")
print("    [3,  2,  1, -1]")
print("    [1,  1, -1, -2]")
print("   [-1, -1, -2, -3]")
print()
print("  Sorted? Baris: 4>3>2>-1 ✓, Kolom: 4>3>1>-1 ✓")
print("  Negatives: -1, -1, -1, -1, -2, -2, -2, -3 = 8 total")
print()
print("TRACE TWO POINTER (Start Bottom-Left):")
print()

grid = [[4, 3, 2, -1], [3, 2, 1, -1], [1, 1, -1, -2], [-1, -1, -2, -3]]
row, col = 3, 0
count = 0
step = 1
n = len(grid[0])

while row >= 0 and col < n:
    val = grid[row][col]
    
    print(f"  Step {step}: row={row}, col={col}")
    print(f"    grid[{row}][{col}] = {val}")
    
    if val < 0:
        negatives_in_row = n - col
        count += negatives_in_row
        print(f"    NEGATIF! Dari col {col} ke end semuanya negative")
        print(f"    Count += ({n} - {col}) = {negatives_in_row}")
        print(f"    Total count sekarang: {count}")
        row -= 1
    else:
        print(f"    Positif, cek kolom di kanan")
        col += 1
    
    print()
    step += 1
    step += 1

result = sol.countNegatives(grid)
print(f"HASIL: {result}")
print(f"PENJELASAN: 8 negative numbers di matrix ✓\n")

# TEST 2: [[3,2],[1,0]]
# ═══════════════════════════════════════════════════════════════
print("TEST 2: grid = [[3,2],[1,0]]")
print("-" * 80)
print("PENJELASAN:")
print("  Grid:")
print("    [3, 2]")
print("    [1, 0]")
print()
print("  Sorted? Baris: 3>2 ✓, 1>0 ✓")
print("  Kolom: 3>1 ✓, 2>0 ✓")
print("  Negatives: TIDAK ADA (semua positif)")
print()
print("TRACE TWO POINTER (Start Bottom-Left):")
print()

grid = [[3, 2], [1, 0]]
row, col = 1, 0
count = 0
step = 1
n = len(grid[0])

while row >= 0 and col < n:
    val = grid[row][col]
    
    print(f"  Step {step}: row={row}, col={col}")
    print(f"    grid[{row}][{col}] = {val}")
    
    if val < 0:
        negatives_in_row = n - col
        count += negatives_in_row
        print(f"    NEGATIF! Count += {negatives_in_row}")
        print(f"    Total count sekarang: {count}")
        row -= 1
    else:
        print(f"    Positif ({val}), cek kolom di kanan")
        col += 1
    
    print()
    step += 1

result = sol.countNegatives(grid)
print(f"HASIL: {result}")
print(f"PENJELASAN: Tidak ada negative numbers ✓\n")

# TEST 3: [[-1]]
# ═══════════════════════════════════════════════════════════════
print("TEST 3: grid = [[-1]]")
print("-" * 80)
print("PENJELASAN:")
print("  Grid:")
print("    [-1]")
print()
print("  Single element, negative")
print("  Negatives: -1 = 1 total")
print()
print("TRACE TWO POINTER (Start Bottom-Left):")
print()

grid = [[-1]]
row, col = 0, 0
count = 0
step = 1
n = len(grid[0])

while row >= 0 and col < n:
    val = grid[row][col]
    
    print(f"  Step {step}: row={row}, col={col}")
    print(f"    grid[{row}][{col}] = {val}")
    
    if val < 0:
        negatives_in_row = n - col
        count += negatives_in_row
        print(f"    NEGATIF! Count += {negatives_in_row}")
        print(f"    Total count sekarang: {count}")
        row -= 1
    else:
        print(f"    Positif, cek kolom di kanan")
        col += 1
    
    print()
    step += 1

result = sol.countNegatives(grid)
print(f"HASIL: {result}")
print(f"PENJELASAN: 1 negative number ✓\n")

# TEST 4: [[1,2,3],[4,5,6],[7,8,9]]
# ═══════════════════════════════════════════════════════════════
print("TEST 4: grid = [[1,2,3],[4,5,6],[7,8,9]]")
print("-" * 80)
print("PENJELASAN:")
print("  Grid (sorted in reverse means non-increasing, tapi ini increasing):")
print("    [1, 2, 3]")
print("    [4, 5, 6]")
print("    [7, 8, 9]")
print()
print("  Note: Ini bukan sorted non-increasing, hanya test edge case")
print("  Negatives: TIDAK ADA")
print()
print("TRACE TWO POINTER (Start Bottom-Left):")
print()

grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
row, col = 2, 0
count = 0
step = 1
n = len(grid[0])

while row >= 0 and col < n:
    val = grid[row][col]
    
    print(f"  Step {step}: row={row}, col={col}")
    print(f"    grid[{row}][{col}] = {val}")
    
    if val < 0:
        negatives_in_row = n - col
        count += negatives_in_row
        print(f"    NEGATIF! Count += {negatives_in_row}")
        print(f"    Total count sekarang: {count}")
        row -= 1
    else:
        print(f"    Positif ({val}), cek kolom di kanan")
        col += 1
    
    print()
    step += 1

result = sol.countNegatives(grid)
print(f"HASIL: {result}")
print(f"PENJELASAN: Tidak ada negative numbers ✓\n")
