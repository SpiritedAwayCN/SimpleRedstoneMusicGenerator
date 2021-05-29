author = 'Spirited_Away_'
description = 'This schematic is auto-generated.'
sche_name = 'redstone-music'

minecraft_dataversion = 2584
version = 5

datapack_name = 'RMGeneratorDatapack'
rebuild_datapack_if_exists = False

ticks_per_row = 3

def playsound_command_list() -> list:
    '''
        @return
        A List, List[str]
        len(list) should be 75, representing the keys from F1 to G7 in turn
        the elements in list indicates the sound name, depending on your resource pack
        
        For example, there's an element in list:
            function_list[30] = 'piano.c4'

        Technically speaking, 2 functions will be generated in datapack:
            * 'key39play' - include playsound(piano.c4) command
            * 'key39stop' - include stopsound(piano.c4) command

        The bias of 9 will be added to 30 since F1 is the 9th key on piano

        C4 is the 39th key, which index should be 30.
    '''

    function_list = []

    for piano_key in range(9, 84):
        function_list.append(f'piano.mp.{piano_key}')
    
    return function_list
