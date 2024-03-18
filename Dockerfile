# Dockerfile

# Python version
FROM python:3.11

# Bu qator, Pythonning bayt kodi yozishini to'xtatadi. Bu, noqulay disk ishlatishni kamaytiradi va amalni tezlashtiradi.
ENV PYTHONDONTWRITEBYTECODE 1

# Bu qator, Pythonning chiqishlarini bufferni to'xtatadi. Bu, Pythonning chiqishlarini tezlik bilan ko'rsatish va Docker konteynerida tezda ko'rsatilishini ta'minlaydi.
ENV PYTHONUNBUFFERED 1

# Bu qator, Docker konteynerida ishlaydigan ishchi katalogini /app sifatida sozlaydi. Keyingi amallar bu katalogda amalga oshiriladi.
WORKDIR app

# Bu qator, mahalliy requeriments.txt faylini Docker konteyneriga ko'chiradi. Bu, Python kerakli modullarini Docker konteyneriga o'rnatish uchun ishlatiladi.
COPY requeriments.txt /app

# Bu qator, Python modullarini Docker konteynerida o'rnatish uchun ishlatiladi. requeriments.txt faylidagi modullar, pip install buyrug'i orqali o'rnatiladi.
RUN pip install -r requeriments.txt

# Bu qator, joriy katalogdagi barcha fayllarni (.), Docker konteyneriga ko'chiradi. Bu, Django ilovasini Docker konteyneriga o'rnatish uchun ishlatiladi.
COPY . /app