# Latihan Soal Serupa - Digit Sum dan Minimum

Latihan ini dibuat agar kamu memahami pola soal tanpa langsung memakai soal LeetCode.

Materi utama:

- Function
- Looping list
- `str()`
- `int()`
- `sum()`
- `min()`
- Digit sum

---

## Latihan 1 - Jumlah Digit Satu Angka

Buat fungsi bernama `digit_sum`.

Fungsi menerima satu angka dan mengembalikan jumlah digit dari angka tersebut.

Contoh:

```python
Input: 123
Output: 6
```

Penjelasan:

```text
1 + 2 + 3 = 6
```

Contoh lain:

```python
Input: 405
Output: 9
```

Penjelasan:

```text
4 + 0 + 5 = 9
```

Template kode:

```python
def digit_sum(num):
    # tulis kode di sini
    pass

print(digit_sum(123))  # 6
print(digit_sum(405))  # 9
```

Target belajar:

- Membuat function.
- Menggunakan `str()` untuk membaca digit.
- Menggunakan `int()` untuk menjumlahkan digit.

---

## Latihan 2 - Mengubah List Menjadi List Digit Sum

Buat fungsi bernama `convert_to_digit_sum`.

Fungsi menerima list angka dan mengembalikan list baru berisi jumlah digit dari setiap angka.

Contoh:

```python
Input: [10, 12, 13, 14]
Output: [1, 3, 4, 5]
```

Penjelasan:

```text
10 -> 1 + 0 = 1
12 -> 1 + 2 = 3
13 -> 1 + 3 = 4
14 -> 1 + 4 = 5
```

Template kode:

```python
def digit_sum(num):
    total = 0
    for digit in str(num):
        total += int(digit)
    return total


def convert_to_digit_sum(nums):
    # tulis kode di sini
    pass

print(convert_to_digit_sum([10, 12, 13, 14]))  # [1, 3, 4, 5]
```

Target belajar:

- Looping pada list.
- Menggunakan fungsi bantuan `digit_sum`.
- Membuat list baru dengan `.append()`.

---

## Latihan 3 - Mencari Minimum dari Digit Sum

Buat fungsi bernama `minimum_digit_sum`.

Fungsi menerima list angka, lalu mengembalikan nilai paling kecil setelah setiap angka diubah menjadi jumlah digitnya.

Contoh:

```python
Input: [999, 19, 199]
Output: 10
```

Penjelasan:

```text
999 -> 27
19 -> 10
199 -> 19
```

Nilai minimum adalah `10`.

Template kode:

```python
def digit_sum(num):
    total = 0
    for digit in str(num):
        total += int(digit)
    return total


def minimum_digit_sum(nums):
    # tulis kode di sini
    pass

print(minimum_digit_sum([999, 19, 199]))  # 10
```

Target belajar:

- Menggabungkan digit sum dan `min()`.
- Mengerti pola utama soal.

---

## Latihan 4 - Cari Angka Asli dengan Digit Sum Terkecil

Buat fungsi bernama `number_with_smallest_digit_sum`.

Fungsi menerima list angka, lalu mengembalikan angka asli yang memiliki jumlah digit terkecil.

Contoh:

```python
Input: [88, 101, 56, 300]
Output: 101
```

Penjelasan:

```text
88 -> 16
101 -> 2
56 -> 11
300 -> 3
```

Digit sum terkecil adalah `2`, berasal dari angka `101`.

Template kode:

```python
def digit_sum(num):
    total = 0
    for digit in str(num):
        total += int(digit)
    return total


def number_with_smallest_digit_sum(nums):
    # tulis kode di sini
    pass

print(number_with_smallest_digit_sum([88, 101, 56, 300]))  # 101
```

Target belajar:

- Menyimpan nilai minimum sementara.
- Menyimpan angka asli yang berhubungan dengan minimum tersebut.

Petunjuk:

```text
smallest_sum = angka besar
answer = None
```

Lalu update jika menemukan digit sum yang lebih kecil.

---

## Latihan 5 - Hitung Berapa Angka yang Digit Sum-nya di Bawah Batas

Buat fungsi bernama `count_digit_sum_under_limit`.

Fungsi menerima list angka dan batas `limit`.

Kembalikan jumlah angka yang digit sum-nya lebih kecil atau sama dengan `limit`.

Contoh:

```python
Input: nums = [10, 29, 300, 88], limit = 3
Output: 2
```

Penjelasan:

```text
10 -> 1, masuk karena 1 <= 3
29 -> 11, tidak masuk
300 -> 3, masuk karena 3 <= 3
88 -> 16, tidak masuk
```

Jadi output-nya `2`.

Template kode:

```python
def digit_sum(num):
    total = 0
    for digit in str(num):
        total += int(digit)
    return total


def count_digit_sum_under_limit(nums, limit):
    # tulis kode di sini
    pass

print(count_digit_sum_under_limit([10, 29, 300, 88], 3))  # 2
```

Target belajar:

- Menggunakan kondisi `if`.
- Menggunakan counter.
- Menggabungkan function, loop, dan comparison.

---

# Kunci Jawaban

Coba kerjakan sendiri terlebih dahulu sebelum membuka bagian ini.

---

## Jawaban Latihan 1

```python
def digit_sum(num):
    total = 0

    for digit in str(num):
        total += int(digit)

    return total

print(digit_sum(123))
print(digit_sum(405))
```

---

## Jawaban Latihan 2

```python
def digit_sum(num):
    total = 0

    for digit in str(num):
        total += int(digit)

    return total


def convert_to_digit_sum(nums):
    result = []

    for num in nums:
        result.append(digit_sum(num))

    return result

print(convert_to_digit_sum([10, 12, 13, 14]))
```

---

## Jawaban Latihan 3

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

print(minimum_digit_sum([999, 19, 199]))
```

Versi tanpa list tambahan:

```python
def digit_sum(num):
    total = 0

    for digit in str(num):
        total += int(digit)

    return total


def minimum_digit_sum(nums):
    smallest = float("inf")

    for num in nums:
        current_sum = digit_sum(num)

        if current_sum < smallest:
            smallest = current_sum

    return smallest

print(minimum_digit_sum([999, 19, 199]))
```

---

## Jawaban Latihan 4

```python
def digit_sum(num):
    total = 0

    for digit in str(num):
        total += int(digit)

    return total


def number_with_smallest_digit_sum(nums):
    smallest_sum = float("inf")
    answer = None

    for num in nums:
        current_sum = digit_sum(num)

        if current_sum < smallest_sum:
            smallest_sum = current_sum
            answer = num

    return answer

print(number_with_smallest_digit_sum([88, 101, 56, 300]))
```

---

## Jawaban Latihan 5

```python
def digit_sum(num):
    total = 0

    for digit in str(num):
        total += int(digit)

    return total


def count_digit_sum_under_limit(nums, limit):
    count = 0

    for num in nums:
        current_sum = digit_sum(num)

        if current_sum <= limit:
            count += 1

    return count

print(count_digit_sum_under_limit([10, 29, 300, 88], 3))
```
