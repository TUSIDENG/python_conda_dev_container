class LogMixin:
    def log(self, message):
        print(f"[{self.__class__.__name__}] {message}")

class SerializeMixin:
    def to_dict(self):
        return self.__dict__

class User(LogMixin, SerializeMixin):
    def __init__(self, name, age):
        self.name = name
        self.age = age

u = User("Alice", 30)
u.log("created")       # [User] created
print(u.to_dict())     # {'name': 'Alice', 'age': 30}
