class SomeObject:
    def __init__(self):
        self.integer_field = 0
        self.float_field = 0.0
        self.string_field = ""
        

class EventGet:
    def __init__(self, obj_type):
        self.obj_type = obj_type


class EventSet:
    def __init__(self, obj_data):
        self.obj_data = obj_data


class NullHandler:
    def __init__(self, successor=None):
        self.__successor = successor

    def handle(self, obj, event):
        if self.__successor is not None:
            return self.__successor.handle(obj, event)


class IntHandler(NullHandler):
    def handle(self, obj, event):
        if isinstance(event, EventGet) and (event.obj_type == int):
            return obj.integer_field
        elif isinstance(event, EventSet) and (type(event.obj_data) == int):
            obj.integer_field = event.obj_data
        else:
            return super().handle(obj, event)  


class FloatHandler(NullHandler):
    def handle(self, obj, event):
        if isinstance(event, EventGet) and (event.obj_type == float):
            return obj.float_field
        elif isinstance(event, EventSet) and (type(event.obj_data) == float):
            obj.float_field = event.obj_data
        else:
            return super().handle(obj, event)  


class StrHandler(NullHandler):
    def handle(self, obj, event):
        if isinstance(event, EventGet) and (event.obj_type ==  str):
            return obj.string_field
        elif isinstance(event, EventSet) and (type(event.obj_data) == str):
            obj.string_field = event.obj_data
        else:
            return super().handle(obj, event)  


obj = SomeObject()
obj.integer_field = 42
obj.float_field = 3.14
obj.string_field = "some text"
chain = StrHandler(IntHandler(FloatHandler(NullHandler)))
print(chain.handle(obj, EventGet(int)))
# 42
print(chain.handle(obj, EventGet(float)))
# 3.14
print(chain.handle(obj, EventGet(str)))
# 'some text'
chain.handle(obj, EventSet(100))
print(chain.handle(obj, EventGet(int)))
# 100
chain.handle(obj, EventSet(0.5))
print(chain.handle(obj, EventGet(float)))
# 0.5
chain.handle(obj, EventSet('new text'))
print(chain.handle(obj, EventGet(str)))
# 'new text'