from os import name
from nbt.nbt import *
from nbt import nbt
import time

current_time = int(time.time() * 1000)

nbtfile = NBTFile()
nbtfile.tags.append(TAG_Int(name="MinecraftDataVersion", value=2230))
nbtfile.tags.append(TAG_Int(name="Version", value=5))
metadata = TAG_Compound()
metadata.name = 'Metadata'
metadata.tags.append(TAG_Long(name='TimeCreated', value=current_time))
metadata.tags.append(TAG_Long(name='TimeModified', value=current_time))

enclosing_size = TAG_Compound()
enclosing_size.name = 'EnclosingSize'
enclosing_size.tags.extend([TAG_Int(name='x', value=2), TAG_Int(name='y', value=2), TAG_Int(name='z', value=2)])
metadata.tags.append(enclosing_size)

metadata.tags.append(TAG_String(name='Description', value=''))
metadata.tags.append(TAG_Int(name='RegionCount', value=1))
metadata.tags.append(TAG_Int(name='TotalBlocks', value=4))
metadata.tags.append(TAG_String(name='Author', value='Spirited_Away_'))
metadata.tags.append(TAG_Int(name='TotalVolume', value=8))
metadata.tags.append(TAG_String(name='Name', value='RedstoneMusic'))

nbtfile.tags.append(metadata)

regions = TAG_Compound()
regions.name = 'Regions'

region_first = TAG_Compound()
region_first.name = 'RedstoneMusic'

region_first.tags.append(TAG_List(name='PendingBlockTicks', type=nbt._TAG_End))

block_states = TAG_Long_Array(name='BlockStates')
block_states.value = [0b0100010110]
region_first.tags.append(block_states)

position = TAG_Compound()
position.name = 'Position'
position.tags.extend([TAG_Int(name='x', value=0), TAG_Int(name='y', value=0), TAG_Int(name='z', value=0)])
region_first.tags.append(position)

blockState_palette = TAG_List(name='BlockStatePalette', type=TAG_Compound)

air_block = TAG_Compound()
air_block.tags.append(TAG_String(name='Name', value='minecraft:air'))

iron_block = TAG_Compound()
iron_block.tags.append(TAG_String(name='Name', value='minecraft:iron_block'))

gold_block = TAG_Compound()
gold_block.tags.append(TAG_String(name='Name', value='minecraft:gold_block'))

blockState_palette.extend([air_block, iron_block, gold_block])
region_first.tags.append(blockState_palette)

region_size = TAG_Compound()
region_size.name = 'Size'
region_size.tags.extend([TAG_Int(name='x', value=2), TAG_Int(name='y', value=2), TAG_Int(name='z', value=2)])
region_first.tags.append(region_size)

region_first.tags.append(TAG_List(name='PendingFluidTicks', type=nbt._TAG_End))
region_first.tags.append(TAG_List(name='TileEntities', type=nbt._TAG_End))
region_first.tags.append(TAG_List(name='Entities', type=nbt._TAG_End))

regions.tags.append(region_first)
nbtfile.tags.append(regions)
print(nbtfile.pretty_tree())

nbtfile.write_file('test.litematic')