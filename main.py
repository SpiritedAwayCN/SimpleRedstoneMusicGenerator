from utils.schematic import build_schematic
import config as c

nbtfile = build_schematic()
# print(nbtfile.pretty_tree())
nbtfile.write_file(f'./{c.sche_name}.litematic')
print('Schematic was successfully generated!')