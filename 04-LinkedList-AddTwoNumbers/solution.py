# ═══════════════════════════════════════════════════════════════
# Q4. ADD TWO NUMBERS (LINKED LIST)
# ═══════════════════════════════════════════════════════════════

# 📖 PENJELASAN SOAL (UNTUK PEMULA)
# ═════════════════════════════════════════════════════════════════
#
# Apa itu Linked List?
# → Struktur data yang berisi VALUE dan POINTER ke node berikutnya
# → Seperti rantai: Node1 → Node2 → Node3 → None
#
# Contoh visual:
#   l1 = [2, 4, 3]
#   2 → 4 → 3 → None
#
# REVERSE ORDER artinya digit-nya terbalik!
# - [2, 4, 3] artinya angka: 3, 4, 2 yang dibaca dari belakang
# - Jadi angkanya adalah: 342
#
# TASK:
# - Diberikan 2 linked list (angka reverse)
# - Tambahkan kedua angka
# - Return hasil sebagai linked list (reverse juga)
#
# Contoh:
#   l1 = [2, 4, 3] → angka 342
#   l2 = [5, 6, 4] → angka 465
#   342 + 465 = 807
#   Output: [7, 0, 8] → linked list reverse
#
# ═════════════════════════════════════════════════════════════════

# 🔢 PENJELASAN STRATEGI (CARA KERJA)
# ═════════════════════════════════════════════════════════════════
#
# Strategi: LOOP + CARRY
#
# Intinya:
# - Loop dari node pertama di kedua list
# - Hitung sum = l1.val + l2.val + carry
# - Ambil digit terakhir: digit = sum % 10
# - Hitung carry: carry = sum // 10
# - Buat node baru dengan digit tersebut
# - Lanjut ke node berikutnya
#
# Contoh trace:
#   l1 = [2, 4, 3] → 342
#   l2 = [5, 6, 4] → 465
#   Ingin: 342 + 465 = 807
#
#   STEP 1 (posisi pertama/paling belakang):
#   sum = 2 + 5 + 0 = 7
#   digit = 7 % 10 = 7
#   carry = 7 // 10 = 0
#   Node baru: 7
#   
#   STEP 2:
#   sum = 4 + 6 + 0 = 10
#   digit = 10 % 10 = 0
#   carry = 10 // 10 = 1
#   Node baru: 0
#   
#   STEP 3:
#   sum = 3 + 4 + 1 = 8
#   digit = 8 % 10 = 8
#   carry = 8 // 10 = 0
#   Node baru: 8
#
#   Hasil: [7, 0, 8]
#   Angka: 807 ✓
#
# ═════════════════════════════════════════════════════════════════


# ═══════════════════════════════════════════════════════════════
# CLASS LISTNODE (STRUKTUR LINKED LIST)
# ═══════════════════════════════════════════════════════════════

class ListNode(object):
    # Setiap node punya 2 bagian:
    # - val = nilai/digit angka
    # - next = pointer ke node berikutnya
    
    def __init__(self, val=0, next=None):
        # Constructor = fungsi untuk membuat node baru
        # val = nilai node (default 0)
        # next = node berikutnya (default None)
        self.val = val
        self.next = next


# ═══════════════════════════════════════════════════════════════
# HELPER FUNCTION: Buat linked list dari list biasa
# ═══════════════════════════════════════════════════════════════

def list_to_linkedlist(arr):
    # Input: arr = list biasa, contoh [2, 4, 3]
    # Output: linked list, 2 → 4 → 3 → None
    
    if not arr:  # Jika list kosong
        return None
    
    head = ListNode(arr[0])  # Buat node pertama
    current = head
    
    # Loop dari elemen kedua sampai akhir
    for val in arr[1:]:
        current.next = ListNode(val)  # Buat node baru
        current = current.next  # Pindah ke node berikutnya
    
    return head


# ═══════════════════════════════════════════════════════════════
# HELPER FUNCTION: Ubah linked list jadi list biasa (untuk print)
# ═══════════════════════════════════════════════════════════════

