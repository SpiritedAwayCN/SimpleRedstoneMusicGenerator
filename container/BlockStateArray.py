from nbt.nbt import TAG_Long_Array


_TWO_64 = 2 ** 64

class BlockStateArray:
    def __init__(self, bit, init_size=0) -> None:
        self._bit = bit
        self._array = [0] * max(1, init_size)
        self._exponent_bit = (1 << bit) - 1
    
    def insert(self, index, value):
        assert value >= 0
        assert value <= self._exponent_bit

        st_index = (index * self._bit) // 64
        ed_index = ((index + 1) * self._bit - 1) // 64
        if len(self._array) <= ed_index:
            self._array.extend([0] * (ed_index - len(self._array) + 1))

        st_offset = (index * self._bit) % 64
        ed_offset = st_offset + self._bit

        mask = (_TWO_64 - 1) - ((self._exponent_bit << st_offset) & (_TWO_64 - 1))
        self._array[st_index] = (self._array[st_index] & mask) + (value << st_offset)
        # print(mask)

        remainder = self._array[st_index] // _TWO_64
        if remainder > 0:
            self._array[st_index] = self._array[st_index] & (_TWO_64 - 1)
            mask = _TWO_64 - (1 << (ed_offset - 64))
            self._array[ed_index] = (self._array[ed_index] & mask) + remainder
    
    def get_array(self):
        return self._array

    def get_bit(self):
        return self._bit
    
    def get_java_array(self):
        return list(map(lambda x: x if x < _TWO_64//2 else x - _TWO_64, self._array))
    
    def get_nbt_tag(self):
        a = TAG_Long_Array(name='BlockStates')
        a.value = self.get_java_array()
        return a

    def get_array_debug(self):
        return list(map(lambda x: bin(x), self._array))

if __name__ == '__main__':
    blockstates = BlockStateArray(5)

    for i in range(20):
        blockstates.insert(i, i)
    
    print(blockstates.get_java_array())