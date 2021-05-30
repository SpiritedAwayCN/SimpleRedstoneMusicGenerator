import config as c

STOP_WIDGET = 11
PLAY_WIDGET = 12, 10, 13

def keys_generator(piano_command_region, file_name=c.input_file_name):

    with open(file_name) as f:
        line = f.readline()
        cache_list = [-1] * len(line.split(','))

        while line:
            res_dict = {}
            tokens = line.strip().split(',')
            for col, s in enumerate(tokens):
                if not s:
                    continue
                strings = s.split(':')
                string = strings[0]
                delay = int(strings[1]) if len(strings) > 1 else 0

                if string == 'x':
                    if cache_list[col] != -1 and not cache_list[col] in res_dict.keys():
                        res_dict[cache_list[col]] = STOP_WIDGET
                        cache_list[col] = -1
                    continue
                
                key_id = c.str2keyid(string)

                piano_command_region.add_new_command_block(74 - key_id, delay)

                if cache_list[col] != -1 and not cache_list[col] in res_dict.keys():
                    res_dict[cache_list[col]] = STOP_WIDGET
                res_dict[key_id] = PLAY_WIDGET[delay]
                cache_list[col] = key_id
            
            yield res_dict

            line = f.readline()