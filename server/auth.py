from flask import jsonify
from flask_jwt_extended import create_access_token
from models import User


def register_user(data):
    email = (data or {}).get('email')
    password = (data or {}).get('password')

    if not email or not password:
        return jsonify({'message': 'Email and password are required'}), 400

    user = User.find_by_email(email)

    if user:
        return jsonify({'message': 'User already exists'}), 400

    # Sifre, generate_password_hash ile hashlenerek saklanir.
    user = User.create(email, password)
    user.save()

    return jsonify({'message': 'User created successfully'}), 201


def login_user(data):
    email = (data or {}).get('email')
    password = (data or {}).get('password')

    if not email or not password:
        return jsonify({'message': 'Invalid email or password'}), 401

    user = User.find_by_email(email)

    # Sifre, check_password_hash ile dogrulanir (duz metin karsilastirma yok).
    if not user or not user.check_password(password):
        return jsonify({'message': 'Invalid email or password'}), 401

    access_token = create_access_token(identity=str(user.email))

    return jsonify({'access_token': access_token}), 200
