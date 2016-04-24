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
    __renames__ = {
        'id_lector': 'id_teacher',
        'pers_number': 'personal_number',
    }

    id_lector = db.Column(db.Integer, primary_key=True)
    title_before = db.Column(db.String)
    name = db.Column(db.String)
    surname = db.Column(db.String)
    title_behind = db.Column(db.String)
    pers_number = db.Column(db.String)
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
    __renames__ = {
        'id_student': 'id_enrollment',
        'utvs': 'course',
    }

    id_student = db.Column(db.Integer, primary_key=True)
    personal_number = db.Column(db.Integer)
    kos_kod = db.Column(db.String)
    utvs = db.Column(db.Integer, db.ForeignKey('v_subjects.id_subjects'))
    semester = db.Column(db.String)
    registration_date = db.Column(db.DateTime)
    tour = db.Column(db.Boolean)
    kos_code = db.Column(db.Boolean)


@modelstore.register
class Courses(mixins.CustomizingMixin, db.Model):
    __tablename__ = 'v_subjects'
    __renames__ = {
        'id_subjects': 'id_course',
        'lector': 'teacher',
    }

    id_subjects = db.Column(db.Integer, primary_key=True)
    sport = db.Column(db.Integer, db.ForeignKey('v_sports.id_sport'))
    shortcut = db.Column(db.String)
    day = db.Column(db.Integer)
    begin = db.Column(db.String)
    end = db.Column(db.String)
    hall = db.Column(db.Integer, db.ForeignKey('v_hall.id_hall'))
    lector = db.Column(db.Integer, db.ForeignKey('v_lectors.id_lector'))
    notice = db.Column(db.String)
    semester = db.Column(db.Integer)

all = modelstore.reverse_models.values
