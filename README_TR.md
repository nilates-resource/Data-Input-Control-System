Kullanıcı Kayıt ve Veri Doğrulama Sistemi
Bu proje, veri bütünlüğünü sağlamak amacıyla tasarlanmış Python tabanlı bir araçtır. Kullanıcı kayıtları sırasında hatalı veri girişini ("kirli veri") engellemek için katı doğrulama kuralları uygular.

Öne Çıkan Özellikler
Telefon Numarası Doğrulaması: Numaranın tam 11 haneli olması, "05" ile başlaması ve sadece rakamlardan oluşması denetlenir.
Veri Tipi Güvenliği: `isalpha()` ve `isdigit()` kontrolleri ile isim ve doğum yeri alanlarına hatalı karakter girişi önlenir.
Kalıcı Veri Depolama: Doğrulanan veriler, mevcut kayıtları koruyacak şekilde "Ekleme (Append - a)" moduyla otomatik olarak `.txt` dosyasına kaydedilir.
Hata Yönetimi: Geçersiz girişlerde kullanıcıya anlık geri bildirim vererek doğru veri girilene kadar yönlendirme yapar.

Teknik Detaylar
Dil: Python 3.x
Veri Yapıları: Bellek içi veri yönetimi için iç içe geçmiş sözlükler (Nested Dictionaries).
Dosya İşlemleri: Metin tabanlı kalıcı depolama.

İş Mantığı (Business Logic)
İş dünyasında, toplandıktan sonra veriyi temizlemek maliyetli ve zaman alıcıdır. Bu script, veriyi "kaynağında doğrulama" yaklaşımını sergilemektedir. Bu, sağlıklı veri setleri oluşturmak için kritik bir yetkinliktir.
