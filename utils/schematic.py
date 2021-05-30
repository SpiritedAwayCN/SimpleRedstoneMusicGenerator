from region.RomRegion import RomRegion
from utils.parser import keys_generator
from region.PianoCommandRegion import PianoCommandRegion
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

    regions.tags.extend(_read_from_template())

    piano_command_region = PianoCommandRegion(42, 0, -89)

    parser_gen = keys_generator(piano_command_region)
    xx = -18
    romregions = [RomRegion(xx, 0, -90, name=f'ROM{xx}')]

    for row, params in enumerate(parser_gen):
        row_mod = row % 248
        if  row_mod == 247:
            params[-1] = 12
            romregions[-1].build_row(row_mod, params)
            xx -= 3
            romregions.append(RomRegion(xx, 0, -90, name=f'ROM{xx}'))
        else:
            romregions[-1].build_row(row_mod, params)

    regions.tags.extend(map(lambda x:x.build_nbt_full(), romregions))
    
    regions.tags.append(piano_command_region.build_nbt_full())


    nbtfile.tags.append(regions)
    nbtfile.tags.append(nbt.TAG_Int(c.minecraft_dataversion, 'MinecraftDataVersion'))
    nbtfile.tags.append(nbt.TAG_Int(c.version, 'Version'))

    nbtfile.tags.append(MetadataBuilder().build(0, 0, 0, region_count=3 + len(romregions)).get_nbt_tag())
    
    return nbtfile

if __name__=='__main__':
    print(build_schematic().pretty_tree())