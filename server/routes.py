from flask import jsonify, request
from flask_jwt_extended import jwt_required
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

from services import get_market_chart
from coinbase import get_coins_search, get_coins_summary, get_coins_histories
from auth import register_user, login_user

# Tum endpointler icin makul bir global limit; /api/prediction ayrica
# daha sikidir cunku model egitimi pahali bir islemdir.
limiter = Limiter(
    key_func=get_remote_address,
    default_limits=["200 per hour"],
)


def register_routes(app):
    limiter.init_app(app)

    @app.errorhandler(ValueError)
    def handle_value_error(error):
        # Girdi dogrulama hatalari (coin/period allowlist) icin temiz 400 dondur.
        return jsonify({'message': str(error)}), 400

    @app.route('/register', methods=['POST'])
    @limiter.limit("10 per hour")
    def register():
        return register_user(request.get_json(silent=True))

    @app.route('/login', methods=['POST'])
    @limiter.limit("20 per hour")
    def login():
        return login_user(request.get_json(silent=True))

    @app.route('/api/prediction', methods=['POST'])
    @jwt_required()
    @limiter.limit("30 per hour")
    def get_coins_prediction():
        data = request.get_json(silent=True) or {}
        coin = data.get('coin')
        period = data.get('period')
        predictions = get_market_chart(coin, period)
        return jsonify(predictions)

    @app.route('/api/get_coins_summary', methods=['GET'])
    @jwt_required()
    def coins_summary():
        result = get_coins_summary()
        return jsonify(result)

    @app.route('/api/get_coins_search', methods=['GET'])
    @jwt_required()
    def coins_search():
        result = get_coins_search()
        return jsonify(result)

    @app.route('/api/get_coins_histories', methods=['POST'])
    @jwt_required()
    def coins_histories():
        data = request.get_json(silent=True) or {}
        coin = data.get('coin')
        period = data.get('period')
        result = get_coins_histories(coin, period)
        return jsonify(result)
