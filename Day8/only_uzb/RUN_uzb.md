# Do‘konni ishga tushirish

Topshirishdan oldin ushbu yo‘riqnomani to‘ldiring va tekshiring.

Qoidalar profili: base

## Muhitni tekshirish

~~~bash
python3 check_environment.py
~~~

## Namoyishni ishga tushirish

~~~bash
python3 client.py demo
~~~

## To‘liq ssenariydan o‘tish

~~~bash
python3 client.py scenario
~~~

## Boshqa mijoz uchun serverni ishga tushirish

~~~bash
python3 -m src.server
~~~

Transport — stdio. Serverning o‘zi mijoz xabarlarini kutadi; ko‘rinadigan ssenariy client.py orqali ishga tushiriladi.

## Loyihani tekshirish

~~~bash
python3 -m pytest -q
python3 checks/acceptance.py --project . --profile base
~~~

Konvertni topshirayotgan bo‘lsangiz, oxirgi buyruqda va ushbu fayl boshida profilni o‘zgartiring.

## Holat

Qo‘lda bajariladigan `client.py call` so‘rovlari va serverni bevosita ishga tushirish data/lavka.db dan foydalanadi. Qayta ishga tushirish bu bazani saqlaydi.

--db siz demo va scenario buyruqlari har safar vaqtinchalik baza yaratadi va tugagandan keyin uni o‘chiradi. Ssenariy natijasini saqlash uchun quyidagi misoldagidek --db ni ko‘rsating.
Mijoz jurnali: logs/client.jsonl.

Alohida toza o‘quv bazasini ishga tushirish uchun yangi fayl nomini ko‘rsating:

~~~bash
python3 client.py --db data/trial_01.db scenario
~~~

Fayl allaqachon mavjud bo‘lsa, holat davom ettiriladi. Namoyish uchun boshqalarning ma’lumotlarini o‘chirmang.

## Bizning so‘rov misolimiz

Buyruqni va olingan javob tushuntirishini qo‘shing.

