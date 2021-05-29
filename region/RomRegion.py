from container.NBTTagBuilders import BlockStateBuilder
from region.Region import Region

class RomRegion(Region):
    def __init__(self, px, py, pz, name) -> None:
        super().__init__(2, 248, 77, blockstatebit=4, px=px, py=py, pz=pz, name=name)
    
    def _generate_blockstate_palette(self):
        self._blockstatepalette.append(BlockStateBuilder('minecraft:air').get_nbt_tag()) #0
        self._blockstatepalette.append(BlockStateBuilder('minecraft:polished_andesite').get_nbt_tag()) #1
        self._blockstatepalette.append(BlockStateBuilder('minecraft:brown_stained_glass').get_nbt_tag()) #2
        self._blockstatepalette.append(BlockStateBuilder('minecraft:white_stained_glass').get_nbt_tag()) #3
        self._blockstatepalette.append(BlockStateBuilder('minecraft:blue_stained_glass').get_nbt_tag()) #4
        self._blockstatepalette.append(BlockStateBuilder('minecraft:magenta_stained_glass').get_nbt_tag()) #5
        self._blockstatepalette.append(BlockStateBuilder('minecraft:pink_stained_glass').get_nbt_tag()) #6
        self._blockstatepalette.append(BlockStateBuilder('minecraft:cyan_stained_glass').get_nbt_tag()) #7
        self._blockstatepalette.append(BlockStateBuilder('minecraft:light_gray_stained_glass').get_nbt_tag()) #8
        self._blockstatepalette.append(BlockStateBuilder('minecraft:green_stained_glass').get_nbt_tag()) #9

        self._blockstatepalette.append(BlockStateBuilder('minecraft:emerald_block').get_nbt_tag()) #10
        self._blockstatepalette.append(BlockStateBuilder('minecraft:obsidian').get_nbt_tag()) #11
        self._blockstatepalette.append(BlockStateBuilder('minecraft:gold_block').get_nbt_tag()) #12
        self._blockstatepalette.append(BlockStateBuilder('minecraft:diamond_block').get_nbt_tag()) #13

        self._blockstatepalette.append(BlockStateBuilder('minecraft:black_stained_glass').get_nbt_tag()) #14
    
    def build_row(self, row, param):
        assert row < 248

        self._blockstate.insert(self._get_array_index(0, row, 0), 1)

        for i in range(6):
            self._blockstate.insert(self._get_array_index(0, row, i * 12 + 1), 2)
            self._blockstate.insert(self._get_array_index(0, row, i * 12 + 2), 3)
            self._blockstate.insert(self._get_array_index(0, row, i * 12 + 3), 4)
            self._blockstate.insert(self._get_array_index(0, row, i * 12 + 4), 5)
            self._blockstate.insert(self._get_array_index(0, row, i * 12 + 5), 3)
            self._blockstate.insert(self._get_array_index(0, row, i * 12 + 6), 6)
            self._blockstate.insert(self._get_array_index(0, row, i * 12 + 7), 3)
            self._blockstate.insert(self._get_array_index(0, row, i * 12 + 8), 7)
            self._blockstate.insert(self._get_array_index(0, row, i * 12 + 9), 8)
            self._blockstate.insert(self._get_array_index(0, row, i * 12 + 10), 3)
            self._blockstate.insert(self._get_array_index(0, row, i * 12 + 11), 9)
            self._blockstate.insert(self._get_array_index(0, row, i * 12 + 12), 3)
        
        self._blockstate.insert(self._get_array_index(0, row, 73), 2)
        self._blockstate.insert(self._get_array_index(0, row, 74), 3)
        self._blockstate.insert(self._get_array_index(0, row, 75), 4)
        self._blockstate.insert(self._get_array_index(0, row, 76), 14)

        for key, value in param.items():
            self._blockstate.insert(self._get_array_index(1, row, 75 - key), value)
    
    def _build(self):
        self._generate_blockstate_palette()
        
