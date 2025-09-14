
from flask import Flask, render_template, request, jsonify
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config.config import DB_URI

# Import Blueprints
from funcs.create_questionaire import get_most_recent_activity
from funcs.make_recommendation import make_recommendation
from funcs.create_profile import use_llm_1

def create_app():
    app = Flask(__name__)
    

    # Set up SQLAlchemy engine and sessionmaker
    engine = create_engine(DB_URI)
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


    @app.route("/", methods=["GET"])
    def index():
        return render_template("directory.html")


    @app.route("/user", methods=["GET"])
    def user(uid):
        with SessionLocal() as session:
            prev_rec = get_most_recent_activity(session, uid)
            # prev_rec = {"uid": uid, "item": activity, "date": date}
        return render_template("user.html", uid=uid, prev_rec=prev_rec)
    

    @app.route('/submit', methods=['POST'])
    def submit():
        data = request.get_json()
        # split data into feedback and current_state
        feedback = {
            'user_id': data.get("user_id", {}),
            'feedback': data.get("prev_recommendations", {})
        }
        responses = {
            'user_id': data.get("user_id", {}),
            'response': data.get("responses", {})
        }

        # TODO @Nimesh: send response to llm #1
        # prompt = use_llm_1(responses)


        # TODO @Tech: send feedback and llm #1 response to llm #2
        


        # Here you would process the input and generate recommendations
        return render_template("user.html", data=data)
        
    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)