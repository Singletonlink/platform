from __future__ import annotations

from flask import Blueprint, jsonify


api_bp = Blueprint("api", __name__)


@api_bp.get("/teams")
def list_teams():
    return jsonify([])


@api_bp.get("/projects")
def list_projects():
    return jsonify([])


@api_bp.get("/tasks")
def list_tasks():
    return jsonify([])

