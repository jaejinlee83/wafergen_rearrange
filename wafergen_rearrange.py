#!/usr/bin/python

"""
This script do...
usage: pythone ...py input > output
"""

import sys

def main():
	dict={}
	sample_name={}
	file_open = open(sys.argv[1],'r')
	for n,line in enumerate(file_open):
		if n==0:
			continue
		spl=line.strip().split('\t')
		sample_name[spl[3]]=0
		if dict.has_key(spl[2]):
			temp_dict=dict[spl[2]]
			temp_dict[spl[3]]=spl[5]
			
		else:
			dict[spl[2]]={spl[3]:spl[5]}
	file_open.close()

	sorted_sample=['']
	for sample in sample_name.items():
		sorted_sample.append(sample[0])
	sorted_sample.sort()
	print '\t'.join(sorted_sample)
	for ARG_array in dict.items():
		result=[ARG_array[0]]
		for sample in sorted_sample[1:]:
			result.append(ARG_array[1][sample])
		print '\t'.join(result)

if __name__ == '__main__':
    main()

