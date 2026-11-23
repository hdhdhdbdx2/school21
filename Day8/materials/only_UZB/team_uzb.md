# Jamoada ishni qanday taqsimlash kerak

Loyiha boshida taqsimot uchun 15 daqiqa ajrating. Birga namoyishni ishga tushiring, quyidagi to‘rt yo‘nalishni o‘qing va har birini kim olishini tanlang. Yetakchi — to‘rt ishtirokchidan biri; uning ham o‘z kodi bor.

| Yo‘nalish | Asosiy fayllar | Nima qilish kerak | Jamoaga nima topshiriladi |
| --- | --- | --- | --- |
| Yetakchi va o‘qish vositalari | `read_handlers.py`, `contracts/tools_schemas.json` | Katalog, balans va holatni tugatish; vositalar tavsiflarini yig‘ish; o‘zgarishlarni birlashtirish | To‘rtta ishlaydigan o‘qish vositasi va umumiy ishga tushadigan tarmoq |
| Qoidalar va testlar | `domain.py`, `testing/test_rules.py` | Qiymat va qaytarishni hisoblash; xarid, bekor qilish va berishni tekshirish; qoidalar testlarini yozish | Kirish ma’lumotlari va kutilgan javoblar misollari bilan qoida funksiyalari |
| Ma’lumotlar | `storage.py` | SQL so‘rovlari, buyurtmani yozish, yechish va qaytarishni bitta tranzaksiyada amalga oshirish | Tayyor signaturali saqlash metodlari; jadvallar o‘zgarishini tushuntirish |
| Buyurtma amallari | `order_handlers.py`, `testing/test_orders.py` | Tekshiruvlar va yozishni bog‘lash; yaratish, bekor qilish va berishni tugatish | Uchta ishlaydigan amal va rad etish testlari |

Metod nomlari va ma’lumot shakllari shablonda allaqachon belgilangan. Ichki metodni o‘zgartirmoqchi bo‘lsangiz, avval uni chaqirayotgan odam bilan kelishing. Boshqalarning asosiy faylini bir vaqtda tahrirlamang.

## Taqsimotdan keyingi dastlabki yarim soat

Yetakchi tavsiflarni tugatadi va katalogni o‘qishni boshlaydi. Qoidalar uchun mas’ul ishtirokchi oddiy sonlarda qiymat hisobini tekshiradi va birinchi testni yozadi. Ma’lumotlar uchun mas’ul ishtirokchi foydalanuvchilar va buyurtmalarni o‘qishdan boshlaydi. Amallar uchun mas’ul ishtirokchi tayyor ishlov beruvchini tahlil qiladi va xarid tekshiruvlari tartibini tuzadi.

Buyurtmani yozish tayyor bo‘lmaguncha qoidalarni alohida tekshirish mumkin. Ishlov beruvchi ustida ishlash uchun saqlash muallifi bilan qaytariladigan lug‘at namunasi haqida kelishing; vaqtinchalik almashtirishni faqat testda ishlating, uni SQL o‘rniga topshirmang.

## Qachon yig‘ilish kerak

1. Namoyishdan keyin — taqsimot va signaturalar haqida kelishuv.
2. O‘qish va qoidalar paydo bo‘lgandan keyin — birinchi umumiy xarid chaqiruvi.
3. 08-kun oxirida — umumiy tarmoqdan ishga tushirish va tugallanmagan ishlar ro‘yxati.
4. 09-kunning bazaviy tekshiruvlaridan keyin — konvert va o‘zgarish bo‘yicha ishni taqsimlash.
5. Topshirishdan oldin — yo‘riqnoma bo‘yicha ishga tushirish va tushuntirishning qisqa mashqi.

Git uchun umumiy `develop` tarmog‘i va alohida ishchi tarmoqlar yetarli. O‘zgarishlarni umumiy tarmoqqa navbat bilan birlashtiring. Birlashtirishdan oldin muallif qaysi buyruqni ishga tushirgani va u nimani tekshirganini ko‘rsatadi. Yetakchi qabul qilingan o‘zgarishlar faqat kimningdir kompyuterida qolib ketmasligini kuzatadi.

Agar 15 daqiqa davomida boshqa qism sababli ishni davom ettira olmasangiz, jamoaga ayting: qaysi metod kerak, qanday natija kutyapsiz va hozirning o‘zida nimani tekshirish mumkin. Bahsda avval qoida va misolni ifodalang. Kelishib bo‘lmasa, yetakchi yechimni tanlaydi va sababini yozadi.

## Tarkib o‘zgargan bo‘lsa

To‘rt kishi — tavsiya. Tarkib kichikroq bo‘lsa, yo‘nalishlarni quyidagicha birlashtiring va `docs/team.md` ni yangilang:

| Tarkib | Yo‘nalishlar |
| --- | --- |
| Uch kishi | 1) Yetakchi, o‘qish vositalari va kontraktlar; 2) Qoidalar va testlar; 3) Ma’lumotlar va buyurtma amallari — `storage.py` va `order_handlers.py` bitta tranzaksiya bilan bog‘langan, ularni bir odam yuritgani qulayroq |
| Ikki kishi | 1) Yetakchi, o‘qish vositalari, kontraktlar, qoidalar va ularning testlari; 2) Ma’lumotlar va buyurtma amallari, rad etish testlari |

`docs/` va `RUN.md` hujjatlarini teng taqsimlang. Tarkib kattaroq bo‘lsa, shu yo‘nalishlar ustida juftlikda ishlang. Majburiy qism hajmi oshmaydi. Yetakchi ketgan bo‘lsa, jamoa yangisini tanlaydi; platformada tarkib o‘zgarishi xodimlar orqali rasmiylashtiriladi.

Taqsimot hujjati ishni tashkil etishga yordam beradi. U bo‘yicha shaxsiy hissa hisoblanmaydi va individual baho qo‘yilmaydi.

