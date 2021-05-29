from container.TagBuilder import TagBuilder
from nbt.nbt import *
import time
import config as c

class BlockStateBuilder(TagBuilder):
    def __init__(self, name) -> None:
        super().__init__('Properties')
        self._root.tags.append(TAG_String(name='Name', value=name))

class CommandBlockBuilder(TagBuilder):
    def __init__(self) -> None:
        super().__init__()
    
    def build(self, x, y, z, command, auto=1, powered=0, conditonMet=1):
        self.add_common_property(TAG_Int(x, 'x')).add_common_property(TAG_Int(y, 'y')).add_common_property(TAG_Int(z, 'z'))
        self.add_common_property(TAG_Byte(auto, 'auto')).add_common_property(TAG_Byte(conditonMet, 'conditionMet'))
        self.add_common_property(TAG_Byte(powered, 'powered')).add_common_property(TAG_Byte(1, 'TrackOutput'))

        self.add_common_property(TAG_Byte(1, 'UpdateLastExecution')).add_common_property(TAG_Int(0, 'SuccessCount'))
        self.add_common_property(TAG_String('{"text":"@"}', 'CustomName'))

        self.add_common_property(TAG_String('minecraft:command_block', 'id'))
        self.add_common_property(TAG_String(command, 'Command'))

        return self

class PendingTicksBuilder(TagBuilder):
    def __init__(self) -> None:
        super().__init__()
    
    def build(self, x, y, z, block, priority=0, time=1):
        self.add_common_property(TAG_Int(x, 'x')).add_common_property(TAG_Int(y, 'y')).add_common_property(TAG_Int(z, 'z'))
        self.add_common_property(TAG_String(block, 'Block'))
        self.add_common_property(TAG_Int(priority, 'Priority'))
        self.add_common_property(TAG_Int(time, 'Time'))

        return self

class MetadataBuilder(TagBuilder):
    def __init__(self) -> None:
        super().__init__('EnclosingSize', 'Metadata')

    def build(self, ex, ey, ez, total_blocks, total_volume, region_count=1):
        self.add_property(TAG_Int(ex, 'x')).add_property(TAG_Int(ey, 'y')).add_property(TAG_Int(ez, 'z'))

        self.add_common_property(TAG_Int(total_blocks, 'TotalBlocks'))
        self.add_common_property(TAG_Int(total_volume, 'TotalVolume'))
        self.add_common_property(TAG_Int(region_count, 'RegionCount'))

        current_time = int(time.time() * 1000)
        self.add_common_property(TAG_Long(current_time, 'TimeCreated'))
        self.add_common_property(TAG_Long(current_time, 'TimeModified'))

        self.add_common_property(TAG_String(c.author, 'Author'))
        self.add_common_property(TAG_String(c.description, 'Description'))
        self.add_common_property(TAG_String(c.sche_name, 'Name'))

        return self

