# Ensure migrations/static collection run on every deploy before starting web
web: sh -c "cd food_delivery && python debug_db.py && python manage.py migrate --noinput && python manage.py collectstatic --noinput && gunicorn food_delivery.wsgi:application --workers=2 --bind=0.0.0.0:$PORT"


