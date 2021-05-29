from nbt.nbt import *

class TagBuilder:
    def __init__(self, name=None, root_name=None) -> None:
        self._root = TAG_Compound()
        self._properties = TAG_Compound()
        # if name:
        self._properties.name = name
        # if root_name:
        self._root.name = root_name

        self._cache = None
    
    def add_property(self, tag):
        self._properties.tags.append(tag)
        return self
    
    def add_common_property(self, tag):
        self._root.tags.append(tag)
        return self
    
    def get_nbt_tag(self):
        if len(self._properties.tags) == 0:
            return self._root

        if not self._cache is None:
            return self._cache
        
        self._root.tags.append(self._properties)
        self._cache = self._root
        return self._root