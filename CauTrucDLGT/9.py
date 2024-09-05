def thap_ha_noi(n, a, b, c):
    if n == 1:
        print(f"Chuyen dia tu 1 cot  {a} sang cot {c}")
        return
    thap_ha_noi(n - 1, a, c, b)
    print(f"Chuyen dia {n} tu cot {a} sang cot {c}")
    thap_ha_noi(n - 1, b,a, c)
 
n = int(input("Nhap so dia: "))
thap_ha_noi(n, 'A', 'B', 'C')
