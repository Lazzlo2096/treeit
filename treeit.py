#!/usr/bin/env python3

import os
import sys

data = sys.stdin.read()

# alike dict()
def create_node(name, contents=[], type=''):
	empty_json_node = {
		'name': name,
		'type': type,
		'contents': contents
	}
	return empty_json_node

def paths_in_jtree(json_tree, paths):

	for path in paths:

		path_parts = path.split('/')

		if json_tree==[]:
			json_tree.append( create_node(path_parts[0], []) )

		p = next( (i for i in json_tree if i['name']==path_parts[0]), "None3")

		if p=="None3":
			json_tree.append( create_node(path_parts[0], []) )
			p = json_tree[-1]

		if len(path_parts) > 1:
			p['contents'].append( '/'.join(path_parts[1:]) )

	for i in json_tree:
		lal = []
		paths_in_jtree(lal, i['contents'])
		i['contents'] = lal

def pretty_print_jtree(json_tree, level = 0):

	for i, subtree in enumerate(json_tree):

		sbml = '└' if i==(len(json_tree)-1) else '├'

		pre = ''
		if level!=0:
			pre = '│   '*(level-1) + sbml+'── '
		print( pre + subtree['name'])
		pretty_print_jtree(subtree['contents'], level+1)



json_tree = [] # list of dicts

paths_in_jtree(json_tree, data.split())

pretty_print_jtree(json_tree)