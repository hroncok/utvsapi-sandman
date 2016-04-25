from sandman2.model import db

from utvsapi import modelstore, mixins


@modelstore.register
class Destinations(mixins.CustomizingMixin, db.Model):
    __tablename__ = 'v_destination'

    id_destination = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    url = db.Column(db.String)


@modelstore.register
class Halls(mixins.CustomizingMixin, db.Model):
    __tablename__ = 'v_hall'

    id_hall = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    url = db.Column(db.String)


@modelstore.register
class Teachers(mixins.CustomizingMixin, db.Model):
    __tablename__ = 'v_lectors'

    id_teacher = db.Column('id_lector', db.Integer,
                           primary_key=True, key='id_teacher')
    title_before = db.Column(db.String)
    name = db.Column(db.String)
    surname = db.Column(db.String)
    title_behind = db.Column(db.String)
    personal_number = db.Column('pers_number', db.String,
                                key='personal_number')
    url = db.Column(db.String)


@modelstore.register
class Sports(mixins.CustomizingMixin, db.Model):
    __tablename__ = 'v_sports'

    id_sport = db.Column(db.Integer, primary_key=True)
    short = db.Column(db.String)
    sport = db.Column(db.String)
    description = db.Column(db.String)


@modelstore.register
class Enrollments(mixins.CustomizingMixin, db.Model):
    __tablename__ = 'v_students'

    id_enrollment = db.Column('id_student', db.Integer,
                              primary_key=True, key='id_enrollment')
    personal_number = db.Column(db.Integer)
    kos_kod = db.Column(db.String)
    course = db.Column('utvs', db.Integer,
                       db.ForeignKey('v_subjects.id_course'), key='course')
    semester = db.Column(db.String)
    registration_date = db.Column(db.DateTime)
    tour = db.Column(db.Boolean)
    kos_code = db.Column(db.Boolean)


@modelstore.register
class Courses(mixins.CustomizingMixin, db.Model):
    __tablename__ = 'v_subjects'

    id_course = db.Column('id_subjects', db.Integer,
                          primary_key=True, key='id_course')
    sport = db.Column(db.Integer, db.ForeignKey('v_sports.id_sport'))
    shortcut = db.Column(db.String)
    day = db.Column(db.Integer)
    begin = db.Column(db.String)
    end = db.Column(db.String)
    hall = db.Column(db.Integer, db.ForeignKey('v_hall.id_hall'))
    teacher = db.Column('lector', db.Integer,
                        db.ForeignKey('v_lectors.id_teacher'), key='teacher')
    notice = db.Column(db.String)
    semester = db.Column(db.Integer)

all = modelstore.reverse_models.values
