import os

from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from routes import register_routes


def _get_required_secret(name):
    """Kritik secret'i ortam degiskeninden oku; yoksa uygulamayi baslatma."""
    value = os.environ.get(name)
    if not value:
        raise RuntimeError(
            f"{name} ortam degiskeni tanimli degil. "
            f"Lutfen guvenli bir deger atayin (bkz. .env.example)."
        )
    return value


def _get_cors_origins():
    """CORS icin guvenilen origin listesini ortamdan oku.

    CORS_ORIGINS virgulle ayrilmis bir liste olarak verilebilir.
    Tanimli degilse gelistirme icin localhost varsayilanlari kullanilir.
    """
    raw = os.environ.get("CORS_ORIGINS")
    if raw:
        return [origin.strip() for origin in raw.split(",") if origin.strip()]
    return ["http://localhost:3000"]


app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = _get_required_secret("JWT_SECRET_KEY")
jwt = JWTManager(app)

CORS(
    app,
    resources={r"/*": {"origins": _get_cors_origins()}},
    supports_credentials=True,
)

register_routes(app)

if __name__ == "__main__":
    debug = os.environ.get("FLASK_DEBUG", "false").lower() in ("1", "true", "yes")
    app.run(debug=debug)
