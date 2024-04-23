import sys, os, string

fp = open ('Concatenated.faa-gb', 'r') # open the alignment in Gblocks format.
fpx = open ('Concatenated_gblocks.fasta', 'w') # open the output file. 
temp_seq = ''
for line in fp:
    if '>' in line:
        if temp_seq!='':
            fpx.write (temp_seq+'\n')
            temp_seq = ''
        fpx.write (line) # write  a sequence header. 
    else:
        line_temp = line.split() # make a list for sequences delimited by space. 
        temp_seq += ''.join(line_temp) # combine space-delimited sequences and append them into the preexisting sequence. 
fpx.write (temp_seq)
fpx.close

