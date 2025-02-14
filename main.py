from flask import Flask, Blueprint, request, jsonify
from flask_cors import CORS
from datetime import datetime

from config.database import sql_exec

app = Flask(__name__)

CORS(app)

v1_bp = Blueprint("v1", __name__, url_prefix="/v1")

chats_bp = Blueprint("chats", __name__, url_prefix="/chats")
users_bp = Blueprint("users", __name__, url_prefix="/users")


@users_bp.route("/login", methods=["POST"])
def logIn():
    data = request.get_json()

    payload = {
        "username": data["username"],
        "avatar": data["avatar"],
        "createdAt": datetime.now().isoformat(),
        "updatedAt": datetime.now().isoformat(),
    }

    cur, con = sql_exec(
        """INSERT INTO users (username, avatar, createdAt, updatedAt)
		VALUES (:username, :avatar, :createdAt, :updatedAt)""",
        payload,
    )
    last_id = cur.lastrowid
    con.commit()
    con.close()

    payload["id"] = last_id

    return jsonify({
        "statusText": "created",
        "record": payload
    }), 201


@chats_bp.route("/channel", methods=["GET"])
def get_channel_messages():
    cur, con = sql_exec(
        """SELECT c.id, c.senderId, c.message, c.mimeType, u.username, u.avatar, c.createdAt, c.updatedAt
      FROM chats c
      INNER JOIN users u
      ON c.senderId = u.id
      ORDER BY c.createdAt DESC"""
    )

    query = cur.fetchall()
    messages = list()

    for row in query:
        id, senderId, row, mimeType, username, avatar, createdAt, updatedAt = row
        messages.append({
            "id": id,
            "senderId": senderId,
            "username": username,
            "avatar": avatar,
            "message": row,
            "mimeType": mimeType,
            "createdAt": createdAt,
            "updatedAt": updatedAt,
        })
    con.close()

    return jsonify(messages), 200


@chats_bp.route("/send", methods=["POST"])
def send_message():
    data = request.get_json()
    payload = {
        "senderId": data["senderId"],
        "message": data["message"],
        "mimeType": "plain/text",
        "createdAt": datetime.now().isoformat(),
        "updatedAt": datetime.now().isoformat(),
    }

    cur, con = sql_exec(
        """INSERT INTO chats (senderId, message, mimeType, createdAt, updatedAt)
		VALUES (:senderId, :message, :mimeType, :createdAt, :updatedAt)""",
        payload,
    )
    last_id = cur.lastrowid
    con.commit()
    con.close()

    payload["id"] = last_id

    return jsonify({
        "statusText": "created",
        "record": payload
    }), 201


v1_bp.register_blueprint(chats_bp)
v1_bp.register_blueprint(users_bp)

app.register_blueprint(v1_bp)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
