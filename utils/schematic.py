from region.RomRegion import RomRegion
from utils.parser import keys_generator
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
    
    regions = nbt.TAG_Compound()
    regions.name = 'Regions'

    regions.tags.append(PainoCommandRegion(42, 0, -89).build_nbt_full())

    regions.tags.extend(_read_from_template())

    parser_gen = keys_generator()
    xx = -18
    romregions = [RomRegion(xx, 0, -90, name=f'ROM{xx}')]

    for row, params in enumerate(parser_gen):
        if row % 248 == 247:
            params[-1] = 12
            romregions[-1].build_row(row, params)
            xx -= 3
            romregions.append(RomRegion(xx, 0, -90, name=f'ROM{xx}'))
        else:
            romregions[-1].build_row(row, params)

    regions.tags.extend(map(lambda x:x.build_nbt_full(), romregions))


    nbtfile.tags.append(regions)
    nbtfile.tags.append(nbt.TAG_Int(c.minecraft_dataversion, 'MinecraftDataVersion'))
    nbtfile.tags.append(nbt.TAG_Int(c.version, 'Version'))

    nbtfile.tags.append(MetadataBuilder().build(0, 0, 0, region_count=3 + len(romregions)).get_nbt_tag())
    
    return nbtfile

if __name__=='__main__':
    print(build_schematic().pretty_tree())