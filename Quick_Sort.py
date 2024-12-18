# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 14:03:24 2024

@author: chana
"""
import time

start_time = time.time()


with open("mm.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()


def QuickSort(a_list, start, end):
    if start < end:
        pIndex = QuickSort_partition(a_list, start, end)  
        QuickSort(a_list, start, pIndex - 1)  
        QuickSort(a_list, pIndex + 1, end)    
    return a_list

# ฟังก์ชันแบ่งลิสต์และหาตำแหน่ง pivot
def QuickSort_partition(a_list, start, end):
    pivot = a_list[end] 
    pIndex = start       
    
    for i in range(start, end):
        if a_list[i] >= pivot:
            a_list[i], a_list[pIndex] = a_list[pIndex], a_list[i]  
            pIndex += 1
    a_list[pIndex], a_list[end] = a_list[end], a_list[pIndex]  
    return pIndex


QuickSort(lines, 0, len(lines) - 1)

end_time = time.time()
elapsed_time = end_time - start_time


for line in lines:
    print(line.strip())  # ลบ \n ออกเมื่อแสดงผล
    
print(f"เวลาที่ใช้: {elapsed_time:.6f} วินาที")
