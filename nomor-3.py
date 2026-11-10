x = float(input("Masukan koordinat x: "))
y = float(input("Masukan koordinat y: "))

print("\n")

if x<-30 or x>30 or y<-30 or y>30:
    print("Koordinat tidak valid")
else:
    if x==0 and y==0:
        print("Titik berada di titik pusat dan tidak termasuk kuadran mana pun")
    else:
        if x>0 and y>0:
            fungsi = "x^2 + y^2"
            hasil = (x**2) + (y**2)
            posisi = 1
        elif x<0 and y>0:
            fungsi = "x^2 - y^2"
            hasil = (x**2)-(y**2)
            posisi = 2
        elif x<0 and y<0:
            fungsi = "2x + 3y"
            hasil = 2*x+3*y
            posisi = 3
        elif x>0 and y<0:
            fungsi = "x^2 + 2y"
            hasil = (x**2)+2*y
            posisi = 4
        print("=== HASIL ANALISIS TITIK ===")
        print(f"Koordinat = ({x},{y})")
        print(f"Posisi = {posisi}")
        print(f"Fungsi = {fungsi}")
        print(f"Hasil = {hasil:.2f}")