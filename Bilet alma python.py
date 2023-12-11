# Cinema Uygulamasi
# Ozellikler:
#	Bilet satis
# 	Bilet iptal
# 	En populer filmlerin listelenmesi
# 	Vizyondaki filmlerin listelenmesi
# 	Biletlerin listelenmesi
# 	Geri donus ve tavsiye verilmesi

# alinan biletleri tutan liste

biletler = []

# populer filmlerin listesi

populer_filmeler = [
	"The Shawshank Redemption",
	"The Godfather",
	"The Dark Knight",
	"The Godfather Part II",
	"12 Angry Man"
]

# vizyondaki filmlerin listesi

inTheaters = [
	"The Shawshank Redemption",
	"The Godfather",
	"The Dark Knight",
	"The Godfather Part II",
	"12 Angry Man",
	"Schindler's List",
	"The Return of the King",
	"Pulp Fiction",
	"The Fellowship of the Ring",
	"The Good, the Bad and the Ugly"
]

def printMenu():
	# Menudeki secenekleri yazdiran fonksiyon

	print("\n1-En populer filmler")
	print("2-Vizyondaki filmler")
	print("3-Biletlerimi gor")
	print("4-Onerileriniz ve Tavsiyeleriniz")
	print("0-Cikis")

def printMovies(movieList):
	# input olarak bi film listesi alir
	# aldigi listedeki butun filmeri tek tek yazdirir

	for i in range(len(movieList)):
		print(i,'-',movieList[i])

'''
Program basaladiginda ilk basta tek sefer yazilan
hos geldin yazisi
'''

print("sinema uygulamasina hos geldiniz")

