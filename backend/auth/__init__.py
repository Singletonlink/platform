from __future__ import annotations

from flask import Blueprint, jsonify, request


auth_bp = Blueprint("auth", __name__)


@auth_bp.post("/login")
def login():
    data = request.get_json(silent=True) or {}
    email = data.get("email")
    return jsonify({"message": "logged in (stub)", "email": email}), 200


@auth_bp.post("/register")
def register():
    data = request.get_json(silent=True) or {}
    email = data.get("email")
    return jsonify({"message": "registered (stub)", "email": email}), 201

