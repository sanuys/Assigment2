# -*- coding: utf-8 -*-
"""
Created on Thu Dec 12 14:32:36 2024

@author: chana
"""
import time

start_time = time.time()

with open("mm.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()  # อ่านไฟล์ทีละบรรทัดแล้วเก็บในลิสต์
    
def MergeSort(a_list):
    n = len(a_list)

    if n < 2:
        return a_list

    mid = n // 2
    left = a_list[:mid]
    right = a_list[mid:]

    MergeSort(left)
    MergeSort(right)

    i = 0  # index for left
    j = 0  # index for right
    k = 0  # index for merged list

    while i < len(left) and j < len(right):
        if left[i] > right[j]:
            a_list[k] = left[i]
            i = i + 1
        else:
            a_list[k] = right[j]
            j = j + 1
        k = k + 1

    while i < len(left):
        a_list[k] = left[i]
        i = i + 1
        k = k + 1

    while j < len(right):
        a_list[k] = right[j]
        j = j + 1
        k = k + 1

    return a_list

a = MergeSort(lines)

sorted_lines = MergeSort(lines)
end_time = time.time()
elapsed_time = end_time - start_time

for line in a:
    print(line.strip())

print(f"เวลาที่ใช้: {elapsed_time} วินาที")

