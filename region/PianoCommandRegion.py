from nbt.nbt import *

from container.NBTTagBuilders import *
from region.Region import Region
from utils.build_datapack import build_new
import config as c


class PianoCommandRegion(Region):
    def __init__(self, px, py, pz) -> None:
        super().__init__(5, 1, 76, pending_block_tick=True, blockstatebit=3, px=px, py=py, pz=pz, name='command-piano')
        self._delay_cache = [[0] * 75 for i in range(3)]
    
    def _generate_blockstate_palette(self):
        self._blockstatepalette.append(BlockStateBuilder('minecraft:air').get_nbt_tag()) #0
        self._blockstatepalette.append(BlockStateBuilder('minecraft:redstone_block').get_nbt_tag()) #1
        self._blockstatepalette.append(BlockStateBuilder('minecraft:iron_block').get_nbt_tag()) #2

        rcb = BlockStateBuilder('minecraft:repeating_command_block') #3
        rcb.add_property(TAG_String(name='facing', value='east'))
        rcb.add_property(TAG_String(name='conditional', value='false') )
        self._blockstatepalette.append(rcb.get_nbt_tag())

        ccb = BlockStateBuilder('minecraft:chain_command_block') #4
        ccb.add_property(TAG_String(name='facing', value='east'))
        ccb.add_property(TAG_String(name='conditional', value='false') )
        self._blockstatepalette.append(ccb.get_nbt_tag())

        # cb = BlockStateBuilder('minecraft:command_block') #5
        # cb.add_property(TAG_String(name='facing', value='east'))
        # cb.add_property(TAG_String(name='contional', value='false') )
        # self._blockstatepalette.append(cb.get_nbt_tag())

    def _generate_command_blocks(self):
        build_new(c.datapack_name)
        for z in range(75):
            key = f'key{83 - z}'

            self._blockstate.insert(self._get_array_index(0, 0, z), 1) # redstone block
            self._blockstate.insert(self._get_array_index(1, 0, z), 3) # repeat
            self._blockstate.insert(self._get_array_index(2, 0, z), 4) # chain
            if self._delay_cache[1][z] == 0:
                self._blockstate.insert(self._get_array_index(3, 0, z), 2) # iron
            if self._delay_cache[2][z] == 0:
                self._blockstate.insert(self._get_array_index(4, 0, z), 2) # iron

            command = f'execute if block ~ ~1 ~ minecraft:gold_block run function rmgen:{key}play_d0'
            rcb_tile = CommandBlockBuilder().build(1, 0, z, command, auto=0, powered=1)
            self._tileeneities.tags.append(rcb_tile.get_nbt_tag())

            pending_rcb = PendingTicksBuilder().build(1, 0, z, 'minecraft:repeating_command_block')
            self._pendingblockticks.tags.append(pending_rcb.get_nbt_tag())

            command = f'execute if block ~-1 ~1 ~ minecraft:obsidian run function rmgen:{key}stop'
            ccb_tile = CommandBlockBuilder().build(2, 0, z, command)
            self._tileeneities.tags.append(ccb_tile.get_nbt_tag())
        

        self._blockstate.insert(self._get_array_index(0, 0, 75), 1) # redstone block
        self._blockstate.insert(self._get_array_index(1, 0, 75), 3) # repeat

        command = 'execute if block ~ ~1 ~ minecraft:gold_block run execute as @e[tag=jd] at @s run tp ~-3 4 ~'
        rcb_tile = CommandBlockBuilder().build(1, 0, 75, command, auto=0, powered=1)
        self._tileeneities.tags.append(rcb_tile.get_nbt_tag())

        pending_rcb = PendingTicksBuilder().build(1, 0, 75, 'minecraft:repeating_command_block')
        self._pendingblockticks.tags.append(pending_rcb.get_nbt_tag())
    
    def _build(self):
        self._generate_blockstate_palette()
        self._generate_command_blocks()
    
    def add_new_command_block(self, z, delay):
        if delay == 0:
            return False
        
        assert delay in (1, 2)
        if self._delay_cache[delay][z] == 1:
            return False

        self.add_new_command_block(z, delay - 1)
            
        key = f'key{83 - z}'
        block =  'emerald_block' if delay == 1 else 'diamond_block'
        command = f'execute if block ~-{delay+1} ~1 ~ minecraft:{block} run function rmgen:{key}play_d{delay}'
        self._blockstate.insert(self._get_array_index(2 + delay, 0, z), 4) # chain
        # print(2 + delay, 0, z)
        ccb_tile = CommandBlockBuilder().build(2 + delay, 0, z, command)
        self._tileeneities.tags.append(ccb_tile.get_nbt_tag())

        self._delay_cache[delay][z] = 1
        return True
