Three three python codes are components of a bioinformatics pipeline for reconstructing bacterial phylogenomic trees. 
The code make_single_line_fasta.py converts multiline fasta files (aligned_\*.fasta) into singleline fasta files (alinged_*_single.faa). 
The code gene_concatenate.py concatenates individual multiple sequence alignments (alinged_*single.faa) into a single MSA (Concatenated.faa). 
The code convert_gb_to_fasta.py produces a singleline fasta file (Concatenated_gblocks.fasta) from a multiline fasta file (Concatenated.faa-gb) that was produced by Gblocks. 
