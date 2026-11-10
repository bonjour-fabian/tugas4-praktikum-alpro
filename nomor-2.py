user_budi = "Saya Budi@Pyton"
sandi_budi = "Budi123"

username = input("Username: ")
sandi = input("Sandi: ")

if username==user_budi and sandi ==sandi_budi:
    print("Berhasil Login")
elif username.lower()==user_budi and sandi.lower()==sandi_budi:
    print("Ada penulisan huruf kapital yang salah")
else:
    print("Gagal Login")