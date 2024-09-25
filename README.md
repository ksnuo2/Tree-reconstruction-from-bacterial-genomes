These python codes are components of a bioinformatics pipeline for reconstructing bacterial phylogenomic trees that will be published in Methods in Molecular Biology as a chapter. 

1. The code extract_universal_orthologs.py identifies universal orthologs from the Proteinortho output (myproject.proteinortho.tsv). The code should run in the same folder of the file myproject.proteinortho.tsv as follows: $python extract_universal_orthologs.py [# of genomes] FAA1 FAA2 ... FAAn (note that FAAi is the proteome file for each genome.)

2. The code make_single_line_fasta.py converts multiline fasta files (aligned_\*.fasta) into singleline fasta files (alinged_\*_single.faa). 

3. The code gene_concatenate.py concatenates individual multiple sequence alignments (alinged_\*_single.faa) into a single MSA (Concatenated.faa). 
4. The code convert_gb_to_fasta.py produces a singleline fasta file (Concatenated_gblocks.fasta) from a multiline fasta file (Concatenated.faa-gb) that was produced by Gblocks. 
