# Serverni qanday tekshirish kerak

Test — kirish ma’lumotlari va kutilgan natija tekshiruvi bor kod. `testing/test_example.py` faylida tayyor vosita misoli bor: u vaqtinchalik baza yaratadi va qaytarilgan tovarni tekshiradi. Ishga tushirish:

~~~bash
python3 -m pytest -q
~~~

Qiymat qoidasi amalga oshirilgandan keyin uni tekshirish misoli:

~~~python
from src.domain import calculate_total

def test_two_bottles_cost_300():
    assert calculate_total(150, 2) == 300
~~~

Funksiya boshqa son qaytarsa, assert testni to‘xtatadi va pytest qaysi kutilma buzilganini ko‘rsatadi. Bunday kodni nomi test_ bilan boshlanadigan faylga saqlang.

O‘z testlaringizni qo‘shing. Kamida uchta mazmunli holat tanlang: qiymatni to‘g‘ri hisoblash; holat o‘zgarmaydigan xarid rad etilishi; buyurtma bilan takroriy amal. Bu ishlab chiqishdagi eng kam yordam, to‘liqlik kafolati emas. Konvert uchun yangi shartning alohida testi kerak bo‘ladi.

Rad etish uchun avval jadvallar holatini saqlang, so‘rovni bajaring va undan keyingi holatni solishtiring. Faqat to‘g‘ri xato kodi yetarli emas: server koinlarni yechishga ulgurgan bo‘lishi mumkin.

## Umumiy tekshiruv

~~~bash
python3 checks/acceptance.py --project . --profile base
~~~

U haqiqiy MCP serverini alohida jarayon sifatida ishga tushiradi, vaqtinchalik papkada o‘z o‘quv ma’lumotlaridan foydalanadi, vositalar ro‘yxati, sxemalar, xaridlar, bekor qilishlar, berish, xatolar va rad etish hamda qayta ishga tushirishdan keyingi baza holatini tekshiradi. Ishchi bazangiz qatnashmaydi.

Konvert uchun `base` ni `E1`, `E2`, `E3`, `E4` yoki `E5` ga almashtiring. Profil kutilgan natijani faqat shart o‘zgargan joyda o‘zgartiradi. Buyruqdagi raqamning o‘zi server xatti-harakatini o‘zgartirmaydi.

Tekshiruvlar ochiq: ularni o‘qish mumkin. Noto‘g‘ri xatti-harakatni qabul qilish uchun tayyor tekshiruvlarni tuzatish mumkin emas. Qabul qilishda tekshiruvchining boshlang‘ich nusxasi ishlatiladi.

Konvert profili bilan ishga tushirish o‘tmasa, o‘zgarishni tugating yoki kodni bazaviy qoidalarga qaytaring va `base` ni topshiring. Buni `docs/change.md` faylida qayd eting.

Tekshiruvlar qasddan zararli Python kodidan himoya emas. Ular xatolarni aniqlashga, jamoa tushuntirishi esa uning yechimini tushunishga yordam beradi.

