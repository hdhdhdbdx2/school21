# 08–09-kunlar. «School 21» do‘koni

QAYTISH KANALI · KIRUVCHI PAKET

yuborilgan 2030 qabul qiluvchi sen

> ***Salom! Dasturlashning asosiy tili inson tili bo‘ladi, degan gap esingdami? Endi tasavvur qil: mashinaga «Menga mana bu narsani buyurtma qil» deb so‘rov yuborasan. Va kompyuterni yopasan.\
Sen o‘z ishlaring bilan band bo‘lganingda nima sodir bo‘lishi kerak?***

> ***Sening davringda inson ko‘pincha ishni SI o‘rniga o‘zi oxiriga yetkazadi: chatdan matnni ko‘chiradi, boshqa dasturni ochadi, kerakli tugmani bosadi.\
2030-yilda biz ishni mashinaga to‘liq topshirishga o‘rganib qolganmiz. Sen aytasan, u bajaradi. Qulay, faqat «buyurtma qil» degan so‘zdan ikkalangiz har xil narsani tushunganingiz ma’lum bo‘lmaguncha.***

> ***Bugun sening roling — SI integratsiyalari muhandisi. SI agentiga suhbatdan tashqarida ham biror ish qila oladigan vositalar berasan. Unga qaysi harakatlarni ishonib topshirish mumkinligini, qanday shartlarda to‘xtashi kerakligini aniqlaysan. SI bilan chatda faqat ovoz bor. Sen unga qo‘l ham berasan.\
SI juda muloyim qilib yozishi mumkin: «Hammasi tayyor». Faqat buyurtmalar olib ketiladigan peshtaxta oldida qo‘li bo‘sh turgan odamga bu muloyimlikdan foyda kam. Buyurtmani peshtaxta oldida allaqachon kutishyapti. Buyurtma esa yo‘q.\
Shuning uchun senga kelajakdan bir odatni beraman: har bir «tayyor» ortida aslida nima o‘zgarganini izla. Buyurtma tizimda paydo bo‘ldimi? Tovar qoldig‘i o‘zgardimi? Yoki senda bu haqda faqat xabar bormi? SI’ga qancha ko‘p ish topshirsang, bu odat shuncha muhim bo‘ladi. Oxir-oqibat SI integratsiyalari muhandisi bo‘lmasang ham.\
Meni ayniqsa mana bu narsa tashvishga soladi. Mashinaga vosita berganingda, unga kimningdir hayotiga ta’sir qilishga ruxsat berasan. Hovuzdagi shu loyihada bu bor-yo‘g‘i koinga olinadigan merch. Boshqa tizimda esa — shifokor qabuliga yozilish, pul o‘tkazish, hujjatlarga kirish. Uning qo‘li nimalarga yetishini sen tanlaysan.***

«School 21»da Do‘kon bor, unda merch sotiladi: School 21 logotipi tushirilgan tovarlar. Merch koinga sotib olinadi. Qoldiq, balans va buyurtma nima bo‘lganini bilish uchun ishtirokchilar administrator oldiga boradi va navbat uzayadi. Tez orada Do‘konga dasturiy SI agenti ulanadi. U muloyim va tez, lekin o‘lchamni adashtirishi, so‘rovni takrorlashi yoki olib ketilgan buyurtmani bekor qilishga urinishi mumkin. Unga vositalar kerak — va Do‘kon qoidalarini buzishga yo‘l qo‘ymaydigan server kerak.

Bugun — guruh loyihasi, unda Do‘konning MCP-serverini yig‘asizlar.

*MCP-server — mening davrimda har bir biznesda bor narsa. SI agentlarini ulash uchun maxsus server. Sening davringda bizneslarda agentlar uchun bunday kirish hali kam uchraydi, lekin tez orada bu o‘zgaradi. Bugun ularni ishlab chiqishni o‘rganasan — bu yaqin orada eng talabgir ko‘nikmalardan biri bo‘ladi.\
Jamoa bo‘lib ishlaysizlar. Tavsiya etilgan tarkib — 4 kishi. Bugun va ertaga jamoa senga tayanadi. Imtihonni qanday yig‘ganingiz esingdami? O‘shanda hamma o‘z qismini yozgan, inson esa bitta umumiy dasturdan o‘tgan edi. Bu yerda ham shunday bo‘ladi. Ikkinchi kun oxirigacha aniq qoidalar bo‘yicha ishlaydigan, xato so‘rovlarga bardosh beradigan va keyingi dasturchiga topshirsa bo‘ladigan serverni yig‘ishingiz kerak.*

**SI integratsiyalari muhandisi nima qiladi.** SI agentini haqiqiy tizim amallari bilan bog‘laydi: masalan, qoldiqlarni ko‘rish, buyurtma yaratish yoki band qilishni bekor qilish. Buning uchun mavjud vositalar va ma’lumotlar formatini tavsiflaydi, qoidalar tekshiruvini serverda amalga oshiradi, ma’lumotlar o‘zgarishini tekshiradi va boshqa jamoa uchun ishga tushirishni tayyorlaydi. «Buyurtma bekor qilindi» degan xabar ortida tekshirsa bo‘ladigan amal turishi kerak: holat o‘zgargan, qaytarish bir marta bo‘lgan.

Bu ikki kunda shunday integratsiyaning server qismini yaratasizlar va uni tayyor dasturiy mijoz bilan tekshirasizlar. Hovuzdan keyin bu tajriba agentni buyurtmalar yoki xizmatga yozilish servisiga ulashda asqatadi. Xuddi shu ko‘nikmalar oddiy ilovada ham kerak: tugma, skript va SI agenti bitta amalni chaqirishi mumkin, uning qoidalarini esa server bajarishi kerak.

1–4-topshiriqlar — 08-kun, 5–8-topshiriqlar — 09-kun.\
Kelajakka tayyorgarlik amaliyotlari topshiriqlarga kiritilgan: jamoaviy kelishuvlar — 2-topshiriq, yakuniy refleksiya — 8-topshiriq. Ikkala amaliyot natijalarini `docs/team.md` fayliga yozinglar.\
Materiallarni kerak bo‘lganda ochinglar: ularda Do‘kon qoidalari, server tuzilishi va buyruq misollari bor. Ishni qanday bo‘lish va qaysi tartibda birlashtirishni jamoa hal qiladi.

