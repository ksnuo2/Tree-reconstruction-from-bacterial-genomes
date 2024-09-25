import sys, os, string

no_genomes = int(sys.argv[1])
genome_names = []
for x in range (2, no_genomes+2):
    genome_names.append(sys.argv[x])

seq_id = {}
for name in genome_names:
    seq_id[name]=[]
    fp = open (name, 'r')
    for line in fp:
        if '>' in line:
            line_temp = line.split()
            seq_id[name].append(line_temp[0][1:])
    fp.close

fp =open ('myproject.proteinortho.tsv', 'r')
fpx = open ('universal.orthologs', 'w')
count = 0
for line in fp:
    count+=1
    if count==1:
        fpx.write (line)
    else:
        line_temp = line.split()
        if int(line_temp[1])==no_genomes:
            orthologs = []
            line_temp1 = line_temp[3].split(',')
            print (line_temp1)
            for value in line_temp1:
                orthologs.append(value)
            hit_no = 0
            for value in orthologs:
                for name in seq_id:
                    if value in seq_id[name]:
                        hit_no+=1
            if hit_no==no_genomes:
                fpx.write (line)
fp.close
fpx.close

