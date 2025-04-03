__all__ = ['LruCache']


class LruCache:

    """
        This class represents Lru cache.

    """
    def __init__(self, size):
        """

        :param size: the size of the cache
        """
        self._size = size
        self._dict_cache = dict()
        self._list_keys = list()

    def put(self, key:any, value: any):
        """

        :param key: the key of the value
        :param value:the value that we want to put in the cache

        """

        if value not in self._dict_cache.values():

            # if the cache full delete the last key
            if len(self._dict_cache) == self._size:
                key1 = self._list_keys[0]
                self._list_keys.remove(key1)
                self._dict_cache.pop(key1)

            # insert the new key and value
            self._dict_cache[key] = value
            self._list_keys.append(key)

    def get(self, key: any):
        """
        :return: return the value if the key is found else return none
        """
        if key in self._dict_cache:
            self._list_keys.remove(key)
            self._list_keys.append(key)
            return self._dict_cache[key]
        else:
            return None

    def __str__(self):
        """

        :return str of all the key and the value
        """
        str_1 = ""
        for key, val in self._dict_cache.items():
            str_1 = str_1 + f"{key} : {val} \n"
        return str_1

    def __hash__(self):
        return hash((self._dict_cache.keys()))


if __name__ == "__main__":
    my_cache = LruCache(3)
    my_cache.put(key=1,value='a')
    my_cache.put(key=2,value='b')
    my_cache.put(key=3,value='c')
    print(my_cache)
    print(my_cache.get(key=1)) # should print: a
    print(my_cache.get(key=2)) # should print: b
    my_cache.put(key=4,value='d')
    print(my_cache.get(key=4)) # should print: d
    print(my_cache) # should print my_cache in a readable way


