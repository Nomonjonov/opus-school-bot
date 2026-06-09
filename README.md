# 🏫 O'quv Markaz Telegram Bot

## Funksiyalar

### O'quvchi uchun:
- 📝 Ro'yxatdan o'tish (ism, telefon, yosh/sinf, kurs)
- ⏳ Ariza holati kuzatish
- ℹ️ Markaz haqida ma'lumot

### Admin uchun:
- 👥 Tasdiqlangan o'quvchilar ro'yxati
- ✅ Kutayotgan arizalarni ko'rish va tasdiqlash/rad etish
- 📢 Barcha foydalanuvchilarga xabar yuborish (broadcast)
- 📚 Kurslar qo'shish va o'chirish

---

## O'rnatish

### 1. Fayllarni yuklab oling
```bash
git clone <repo_url>
cd edu_bot
```

### 2. Kutubxonalarni o'rnating
```bash
pip install -r requirements.txt
```

### 3. config.py ni to'ldiring
```python
BOT_TOKEN = "1234567890:ABCdef..."   # BotFather dan
ADMIN_IDS = [123456789]              # Sizning Telegram ID ingiz
```

> **ID ni bilish:** @userinfobot ga `/start` yuboring

### 4. Botni ishga tushiring
```bash
python bot.py
```

---

## Railway.app ga deploy qilish

1. GitHub ga push qiling
2. Railway.app da yangi project yarating
3. GitHub repo ni ulang
4. Environment variables qo'shing:
   - `BOT_TOKEN` = tokeningiz
   - `ADMIN_IDS` = `123456789` (vergul bilan ajrating)
5. Deploy!

---

## Fayl tuzilmasi

```
edu_bot/
├── bot.py          # Asosiy bot kodi
├── database.py     # SQLite baza funksiyalari
├── config.py       # Token va sozlamalar
├── requirements.txt
├── Procfile        # Railway uchun
└── README.md
```

---

## Default kurslar (o'zgartirishingiz mumkin)
- Matematika
- Ingliz tili  
- Informatika
- Fizika

Admin paneldan yangi kurs qo'shish yoki o'chirish mumkin.
