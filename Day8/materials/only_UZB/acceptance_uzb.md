# 45 daqiqada qabul qilish

Yetakchi boshqa jamoa yetakchisini tekshiradi. Qolgan ishtirokchilar qatnashishi va savol berishi mumkin. Platformani faqat tekshiruvchi yetakchi to‘ldiradi. Natija jamoa uchun umumiy, shaxsiy hissa baholanmaydi.

## Ishga tushirishdan oldin

Repozitoriyning yuborilgan versiyasi tekshiriladi. Tekshirilayotgan jamoa ish joyida uning yetakchisi o‘z kirish huquqi bilan yuborilgan kommitning alohida toza nusxasini ochadi. Tekshiruvchi kommit identifikatorini platforma bilan solishtiradi va `git status --short` ni ko‘radi: manba fayllarida lokal tahrirlar bo‘lmasligi kerak. Boshqalarning parolini berish va yopiq repozitoriyni boshqa birovning akkaunti ostida klonlash kerak emas.

Ish joyidagi muhit allaqachon tayyorlangan. Tekshiruvchi `checks/acceptance.py` ning o‘zidagi boshlang‘ich nusxasini ishga tushirib, loyihaning toza nusxasiga yo‘lni va e’lon qilingan profilni beradi. Tashkilotchi bu nusxani qanday berishi uning reglamentida tavsiflangan.

Boshlang‘ich tekshiruvlar qo‘shni `official_checks` papkasida bo‘lsa, buyruq misoli:

~~~bash
python3 ../official_checks/acceptance.py --project . --profile base
~~~

## Tekshiruv jarayoni

| Vaqt | Nima sodir bo‘ladi |
| --- | --- |
| 0–5 daqiqa | Repozitoriy, kommit, profilni solishtirish va muhit tekshiruvini ishga tushirish |
| 5–13 daqiqa | Yetakchi mijoz orqali so‘rov, xarid va rad etishni ko‘rsatadi |
| 13–23 daqiqa | Umumiy tekshiruvlar va jamoa testlarini ishga tushirish; natijani o‘qish |
| 23–35 daqiqa | Chaqiruv yo‘li, qoida joyi, tranzaksiya va konvert natijasini tahlil qilish |
| 35–40 daqiqa | Aniqlashtiruvchi savollar, jumladan, qatnashayotgan ishtirokchilardan |
| 40–45 daqiqa | Tekshiruvchi yetakchi platformani to‘ldiradi va belgilarni tushuntiradi |

Savollar taqdim etilgan loyiha bilan cheklanadi. Tekshiruvchi yangi funksiya yozishni so‘ramaydi va butun Python bo‘yicha so‘rov o‘tkazmaydi.

## Asosiy qism

Har bir band bo‘yicha tekshiruvchi «ha» yoki «yo‘q» qo‘yadi va «yo‘q» bo‘lsa, kuzatilgan sababni ko‘rsatadi.

1. **Ishga tushirish.** Topshirilgan versiya tayyorlangan muhitda `RUN.md` bo‘yicha ishga tushadi; haqiqiy MCP chaqiruvi namoyish etilgan.
2. **Xatti-harakat.** Tanlangan profilning umumiy tekshiruvi xatosiz tugaydi; yettita majburiy vosita mavjud.
3. **Kodni ajratish.** Jamoa bitta misolda tegishli qismlardagi ishlov beruvchi, qoida va SQL ni ko‘rsatadi; qoida hisobini bazasiz chaqirish mumkin.
4. **O‘z tekshiruvlari.** Uchta mazmunli test bor va o‘tadi: hisoblash, holat o‘zgarmaydigan rad etish, takroriy amal. Tayyor namuna ularning o‘rnini bosmaydi.
5. **Tushuntirish.** Yetakchi bitta so‘rov yo‘lini tushuntiradi va tanlangan xatoning oldini oladigan kodni ko‘rsatadi. «Bu tekshiriladi» degan umumiy gap yetarli emas.
6. **Topshirish.** Kontraktlar, `RUN.md` va pasport xatti-harakatga mos; profil, kirish chegaralari va jurnal yo‘li ko‘rsatilgan; jurnal haqiqiy ishga tushirishda yaratilgan.
7. **Konvert natijasi.** `docs/change.md` faylida shart, tegiladigan fayllar haqidagi taxmin, haqiqiy natija va topshirish profili bor. Tugallanmagan urinish mumkin.

Asosiy qism barcha yetti band bajarilganda hisobga olinadi. Rollar taqsimoti, kommitlar soni va shaxsiy kod hajmi baholash mezonlari emas.

## Konvert uchun qo‘shimcha band

Yangi qoida amalga oshirilgan, tegishli profilning umumiy tekshiruvlari o‘tgan va jamoa eski hamda yangi xatti-harakatni farqlaydigan o‘z testini ko‘rsatgan bo‘lsa, hisobga olinadi. Yetakchi nega o‘zgarish aynan shu qismga kiritilganini tushuntiradi.

Jamoa `base` ni topshirsa, qo‘shimcha band hisobga olinmaydi. To‘g‘ri amalga oshirilgan konvert o‘z profili bo‘yicha tekshiriladi: masalan, to‘liq qaytarish haqidagi eski kutilma yangi komissiyani tekshirishga xalaqit bermasligi kerak.

## Biror narsa ishlamasa

Loyiha xatosi tegishli bandda belgilanadi. Boshlangan qabul qilishda o‘ylab topilgan «qayta ishlashga qaytarish» amali yo‘q: natija platforma vositalari bilan qayd etiladi.

Tayyorlangan muhit ishga tushmasa yoki maydoncha nosozligi tufayli yuborilgan versiyaga kirib bo‘lmasa, xodimlarni chaqiring. Texnik nosozlik alohida qayd etiladi va biznes qoidasi xatosi sifatida ko‘rsatilmaydi.

