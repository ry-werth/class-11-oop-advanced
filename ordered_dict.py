class OrderedDict:
    def __init__(self):
        self._keys = []
        self._values = []

    def keys(self):
        return self._keys

    def values(self):
        return self._values

    def items(self):
        result = []
        for key, value in zip(self._keys, self._values):
            result.append((key,value))
        return result
        
    def __setitem__(self, key, value):
        if key not in self:
            self._keys.append(key)
            self._values.append(value)
        else:
            index = self.keys().index(key)
            self.values()[index] = value
            
        
    def __getitem__(self, search_key):
        for key, value in zip(self._keys, self._values):
            if key == search_key:
                return value
        raise KeyError(repr(search_key))
        
    def __contains__(self, item):
        for key in self._keys:
            if key == item:
                return True
        return False
        
    def __len__(self):
        return len(self._keys)
        
    def __eq__(self, other):
        if len(self) != len(other):
            return False
        for key, value in zip(self._keys, self._values):
            if not key in other.keys() or other[key] != value:
                return False
            if isinstance(other, OrderedDict):
                key_index = self.keys().index(key) 
                other_key_index = other.keys().index(key)
                if key_index != other_key_index:
                    return False
        return True
        
    def __ne__(self, other):
        return not self == other
    
    def __str__(self):
        s = '{'
        for key, value in zip(self._keys, self._values):
            s += '{}: {}, '.format(repr(key), repr(value))
        s = s.rstrip(', ')
        s += '}'
        return s
    
    __repr__ = __str__
    
    def __add__(self, other):
        new = OrderedDict()
        
        for key, value in self.items():
            new[key] = value
            
        for key, value in other.items():
            new[key] = value
        
        return new
            
    @classmethod
    def from_keys(cls, sequence):
        new = OrderedDict()
        for key in sequence:
            new[key] = None
            
        return new
        
        
        
        
