# E1 konverti. Saqlanib qoladigan qoldiq

Do‘kondan xabar:

«Ishtirokchilar hamma koinlarini merchga sarflashadi, keyin esa koinlar boshqa mashg‘ulotlar uchun ham kerakligini bilishadi. Yangi xariddan keyin balansda kamida 50 koin qolishi kerak».

## Yangi shart

Yechilgandan keyin 50 koin yoki undan ko‘p qolsa, xaridni bajarish mumkin. Aynan 50 — mumkin. Kamroq qolsa, `INSUFFICIENT_COINS` qaytaring. Yechishdan oldin hech narsani o‘zgartirish mumkin emas.

Balansi 180 bo‘lgan ishtirokchi 150 ga butilka xarid qila olmaydi. Balansi 200 bo‘lsa — mumkin.

Foydalanuvchi, tovar, o‘lcham va limitning oldingi tekshiruvlari saqlanadi va balans tekshiruvidan oldin bajariladi. Bekor qilish butun qiymatni qaytaradi. Vosita nomlari, argumentlar va javob maydonlari o‘zgarmaydi.

## Sizning ishingiz

Tahrirdan oldin taxminiy fayllarni `docs/change.md` ga yozing. Shartni amalga oshiring, rad etish va chegaraviy holat testini qo‘shing. Birinchi urinish — 45 daqiqa. SI va qidiruv tizimi mavjud.

~~~bash
python3 -m pytest -q
python3 checks/acceptance.py --project . --profile E1
~~~

Bu o‘zgarishni topshirsangiz, yo‘riqnoma, pasport va konvert hisobotida E1 ni ko‘rsating.

