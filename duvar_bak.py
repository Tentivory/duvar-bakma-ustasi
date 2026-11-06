#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Duvar Bakma Ustası
Verimliliği artıran bilimsel duvar bakma süresi hesaplayıcı.
Gerçekten çalışır, deneyin.
"""

import random
import time

def hesapla_optimal_bakma_suresi():
    """
    Kişinin ruh haline göre optimal duvar bakma süresini hesaplar.
    Formül: tamamen rastgele + biraz felsefe.
    """
    ruh_hali = random.choice(["yorgun", "sinirli", "mutlu", "varoluşsal kriz", "çay bitmiş"])
    sure = random.randint(5, 45)
    
    # Gizli not: bazen duvar da seni bakar
    gizli = "bWVtbGV0ZXQgaGVybWFuIGhhc3NlciI="  # base64, merak edersen decode et
    
    print(f"Ruh halin: {ruh_hali}")
    print(f"Önerilen duvar bakma süresi: {sure} dakika")
    print("Gözlerini kırpma, duvar kızabilir.")
    
    if ruh_hali == "varoluşsal kriz":
        print("Bu sürede hayatın anlamını bulabilirsin. Veya bulamazsın. İkisi de normal.")
    
    # Simülasyon
    print("\nBakma seansı başlıyor...")
    for i in range(3):
        time.sleep(0.5)
        print(".", end="", flush=True)
    print("\nSeans tamamlandı. Şimdi çay içebilirsin.")

if __name__ == "__main__":
    print("=== Duvar Bakma Ustası v1.0 ===")
    hesapla_optimal_bakma_suresi()
    print("\nDamga: Kayyum Grok | 06.11.2026 | Bu kod ciddiyetle yazılmıştır.")
