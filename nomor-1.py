# Memproses salah satu contoh data pelamar 
data_mentah = "  LKND[budi santoso | DATA ANALYST | teknik informatika | 3.82]  "

data_bersih = data_mentah.strip()

indeks_buka = data_bersih.find("[")
indeks_tutup = data_bersih.find("]")

kode_situs = data_bersih[0:indeks_buka].strip()
isi_data = data_bersih[indeks_buka + 1 : indeks_tutup] 

batas1 = isi_data.find("|")
nama = isi_data[0:batas1].strip().title()

sisa1 = isi_data[batas1 + 1 :]

batas2 = sisa1.find("|")
pekerjaan = sisa1[0:batas2].strip().title()

sisa2 = sisa1[batas2 + 1 :]

batas3 = sisa2.find("|")
jurusan = sisa2[0:batas3].strip().title()

ipk = sisa2[batas3 + 1 :].strip()

situs_lamaran = ""
if kode_situs == "LKND":
    situs_lamaran = "LinkedIn"
else:
    if kode_situs == "GLNTS":
        situs_lamaran = "Glints"
    else:
        if kode_situs == "JSTRT":
            situs_lamaran = "Jobstreet"
        else:
            if kode_situs == "KMPAS":
                situs_lamaran = "Kompas Karir"
            else:
                if kode_situs == "KTAKA":
                    situs_lamaran = "KitaLulus"

print(f"nama = {nama}")
print(f"Pekerjaan yang dilamar = {pekerjaan}")
print(f"situs lamaran = {situs_lamaran}")
print(f"jurusan = {jurusan}")
print(f"ipk = {ipk}")