from .models import YourModel

class YourModelSerializer:
    def __init__(self, instance):
        self.instance = instance

    def to_dict(self):
        return {
            'field1': self.instance.field1,
            'field2': self.instance.field2,
            'field3': self.instance.field3
        }
