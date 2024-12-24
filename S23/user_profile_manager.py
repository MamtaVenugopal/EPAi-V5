from datetime import datetime
import weakref # Import the weakref module
class ValidatedProperty:
    def __init__(self, type_, validate_empty_string=False, validate_email=False,validate_login=False):
        """
        Initializes the ValidatedProperty descriptor.

        Args:
            type_: The expected type of the property.
            validate_empty_string: If True, validates against empty strings.
                                    Defaults to False, allowing empty strings.
            validate_email: If True, validates if the string contains "@" and ".".
                             Defaults to False, no email validation.
        """
        self.data = {}

        self._type = type_
        self.validate_empty_string = validate_empty_string
        self.validate_email = validate_email
        self.validate_login = validate_login  # New parameter to control nullability

    def __set_name__(self, owner_class, prop_name):
        self.prop_name = prop_name

    def __set__(self, instance, value):
        if value is not None and not isinstance(value, self._type):
            raise ValueError(f'{self.prop_name} must be of type 'f'{self._type.__name__}')
        if self.validate_empty_string and not len(value.strip()) > 0:
            raise ValueError(f'Invalid: Empty string not allowed for {self.prop_name}')
        elif self.validate_empty_string and len(value.strip()) > 0:
            print("Valid String")

        # Separate checks for "@" and "." with specific error messages
        if self.validate_email:
            if "@" not in value:
                raise ValueError(f"Invalid email format for {self.prop_name}: Missing '@'")
            if "." not in value:
                raise ValueError(f"Invalid email format for {self.prop_name}: Missing '.'")


        if self.validate_login:
           if value is not None and not isinstance(value, self._type):
                raise ValueError(f'{self.prop_name} must be of type 'f'{self._type.__name__}')

        instance.__dict__[self.prop_name] = value
        self.data[id(instance)] = (weakref.ref(instance, self._finalize_instance), value)
        print('Data presented:',self.data)

    def __get__(self, instance, owner_class):
        if instance is None:
            return self
        else:
            return instance.__dict__.get(self.prop_name, None)
    def _finalize_instance(self, weak_ref):
        reverse_lookup = [key for key, value in self.data.items()
                         if value[0] is weak_ref]
        if reverse_lookup:
            # key found
            key = reverse_lookup[0]
            del self.data[key]



class UserProfileManager:
    username = ValidatedProperty(str, validate_empty_string=True)
    email = ValidatedProperty(str, validate_email=True)  # Enable email validation
    last_login = ValidatedProperty(datetime, validate_login=True)  # Allow last_login to be None
    cache = weakref.WeakValueDictionary()  # Use WeakValueDictionary for cache

    def __init__(self, name=None):
        self.name = name

    def add_to_cache(self):
        print("Adding to cache")
        self.cache[id(self)] = self
        print('whats in cache',self.cache)
        # Access data through the descriptors
        for name in ['username', 'email', 'last_login']:
            descriptor = getattr(self.__class__, name)  # Get the descriptor instance
            if id(self) in descriptor.data:
                key = id(self)
                value = descriptor.data[key][1]
                print(f"  Key: {key}, Value: {value}")
        return self.cache


    @classmethod
    def get_from_cache(cls, cache_add):
        ref = cls.cache.get(cache_add)
        print('ref name',ref)
        if ref:
            return cls.cache.get(cache_add)

        return None