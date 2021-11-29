# Meeting Organizer

Müşteriler ile yapılacak toplantıların kaydedilebileceği, güncellenebileceği ve silinebileceği bir tek sayfa uygulamasıdır.

## Proje İçeriği
* Toplantı Kayıt Formu
* Toplantı Güncelleme Formu
* Toplantı Listesi
* WEB API Backend

## Toplantı Kayıt Formu
Kullanıcıların toplantıya ait bilgileri girebilecekleri ara yüz. Toplantı için formda alınması gereken
özellikler;
* Toplantı Konusu
* Tarih
* Başlangıç Saati
* Bitiş Saati
* Katılımcılar

## Toplantı Güncelleme Formu
Kullanıcıların toplantı bilgilerini güncelleyebilecekleri ara yüz.
Kullanıcıların eklenen toplantıları;
* görüntüleyebilecekleri,
* düzenleyebilecekleri,
* silebilecekleri
bir arayüz içerir.


## Uygulamayı Başlat

Uygulamanın başlatılması için aşağıdaki

```bash
python app.py
```
komutu kullanınız.

## Gerekli Kütüphaneler

```
pip install flask
pip install flask_sqlalchemy
```
## Ekran Görüntüleri

### Anasayfa

![home](/static/home.JPG)

### Toplantı Ekleme 

![add](/static/add.JPG)
![add_message](/static/add_message.JPG)

### Toplantı Güncelleme 

![edit](/static/edit.JPG)
![edit_message](/static/edit_message.JPG)

### Toplantı Silme

![delete](/static/delete.JPG)
![delete_message](/static/delete.JPG)