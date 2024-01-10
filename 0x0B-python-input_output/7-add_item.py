#!/usr/bin/python3
"""add arguments to python list"""
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
arguments = list(sys.argv[1:])
try:
    original_file = load_from_json_file('add_item.json')
except Exception:
    original_file = []
original_file.extend(arguments)
save_to_json_file(original_file, 'add_item.json')