[Ishni boshlash](#ishni-boshlash)

08-kun
- [1-topshiriq. Birinchi ishga tushirish va so‘rov yo‘li](#1-topshiriq-birinchi-ishga-tushirish-va-sorov-yoli)
- [2-topshiriq. Jamoaviy kelishuvlar](#2-topshiriq-jamoaviy-kelishuvlar)
- [3-topshiriq. Vositalar kontraktlari](#3-topshiriq-vositalar-kontraktlari)
- [4-topshiriq. Xarid va birinchi buyurtma](#4-topshiriq-xarid-va-birinchi-buyurtma)

09-kun
- [5-topshiriq. Bekor qilish, olib ketish va o‘z testlaringiz](#5-topshiriq-bekor-qilish-olib-ketish-va-oz-testlaringiz)
- [6-topshiriq. Konvert](#6-topshiriq-konvert)
- [7-topshiriq. Serverni topshirish](#7-topshiriq-serverni-topshirish)
- [8-topshiriq. Keyingi jamoaviy ishga nimalarni olib o‘tamiz](#8-topshiriq-keyingi-jamoaviy-ishga-nimalarni-olib-otamiz)

[Nazorat nuqtasi](#nazorat-nuqtasi)

## Ishni boshlash

<details>
<summary>«School 21»da qanday ta’lim olinadi</summary>

- Bu yerda seni katta erkinlik beriladigan o‘ziga xos ta’lim tajribasi kutmoqda. Sen vazifa olasan va yechim yo‘llarini mustaqil izlaysan.
- O‘zaro ta’lim (tengdosh-tengdoshga, P2P) — bu boshqa ishtirokchilar bilan bilim va tajriba almashish bo‘lib, bunda hamma ham o‘qituvchi, ham o‘quvchi vazifasini bajaradi. Bu yondashuv bir-biringizdan o‘rganib, materialni chuqurroq tushunishga yordam beradi.
- O‘zingni erkin his qil va yordam so‘ra. Atrofingdagilar ham bu yo‘ldan birinchi bor o‘tmoqda. Tajriba va g‘oyalaringni boshqalar bilan bo‘lish.
- Boshqalarning yechimlarini ko‘chirsang, o‘qishdan hech qanday ma’no qolmaydi. Boshqalarning yordamidan foydalansang, har doim nima uchun, qanday va nima maqsadda ekanini oxirigacha tushunib ol. Xato qilishdan qo‘rqma.
- Vazifa bajarishning imkoni yo‘qdek tuyulyaptimi? Tanaffus qil, toza havoga chiq, miyangni dam oldir — bu ko‘pchilikka yordam bergan. Balki shundan so‘ng yechim o‘z-o‘zidan kelar.
- Loyihani bajarishda vaqtni kuzatib bor. Kuniga kamida bitta sinovdan o‘tishni tavsiya qilamiz.

</details>

<details>
<summary>Loyiha bilan qanday ishlash kerak</summary>

- «Kirish ochiq» rejimi: qidiruv tizimi va SI yordamchilari ruxsat etilgan. Taklif qilingan kodni Do‘kon ma’lumotlarida tekshiringlar: model takroriy bekor qilish xavfsiz deb ta’kidlasa, buni so‘rov va baza holati bilan ko‘rsatinglar.
- Loyiha guruhli. Tavsiya etilgan tarkib — 4 kishi. Jamoa bitta repozitoriyda ishlaydi, bitta versiyani topshiradi va hammaga bitta baho oladi.
- 1–4-topshiriqlar — 08-kun, 5–8-topshiriqlar — 09-kun. Barcha topshiriqlar majburiy. 6-topshiriqdagi bajarilgan konvert qo‘shimcha ball beradi. Loyihani 09-kundan keyin boshqa jamoaning yetakchisi tekshiradi.
- Materiallarni kerak bo‘lganda ochinglar: ularda Do‘kon qoidalari, server tuzilishi va buyruq misollari bor. Ishni qanday bo‘lish va qaysi tartibda birlashtirishni jamoa hal qiladi.
- Majburiy qism lokal ishlaydi. Bajarish va tekshirish uchun pullik servislar, model kalitlari va SI’ga ulanish kerak emas.
- Jamoa bitta jamoaviy repozitoriyda ishlaydi. Har bir ishtirokchi uni GitLab’dan klonlaydi va ildizga — README joylashgan papkaga o‘tadi.
- Umumiy tarmoq (branch) — `develop`: tekshiruvga shu topshiriladi. O‘z ishchi tarmoqlaringizda ishlanglar va o‘zgarishlarni `develop` tarmog‘iga navbat bilan birlashtiringlar. Kim va qanday birlashtirishini jamoa `docs/team.md` fayliga yozadi.
- **Barcha ishga tushirish buyruqlari repozitoriy ildizidan bajariladi.** Fayl yo‘lining tilga olinishi buyruq emas.
- Kodni `src/` ichida, o‘z testlaringizni `testing/` ichida yozinglar. Berilgan `checks/` tekshiruvlarini va `data/seed.sql` boshlang‘ich ma’lumotlarini o‘zgartirmanglar. Majburiy qismda `src/server.py` va `src/mcp_adapter.py` ulash kodini o‘zgartirish kerak emas.
- Lokal `data/*.db` bazalarini va virtual muhitni repozitoriyga qo‘shmanglar.
- Ish joyidagi muhit allaqachon tayyorlangan, `python3` dan foydalaninglar.

**Jamoaviy ish**

Ish 4 yo‘nalishga bo‘lingan. Yo‘nalish albatta bitta odam degani emas: tarkib kam bo‘lsa, yo‘nalishlar birlashtiriladi, ko‘p bo‘lsa, bitta yo‘nalishda juft bo‘lib ishlashadi.

| **Yo‘nalish** | **Asosiy fayllar** | **Jamoaga nima topshirish kerak** |
| --- | --- | --- |
| Yetakchi va o‘qish vositalari | `src/read_handlers.py`, `contracts/tools_schemas.json` | 4 ta ishlaydigan o‘qish vositasi, vositalar tavsiflari, umumiy ishga tushadigan `develop` tarmog‘i |
| Qoidalar va testlar | `src/domain.py`, `testing/test_rules.py` | Kirish ma’lumotlari va kutilgan javoblar misollari bilan qoida funksiyalari |
| Ma’lumotlar | `src/storage.py` | Saqlash metodlari: SQL so‘rovlari, buyurtmani yozish, yechish va qaytarish bitta tranzaksiyada |
| Buyurtma amallari | `src/order_handlers.py`, `testing/test_orders.py` | Buyurtmani yaratish, bekor qilish va olib ketish, rad etish testlari |

Jamoa tarkibi 4 kishidan kam bo‘lsa:

| **Tarkib** | **Yo‘nalishlar** |
| --- | --- |
| Uch kishi | 1) Yetakchi, o‘qish vositalari va kontraktlar; 2) Qoidalar va testlar; 3) Ma’lumotlar va buyurtma amallari: `storage.py` va `order_handlers.py` bitta tranzaksiya bilan bog‘langan, ularni bitta odam olib borgani qulayroq |
| Ikki kishi | 1) Yetakchi, o‘qish vositalari, kontraktlar, qoidalar va ularning testlari; 2) Ma’lumotlar va buyurtma amallari, rad etish testlari |

`docs/` dagi hujjatlar va `RUN.md` ni teng bo‘linglar.

**Yetakchi** muvofiqlashtirishni ishlab chiqish yo‘nalishlaridan biri bilan birga olib boradi. Yetakchi o‘zgarishlarni `develop` tarmog‘iga birlashtiradi, qabul qilingan ish faqat kimningdir kompyuterida qolib ketmasligini kuzatadi va qabulda loyihani himoya qiladi.

**Qachon yig‘ilish kerak:**

1.  Namoyishdan keyin — yo‘nalishlarni taqsimlash va funksiya signaturalari bo‘yicha kelishuv. 1-topshiriqdan keyin jamoaviy kelishuvlarni muhokama qilinglar; kerak bo‘lsa, ularni shakllantirishni 08-kun oxiriga ko‘chiringlar.
2.  O‘qish va qoidalar tayyor bo‘lganda — xaridning birinchi umumiy chaqiruvi.
3.  08-kun oxirida — `develop` dan ishga tushirish va tugallanmagan ishlar ro‘yxati. `docs/team.md` faylini kuchli tomonlardan birgalikda foydalanish misoli bilan to‘ldiringlar yoki muhokamani qoldirgan bo‘lsangiz, kelishuvlarni shakllantiringlar.
4.  09-kunning bazaviy tekshiruvlaridan keyin — konvert (6-topshiriqdagi havola orqali olingan) va o‘zgarishni taqsimlash.
5.  Topshirishdan oldin — yo‘riqnoma bo‘yicha ishga tushirish va tushuntirishning qisqa mashqi. 7-topshiriqdan keyin ikki kunlik tajribani muhokama qilinglar va keyingi jamoaviy ish uchun umumiy va shaxsiy xulosalarni yozinglar.

Agar 15 daqiqa davomida boshqa birovning qismi sababli davom eta olmasangiz, jamoaga aytinglar: qaysi metod kerak, qanday natija kutyapsizlar va hozir nimani tekshirish mumkin. Batafsil — `materials/team.md` faylida.\
Qiyin joyda qolib ketsang, jamoadoshlaringga ayt. Bilaman, avval o‘zing tushunib olib, keyin yaxshi xabar bilan kelging keladi. Sen jim turganingda qolganlar hammasi senda chiqayotgandek reja tuzadi. Jim turib jamoani qiyin ahvolga solma. Koddagi xatoni birga topa olasizlar. Senga yordam kerakligini taxmin qilish ancha qiyin. Hatto kelajakda ham biz hali bir-birimizning fikrimizni o‘qiy olmaymiz.

</details>

<details>
<summary>Materiallar</summary>

| **Nima kerak** | **Qayerdan topish mumkin** |
| --- | --- |
| Do‘kon qoidalari: tovarlar, foydalanuvchilar, javoblar, kontraktlar, xaridni tekshirish tartibi, buyurtma holatlari | `materials/lavka_rules.md` |
| Jamoaviy ish | `materials/team.md` |
| Server qanday tuzilgan: ishlov beruvchilar, qoidalar, saqlash, tranzaksiya | `materials/architecture.md` |
| Testlarni qanday yozish va umumiy tekshiruvni qanday ishga tushirish | `materials/testing.md` |
| Loyihani tekshirish | `materials/acceptance.md`, `check-list.yml` |
| Python va bog‘liqliklar | `materials/environment_uzb.md`, `materials/requirements.txt`, `materials/requirements-campus.lock.txt` |

**Berilgan fayllar.** Ularni qayta yaratish kerak emas.

| **Fayl** | **Bu nima** |
| --- | --- |
| `src/` | Server: tayyor `get_product` vositasi, bazaga ulanish va `TODO` belgili funksiya shablonlari |
| `client.py` | Mijoz: namoyish, ssenariy va vositalarni qo‘lda chaqirish. Har bir chaqiruv `logs/client.jsonl` fayliga yoziladi |
| `check_environment.py` | Ish joyini tekshirish |
| `data/seed.sql` | O‘quv tovarlari, foydalanuvchilar va jadvallar. O‘zgartirish mumkin emas |
| `contracts/tools_schemas.json` | Vositalar sxemalari. Tavsiflarni to‘ldirish kerak |
| `checks/` | Umumiy qabul tekshiruvlari. Ishga tushirish mumkin, o‘zgartirish mumkin emas |
| `testing/test_example.py` | Test namunasi. O‘z testlaringiz hisobiga kirmaydi |
| `docs/team.md`, `docs/system.md`, `docs/change.md` | Jamoa hujjatlari shablonlari |
| `RUN.md` | Ishga tushirish yo‘riqnomasi shabloni |

</details>

## 1-topshiriq. Birinchi ishga tushirish va so‘rov yo‘li

_08-kun, butun jamoa._

1\.  Barcha ishtirokchilar jamoaviy repozitoriyni klonlaydi. Yetakchi `develop` tarmog‘ini yaratib, GitLab’ga yuboradi (push), qolganlar shu tarmoqqa o‘tadi.

2\.  `materials/environment_uzb.md` bo‘yicha muhitni faollashtiringlar, keyin ish joyini tekshiringlar va namoyishni ishga tushiringlar:

- `python3 check_environment.py`
- `python3 client.py demo`

Namoyish serverni o‘zi ishga tushiradi va 2 ta tovarni so‘raydi. `hoodie` uchun server 500 narxini va o‘lchamlar bo‘yicha qoldiqlarni, `missing` uchun esa `PRODUCT_NOT_FOUND` rad javobini qaytaradi. Butun jamoa ikkala javobni ham ko‘rishi kerak.

3\.  `get_product` yo‘lini kod bo‘ylab birga kuzatinglar: `src/mcp_adapter.py` → `src/read_handlers.py` → `src/storage.py`. So‘rovni qabul qiladigan funksiyani, bazadan o‘qiydigan SQL so‘rovini va javob yoki rad javobi shakllanadigan joyni topinglar. Qisqa ma’lumot — `materials/architecture.md` faylida.

4\.  Bu yo‘lni funksiya nomlari bilan bitta satrda `docs/system.md` faylining «So‘rov yo‘li» bo‘limiga yozinglar.

5\.  Yo‘nalishlarni taqsimlanglar (bunga 15 daqiqa) va `docs/team.md` faylini to‘ldiringlar: yetakchi, kim qaysi yo‘nalishni oladi, o‘zgarishlarni qanday birlashtirasizlar.

Birinchi ishga tushirishgacha butun loyihani o‘qish kerak emas.

**Natija:** butun jamoada ishga tushirish va serverning haqiqiy javobini tahlil qilish tajribasi bor; `docs/team.md` faylida taqsimot, `docs/system.md` faylida `get_product` yo‘li yozilgan.  

**Tekshiruv:** `python3 client.py demo` xudining narxi va qoldiqlarini hamda `PRODUCT_NOT_FOUND` rad javobini ko‘rsatadi. Yetakchi `get_product` yo‘lini 3 ta fayl orqali ko‘rsatadi, SQL so‘rovini aytadi va `PRODUCT_NOT_FOUND` rad javobi kutilmagan Python istisnosidan nimasi bilan farq qilishini tushuntiradi. `docs/team.md` faylida yetakchi, 4 yo‘nalish va o‘zgarishlarni birlashtirish usuli ko‘rsatilgan.  
**Nima uchun:** hozir tayyor `get_product` yo‘li qolgan 6 ta vositani yozib tugatishga va xatoni qayerdan izlashni tushunishga yordam beradi: so‘rovni qabul qilishda, ishlov beruvchida yoki ma’lumotlarni o‘qishda. Hovuzdan keyin bunday tahlil agent noto‘g‘ri tovar qoldig‘ini aytganda asqatadi: SI integratsiyalari muhandisi sababni topish uchun aniq chaqiruvni baza va javobgacha kuzatadi.

## 2-topshiriq. Jamoaviy kelishuvlar

Oldingi individual loyihalarda o‘z holatingizni anglashni va qiyinchiliklarga reaksiyangizni boshqarishni o‘rgandingizlar — Hissiy intellektni rivojlantirdingizlar, shuningdek, muvaffaqiyatsizlikni aniq saboq va keyingi qadamga aylantirishni o‘rgandingizlar. Tahliliy loyihalarda Tizimli fikrlashni rivojlantirish uchun «Aysberg»dan, Analitik fikrlashni rivojlantirish uchun muammoni o‘lchanadigan qismlarga ajratishdan foydalandingizlar.

Endi birga Do‘kon serverini yig‘asizlar. Jamoaviy ishni tashkil qilishga Kelajakka tayyorgarlikning yana bir amaliyoti orqali yondashishni va Hamkorlik va sheriklik ko‘nikmasini mashq qilishni taklif qilamiz: harakatlarni muvofiqlashtirish, mas’uliyatni bo‘lishish va bir-biringizning o‘zaro to‘ldiruvchi kuchli tomonlaringizdan foydalanish.

Buning uchun «Jamoaviy ish kelishuvlari» vositasidan foydalaninglar. U hamma bir xil ishlaydi deb taxmin qilish o‘rniga o‘zaro ishlash qoidalarini ochiq muhokama qilishga yordam beradi.

Serverni allaqachon ishga tushirdingizlar va yo‘nalishlarni taqsimladingizlar. Oldingi jamoaviy loyihani eslanglar: birga ishlashga nima yordam bergan, nima kechikish yoki chalkashlikka olib kelgan? Muhokamada shu tajribani hisobga olinglar.

`docs/team.md` faylini uchta qisqa blok bilan to‘ldiringlar:
1. Qanday birga ishlaymiz. 08-kun natijasi, aloqa kanali, javob berish muddatlari va qaror qabul qilish tartibini kelishib olinglar. 1-topshiriqdagi taqsimotga tayanib, jamoa umumiy natijani qanday tekshirishini kelishib olinglar. Yozib qo‘yilgan ma’lumotlarni takrorlash kerak emas.
2. Kelishmovchilik va kechikishlarni qanday hal qilamiz. Kelishmovchiliklarni bevosita qanday muhokama qilish, yechimni qaysi obyektiv mezonlar bo‘yicha tanlash va kimdan yordam so‘rashni kelishib olinglar. Yakuniy qarorni kim va qanday qabul qilishini hamda kechikish yoki boshqa birovning qismi sababli to‘xtab qolishda nima qilishni ko‘rsatinglar.
3. Kuchli tomonlardan qanday foydalanamiz. Ishtirokchilarning kuchli tomonlarini va ularning ishda yoki o‘zaro yordamda qo‘llanishini aytinglar.

Qisqa yozinglar: har bir blokda bir necha band yetarli. Kelishuvlar barcha ishtirokchilarga tushunarli va joriy loyihada qo‘llasa bo‘ladigan bo‘lishi kerak.

08-kun oxirida kuchli tomonlar uyg‘unligi umumiy natijaga qanday yordam berganiga bitta aniq misol qo‘shinglar. Hali yordam bermagan bo‘lsa, ishni tashkil qilishda nimani o‘zgartirish kerakligini ko‘rsatinglar.

**Natija:** `docs/team.md` faylida o‘zaro ishlashning kelishilgan qoidalari, kelishmovchiliklarni hal qilish tartibi va jamoaning kuchli tomonlaridan foydalanish qayd etilgan.

**Tekshiruv:** yetakchi `docs/team.md` faylidagi uch blokni ko‘rsatadi, jamoa qanday qaror qabul qilishini va kechikishlarda qanday yo‘l tutishini tushuntiradi hamda kuchli tomonlardan birgalikda foydalanishning yozib qo‘yilgan misolini keltiradi yoki taklif qilingan o‘zgarishni tushuntiradi.

Kelishuvlarni shakllantirishni 08-kun oxiriga ko‘chirish mumkin: o‘shanda birga ishlash tajribasiga ega bo‘lasizlar va bir-biringizning kuchli tomonlaringizni yaxshiroq tushunasizlar. Bunday holda o‘tgan kundagi aniq vaziyatlarga tayaninglar va 09-kunda loyihani davom ettirish uchun qoidalarni shakllantiringlar.

## 3-topshiriq. Vositalar kontraktlari

_08-kun, yetakchining yo‘nalishi; tavsiflarni tekshirish — butun jamoa._

MCP — dastur server qanday vositalar taqdim etishini bilib oladigan va ularni kerakli argumentlar bilan chaqiradigan protokol. Vosita — bitta amal, masalan, `get_product`. Kontrakt — vosita nimani qabul qilishi va nimani qaytarishi haqidagi kelishuv.

Serverda yettita vosita bor:

| **Vosita** | **Nima qiladi** |
| --- | --- |
| `list_products` | Katalog va qoldiqlarni ko‘rsatadi |
| `get_product` | Bitta tovarni ko‘rsatadi |
| `get_coin_balance` | Ishtirokchi balansini ko‘rsatadi |
| `create_order` | Buyurtma yaratadi, koinlarni yechadi va tovarni band qiladi |
| `get_order_status` | Buyurtma holatini ko‘rsatadi |
| `cancel_order` | Buyurtmani bekor qiladi, tovar va koinlarni qaytaradi |
| `confirm_pickup` | Buyurtma olib ketilganini belgilaydi |

Kontraktlar karkasi `contracts/tools_schemas.json` faylida bor. Server vositalar tavsiflarini shu fayldan oladi va mijozga ko‘rsatadi.

1.  6 ta vosita uchun `TODO` belgisini o‘z tavsifingiz bilan almashtiringlar. Tavsifda vosita qachon kerakligini, nimani o‘zgartirishini va qaysi holatda rad etishini ko‘rsatinglar. Masalan, bekor qilish tavsifi olib ketilgan buyurtmani bekor qilib bo‘lmasligi haqida ogohlantiradi.
2.  Vosita nomlari, argumentlar va javob sxemalarini o‘zgartirmanglar: keyingi dasturchining mijozi serverga shular orqali murojaat qiladi.
3.  Tavsiflarni jamoa ichida tekshiringlar: ikki guruhga bo‘lininglar. Biri vaziyatni aytadi, ikkinchisi vositani faqat tavsif bo‘yicha tanlaydi. Tanlov noaniq bo‘lib chiqsa, matnni aniqlashtiringlar. Mijoz nimani ko‘rishini ko‘rish: `python3 client.py list`.
4.  `docs/system.md` faylidagi «Server nima qiladi» va «Chegaralar» bo‘limlarini to‘ldiringlar: tizim qaysi amallarni bajaradi va mijozga nimani va’da qilib bo‘lmaydi. Yordam — `materials/lavka_rules.md` faylining «O‘quv servisi chegaralari» bo‘limida.

**Natija:** `contracts/tools_schemas.json` faylida `TODO` belgisiz 7 ta tavsif bor; `docs/system.md` faylida server imkoniyatlari va chegaralari tavsiflangan.  

**Tekshiruv:** «butilka uchun yaratilgan buyurtma hali olib ketilmagan, ishtirokchi uni bekor qilmoqchi» vaziyatida yetakchi tavsiflar bo‘yicha `cancel_order` vositasini tanlaydi va kerakli argumentni aytadi. Yetakchi nega tavsif koddagi tekshiruv o‘rnini bosmasligini va nega ommaviy vositani xohlagancha qayta nomlab bo‘lmasligini tushuntiradi. `docs/system.md` faylida mijozga va’da qilib bo‘lmaydigan kamida bitta amal aytilgan.  
**Nima uchun:** hozir aniq tavsiflar kerakli amal va argumentlarni tanlashga, umumiy sxemalar esa jamoaga o‘z qismlarini birlashtirishga yordam beradi. SI integratsiyalari muhandisi ishida bunday kontrakt boshqa mijoz yoki agentni buyurtmalar servisiga ma’lumotlar formatini taxmin qilmasdan ulash uchun kerak. Tavsif amalni tanlashga yordam beradi; argumentlar va amalning o‘zi joizligini server tekshiradi.

## 4-topshiriq. Xarid va birinchi buyurtma

_Eng murakkab topshiriq._

_08-kun, barcha yo‘nalishlar parallel._

Bugun 4 ta o‘qish vositasi va xarid ishlay boshlaydi. Tugatish kerak bo‘lgan funksiyalar `TODO` bilan belgilangan va hozircha `NotImplementedError` istisnosini chiqaradi.

| **Yo‘nalish** | **4-topshiriqda nimani tugatish kerak** |
| --- | --- |
| Yetakchi va o‘qish vositalari | `src/read_handlers.py`: `list_products`, `get_coin_balance`, `get_order_status` |
| Qoidalar va testlar | `src/domain.py`: `calculate_total`, `purchase_error`; qoidalarning birinchi testlari |
| Ma’lumotlar | `src/storage.py`: `list_products`, `get_user`, `get_order`, `count_owned`, `create_order` |
| Buyurtma amallari | `src/order_handlers.py`: `create_order`; rad etishning birinchi testlari |

1\.  `docs/team.md` faylidagi yo‘nalishlaringiz bo‘yicha tarqalinglar. Yo‘nalishlar bir vaqtda tayyor bo‘lmaydi va bu normal:

- `src/domain.py` faylidagi qoidalar bazaga murojaat qilmaydi: saqlash tayyor bo‘lmaguncha ularni tugatib, testlar bilan qamrab olish mumkin;
- xarid ishlov beruvchisini saqlashning vaqtinchalik o‘rinbosariga (stub) — siz kelishgan maydonlari bor lug‘atga tayanib yozish mumkin. O‘rinbosar faqat test ichida yashaydi: uni SQL o‘rniga topshirish mumkin emas.

2\.  Xarid shartlarni qat’iy shu tartibda tekshiradi: foydalanuvchi mavjud → tovar mavjud → o‘lcham bor va qoldiq yetarli → limit oshmagan → koin yetarli. Rad etish kodlari — `materials/lavka_rules.md` faylining «Xarid» bo‘limida.

3\.  Buyurtmani yozish, koinlarni yechish va qoldiqni kamaytirish bitta tranzaksiyada bajariladi: yo 3 ta o‘zgarishning hammasi saqlanadi, yo hech biri. Buni qanday qilish — `materials/architecture.md` faylining «Tranzaksiya» bo‘limida.

4\.  Yangi o‘quv bazasida birinchi umumiy tekshiruvni bajaringlar:

- `python3 client.py --db data/day08.db call create_order '{"user_id":"student_01","product_id":"bottle","size":"one_size","quantity":1}'`
- `python3 client.py --db data/day08.db call get_coin_balance '{"user_id":"student_01"}'`
- `python3 client.py --db data/day08.db call get_product '{"product_id":"bottle"}'`
- `python3 client.py --db data/day08.db call create_order '{"user_id":"student_poor","product_id":"hoodie","size":"M","quantity":1}'`

Kutilgan natija: `created` holatidagi va qiymati 150 bo‘lgan butilka buyurtmasi, `student_01` balansi — 850, butilkalar qoldig‘i — 11. `student_poor` uchun xudi xaridi — `INSUFFICIENT_COINS` rad javobi, balans 20 bo‘lib qoladi, M o‘lchamli xudilar qoldig‘i — 5.

5\.  `testing/` ichiga hisoblash va rad etish bo‘yicha o‘z testlaringizni qo‘shinglar. Test qanday tuzilgani — `materials/testing.md` va `testing/test_example.py` fayllarida.

6\.  Ketishdan oldin ishni `develop` tarmog‘iga birlashtiringlar. Har kim jamoaga o‘z yo‘nalishini bitta so‘rovda ko‘rsatadi. Birinchi buyurtma hali o‘tmayotgan bo‘lsa, aniq sababni `docs/team.md` faylining «08-kun oxirigacha nima qoldi» bo‘limiga yozinglar va 09-kunni shundan boshlanglar.

**Natija:** 4 ta o‘qish vositasi va `create_order` ishlaydi; buyurtma bazada ko‘rinadi, balans va qoldiq to‘g‘ri o‘zgargan; `testing/` ichida hisoblash va rad etish bo‘yicha o‘z testlaringiz bor.  

**Tekshiruv:** yangi bazada butilka xaridi va `student_poor` uchun rad etish kutilgan javoblarni beradi. Yetakchi xarid tekshiruvlarini kerakli tartibda ko‘rsatadi va nega foydalanuvchi ham, tovar ham noma’lum bo‘lganda `USER_NOT_FOUND` qaytishini tushuntiradi. Yetakchi rad etish yozuvdan oldin sodir bo‘lishini ko‘rsatadi va umumiy tranzaksiyani ko‘rsatadi. Xarid misolida yetakchi ishlov beruvchi, SQL’siz qoida va SQL qayerda ekanini ko‘rsatadi.  

**Nima uchun:** hozir tranzaksiya buyurtma, koinlarni yechish va qoldiqni kamaytirishni bog‘laydi: xato bo‘lganda bu o‘zgarishlarning faqat bir qismini saqlab bo‘lmaydi. Hovuzdan keyin xuddi shu yondashuv, masalan, joy band qilishda kerak bo‘ladi: band qilish yozuvi va bo‘sh joylar soni bir-biriga mos qolishi kerak. SI integratsiyalari muhandisi vosita chaqiruvi ma’lumotlarning yaxlit o‘zgarishiga olib kelishini tekshiradi.

>***Xo‘sh, birinchi buyurtmani o‘tkaza oldingmi?\
Ha bo‘lsa, bir soniya to‘xta: endi koding odamning balansi o‘zgaradigan harakatda ishtirok etyapti. Farqni sezyapsanmi? Hali chiqmagan bo‘lsa — ketishdan oldin ertalab nimadan boshlashingizni kelishib olinglar. Ertaga albatta kel, o‘z qisming allaqachon ishlayotgan bo‘lsa ham. Ikkinchi kuni bugun o‘z faylingda o‘tirib umuman sezmasliging mumkin bo‘lgan narsani ko‘rasan. Qolganlar ham yonida bo‘lishingga ishonib turibdi.***

QAYTISH KANALI · KIRUVCHI PAKET

yuborilgan 2030 qabul qiluvchi sen

> ***Salom.\
Tasavvur qil: SI agenti serverdan buyurtmani bekor qilishni so‘radi. Server bekor qildi, koinlarni qaytardi va javob yubordi. Javob yo‘qoldi.\
SI agenti hech narsa olmadi. U odamga yordam berishga urinadi va buyurtmani yana bir marta bekor qilishni so‘raydi.\
Xaridor fikridan bir marta qaytdi. So‘rov ikki marta keldi. Hech kim hech narsani buzmoqchi emas edi. Lekin tizim bunday holatlarni hal qila olmasa, pul ikki marta qaytarilishi mumkin.\
Holbuki, alohida olganda hammaga hammasi to‘g‘ri qilingandek tuyulishi mumkin…***

>***Endi butun tizimga qarashing kerak: kim kim bilan gaplashadi, kim nimani biladi, kimga bog‘liq va odatiy tartib buzilganda nima bo‘ladi.\
2030-yilda bitta loyihaning qismlarini turli odamlar va turli SI’lar yaratishi mumkin. Har bir model o‘z topshirig‘ini ko‘rgan va uddalaganini ishonch bilan aytgan. Arxitektor har bir qism nima bo‘ldi deb hisoblayotganini va aslida nima bo‘lganini tushunishi kerak. Bekor qilish hikoyasidagidek: server koinlarni allaqachon qaytargan, SI agenti esa buni hali bilmaydi. Keyin u nima qiladi?\
Do‘koningiz o‘sha-o‘sha. Lekin unga bir yildan keyin uni o‘zgartirishi kerak bo‘lgan odamning ko‘zi bilan qarab ko‘r. U sizlarning suhbatlaringizni bilmaydi. Nega hammasi aynan shunday tuzilganini tushuna oladimi?\
Balki o‘sha odam sen bo‘larsan. Ikkimizning xotiramiz, albatta, ajoyib. Lekin baribir tushuntirish qoldirgan yaxshi. Xe-xe.***

## 5-topshiriq. Bekor qilish, olib ketish va o‘z testlaringiz

_09-kun, barcha yo‘nalishlar._

Buyurtmaning 3 ta holati bor: `created`, `cancelled`, `picked_up`. Faqat `created` holatidagi buyurtmani bekor qilish yoki olib ketish mumkin.

| **Yo‘nalish** | **5-topshiriqda nimani tugatish kerak** |
| --- | --- |
| Qoidalar va testlar | `src/domain.py`: `refund_amount`, `can_cancel`, `can_pickup` |
| Ma’lumotlar | `src/storage.py`: `cancel_order`, `confirm_pickup` |
| Buyurtma amallari | `src/order_handlers.py`: `cancel_order`, `confirm_pickup` |
| Yetakchi | `develop` tarmog‘iga birlashtirish, tekshiruvlarni umumiy ishga tushirish |

1\.  Bekor qilish va olib ketishni tugatinglar:

- bekor qilish tovar va koinlarni roppa-rosa 1 marta qaytaradi; qaytariladigan summa joriy narxdan emas, buyurtmaning saqlangan qiymatidan olinadi;
- olib ketish faqat holatni o‘zgartiradi: tovar va koinlar yaratishda allaqachon yechilgan;
- takroriy bekor qilish, takroriy olib ketish, bekor qilingan buyurtmani olib ketish va olib ketilgan buyurtmani bekor qilish — `ORDER_STATUS_ERROR` rad javobi; noma’lum buyurtma — `ORDER_NOT_FOUND`.

2\.  To‘liq yo‘lni o‘tinglar: buyurtma yaratish, holatini bilish, bekor qilish; boshqasini yaratish, olib ketish, olib ketilganini bekor qilishga urinish. Takroriy bekor qilish ssenariysi mijozda allaqachon yig‘ilgan: `python3 client.py scenario`.

3\.  O‘z testlaringizni kamida 3 ta holatgacha yetkazinglar:

- qiymatni hisoblash;
- ma’lumotlar o‘zgarmagan rad etish: products, stock, users, orders jadvallari tarkibini oldin va keyin solishtiringlar;
- buyurtma bilan takroriy amal.

Tayyor misol hisobga kirmaydi. Tekshiruvsiz testlar va `assert True` hisobga olinmaydi.

4\.  Testlar va umumiy tekshiruvni ishga tushiringlar:

- `python3 -m pytest -q`
- `python3 checks/acceptance.py --project . --profile base`

Tekshiruv xato bilan tugasa, birinchi xato xabaridan boshlanglar. Server xatti-harakatini tuzatinglar: tayyor tekshiruvlar va boshlang‘ich tovarlarni o‘zgartirish mumkin emas.

**Natija:** barcha 7 ta vosita ishlaydi; umumiy tekshiruv `base` profili uchun `PASS` bilan tugaydi; `testing/` ichida kamida 3 ta o‘z testingiz bor va ular o‘tadi.  

**Tekshiruv:** qabulda tekshiruvchi o‘zidagi tekshiruvlarning asl nusxasini va `pytest` ni ishga tushiradi. Yetakchi jamoaning bitta o‘z testini tahlil qiladi: kirish ma’lumotlari, kutilgan natija va test ushlaydigan xato. Yetakchi bekor qilish va olib ketishdan oldin holat tekshiruvini ko‘rsatadi va nega takroriy bekor qilish koinlarni yana qaytarmasligini tushuntiradi.  

**Nima uchun:** hozir holat tekshiruvi va takroriy bekor qilish testi server koinlarni bir marta qaytarishiga ishonch hosil qilishga yordam beradi. Hovuzdan keyin bu agent so‘rovni qayta yuborganda yoki ilovadagi tugma ikki marta bosilganda asqatadi. SI integratsiyalari muhandisi javobni ham, ma’lumotlar holatini ham tekshirishi kerak: takroriy so‘rov allaqachon bajarilgan qaytarishni takrorlamasligi kerak.

## 6-topshiriq. Konvert

_09-kun, butun jamoa._

💡 Umumiy `base` tekshiruvi xatosiz o‘tganda, [**bosinglar va konvertni olinglar**](http://21-school-programs.ru/page301377209.html)

Do‘konning yangi shartini o‘rganinglar: bitta o‘zgargan qoida va o‘z tekshiruv profilingiz (`E1`–`E5`).

1\.  Kodni o‘zgartirishdan oldin `docs/change.md` fayliga konvert raqamini va shartini hamda sizningcha qaysi fayllarga tegish kerak bo‘lishini yozinglar.

2\.  O‘zgarishni kiritinglar. Vosita nomlari, argumentlar va javob maydonlari saqlanadi.

3\.  Yangi xatti-harakatni eskisidan ajratadigan test qo‘shinglar.

4\.  Testlar va umumiy tekshiruvni o‘z konvertingiz profili bilan ishga tushiringlar:

- `python3 -m pytest -q`
- `python3 checks/acceptance.py --project . --profile E1`

`E1` o‘rniga o‘z konvertingiz raqamini qo‘yinglar.

5\.  `docs/change.md` fayliga aslida nimani o‘zgartirganingizni, qaysi test qoidalarni farqlashini va tekshiruv qanday tugaganini yozinglar.

6\.  Topshiriladigan profilni `RUN.md`, `docs/system.md` va `docs/change.md` fayllarida bir xil ko‘rsatinglar.

Birinchi urinishga — 45 daqiqa. Chiqmasa, qayerda to‘xtaganingizni yozinglar. Topshirishgacha davom etish yoki bazaviy qoidalarga qaytib, `base` ni topshirish mumkin. Olingan konvert raqami hisobotda qoladi.

**Natija:** `docs/change.md` faylida shart, fayllar haqidagi taxmin, haqiqiy o‘zgarish va tekshiruv natijasi yozilgan; profil 3 ta hujjatda bir xil.  

**Tekshiruv:** yetakchi yangi qoidani o‘z so‘zlari bilan aytib beradi, eski va yangi xatti-harakat farq qiladigan misol keltiradi va kodda qoida o‘zgartirilgan yoki o‘zgartirilishi mo‘ljallangan joyni ko‘rsatadi. `base` topshirilganda to‘liq tahlil bu topshiriq uchun 4 ga teng. 5 uchun olingan konvertning topshirilgan profili, rasmiy tekshiruvning `PASS` natijasi va yangi qoidaning o‘tadigan o‘z testi kerak. Tugallanmagan konvert boshqa topshiriqlar bahosini nolga tushirmaydi.  

**Nima uchun:** hozir konvert ishlayotgan serverda bitta qoidani topish va o‘zgartirish qanchalik oson ekanini ko‘rsatadi. Hovuzdan keyin bu ko‘nikma yangi chegirma yoki buyurtma limiti o‘zgarganda kerak bo‘ladi: SI integratsiyalari muhandisi chaqiruvlarning kelishilgan formatini saqlab, servis xatti-harakatini o‘zgartiradi. Yangi shart testi xatti-harakat farqini ko‘rsatadi, qolgan tekshiruvlarni qayta ishga tushirish esa yon xatolarni payqashga yordam beradi.

## 7-topshiriq. Serverni topshirish

_09-kun, butun jamoa._

Serverga SI agentini ulash kerak bo‘ladi. Bu ishni boshqa odamga topshirish uchun barcha kerakli narsa repozitoriyda bo‘lishi kerak.

1.  `RUN.md` faylini to‘ldiringlar:
    - ishga tushirish va tekshirish buyruqlari;
    - so‘rov va olingan javob misoli;
    - ishchi ma’lumotlarni yo‘qotmasdan `--db` orqali yangi o‘quv bazasidan qanday boshlash;
    - qaysi fayllar holatni saqlaydi: `--db` ko‘rsatilmagan `client.py call` qo‘lda chaqiruvlari `data/lavka.db` bilan ishlaydi, `--db` ko‘rsatilmagan `demo` va `scenario` vaqtinchalik baza yaratadi, jurnal `logs/client.jsonl` fayliga yoziladi;
    - topshiriladigan profil.
2.  `docs/system.md` faylini oxiriga yetkazinglar: so‘rov yo‘li, tizim chegaralari, qayerda tekshirilishi tushuntirilgan bitta rad etish misoli, topshiriladigan profil va «Boshqa mijozni ulash» bo‘limi: serverni ishga tushirish buyrug‘i `python3 -m src.server`, transport `stdio`.
3.  Mijoz haqiqiy ishga tushirish vaqtida yaratgan `logs/client.jsonl` jurnalini ilova qilinglar. Jurnal qo‘lda yozilmaydi va tuzatilmaydi.
4.  Jamoa ichida almashinglar: yo‘riqnomani jamoaning boshqa qismi bajaradi: repozitoriyning toza nusxasidan boshlaydi va matnni mualliflar ishtirokisiz tekshiradi. Og‘zaki ko‘rsatma kerak bo‘lgan joylarni tuzatinglar.

**Natija:** boshqa odam serverni `RUN.md` bo‘yicha ishga tushiradi va uning imkoniyatlarini `docs/system.md` bo‘yicha tushunadi.  

**Tekshiruv:** tekshiruvchi toza nusxadan `RUN.md` buyruqlarini bajaradi va jamoa ko‘rsatmalarisiz server javobini oladi. Tekshiruvchi oldida bajarilgan so‘rovdan keyin `logs/client.jsonl` faylida yangi yozuv paydo bo‘ladi. Yetakchi server kodi, kontraktlar, pasport, `RUN.md` va jurnalni ko‘rsatadi va har birining vazifasini tushuntiradi; baza va jurnal orasidagi farqni tushuntiradi.  

**Nima uchun:** hozir jamoaning boshqa qismi ishga tushirganda yo‘riqnomada tushib qolgan qadamlar aniqlanadi. Hovuzdan keyin SI integratsiyalari muhandisi servisni agentni ulaydigan yoki ilovani qo‘llab-quvvatlaydigan odamlarga topshirishi kerak bo‘ladi: ularga ishga tushirish buyruqlari, chaqiruv formati, servis chegaralari va natijani tekshirish usuli kerak. Tushunarli yo‘riqnoma mualliflarning doimiy og‘zaki ko‘rsatmalarisiz ishni davom ettirishga imkon beradi.

## 8-topshiriq. Keyingi jamoaviy ishga nimalarni olib o‘tamiz

08-kunda jamoaviy kelishuvlarni shakllantirdingizlar: qanday muloqot qilish, qaror qabul qilish, kelishmovchiliklarni hal qilish va bir-biringizning kuchli tomonlaringizdan foydalanishni muhokama qildingizlar. Endi birgalikdagi ishingiz yakunlanyapti. Olingan tajribani anglab olishni va kelajakdagi jamoalarda sizga nima asqatishini aniqlashni taklif qilamiz.

Kelajakka tayyorgarlik amaliyotlarini davom ettiramiz va Ichki tadbirkorlik ko‘nikmasini mashq qilamiz — umumiy ishni yaxshilash imkoniyatlarini payqash va foydali o‘zgarishlarni taklif qilish qobiliyatini.

Avval har kim shu ikki kundagi bir vaziyatni eslaydi va jamoaga qisqacha aytib beradi: ishga nima yordam bergan yoki xalaqit bergan, 08-kun kelishuvlari qanday ishlagan va kelajakda nima asqatadi. Alohida yozma javob kerak emas.

Keyin tajribani birga muhokama qilinglar. Foydali saboq olsa bo‘ladigan bitta vaziyatni tanlanglar. `docs/team.md` fayliga «Keyingi jamoaviy ishga nimalarni olib o‘tamiz» bo‘limini qo‘shinglar:
1. Vaziyat va xulosa. Nima bo‘ldi, ishga qanday ta’sir qildi va nimani o‘rgatdi? 08-kun kelishuvlarida nima yordam berdi yoki aniqlashtirishni talab qiladi?
2. Kelajak uchun yondashuv. Bitta qoida, usul yoki oddiy shablon taklif qilinglar. Qachon asqatishini va qanday yordam berishini ko‘rsatinglar.
3. Har kimning shaxsiy xulosasi. Har bir ishtirokchidan bittadan gap yozinglar: u keyingi jamoaviy ishga aynan nimani olib o‘tadi.

Qiyinchilik bo‘lmagan bo‘lsa, muvaffaqiyatli holatni tahlil qilinglar: yaxshi natijani nima ta’minladi va bu yondashuvni boshqa jamoada qanday saqlab qolish mumkin. Muammo yoki o‘zgarish o‘ylab topish kerak emas.

**Natija:** `docs/team.md` faylida aniq vaziyat, kelajakdagi jamoaviy ish uchun xulosa va har bir ishtirokchining qisqa shaxsiy xulosasi bor bitta umumiy bo‘lim. Yakunlanayotgan loyihada o‘zgarishni joriy qilish va uning ta’sirini isbotlash talab qilinmaydi.

**Tekshiruv:** yetakchi `docs/team.md` faylidagi «Keyingi jamoaviy ishga nimalarni olib o‘tamiz» bo‘limini ko‘rsatadi, kelgusi jamoaviy ish uchun ishtirokchilarning jamoaviy va shaxsiy xulosalarini taqdim etadi.

## Nazorat nuqtasi

Tekshiruvga GitLab’dagi jamoaviy repozitoriyning `develop` tarmog‘i topshiriladi.

Ishni tugatishdan oldin:

- Barcha yo‘nalishlar ishi `develop` tarmog‘iga birlashtirilgani va yuborilganiga ishonch hosil qilinglar.
- `git status` tekshiringlar: topshirmoqchi bo‘lgan fayllaringiz commit’lardan tashqarida qolmasligi kerak. Commit’larda lokal `data/*.db` bazalari va virtual muhit yo‘q.
- Topshiriladigan profil `RUN.md`, `docs/system.md` va `docs/change.md` fayllarida bir xil.
- `develop` tarmog‘ini alohida papkaga klonlanglar va loyihani `RUN.md` bo‘yicha ishga tushiringlar.
- `docs/team.md` faylida jamoaviy kelishuvlarning uchta bloki va kuchli tomonlardan birgalikda foydalanish misoli yoki ishni o‘zgartirish taklifi, shuningdek, har bir ishtirokchining shaxsiy xulosasi bilan «Keyingi jamoaviy ishga nimalarni olib o‘tamiz» bo‘limi yozilganini tekshiringlar.
- GitLab’da repozitoriyni ochinglar, `develop` tarmog‘ini tanlanglar va oxirgi o‘zgarishlar serverda ekanini tekshiringlar.
- Platformada loyihani yakunlanglar. Yuborishning o‘zi loyihani yakunlamaydi.

**Tekshiruv qanday o‘tadi.** Bir jamoa yetakchisi boshqa jamoa yetakchisini tekshiradi, qolgan ishtirokchilar qatnashishi va savol berishi mumkin. Tekshiruv 45 daqiqagacha davom etadi. Tekshiruvchi topshirilgan versiyani toza nusxada ishga tushiradi va repozitoriyingizdagi `checks/` papkasidan emas, o‘zidagi tekshiruvlarning asl nusxasidan foydalanadi. Taymer ostida yangi kod yozish kerak emas. Baho jamoa uchun umumiy: shaxsiy hissa, commit’lar va kod satrlari soni o‘lchanmaydi. Loyihaning bir qismi ishlamasa, qolgan topshiriqlar tekshirilaveradi. Qabul tartibi — `materials/acceptance.md` faylida.

Tekshiruvdan oldin o‘ylab ko‘ringlar:

- tovar yetarli bo‘lib, koinlar yetmasa, balansga nima bo‘ladi;
- nega har bir takroriy bekor qilishda koinlarni qaytarib bo‘lmaydi;
- mijozni qayta yozmaslik uchun xarid qoidasini qayerda o‘zgartirish kerak;
- vosita tavsifi uning argumentlarini tekshirishdan nimasi bilan farq qiladi;
- rad etishdan keyin bazada hech narsa o‘zgarmaganini qanday isbotlash mumkin;
- yordamchini ulash uchun keyingi kun dasturchisi nimalarni olishi kerak.

### Yakuniy natija

Sanab o‘tilganlarning barchasi GitLab’dagi `develop` tarmog‘ida bo‘lishi kerak.

| **Topshiriq** | **Nima topshiriladi** | **Qanday tekshiriladi** |
| --- | --- | --- |
| 1   | `docs/team.md`, `docs/system.md` faylida so‘rov yo‘li | Namoyish ishlaydi; yetakchi `get_product` yo‘lini ko‘rsatadi |
| 2   | `docs/team.md` faylida uch blok va kuchli tomonlardan birgalikda foydalanish misoli yoki ishni o‘zgartirish taklifi | Yetakchi o‘zaro ishlash qoidalarini, kelishmovchilik va kechikishlardagi harakatlar tartibini hamda kuchli tomonlar uyg‘unligini tushuntiradi |
| 3   | `contracts/tools_schemas.json`, `docs/system.md` faylida chegaralar | `TODO` bo‘lmagan 7 ta tavsif; yetakchi tavsif bo‘yicha vositani tanlaydi |
| 4   | `src/` ichida o‘qish va xarid kodi, `testing/` ichida testlar | Yangi bazada xarid va rad etish; tekshiruvlar tartibi va tranzaksiya |
| 5   | Bekor qilish va olib ketish kodi, kamida 3 ta o‘z testingiz | Umumiy tekshiruv `PASS`, `pytest` o‘tadi; yetakchi testni tahlil qiladi |
| 6   | `docs/change.md`, topshirilsa — konvert o‘zgarishi | Shart va misol; `base` bilan to‘liq tahlil uchun 4, tasdiqlangan konvert uchun 5 |
| 7   | `RUN.md`, `docs/system.md`, `logs/client.jsonl` | Tekshiruvchi serverni `RUN.md` bo‘yicha ishga tushiradi; jurnalda yangi yozuv paydo bo‘ladi |
| 8   | `docs/team.md` faylida «Keyingi jamoaviy ishga nimalarni olib o‘tamiz» bo‘limi | Aniq vaziyat, kelajak uchun qo‘llanadigan yondashuv va ishtirokchilarning shaxsiy xulosalari |

Berilgan `checks/` fayllari va `data/seed.sql` o‘zgarishsiz qoladi. Lokal bazalar va virtual muhit topshirishga kirmaydi.

> ***Og‘zaki ko‘rsatmalarsiz boshqa odamga hozirning o‘zida nimani topshirsa bo‘ladi? Server tayyorligini tekshirishni shundan boshla. Qoidalar tekshiruvlarga bardosh bersa va yo‘riqnoma ishlasa, SI agentini ulab ko‘rsa bo‘ladi.***

> ***Bu yana men. Seni nima ko‘proq qiziqtirdi: SI agenti iltimosni bajara olishiga erishishmi yoki hammasi qanday bog‘langanini va qoidalar o‘zgarsa nima bo‘lishini tushunishmi?***

> ***Yengilroq chiqqan narsa yoqdi, deb javob berishga shoshilma. Balki terminalga qaysi tomondan yondashishni umuman tushunmagandirsan. Endi senda keyingi tanlov uchun tayanch bo‘ladigan tajriba bor.\
Kim bo‘lganimizni hali ham aytmayman. Balki hozir boshqacha tanlarsan. Unda bu yerda, kelajakda, mening ham qayta ko‘rib chiqadigan narsam chiqadi…***

> ***Endi tasavvur qil: server ishlayapti, SI agenti so‘rovlarni bajaryapti va insonga javob beryapti. Hammasi mantiqli eshitiladi. Hatto o‘qish haddan tashqari yoqimli. Qaysi joyda nimadir noto‘g‘ri ekanidan shubhalanasan?\
Ertaga alohida to‘plam bo‘ladi — bugungi serverni ko‘chirish shart emas. Sen SI muhandisi kasbini sinab ko‘rasan: SI agentini yig‘asan va model taklifi qanday qilib bajarilgan amalga aylanishini tushunasan. Mana senga kelajakdan iltimos: ayniqsa o‘zingga yoqqan javobni diqqat bilan tekshir. Mashina biz eshitmoqchi bo‘lgan gapni aytganda, ikkalamiz ham savol berishni hayratlanarli darajada tez to‘xtatamiz. Ertagacha.***

💡 Ushbu loyiha haqida fikr-mulohaza qoldirish uchun [**shu yerni bos**](http://opros.so/BQbV3). Bu anonim va ta’limni yaxshilashimizga yordam beradi.

![img1](misc/images/д8.png)