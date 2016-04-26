from sandman2.model import db

from utvsapi import modelstore, mixins


@modelstore.register
class Destinations(mixins.CustomizingMixin, db.Model):
    __tablename__ = 'v_destination'

    id = db.Column('id_destination', db.Integer, primary_key=True, key='id')
    name = db.Column(db.String)
    url = db.Column(db.String)


@modelstore.register
class Halls(mixins.CustomizingMixin, db.Model):
    __tablename__ = 'v_hall'

    id = db.Column('id_hall', db.Integer, primary_key=True, key='id')
    name = db.Column(db.String)
    url = db.Column(db.String)


@modelstore.register
class Teachers(mixins.CustomizingMixin, db.Model):
    __tablename__ = 'v_lectors'

    id = db.Column('id_lector', db.Integer,
                   primary_key=True, key='id')
    degrees_before = db.Column('title_before', db.String, key='degrees_before')
    first_name = db.Column('name', db.String, key='first_name')
    last_name = db.Column('surname', db.String, key='last_name')
    degrees_after = db.Column('title_behind', db.String, key='degrees_after')
    personal_number = db.Column('pers_number', db.String,
                                key='personal_number')
    url = db.Column(db.String)


@modelstore.register
class Sports(mixins.CustomizingMixin, db.Model):
    __tablename__ = 'v_sports'

    id = db.Column('id_sport', db.Integer, primary_key=True, key='id')
    shortcut = db.Column('short', db.String, key='shortcut')
    name = db.Column('sport', db.String, key='name')
    description = db.Column(db.String)


@modelstore.register
class Enrollments(mixins.CustomizingMixin, db.Model):
    __tablename__ = 'v_students'

    id = db.Column('id_student', db.Integer,
                   primary_key=True, key='id')
    personal_number = db.Column(db.Integer)
    kos_course_code = db.Column('kos_kod', db.String, key='kos_course_code')
    course = db.Column('utvs', db.Integer,
                       db.ForeignKey('v_subjects.id'), key='course')
    semester = db.Column(db.String)
    registration_date = db.Column(db.DateTime)
    tour = db.Column(db.Boolean)
    _kos_code = db.Column('kos_code', db.Boolean, key='_kos_code')


@modelstore.register
class Courses(mixins.CustomizingMixin, db.Model):
    __tablename__ = 'v_subjects'

    id = db.Column('id_subjects', db.Integer,
                   primary_key=True, key='id')
    sport = db.Column(db.Integer, db.ForeignKey('v_sports.id'))
    shortcut = db.Column(db.String)
    day = db.Column(db.Integer)
    starts_at = db.Column('begin', db.String, key='starts_at')
    ends_at = db.Column('end', db.String, key='ends_at')
    hall = db.Column(db.Integer, db.ForeignKey('v_hall.id'))
    teacher = db.Column('lector', db.Integer,
                        db.ForeignKey('v_lectors.id'), key='teacher')
    notice = db.Column(db.String)
    semester = db.Column(db.Integer)

all = modelstore.reverse_models.values
