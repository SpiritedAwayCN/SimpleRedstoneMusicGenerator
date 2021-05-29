import config as c

STOP_WIDGET = 11
PLAY_WIDGET = 12

def keys_generator(file_name=c.input_file_name):

    with open(file_name) as f:
        line = f.readline()
        cache_list = [-1] * len(line.split(','))

        while line:
            res_dict = {}
            tokens = line.strip().split(',')
            for col, string in enumerate(tokens):
                if not string:
                    continue

                if string == 'x':
                    if cache_list[col] != -1:
                        res_dict[cache_list[col]] = STOP_WIDGET
                        cache_list[col] = -1
                    continue
                
                key_id = c.str2keyid(string)
                if cache_list[col] != -1:
                    res_dict[cache_list[col]] = STOP_WIDGET
                res_dict[key_id] = PLAY_WIDGET
                cache_list[col] = key_id
            
            yield res_dict

            line = f.readline()