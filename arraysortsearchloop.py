data = ["nike","adidas","puma","dk","converse"]
print("data asli:", data)

pencari = input("masukkan pencarian: ")
if pencari in data:
    print("data ditemukan")
else:
    print("data tidak ditemukan")

print("data di loop")
i = 0
while i < len(data):
    print("Brand:", data[i])
    i += 1
    
print("data diurutkan atau sorting berdasarkan abjad")
data.sort()
print(data)

print("data di loop dan sudah versi sort")
i = 0
while i < len(data):
    print("Brand:", data[i])
    i += 1


