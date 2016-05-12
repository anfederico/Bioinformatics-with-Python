
'''
Text file containing codon/protein pairs (per line)
For example...
TTT F      CTT L      ATT I      GTT V
TTC F      CTC L      ATC I      GTC V
TTA L      CTA L      ATA I      GTA V
TTG L      CTG L      ATG M      GTG V
TCT S      CCT P      ACT T      GCT A
TCC S      CCC P      ACC T      GCC A
TCA S      CCA P      ACA T      GCA A
TCG S      CCG P      ACG T      GCG A
TAT Y      CAT H      AAT N      GAT D
TAC Y      CAC H      AAC N      GAC D
TAA Stop   CAA Q      AAA K      GAA E
TAG Stop   CAG Q      AAG K      GAG E
TGT C      CGT R      AGT S      GGT G
TGC C      CGC R      AGC S      GGC G
TGA Stop   CGA R      AGA R      GGA G
TGG W      CGG R      AGG R      GGG G

Text file containing pre-RNA and splice sites
>Pre-RNA_1
ATGGTCTACATAGCTGACAAACAGCACGTAGCAATCGGTCGAATCTCGAGAGGCATATGGTCACATGATCGGTCGAGCGTGTTTCAAAGTTTGCGCCTAG
>Splice_1
ATCGGTCGAA
>Splice_2
ATCGGTCGAGCGTGT

'''

pre_mRNA = open("pre_mRNA.txt", "r")
sites = open("sites.txt", "w")

x = 0
y = 0

for line in pre_mRNA:
    if y != 2:
        if line[0] == ">":
            y += 1
    if y == 2:
        sites.write(line)
        
sites.close()





