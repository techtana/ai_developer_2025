
from sqlalchemy.orm import Session, declarative_base
from sqlalchemy import Column, Integer, String, DateTime, desc

Base = declarative_base()

# Assuming you have a model like this:
class Activity(Base):
    __tablename__ = 'activity'
    uid = Column(String, primary_key=True)
    date = Column(DateTime)
    activity = Column(String)
    feedback = Column(Integer)


example_output = ("Go running for 30 minutes", "2025-09-14")

def get_most_recent_activity(session: Session, uid: str):
    # result = (
    #     session.query(Activity.activity, Activity.date)
    #     .filter(Activity.uid == uid)
    #     .order_by(desc(Activity.date))
    #     .first()
    # )

    # testing only
    result = example_output

    if result:
        activity, date = result
        return {"uid": uid, "item": activity, "date": date}
    else:
        return None