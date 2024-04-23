import sys, os, string

fp = open ('MSA.list', 'r') # get a file list for multiple sequence alignments.
for line in fp:
        line_temp = line.split('.fasta')
        fpr = open (line_temp[0]+'.fasta', 'r') # open an alignment file with multiple-line sequences.
        fpx = open (line_temp[0]+'_single.faa', 'w') # write an alignment file with single-line sequences.
        temp_seq = ''  # temporary variable for storing molecular sequences only. 
        for liner in fpr:
            if '>' in liner:
                if temp_seq!='':
                    fpx.write (temp_seq[:-1]+'\n') # write a single-line sequence into a file, where :-1 for deleting symbol * at the end of sequence. 
                    temp_seq='' # initializing 
                fpx.write (liner) # write a sequence header. 
            else:
                temp_seq+=liner[:-1] # converting multiple-line seqs into a single-line seqs. 
        fpx.write(temp_seq[:-1]) # remove a symbol * at the end of the sequence and write the line to the file. 
        fpr.close
        fpx.close
fpx.close
