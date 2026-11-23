# E3 konverti. Bekor qilish komissiyasi

Do‘kondan xabar:

«Biz buyurtmani allaqachon yig‘ib qo‘ydik, uni esa bekor qilishyapti. Endi bekor qilishda yechilgan koinlarning 90 foizini qaytaramiz».

## Yangi shart

Yaratilgan buyurtmani bekor qilishda uning saqlangan qiymatining 90% ini qaytaring, qaytarish summasini butun koingacha pastga yaxlitlang. Formula: `total_price * 9 // 10`.

Qiymati 150 bo‘lgan butilka uchun 135 koin qaytadi. Ishtirokchidan 151 yechilgan bo‘lsa, yana 135 qaytadi. Tovar to‘liq qaytariladi. Limit avvalgidek bo‘shaydi.

Takroriy bekor qilish hech narsa qaytarmaydi. Berilgan buyurtmani bekor qilish mumkin emas. Tovarning joriy narxi o‘zgarishi allaqachon yaratilgan buyurtma qaytarishiga ta’sir qilmaydi.

Sxemalar o‘zgarmaydi: `cancel_order` hali ham data ichida faqat `order_id` va `status` ni qaytaradi. Qaytarish summasini `get_coin_balance` orqali balans o‘zgarishi bilan ko‘rsating.

## Sizning ishingiz

Fayllar bo‘yicha taxminni yozing, o‘zgarish kiriting va yaxlitlash yoki bir martalik qaytarish testini qo‘shing. Dastlabki 45 daqiqa — jamoa urinishi; SI va qidiruv tizimi mavjud.

~~~bash
python3 -m pytest -q
python3 checks/acceptance.py --project . --profile E3
~~~

Eski testingiz to‘liq qaytarishni kutgan bo‘lsa, bu kutilmani yangilang va sababini `docs/change.md` faylida tushuntiring. Topshirish profili — E3.

