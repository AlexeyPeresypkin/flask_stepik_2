from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

teachers_goals_association = db.Table(
    'teachers_goals',
    db.Column('teacher_id', db.Integer, db.ForeignKey('teachers.id')),
    db.Column('goal_id', db.Integer, db.ForeignKey('goals.id'))
)


class Goal(db.Model):
    __tablename__ = 'goals'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, unique=True)
    translate_title = db.Column(db.String)
    teachers = db.relationship(
        'Teacher', secondary=teachers_goals_association, back_populates='goals'
    )
    # applicationforms = db.relationship('ApplicationForm')


class Teacher(db.Model):
    __tablename__ = 'teachers'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    about = db.Column(db.String)
    rating = db.Column(db.Float)
    picture = db.Column(db.String)
    price = db.Column(db.Integer)
    goals = db.relationship(
        'Goal', secondary=teachers_goals_association, back_populates='teachers'
    )
    free = db.Column(db.JSON())


class Booking(db.Model):
    __tablename__ = 'bookings'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    phone = db.Column(db.String, nullable=False)
    time = db.Column(db.String)
    day = db.Column(db.String)
    teacher_id = db.Column(db.Integer, db.ForeignKey('teachers.id'))
    teacher = db.relationship('Teacher')


class ApplicationForm(db.Model):
    __tablename__ = "applicationforms"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    phone = db.Column(db.String, nullable=False)
    time = db.Column(db.String)
    goal_id = db.Column(db.Integer, db.ForeignKey('goals.id'))
    goal = db.relationship('Goal')
