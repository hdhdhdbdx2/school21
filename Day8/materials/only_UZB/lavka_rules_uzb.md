# Do‘kon qoidalari va vositalar

## Ma’lumotlar

| Identifikator | Tovar | Narx | Ishtirokchi uchun limit | Qoldiqlar |
| --- | --- | --- | --- | --- |
| hoodie | Xudi | 500 | 1 | S 3, M 5, L 2, XL 1 |
| tshirt | Futbolka | 250 | 2 | S 10, M 8, L 6, XL 4 |
| stickers | Stikerlar | 50 | 5 | one_size 50 |
| bottle | Butilka | 150 | 2 | one_size 12 |
| tote | Shopper sumka | 100 | 3 | one_size 20 |

Foydalanuvchilar bazaga oldindan kiritilgan: `student_01` — 1000 koin, `student_02` — 300, `student_poor` — 20. Balansni o‘qish yangi foydalanuvchi yaratmaydi. Noma’lum foydalanuvchi uchun `USER_NOT_FOUND` qaytariladi.

Narx va miqdor — butun sonlar. Bitta buyurtmada bitta o‘lchamdagi bitta tovar bo‘ladi. Standart miqdor — 1. Limit foydalanuvchining `created` va `picked_up` holatidagi barcha buyurtmalarida ushbu tovar birliklari yig‘indisi bo‘yicha, barcha o‘lchamlar hisobga olinib aniqlanadi. Bekor qilish limitni bo‘shatadi.

Yaratishda server qiymatni buyurtmaga yozadi. Bekor qilishda katalogning joriy narxi emas, saqlangan qiymat ishlatiladi. Bazaviy versiyada butun summa qaytariladi.

## Javoblar

Muvaffaqiyat: `{"ok": true, "data": {...}}`.

Do‘kon qoidasi bo‘yicha rad etish: `{"ok": false, "error": {"code": "OUT_OF_STOCK", "message": "Tovar yetarli emas"}}`. Xabar matnini tushunarli yozing; tekshiruv aniq iborani emas, kodni solishtiradi.

Argumentning noto‘g‘ri turi yoki 1 dan kichik miqdor MCP kirishida, ishlov beruvchi chaqirilishidan oldin rad etiladi. Protokolning bunday javobida `isError` o‘rnatiladi; mijoz uni so‘rov xatosi sifatida ko‘rsatadi. Bu Do‘kon kodlaridan biri emas, alohida holat. "2" satri, 1.5 kasri va true butun miqdor hisoblanmaydi.

## Kontraktlar

`quantity` dan boshqa barcha argumentlar majburiy. Identifikatorlar va o‘lcham — bo‘sh bo‘lmagan satrlar. data ichidagi maydon nomlari quyida keltirilgan; to‘liq sxemalar — `contracts/tools_schemas.json` faylida.

| Vosita | Argumentlar | data ichidagi maydonlar |
| --- | --- | --- |
| list_products | Yo‘q | products — tovarlar ro‘yxati |
| get_product | product_id | id, name, price_coins, user_limit, stock |
| get_coin_balance | user_id | user_id, balance |
| create_order | user_id, product_id, size, quantity = 1 | order_id, status, total_price |
| get_order_status | order_id | order_id, status |
| cancel_order | order_id | order_id, status |
| confirm_pickup | order_id | order_id, status |

`stock` — o‘lchamlar va qoldiqlar lug‘ati; `products` elementi `get_product` bilan bir xil maydonlarga ega. Katalog identifikatorlar tartibida qaytariladi. `order_id` — server belgilaydigan yangi, bo‘sh bo‘lmagan satr.

## Xarid

Tekshiruvlar quyidagi tartibda bajariladi:

1. Foydalanuvchi mavjud — aks holda `USER_NOT_FOUND`.
2. Tovar mavjud — aks holda `PRODUCT_NOT_FOUND`.
3. O‘lcham mavjud va qoldiq yetarli — aks holda `OUT_OF_STOCK`.
4. Yangi buyurtma oldingilarni hisobga olganda limitdan oshmaydi — aks holda `USER_LIMIT_EXCEEDED`.
5. Koinlar butun qiymatga yetadi — aks holda `INSUFFICIENT_COINS`.

Barcha tekshiruvlardan keyin server buyurtma yaratadi, balans va qoldiqni kamaytiradi. Bu uch o‘zgarish bitta tranzaksiyada bajariladi: yo hammasi saqlanadi, yo hech biri.

Xaridni takroriy chaqirish yangi buyurtma hisoblanadi va barcha tekshiruvlardan qayta o‘tadi. Maxsus kalit bo‘yicha takrorlardan himoya majburiy qismga kirmaydi.

## Buyurtma holatlari

`created` dan `cancelled` yoki `picked_up` ga o‘tish mumkin. `cancelled` va `picked_up` dan o‘tishlar yo‘q.

Noma’lum buyurtma — `ORDER_NOT_FOUND`. Takroriy bekor qilish, takroriy berish, bekor qilingan buyurtmani berish va berilgan buyurtmani bekor qilish — `ORDER_STATUS_ERROR`.

Bekor qilish qoldiq va koinlarni aynan bir marta qaytaradi. Berish faqat holatni o‘zgartiradi: tovar va koinlar yaratishda allaqachon yechilgan.

Har qanday rad etishda products, stock, users va orders jadvallari avvalgi qiymatlarini saqlaydi. O‘qish ham ularni o‘zgartirmaydi.

## O‘quv servisining chegaralari

Loyihada haqiqiy to‘lovlar va haqiqiy buyurtmalar yo‘q. Foydalanuvchilar o‘quv uchun; kirish va shaxsni tekshirish amalga oshirilmaydi. Mijoz o‘quv identifikatorlarining istalganini yuborishi mumkin. Keyingi dasturchi servisni kirish huquqlari ajratilgan tizim deb qabul qilmasligi uchun buni pasportga ochiq yozish kerak.

Server lokal ishlaydi, tekshiruvlardagi chaqiruvlar ketma-ket bajariladi. Bir nechta mijozning bir vaqtdagi xaridlari, yetkazib berish, MCP orqali katalogni o‘zgartirish va shaxsiy kabinetlar majburiy qismga kirmaydi.

Konvert bitta qoidani o‘zgartiradi. Vosita nomlari va javob tuzilmalari saqlanadi. Yangi qoida va tekshirish profilini pasportda ko‘rsatish kerak.

