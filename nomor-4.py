tinggi = float(input("Tinggi Badan (cm) = "))
berat = float(input("Berat Badan (kg) = "))

if tinggi>=150 and tinggi<=160 and berat<=40 and berat<=50:
    print("Ukuran = Small (S)")
elif tinggi>=161 and tinggi<=170 and berat<=51 and berat<=60:
    print("Ukuran = Medium (M)")
elif tinggi>=171 and tinggi<=180 and berat<=61 and berat<=75:
    print("Ukuran = Large (L)")
elif tinggi>180 and berat>75:
    print("Ukuran = Extra Large (XL)")
elif tinggi>0  and berat>0:
    print("Ukuran tidak ditemukan")
else:
    print("Input tidak valid")
