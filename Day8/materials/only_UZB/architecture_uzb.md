# Server qanday tuzilgan

Mijoz serverni alohida jarayon sifatida ishga tushiradi va u bilan standart oqimlar orqali muloqot qiladi — bu ulanish usuli stdio deyiladi. Alohida port va brauzer kerak emas. FastMCP xabar almashishni allaqachon bajaradi.

## Kodingizning uch qismi

**Ishlov beruvchilar** vosita chaqiruvini qabul qiladi, kerakli ma’lumotlarni oladi, qoidalarga murojaat qiladi va amalni tanlaydi. O‘qish uchun bu `read_handlers.py`, buyurtmani o‘zgartirish uchun — `order_handlers.py`. Bu yerda SQL yozilmaydi.

**Qoidalar** `domain.py` ichida sonlar va lug‘atlar bilan ishlaydi. Ular summani hisoblaydi va amal joizligini hal qiladi. Bu funksiyalarni bazasiz va MCPsiz tekshirish mumkin.

**Saqlash** `storage.py` ichida SQLite’dan o‘qiydi va unga yozadi. SQL so‘rov parametrlaridan foydalanadi. Bog‘liq yozuvlar bitta tranzaksiyada bajariladi. Bu yerda kimga chegirma berilishi yoki buyurtmani bekor qilish mumkinligi hal qilinmaydi.

Tayyor ulash kodi — `server.py` va `mcp_adapter.py`. U serverni ishga tushiradi, vositalarni ro‘yxatdan o‘tkazadi va kirish turlarini tekshiradi. Majburiy qismda uni o‘zgartirish talab etilmaydi.

## Tayyor chaqiruv yo‘li

`mcp_adapter.py` ichida `get_product` ni toping. U `read_handlers.get_product` ni, ishlov beruvchi esa `Storage.get_product` ni chaqiradi. Saqlash metodi SELECT bajaradi. Ishlov beruvchi natijani muvaffaqiyatli javobga yoki xatoga aylantiradi.

Farqni o‘zingiz ko‘ring:

~~~bash
python3 client.py call get_product '{"product_id":"hoodie"}'
python3 client.py call get_product '{"product_id":"missing"}'
~~~

`logs/client.jsonl` jurnalida mijozning har bir chaqiruvi uchun vosita nomi, argumentlar va olingan javob bor. Bu haqiqiy ishga tushirish izi. U qolgan barcha so‘rovlar to‘g‘riligini isbotlamaydi.

## Tranzaksiya

`with connection:` ichida bir nechta SQL buyrug‘ini bajarish mumkin. Normal yakunlanganda ular tasdiqlanadi; istisnoda ortga qaytariladi. Koinlarni yechish va buyurtmani yozish orasiga alohida commit qo‘ymang.

Boshlang‘ich sozlash dastlabki ma’lumotlarni faqat yangi bazaga qo‘shadi. Oddiy qayta ishga tushirish sarflangan koinlar va qoldiqlarni tiklamasligi kerak.

