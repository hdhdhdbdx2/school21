# Python va Linux’da ishga tushirish

Loyiha buyruqlari terminalda repozitoriy ildizidan — `README.md` bor papkadan bajariladi. Ko‘rsatilgan bog‘liqliklar to‘plami uchun Python 3.12 yoki yangiroq versiya kerak. Kampus tayyorlash profili Python 3.12.14 dan foydalanadi; boshqa versiyada avval quyidagi tekshiruvni bajaring. Bash faollashtirish buyruqlari Linux va macOS’da bir xil.

## Kampus muhiti allaqachon tayyorlangan bo‘lsa

`campus_preflight.py --prepare` skripti alohida muhit yaratadi va Python paketlarini o‘rnatadi. Tayyorlash to‘plamida yo‘l `--venv` parametri bilan belgilanadi; standart ishga tushirish yo‘li — `$HOME/.venvs/bassein-12-10`. Texnik yordam boshqa yo‘l ko‘rsatgan bo‘lsa, undan foydalaning.

```bash
source "$HOME/.venvs/bassein-12-10/bin/activate"
python3 -c "import sys; print(sys.executable); print(sys.version)"
python3 check_environment.py
python3 client.py demo
```

Birinchi buyruq faqat mavjud muhitni faollashtiradi. `bin/activate` fayli topilmasa, bu yo‘lda tayyorlash hali bajarilmagan. Texnik yordamdan yo‘lni aniqlashtiring yoki quyidagi qadamlar bo‘yicha shaxsiy muhit yarating. Yangi terminalda faollashtirishni takrorlash kerak. Muhitdan chiqish uchun `deactivate` ni bajaring.

## Shaxsiy muhit yaratish kerak bo‘lsa

Loyiha ildizidan bajaring:

```bash
python3 --version
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -r requirements.txt -c requirements-campus.lock.txt
python3 -m pip check
python3 check_environment.py
python3 client.py demo
```

`requirements.txt` loyiha paketlarini sanaydi, `requirements-campus.lock.txt` esa ularning bog‘liqliklari versiyalarini cheklaydi. Buyruq faqat shu loyiha uchun kerakli paketlar daraxtini o‘rnatadi. O‘rnatish uchun ruxsat etilgan paketlar repozitoriysiga kirish kerak; tarmoq cheklangan bo‘lsa, tayyor kampus muhitidan foydalaning yoki texnik yordamga murojaat qiling.

`python3` yo‘q, versiya 3.12 dan past yoki muhit yaratishda `venv`/`ensurepip` yo‘qligi xabar qilinsa, tizim komponentlari kerak. Ularning nomi va o‘rnatish usuli Linux distributiviga bog‘liq — xatoning to‘liq matni bilan texnik yordamga murojaat qiling. Python paketlari muhit ichida o‘rnatiladi; `sudo pip`, `--user` va tizim Python himoyasini chetlab o‘tish kerak emas.

`.venv/` papkasini Git’ga qo‘shmang. Git, muharrir va brauzer — alohida dasturlar: `pip` ularni o‘rnatmaydi.

## Birinchi natija

Namoyish `hoodie` tovarini (narxi 500, M qoldig‘i — 5) va `missing` uchun ko‘zda tutilgan `PRODUCT_NOT_FOUND` rad javobini ko‘rsatishi kerak. Bu haqiqiy lokal MCP chaqiruvi. Chaqiruvning o‘zi uchun modelga kirish, API kaliti va internet kerak emas.

`python3 -m pytest testing/test_example.py -q` berilgan namunani tekshiradi. To‘liq `python3 checks/acceptance.py --project . --profile base` tekshiruvi boshlang‘ich shablonda o‘tmaydi: `TODO` bilan belgilangan tavsiflar va funksiyalar topshiriqlarda amalga oshiriladi.
