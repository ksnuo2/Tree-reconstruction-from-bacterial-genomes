import sys, os, string

Con_seq={'NZ_CP016770':'', 'NZ_CP016782':'', 'NZ_CP016773':'', 'NZ_CP016783':'','NZ_CP016778':''} # define a dictionary for the five concatenated sequences.
fp = open ('MSA_single.list', 'r') # read the file names ending with single.faa
for line in fp:
    fpx = open (line[:-1], 'r') # read a sequence file
    temp_taxon = ''
    for linex in fpx:
        if '>' in linex:
            line_temp = linex.split('.')
            temp_taxon=line_temp[0][1:] # sample a taxon name from a sequence eader.
        else:
            line_temp1 = linex.split() # to remove a new line character at the end of the sequence.
            Con_seq[temp_taxon]+=line_temp1[0] # append a sequence to a corresponding taxon. 
    fpx.close
fp.close

fpy = open ('Concatenated.faa', 'w') # write a file for saving the concatenated sequences.
fpy.write ('>NZ_CP016770\n'+Con_seq['NZ_CP016770']+'\n'+'>NZ_CP016782\n'+Con_seq['NZ_CP016782']+'\n'+'>NZ_CP016773\n'+Con_seq['NZ_CP016773']+'\n'+'>NZ_CP016783\n'+Con_seq['NZ_CP016783']+'\n'+'>NZ_CP016778\n'+Con_seq['NZ_CP016778']) # write  the five concatenated sequences in a fasta format. 
fpy.close

print (len(Con_seq['NZ_CP016770']), len(Con_seq['NZ_CP016782']), len(Con_seq['NZ_CP016773']), len(Con_seq['NZ_CP016783']), len(Con_seq['NZ_CP016778'])) # check if the concatenated sequences are all the same in length. 

