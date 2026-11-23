# E2 konverti. Bir martada ikkitadan ko‘p emas

Do‘kondan xabar:

«Buyurtma berish joyida navbat paydo bo‘ldi. Hozircha bitta buyurtmani ikkita tovar birligi bilan cheklaymiz».

## Yangi shart

Bitta buyurtmada ikkitadan ko‘p birlik bo‘lishi mumkin emas. Miqdori 3 yoki undan ko‘p buyurtma, tovarning shaxsiy limiti yuqoriroq bo‘lsa ham, `USER_LIMIT_EXCEEDED` oladi.

Masalan, bir martada uchta stiker to‘plamini xarid qilib bo‘lmaydi, ikkita — mumkin. Bir nechta alohida buyurtma orqali ishtirokchi hali ham beshtagacha stiker to‘plamini olishi mumkin: tovarning umumiy limiti saqlanadi.

Yangi chegara shaxsiy limit bilan birga, omborda mavjudlikdan keyin va balansdan oldin tekshiriladi. Narx, qaytarish, vosita sxemalari va eng kam miqdor 1 o‘zgarmaydi.

## Sizning ishingiz

Tahrirdan oldin taxminiy fayllarni `docs/change.md` ga yozing. Qoidani amalga oshiring va 2 hamda 3 miqdori uchun testlar qo‘shing. Birinchi urinish — 45 daqiqa. SI va qidiruv tizimi mavjud.

~~~bash
python3 -m pytest -q
python3 checks/acceptance.py --project . --profile E2
~~~

O‘zgarish bajarilgandagi topshirish profili — E2.

