#!/usr/bin/env bash
set -e

python manage.py migrate --noinput
python manage.py collectstatic --noinput

if [ "${DEMO_CREATE_DOCTOR}" = "true" ]; then
  python manage.py shell -c "from django.contrib.auth import get_user_model; User=get_user_model(); u,created=User.objects.get_or_create(username='${DEMO_DOCTOR_USER}', defaults={'rol':'doctor','email':'${DEMO_DOCTOR_EMAIL}'}); 
u.rol='doctor'; 
u.is_active=True; 
u.set_password('${DEMO_DOCTOR_PASSWORD}'); 
u.save()"
fi

gunicorn config.wsgi:application --bind 0.0.0.0:${PORT:-8000}
