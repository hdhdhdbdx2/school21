# E4 konverti. Miqdor uchun chegirma

Do‘kondan xabar:

«Kichik aksiya sinab ko‘ramiz: bitta tovardan uchta yoki undan ko‘p birlik xarid qilinganda o‘n foizlik chegirma beramiz».

## Yangi shart

Miqdor 3 yoki undan ko‘p bo‘lsa, yakuniy qiymat `price * quantity * 9 // 10` ga teng. Butun buyurtmaning yakuniy qiymati pastga yaxlitlanadi. 1 va 2 miqdori uchun narx avvalgidek.

Har biri 50 dan uchta stiker to‘plami 135 turadi. Bir birlik narxi 51 bo‘lsa, uchtasi 137 turadi. Shaxsiy limitlar va qoldiqlar saqlanadi: aksiya limit 1 bo‘lganda uchta xudi olishga ruxsat bermaydi.

Balansni tekshirish, yechish va qiymatni yozish chegirmali summadan foydalanadi. Bekor qilishda aynan yechilgan summa qaytariladi. Vosita sxemalari va javob maydonlari o‘zgarmaydi.

## Sizning ishingiz

Fayllar bo‘yicha taxminni yozing, hisobni o‘zgartiring va eski narx bilan chegirmani farqlaydigan test qo‘shing. Birinchi urinish — 45 daqiqa; SI va qidiruv tizimi mavjud.

~~~bash
python3 -m pytest -q
python3 checks/acceptance.py --project . --profile E4
~~~

Topshirish profili — E4.