def linkedlist_to_list(node):
    # Input: linked list
    # Output: list biasa untuk mudah dibaca
    
    result = []
    current = node
    
    while current:  # Loop sampai current jadi None
        result.append(current.val)
        current = current.next
    
    return result


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        # Input: 
        #   l1 = linked list pertama
        #   l2 = linked list kedua
        # Output:
        #   linked list hasil penjumlahan
        
        # ═══════════════════════════════════════════════════════════
        # STEP 1: Buat dummy node (node awal kosong)
        # ═══════════════════════════════════════════════════════════
        # 
        # Kenapa perlu dummy node?
        # → Supaya mudah buat list baru
        # → Dummy tidak ikut di hasil akhir
        # → Hanya sebagai "anchor" atau "pegangan"
        #
        # Contoh:
        # Dummy (awal, tidak pakai) → 7 → 0 → 8 (hasil akhir)
        # Hasilnya: [7, 0, 8]
        #
        dummy = ListNode(0)
        current = dummy
        carry = 0
        
        # ═══════════════════════════════════════════════════════════
        # STEP 2: Loop sampai l1, l2, dan carry SEMUA habis
        # ═══════════════════════════════════════════════════════════
        #
        # Kondisi loop:
        # - while l1 or l2 or carry
        # 
        # Artinya: terus loop JIKA:
        # - l1 masih ada (belum selesai)
        # - ATAU l2 masih ada (belum selesai)
        # - ATAU carry masih ada (ada sisa pembagian)
        #
        # Contoh:
        # l1 = [2, 4, 3]
        # l2 = [5, 6, 4]
        # 
        # Iterasi 1: l1=2, l2=5, carry=0 → loop
        # Iterasi 2: l1=4, l2=6, carry=0 → loop
        # Iterasi 3: l1=3, l2=4, carry=1 → loop
        # Iterasi 4: l1=None, l2=None, carry=0 → stop
        #
        while l1 or l2 or carry:
            # ═════════════════════════════════════════════════════
            # STEP 2A: Ambil nilai dari l1 (jika ada)
            # ═════════════════════════════════════════════════════
            #
            # Jika l1 masih ada, ambil nilainya
            # Jika l1 habis (None), gunakan 0
            #
            val1 = l1.val if l1 else 0
            
            # ═════════════════════════════════════════════════════
            # STEP 2B: Ambil nilai dari l2 (jika ada)
            # ═════════════════════════════════════════════════════
            #
            # Jika l2 masih ada, ambil nilainya
            # Jika l2 habis (None), gunakan 0
            #
            val2 = l2.val if l2 else 0
            
            # ═════════════════════════════════════════════════════
            # STEP 2C: Hitung SUM dan CARRY
            # ═════════════════════════════════════════════════════
            #
            # sum = val1 + val2 + carry (dari iterasi sebelumnya)
            #
            # digit = sum % 10 (ambil digit terakhir)
            # carry = sum // 10 (ambil sisa untuk iterasi berikutnya)
            #
            # Contoh:
            # sum = 2 + 5 + 0 = 7
            # digit = 7 % 10 = 7
            # carry = 7 // 10 = 0
            #
            # Contoh 2:
            # sum = 4 + 6 + 0 = 10
            # digit = 10 % 10 = 0
            # carry = 10 // 10 = 1
            #
            total = val1 + val2 + carry
            digit = total % 10
            carry = total // 10
            
            # ═════════════════════════════════════════════════════
            # STEP 2D: Buat node baru dan tambahkan ke linked list
            # ═════════════════════════════════════════════════════
            #
            # Buat node baru dengan digit
            # Tambahkan ke posisi current.next
            # Pindahkan current ke node yang baru dibuat
            #
            current.next = ListNode(digit)
            current = current.next
            
            # ═════════════════════════════════════════════════════
            # STEP 2E: Pindah ke node berikutnya di l1 dan l2
            # ═════════════════════════════════════════════════════
            #
            # Jika l1 masih ada, lanjut ke node berikutnya
            # Jika l1 habis, tetap None
            #
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
        # ═══════════════════════════════════════════════════════════
        # STEP 3: Return dummy.next
        # ═══════════════════════════════════════════════════════════
        #
        # dummy.next adalah node pertama hasil
        # (dummy sendiri tidak termasuk)
        #
        return dummy.next


