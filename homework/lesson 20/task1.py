class Personality:      # Singleton class
    __instance = None

    def __new__(cls):           # Class method creates allows to create a class instance
        if cls.__instance is None:      # in case there is no one created yet
            cls.__instance = super().__new__(cls)
        return cls.__instance       # In case there is one - it is returned

    def develop(self, feature, value):          # Method allows to develop any personality feature you want
        setattr(self, feature, value)
        return True

    def get_features(self):         # Method allows to get all created features with there values
        obj_attrs = [attr for attr in dir(self) if attr not in dir(Personality)]
        return {attr: getattr(self, attr) for attr in obj_attrs}


me = Personality()
second_me = Personality()

print(me, second_me)            # Both are the same

me.develop('humor', True)
me.develop('joy', 80)
print(me.get_features())


