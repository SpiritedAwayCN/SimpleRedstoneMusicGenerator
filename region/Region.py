from container.TagBuilder import TagBuilder
from nbt import nbt

from container.NBTTagBuilders import BlockStateBuilder
from container.BlockStateArray import BlockStateArray

class Region:
    def __init__(self, sx, sy, sz, pending_block_tick=False,
            blockstatebit=3, px=0, py=0, pz=0, name=None) -> None:
        self._sx = sx
        self._sy = sy
        self._sz = sz
        self._px = px
        self._py = py
        self._pz = pz

        assert not name is None
        self.name = name
    
        self._blockstate = BlockStateArray(blockstatebit, (sx * sy * sz * blockstatebit + 63) // 64)

        self._blockstatepalette = nbt.TAG_List(name='BlockStatePalette', type=nbt.TAG_Compound)
        self._tileeneities = nbt.TAG_List(name='TileEntities', type=nbt.TAG_Compound)

        if pending_block_tick:
            self._pendingblockticks = nbt.TAG_List(name='PendingBlockTicks', type=nbt.TAG_Compound)
        else:
            self._pendingblockticks = nbt.TAG_List(name='PendingBlockTicks', type=nbt._TAG_End)
        
        self._pendingfluidticks =  nbt.TAG_List(name='PendingFluidTicks', type=nbt._TAG_End)
        self._entities =  nbt.TAG_List(name='Entities', type=nbt._TAG_End)
    
    def _get_array_index(self, x, y, z):
        return z * self._sx + y * self._sx * self._sz + x

    def build_nbt_full(self):
        self._build()

        root = nbt.TAG_Compound()
        root.name = self.name

        position = TagBuilder(root_name='Position')
        position.add_common_property(nbt.TAG_Int(self._px, 'x'))
        position.add_common_property(nbt.TAG_Int(self._py, 'y'))
        position.add_common_property(nbt.TAG_Int(self._pz, 'z'))

        size = TagBuilder(root_name='Size')
        size.add_common_property(nbt.TAG_Int(self._sx, 'x'))
        size.add_common_property(nbt.TAG_Int(self._sy, 'y'))
        size.add_common_property(nbt.TAG_Int(self._sz, 'z'))

        root.tags.extend(map(lambda x: x.get_nbt_tag(), [position, size, self._blockstate]))
        root.tags.extend([self._blockstatepalette, self._tileeneities, self._pendingblockticks, self._pendingfluidticks, self._entities])

        return root

    def _build(self):
        pass