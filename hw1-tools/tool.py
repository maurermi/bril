#!/usr/bin/env python3

import json
import sys

def read_json_file(input):
    try:
        data = json.load(input)
        return data
    except json.JSONDecodeError:
        print(f"Error: The input does not contain valid JSON.")
        sys.exit(1)
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        sys.exit(1)

def count_instr_types(data: dict):
    db = {'constant': 0, 'value': 0, 'effect': 0}
    for func in data['functions']:
        for instr in func['instrs']:
            if 'op' in instr and instr['op'] == 'const':
                db['constant'] += 1
            elif 'dest' in instr:
                db['value'] += 1
            elif 'label' in instr:
                continue
            else:
                db['effect'] += 1
    return db


def main():
    data = read_json_file(sys.stdin)

    print(count_instr_types(data))

if __name__ == "__main__":
    main()
