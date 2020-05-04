#!/usr/bin/env python3

import os
import sys

# alike dict()
def create_node(name, contents=[], type=''):
	empty_json_node = {
		'name': name,
		'type': type,
		'contents': contents
	}
	return empty_json_node

def paths_into_jtree(paths, json_tree):

	for path in paths:

		path_parts = path.split('/')

		if json_tree==[]:
			json_tree.append( create_node(path_parts[0], []) )

		p = next( (i for i in json_tree if i['name']==path_parts[0]), "no_node_with_that_name")

		if p=="no_node_with_that_name":
			json_tree.append( create_node(path_parts[0], []) )
			p = json_tree[-1]

		if len(path_parts) > 1:
			p['contents'].append( '/'.join(path_parts[1:]) )

	for i in json_tree:
		tmp_jtree = []
		paths_into_jtree(i['contents'], tmp_jtree)
		i['contents'] = tmp_jtree

def leveling_to_padding(leveling):
	continuation_tiem_prefix = lambda x: ('    ' if x else '│   ')
	return ''.join(map(continuation_tiem_prefix , leveling[1:]))

def pretty_print_jtree(json_tree, leveling = [], parent_is_last=False):

	for i, subtree in enumerate(json_tree):

		isLast = i==(len(json_tree)-1)
		new_tiem_prefix = '└' if isLast else '├'

		pre = ''
		level = len(leveling)
		if level!=0:
			pre = leveling_to_padding(leveling) + new_tiem_prefix+'── '

		print( pre + subtree['name'])
		pretty_print_jtree(subtree['contents'], leveling+[isLast], isLast)



data = sys.stdin.read()

#json_tree = create_node('.', 'directory', [])
json_tree = [] # list of dicts
paths_into_jtree(data.split(), json_tree)

print(json_tree)
pretty_print_jtree(json_tree)
