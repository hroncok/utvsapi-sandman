import datetime

from sandman2.model import db, Model

from utvsapi import modelstore


class CustomizingMixin(Model):
    '''Mixin that fixes primary_key method
    and adds customization for the output'''
    def to_dict(self):
        '''Return the resource as a dictionary'''
        result_dict = {}
        for column in self.__table__.columns:
            name = column.key
            value = result_dict[name] = getattr(self, name, None)
            try:
                if column.foreign_keys:
                    # Foreign key, turn it to a link, HATEOAS, yay!
                    # We always have only one f. key in one column
                    fk = list(column.foreign_keys)[0]
                    model = modelstore.reverse_lookup(fk.column.table)
                    instance = model.query.get(int(value))
                    if instance:
                        result_dict[name] = instance.resource_uri()
                elif isinstance(column.type, db.Integer):
                    # Return the value as int, otherwise it might
                    # get returned as str due to bad SQL type
                    result_dict[name] = int(value)
                elif isinstance(value, datetime.datetime):
                    # Display datetimes in ISO format
                    result_dict[name] = value.isoformat()
            except (TypeError, ValueError):
                pass  # data header won't pass
            result_dict['self'] = self.resource_uri()
        return result_dict

    def primary_key(self):
        '''Return the key of the model's primary key field'''
        return list(self.__table__.primary_key.columns)[0].key
