from datetime import datetime

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import render_template, request,


app = Flask(__name__)
app.debug = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:47458973@localhost/flaskDB'
db = SQLAlchemy(app)

class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ip = db.Column(db.String(50), nullable=True)
    Date = db.Column(db.DateTime)

    def __init__(self, ip, date):
        self.ip = ip
        self.Date = date

    def __repr__(self):
        return f"<{self.ip}>: {self.Date}"

@app.route('/')
def index():
    event = Event(request.remote_addr, datetime.utcnow())
    db.session.add(event)
    db.session.commit()
    data = Event.query.all()
    return render_template('index.html', data=data)


if __name__ == '__main__':
    app.run()

