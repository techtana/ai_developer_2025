from flask import Flask

# Import Blueprints
from profile_building.update_model import update_model_bp
from profile_building.login import login_bp
from solution_building.make_recommendation import make_recommendation_bp

def create_app():
    app = Flask(__name__)
    # Register Blueprints
    app.register_blueprint(update_model_bp)
    app.register_blueprint(login_bp)
    app.register_blueprint(make_recommendation_bp)

    @app.route("/")
    def index():
        return {"message": "AI Developer 2025 Flask API is running."}

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)