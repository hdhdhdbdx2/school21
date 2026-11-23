# E5 konverti. Oldindan buyurtma qilinadigan xudi

Do‘kondan xabar:

«Xudini buyurtmadan keyin darhol jamlashga topshiramiz. Xudi buyurtmasini bekor qilishni vaqtincha yopamiz. Qolgan merch — oldingi qoidalar bo‘yicha».

## Yangi shart

`product_id = "hoodie"` bo‘lgan tovar buyurtmasini hatto `created` holatida ham bekor qilib bo‘lmaydi. Javob — `ORDER_STATUS_ERROR`; balans, qoldiq va holat saqlanadi.

Yaratilgan xudi buyurtmasini berish mumkin. Boshqa tovarlarni bekor qilish avvalgidek ishlaydi. Mavjud bo‘lmagan buyurtma uchun hali ham `ORDER_NOT_FOUND` qaytariladi.

Qoida katalogdagi ruscha nom bilan emas, tovar identifikatori bilan belgilanadi. Vosita sxemalari o‘zgarmaydi.

## Sizning ishingiz

Fayllar bo‘yicha taxminni yozing. Yangi shartni va ikkita testni qo‘shing: xudini bekor qilish rad etiladi, butilkani bekor qilish mumkin bo‘lib qoladi. Birinchi urinish — 45 daqiqa; SI va qidiruv tizimi mavjud.

~~~bash
python3 -m pytest -q
python3 checks/acceptance.py --project . --profile E5
~~~

Topshirish profili — E5.

