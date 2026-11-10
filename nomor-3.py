x = float(input("Masukan koordinat x: "))
y = float(input("Masukan koordinat y: "))

print("\n")

if x<-30 or x>30 or y<-30 or y>30:
    print("Koordinat tidak valid")
else:
    if x==0 and y==0:
        print("Titik berada di titik pusat dan tidak termasuk kuadran mana pun")
    elif x==0 and y!=0:
        posisi = "positif" if y>0 else "negatif"
        print(f"Titik berada pada sumbu Y bagian {posisi}.")
    elif y==0 and x!=0:
        posisi = "positif" if x>0 else "negatif"
        print(f"Titik berada pada sumbu X bagian {posisi}.")
    else:
        if x>0 and y>0:
            fungsi = "f(x,y) = x^2 + y^2"
            hasil = (x**2) + (y**2)
            posisi = "Kuadran I"
        elif x<0 and y>0:
            fungsi = "f(x,y) = x^2 - y^2"
            hasil = (x**2)-(y**2)
            posisi = "Kuadran II"
        elif x<0 and y<0:
            fungsi = "f(x,y) = 2x + 3y"
            hasil = 2*x+3*y
            posisi = "Kuadran III"
        elif x>0 and y<0:
            fungsi = "f(x,y) = x^2 + 2y"
            hasil = (x**2)+2*y
            posisi = "Kuadran IV"
        print("=== HASIL ANALISIS TITIK ===")
        print(f"Koordinat: ({x},{y})")
        print(f"Posisi: {posisi}")
        print(f"Fungsi: {fungsi}")
        print(f"Hasil: {hasil:.2f}")