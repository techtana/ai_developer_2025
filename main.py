from flask import Flask, render_template

# Import Blueprints
from solution_building.update_model import update_model_bp
from profile_building.create_questionaire import create_questionaire_bp
from make_recommendation.make_recommendation import make_recommendation_bp

def create_app():
    app = Flask(__name__)
    # Register Blueprints
    app.register_blueprint(create_questionaire_bp)
    app.register_blueprint(update_model_bp)
    app.register_blueprint(make_recommendation_bp)

    @app.route("/", methods=["GET"])
    def index():
        return render_template("index.html")
    
    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)