# Sonsuz dongu
while (True):

	# Menuyu yazdir
	printMenu();
	
	# Kullanicidan secmesini bekle
	uc = int(input("Sec:"))

	# 0 secerse donguden cik ve programi bitir
	if (uc == 0):
		break

	# 1 secerse populer filmleri yazdir
	elif (uc == 1):
		
		# Filmleri yazdir
		printMovies(populer_filmeler)

		# 0-Geri yaz ve kullanicinin secmesini bekle
		print("\n0-Geri")
		uc = int(input("Sec:"))

		# eger 0 secerse dongunun basina git ve menuyu
		# yeniden baslat
		if (uc == 0):
			continue
		
		# eger olmayan bir secenek girilirse kullanici
		# uyarilir ve menuye geri yonlendirilir
		else:
			# kullanici uyarilir
			print("boyle bir secenek yok")
			print("menuye geri yonlendiriliyorsunuz")
			
			# menuye geri yonlendirilir
			continue

	# 2 secerse vizyondaki filmleri yazdir ve eger
	# isterse bilet almasi icin gerekli bilgileri iste
	elif (uc == 2):
		
		# Filmleri yazdir
		printMovies(inTheaters)

		# Secenekleri yaz ve kullanicidan giris yapmasini
		# bekle
		print("\n1-Bilet Al")
		print("0-Geri")
		uc = int(input("Sec:"))

		# Eger 0 girerse menuye geri don
		if (uc == 0):
			continue

		# Eger 1 girerse gerekli bilgileri iste ve bilet
		# olusturup bileti biletlere ekle
		elif (uc == 1):
			
			# Kullanicinin ismi sorulur
			name = input("Isim:")

			# Istenilen filmin numarasi sorulur
			movieCode = int(input("Film no:"))

			# Gidilmek istenen gosterim saati sorulur
			time = input("Saat [13:00, 15:00, 17:00, 19:30]:")

			# Koltuk numarasi secilmesi istenir
			koltuk = int(input("Koltuk No (1-30):"))

			# Bos bir liste olusturulur, bu liste yeni biletin
			# bilgilerini bulundurucak
			bilet = []

			# Bilgilerin bilet listesine eklenmesi
			bilet.append(name)
			bilet.append(inTheaters[movieCode])
			bilet.append(time)
			bilet.append(koltuk)

			# Yeni biletin biletler listesine eklenmesi
			biletler.append(bilet)

			# Kullaniciya biletin basariyla satin alindigi bildirilir
			print("Bilet basariyla satin alindi")
		
		# eger olmayan bir secenek girilirse kullanici
		# uyarilir ve menuye geri yonlendirilir
		else:
			# kullanici uyarilir
			print("boyle bir secenek yok")
			print("menuye geri yonlendiriliyorsunuz")
			
			# menuye geri yonlendirilir
			continue

	# Kullanici eger 3 secerse biletler listesindeki butun biletler
	# yazdirilir
	# Eger hic bilet yoksa herhangi bir biletiniz bulunmamakta
	# diye uyari cumlesi bastirilir
	elif (uc == 3):
		# Biletler basligi yazdirilir
		print("=======Biletler=======")

		# Eger hic bilet yoksa herhangi bir biletiniz bulunmamakta
		# diye uyari ver
		if (len(biletler) == 0):
			print("Herhangi bir biletiniz bulunmamakta")

		# Eger bilet varsa
		else:
			
			# Biletlerdeki her bir bilet icin isim, film ismi
			# saat ve koltuk no sunu yazdir
			# Ayrica bilet no sunu yazdirir (silme islemi icin sonradan eklendi)
			for bilet in biletler:
				print("isim:", bilet[0])
				print("Bilet no:", biletler.index(bilet))
				print("Film:", bilet[1])
				print("saat:", bilet[2])
				print("koltuk no:",bilet[3])
				print("=====================")

			# Kullanicidan isterse bilet iptal edebilmesi veya menuye
			# geri donebilmesi icin girdi beklenir
			# eger girdi 0 sa menuye geri doner, 1 ise bilet silmek
			# icin gerekli degerler sorulur
			print("\n0-Geri")
			print("1-Bilet iptal")

			# Kullanici secimini yapar
			uc = int(input("Sec: "))

			# Eger 0 girerse continue ile menuye geri donulur
			if (uc == 0):
				continue

			# Eger 1 girerse bilet iptal etmek istiyor demektir
			# iptal etmek istedigi biletin numarasi sorulur ve
			# biletler listesinden silinir
			elif (uc == 1):
				# Bilet numarasi sorulur
				silinecekBilet = int(input("Bilet numarasi: "))

				# Girilen bilet numarasindaki bilet biletler listesinden
				# silinir
				biletler.pop(silinecekBilet)

				# Biletin iptal edildigine dair mesaj print edilir
				print("Bilet basariyla iptal edildi")
		
			# eger olmayan bir secenek girilirse kullanici
			# uyarilir ve menuye geri yonlendirilir
			else:
				# kullanici uyarilir
				print("boyle bir secenek yok")
				print("menuye geri yonlendiriliyorsunuz")
				
				# menuye geri yonlendirilir
				continue

	# Eger kullanici 4 secerse oneri yapma bolumune yonlendirilir
	elif (uc == 4):
		# Kullanicidan oneri yazmasi istenir
		print("Onerinizi yaziniz lutfen.")
		
		# Kullanicidan oneri alinir
		oneri = input("Oneri:")

		# Kullaniciya onerisi icin tesekkur edilir
		print("Oneriniz basariyla tarafimiza aktarilmistir")
		print("Geri donusunuz icin tesekkur ederiz")

		# Menuye geri donmek icin geri secenegi bastirilir
		# ve kullanicidan giris yapmasi beklenir
		print("\n0-Geri")

		# Kullanici giris yapar
		uc = input("Sec:")

		# Eger 0 girerse menuye geri dondurur
		if (uc == 0):
			continue
		
		# eger olmayan bir secenek girilirse kullanici
		# uyarilir ve menuye geri yonlendirilir
		else:
			# kullanici uyarilir
			print("boyle bir secenek yok")
			print("menuye geri yonlendiriliyorsunuz")
			
			# menuye geri yonlendirilir
			continue
