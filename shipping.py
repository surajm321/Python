class ShippingContainer:

    nextSerial = 1337

    @classmethod
    def _get_next_serial(cls):
        result = cls.nextSerial
        cls.nextSerial += 1
        return result

    @classmethod
    def create_empty(cls,owner_code):
        return cls(owner_code,contents=None)

    @classmethod
    def create_with_items(cls,owner_code, items):
        return cls(owner_code,contents=list(items))

#  @staticmethod
#  def _get_next_serial():
#        result = ShippingContainer.nextSerial
#        ShippingContainer.nextSerial += 1
#        return result


    def __init__(self, owner_code, contents):
        self.owner_code = owner_code
        self.contents = contents
        self.serial = ShippingContainer._get_next_serial()
