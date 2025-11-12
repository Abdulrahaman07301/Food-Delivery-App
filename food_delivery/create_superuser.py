#!/usr/bin/env python
"""Script to create a Django superuser non-interactively"""
import os
import django

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'food_delivery.settings')
django.setup()

from django.contrib.auth.models import User

# Default credentials
username = 'admin'
email = 'admin@fooddelivery.com'
password = 'admin123'

# Check if superuser already exists
if User.objects.filter(username=username).exists():
    print(f"Superuser '{username}' already exists!")
    user = User.objects.get(username=username)
    if user.is_superuser:
        print(f"\n[SUCCESS] Existing Admin Credentials:")
        print(f"   Username: {username}")
        print(f"   Password: {password if user.check_password(password) else '(set previously)'}")
    else:
        # Make existing user a superuser
        user.is_superuser = True
        user.is_staff = True
        user.set_password(password)
        user.save()
        print(f"\n[SUCCESS] Updated user '{username}' to superuser!")
        print(f"\nAdmin Credentials:")
        print(f"   Username: {username}")
        print(f"   Password: {password}")
else:
    # Create new superuser
    User.objects.create_superuser(username=username, email=email, password=password)
    print(f"\n[SUCCESS] Superuser created successfully!")
    print(f"\nAdmin Credentials:")
    print(f"   Username: {username}")
    print(f"   Password: {password}")

print(f"\nAccess admin panel at: http://127.0.0.1:8000/admin/")

