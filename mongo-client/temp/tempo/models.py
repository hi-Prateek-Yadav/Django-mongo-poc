from mongoengine import Document, StringField, IntField, DynamicField

class YourModel(Document):
    field1 = StringField(max_length=100)
    field2 = IntField()
    field3 = StringField(max_length=100)
    dynamic_field = DynamicField() # dynamic field

    def __str__(self):
        return self.field1