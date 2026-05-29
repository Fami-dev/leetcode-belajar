# 11 - Math - Digit Sum Minimum

Folder ini dibuat untuk latihan konsep yang mirip dengan soal LeetCode **3300. Minimum Element After Replacement With Digit Sum**.

Tujuan belajar:

- Memahami fungsi Python yang dibutuhkan dalam kode.
- Memahami cara menjumlahkan digit angka.
- Memahami cara melakukan looping pada list.
- Memahami cara mencari nilai minimum.
- Berlatih dengan contoh soal serupa, bukan langsung dari LeetCode.

---

## 1. Gambaran Masalah

Kita memiliki sebuah list berisi angka.

Contoh:

```python
nums = [10, 12, 13, 14]
```

Setiap angka perlu diganti dengan jumlah digitnya.

```text
10 -> 1 + 0 = 1
12 -> 1 + 2 = 3
13 -> 1 + 3 = 4
14 -> 1 + 4 = 5
```

Setelah itu, cari nilai paling kecil.

```text
[1, 3, 4, 5]
```

Nilai minimum adalah:

```text
1
```

---

## 2. Fungsi dan Konsep Python yang Perlu Dipelajari

### A. Function

Function digunakan untuk membuat kode lebih rapi dan bisa dipakai ulang.

Contoh:

```python
def digit_sum(num):
    total = 0
    for digit in str(num):
        total += int(digit)
    return total
```

Penjelasan:

- `def` digunakan untuk membuat fungsi.
- `digit_sum` adalah nama fungsi.
- `num` adalah parameter atau input fungsi.
- `return` digunakan untuk mengembalikan hasil.

Contoh penggunaan:

```python
print(digit_sum(123))
```

Output:

```text
6
```

Karena:

```text
1 + 2 + 3 = 6
```

---

### B. Looping dengan `for`

Looping digunakan untuk mengulang proses.

Dalam soal ini, kita perlu mengecek setiap angka di dalam list.

Contoh:

```python
nums = [10, 12, 13, 14]

for num in nums:
    print(num)
```

Output:

```text
10
12
13
14
```

Artinya, Python membaca angka satu per satu dari list.

---

### C. Mengubah Angka Menjadi String dengan `str()`

Untuk membaca digit satu per satu, angka bisa diubah menjadi string.

Contoh:

```python
num = 123
text = str(num)
```

Sekarang `text` berisi:

```python
"123"
```

Karena sudah menjadi string, kita bisa mengambil digitnya satu per satu.

```python
for digit in str(123):
    print(digit)
```

Output:

```text
1
2
3
```

Catatan:

- Digit yang keluar masih berbentuk teks/string.
- Agar bisa dijumlahkan, harus diubah menjadi integer.

---

### D. Mengubah String Menjadi Angka dengan `int()`

Jika digit masih berupa string, kita tidak bisa langsung menjumlahkannya sebagai angka.

Contoh:

```python
digit = "5"
angka = int(digit)
```

Sekarang `angka` bernilai integer `5`.

Dalam digit sum:

```python
total += int(digit)
```

Artinya:

```text
tambahkan nilai digit ke total
```

---

### E. Operator `+=`

Operator `+=` digunakan untuk menambahkan nilai ke variabel yang sudah ada.

Contoh:

```python
total = 0
total += 5
```

Sama artinya dengan:

```python
total = total + 5
```

Jika:

```python
total = 0
```

Lalu:

```python
total += 1
total += 2
total += 3
```

Maka hasil akhirnya:

```python
total = 6
```

---

### F. Mencari Nilai Minimum dengan `min()`

Python memiliki fungsi bawaan `min()` untuk mencari nilai terkecil.

Contoh:

```python
nums = [5, 2, 8, 1]
print(min(nums))
```

Output:

```text
1
```

Dalam soal digit sum, kita bisa membuat list baru berisi hasil jumlah digit, lalu mengambil nilai minimumnya.

Contoh:

```python
hasil = [1, 3, 4, 5]
print(min(hasil))
```

Output:

```text
1
```

---

## 3. Solusi Bertahap

### Tahap 1: Membuat fungsi jumlah digit

```python
def digit_sum(num):
    total = 0

    for digit in str(num):
        total += int(digit)

    return total
```

Contoh:

```python
print(digit_sum(999))
```

Output:

```text
27
```

---

### Tahap 2: Mengubah semua angka dalam list menjadi digit sum

```python
nums = [10, 12, 13, 14]
result = []

for num in nums:
    result.append(digit_sum(num))

print(result)
```

Output:

```text
[1, 3, 4, 5]
```

---

### Tahap 3: Mengambil nilai minimum

```python
answer = min(result)
print(answer)
```

Output:

```text
1
```

---

## 4. Solusi Lengkap Versi Mudah Dibaca

```python
def digit_sum(num):
    total = 0

    for digit in str(num):
        total += int(digit)

    return total


def minimum_digit_sum(nums):
    result = []

    for num in nums:
        result.append(digit_sum(num))

    return min(result)


nums = [10, 12, 13, 14]
print(minimum_digit_sum(nums))
```

Output:

```text
1
```

---

## 5. Solusi Versi Lebih Singkat

```python
def minimum_digit_sum(nums):
    return min(sum(int(digit) for digit in str(num)) for num in nums)
```

Versi ini lebih pendek, tetapi untuk pemula lebih baik memahami versi bertahap terlebih dahulu.

---

## 6. Cara Berpikir Saat Mengerjakan

Gunakan urutan ini:

1. Ambil satu angka dari list.
2. Ubah angka menjadi string.
3. Ambil setiap digit.
4. Ubah digit menjadi integer.
5. Jumlahkan semua digit.
6. Ulangi untuk semua angka.
7. Ambil hasil jumlah digit yang paling kecil.

---

## 7. Materi Tambahan: Cara Matematika dengan Modulo

Selain memakai `str()`, digit sum juga bisa dibuat dengan `%` dan `//`.

```python
def digit_sum_math(num):
    total = 0

    while num > 0:
        digit = num % 10
        total += digit
        num = num // 10

    return total
```

Penjelasan:

- `% 10` mengambil digit terakhir.
- `// 10` menghapus digit terakhir.

Contoh:

```text
123 % 10 = 3
123 // 10 = 12
```

Untuk pemula, cara `str()` biasanya lebih mudah dipahami.
