from region.PianoCommandRegion import PainoCommandRegion
from container.NBTTagBuilders import MetadataBuilder
from nbt import nbt

import config as c

def _read_from_template():
    nbtfile = nbt.NBTFile('template.nbt', 'rb')
    nbtfile['control']['TileEntities'][31]['Command'].value = 'scoreboard players set @e[scores={jdt=%d..}] jdt 0'%(c.ticks_per_row)

    return nbtfile['control'], nbtfile['piano']

def build_schematic():
    nbtfile = nbt.NBTFile()

    nbtfile.tags.append(MetadataBuilder().build(76, 1, 5, 377, 380).get_nbt_tag())
    
    regions = nbt.TAG_Compound()
    regions.name = 'Regions'

    regions.tags.append(PainoCommandRegion(0, 0, 0).build_nbt_full())

    control_region, piano_region = _read_from_template()

    nbtfile.tags.append(regions)
    nbtfile.tags.append(nbt.TAG_Int(c.minecraft_dataversion, 'MinecraftDataVersion'))
    nbtfile.tags.append(nbt.TAG_Int(c.version, 'Version'))

    return nbtfile

if __name__=='__main__':
    print(build_schematic().pretty_tree())