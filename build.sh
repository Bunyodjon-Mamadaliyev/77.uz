#!/usr/bin/env bash
set -o errexit  # Agar xato bo‘lsa, deploy to‘xtasin

# Kutubxonalarni o‘rnatish
pip install -r requirements/production.txt

# Statik fayllarni yig‘ish
python manage.py collectstatic --noinput

# Migratsiyalarni bazaga qo‘llash
python manage.py migrate --noinput
