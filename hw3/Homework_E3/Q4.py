my_file = open("dna_sequence.fasta", "w")
my_file.write(">ABC123\n")
my_file.write("ATCGACGATCGATCGATCGCAGACGTATCG\n")
my_file.write(">DEF456\n")
my_file.write("ACTGATGACGATGATCGACACGACT\n")
my_file.write(">HIJ789\n")
my_file.write("ACTGACACTGTATGTACATGTG\n")
my_file.close()