# ═══════════════════════════════════════════════════════════════
# TEST CASES (JALANKAN DAN LIHAT OUTPUT)
# ═══════════════════════════════════════════════════════════════

print("=" * 80)
print("TESTING Q4: Add Two Numbers (Linked List)")
print("=" * 80 + "\n")

sol = Solution()

# TEST 1: l1 = [2,4,3], l2 = [5,6,4] → Output: [7,0,8]
# ═══════════════════════════════════════════════════════════════
print("TEST 1: l1 = [2,4,3], l2 = [5,6,4]")
print("-" * 80)
print("PENJELASAN:")
print("  l1 = [2,4,3] → angka 342 (reverse)")
print("  l2 = [5,6,4] → angka 465 (reverse)")
print("  342 + 465 = 807")
print("  Output: [7,0,8] (reverse)")
print()
print("TRACE EXECUTION:")
print()

l1_arr = [2, 4, 3]
l2_arr = [5, 6, 4]
print(f"  Input l1: {l1_arr}")
print(f"  Input l2: {l2_arr}")
print()

# Manual trace
carry = 0
for i in range(max(len(l1_arr), len(l2_arr))):
    val1 = l1_arr[i] if i < len(l1_arr) else 0
    val2 = l2_arr[i] if i < len(l2_arr) else 0
    total = val1 + val2 + carry
    digit = total % 10
    carry = total // 10
    print(f"  Step {i+1}: {val1} + {val2} + {carry-carry if i > 0 else 0} = {total}")
    print(f"    digit = {total} % 10 = {digit}")
    print(f"    carry = {total} // 10 = {carry}")
    print()

l1 = list_to_linkedlist(l1_arr)
l2 = list_to_linkedlist(l2_arr)
result = sol.addTwoNumbers(l1, l2)
result_arr = linkedlist_to_list(result)

print(f"HASIL: {result_arr}")
print(f"PENJELASAN: 342 + 465 = 807 ✓\n")

# TEST 2: l1 = [0], l2 = [0] → Output: [0]
# ═══════════════════════════════════════════════════════════════
print("TEST 2: l1 = [0], l2 = [0]")
print("-" * 80)
print("PENJELASAN:")
print("  l1 = [0] → angka 0")
print("  l2 = [0] → angka 0")
print("  0 + 0 = 0")
print("  Output: [0]")
print()

l1 = list_to_linkedlist([0])
l2 = list_to_linkedlist([0])
result = sol.addTwoNumbers(l1, l2)
result_arr = linkedlist_to_list(result)

print(f"HASIL: {result_arr}")
print(f"PENJELASAN: 0 + 0 = 0 ✓\n")

# TEST 3: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9] → Output: [8,9,9,9,0,0,0,1]
# ═══════════════════════════════════════════════════════════════
print("TEST 3: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]")
print("-" * 80)
print("PENJELASAN:")
print("  l1 = [9,9,9,9,9,9,9] → angka 9,999,999")
print("  l2 = [9,9,9,9] → angka 9,999")
print("  9,999,999 + 9,999 = 10,009,998")
print("  Output: [8,9,9,9,0,0,0,1] (reverse)")
print()
print("TRACE EXECUTION:")
print()

l1_arr = [9,9,9,9,9,9,9]
l2_arr = [9,9,9,9]
print(f"  Input l1: {l1_arr}")
print(f"  Input l2: {l2_arr}")
print()

carry = 0
for i in range(max(len(l1_arr), len(l2_arr))):
    val1 = l1_arr[i] if i < len(l1_arr) else 0
    val2 = l2_arr[i] if i < len(l2_arr) else 0
    prev_carry = carry
    total = val1 + val2 + carry
    digit = total % 10
    carry = total // 10
    print(f"  Step {i+1}: {val1} + {val2} + {prev_carry} = {total} → digit={digit}, carry={carry}")

print()

l1 = list_to_linkedlist([9,9,9,9,9,9,9])
l2 = list_to_linkedlist([9,9,9,9])
result = sol.addTwoNumbers(l1, l2)
result_arr = linkedlist_to_list(result)

print(f"HASIL: {result_arr}")
print(f"PENJELASAN: 9,999,999 + 9,999 = 10,009,998 ✓\n")
