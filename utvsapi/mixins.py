import datetime

from sandman2.model import db, Model

from utvsapi import modelstore


class CustomizingMixin(Model):
    '''Mixin that fixes primary_key method
    and adds customization for the output'''

    def to_dict(self):
        '''Return the resource as a dictionary'''
        result_dict = {'_links': {}}
        for column in self.__table__.columns:
            name = column.key
            value = result_dict[name] = getattr(self, name, None)
            if column.foreign_keys:
                # Foreign key, turn it to a link, HATEOAS, yay!
                # We always have only one f. key in one column
                fk = list(column.foreign_keys)[0]
                model = modelstore.reverse_lookup(fk.column.table)
                instance = model.query.filter_by(id=int(value)).first()
                if instance:
                    result_dict['_links'][name] = {'href': instance.resource_uri()}
                    del result_dict[name]
            elif isinstance(column.type, db.Integer):
                # Return the value as int, otherwise it might
                # get returned as str due to bad SQL type
                result_dict[name] = int(value)
            elif isinstance(value, datetime.datetime):
                # Display datetimes in ISO format
                result_dict[name] = value.isoformat()
        result_dict['_links']['self'] = {'href': self.resource_uri()}
        try:
            if not result_dict['_kos_code']:
                result_dict['kos_course_code'] = None
            del result_dict['_kos_code']
        except KeyError:
            pass
        return result_dict

    def primary_key(self):
        '''Return the key of the model's primary key field

        https://github.com/jeffknupp/sandman2/pull/35'''
        return list(self.__table__.primary_key.columns)[0].key
