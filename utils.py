import json
import re

def quote_str(s):
	s = s.replace('\\', '\\\\')
	s = s.replace('"', '\\"')
	s = s.replace('\n', '\\n')
	s = s.replace('\t', '\\t')
	s = s.replace('\r', '\\r')
	s = '"' + s + '"'
	return s

def isTableStrIndex(s):
	regex = re.compile("^[a-zA-Z_]+$")
	m = regex.match(s)
	return not not m
