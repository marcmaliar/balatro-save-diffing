import zlib
import ast
import json
from slpp import slpp as lua


def decompress(data):
    return zlib.decompress(data, wbits=-15)


def compress(data):
    return zlib.compress(data, wbits=-15)


def raw_to_json(data):
    data = data.decode('utf-8')[7:]
    # Replace Lua table syntax with Python dict syntax
    # data = data.replace('={', '={')  # Add space before '{'
    # data = data.replace('=\[', '=[')  # Replace '\[' with '['
    # data = data.replace('\]=', ']=')  # Add space after ']'

    # Parse the modified string as a Python literal
    # parsed_data = ast.literal_eval(data)

    # Convert the parsed data to JSON
    json_data = lua.decode(data)  # json.dumps(parsed_data, indent=2)
    return json_data


def fix_json_arrays(json_data):
    if not isinstance(json_data, dict):
        return json_data

    keys = list(json_data.keys())
    if not all(key.startswith('NOSTRING_') for key in keys):
        for key in keys:
            json_data[key] = fix_json_arrays(json_data[key])
        return json_data

    array = []
    for key in keys:
        index = int(key[10:]) - 1  # -1 because Lua is 1-indexed
        array.insert(index, fix_json_arrays(json_data[key]))
    return array


def fix_lua_arrays(json_data):
    if isinstance(json_data, list):
        lua_array = {}
        for i, item in enumerate(json_data):
            lua_array[f'NOSTRING_{i + 1}'] = fix_lua_arrays(item)
        return lua_array
    elif isinstance(json_data, dict):
        for key, value in json_data.items():
            json_data[key] = fix_lua_arrays(value)
    return json_data


def json_to_raw(data):
    return f'return {str(data)}'.replace('"NOSTRING_(\d+)":', r'[\1]=').replace(r'"(.*?)":', r'["\1"]=')


def process_file(buffer):
    data = decompress(buffer)
    json_data = raw_to_json(data)
    return json_data


def process_json(json_data):
    json_data = fix_lua_arrays(json_data)
    data = json_to_raw(json_data)
    return compress(data.encode('utf-8'))
