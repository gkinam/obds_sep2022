# Task 1: Occurences of motif in a promoter seq
prom_seq = 'TATAATGCTGACTTATAGCGCTATATATATATA'
motif_seq ='TATA'
# prom_seq.find('TATA')
# prom_seq.index('TATA')

counter = 0
len_prom = len(prom_seq)
for i in range(0, len_prom-3):
    if prom_seq[i:i+4] == motif_seq: 
        print(i+1, i+4)
        counter += 1
print (counter)

#Task2: GC content calculation
# DNA_seq = 'TATAATGCTGACTTATAGCGCTATATATATATA'
DNA_seq = '''GTGGCTTAAGAGGGGAGTCGTCACAGGCGTCAAGTCTTCTTTCTAAA
GCCGGGGACCTGGGGAGGAGGTGGGAGTTTACGGGAGGAAGGGCCACGGAGATGGGTCGC
TTCTCCTGGAGCTAGAGCTGCGGGCTGGGGTCTCCAGGGTTCGGCCCGGGGAGCCGACCC
TGGTCGGCCGTCGGGGCTCTGCTCGGCCCTCCTGAAACCTCCGCCTCCTCCAGCAGGGGG
CGGGCCGGGGCCGCGTCTCGGGGGGAAGGCGATCAGGTCGCCCCCTCCTCCGATTCCCCC
GCCTTCCAGGACAGCCTCCAGCCCAGAGGGGCGGTCCGGGGGCGGGGTCGCACCGCCCCC
TCTCGCTCCCAATCCCGGGGCGGCCGGGCGGGGGTGGGCAGGGGGCGTGAGGCCGCCCCT
GCGTCCCGGGGGCCCCCCGAAAACGCGCTCCGGGTGCCCGGTCCCTCCGCTGCGCCCTGC
CGCCGTCCTCCCGGGGGTCTCGGGCGGCCGCGGCCGTGTCCTTCGCGTCCCGGCGGCGCG
GCGGGAGGGGCCGGCGTGACGCAGCGGTTGCTACGGGCCGCCCTTATAAATAACCGGGCT
CAGGAGAAACTTTAGCGAGTCAGAGCCGCGCACGGGACTGGGAAGGGGACCCACCCGAGG
GTCCAGCCACCCCCCCTCACTAATAGCGGCCACCCCGGCAGCGGCGGCAGCAGCAGCAGC
GACGCAGCGGCGACAGCTCAGAGCAGGGAGGCCGCGCCACCTGCGGGCCGGCCGGAGCGG
GCAGCCCCAGGCCCCCTCCCCGGGCACCCGCGTTCATGCAACGCCTGGTGGCCTGGGACC
CAGCATGTCTCCCCCTGCCGCCGCCGCCGCCTGCCTTTAAATCCATGGAAGTGGCCAACT
TCTACTACGAGGCGGACTGCTTGGCTGCTGCGTACGGCGGCAAGGCGGCCCCCGCGGCGC
CCCCCGCGGCCAGACCCGGGCCGCGCCCCCCCGCCGGCGAGCTGGGCAGCATCGGCGACC
ACGAGCGCGCCATCGACTTCAGCCCGTACCTGGAGCCGCTGGGCGCGCCGCAGGCCCCGG
CGCCCGCCACGGCCACGGACACCTTCGAGGCGGCTCCGCCCGCGCCCGCCCCCGCGCCCG
CCTCCTCCGGGCAGCACCACGACTTCCTCTCCGACCTCTTCTCCGACGACTACGGGGGCA
AGAACTGCAAGAAGCCGGCCGAGTACGGCTACGTGAGCCTGGGGCGCCTGGGGGCCGCCA
AGGGCGCGCTGCACCCCGGCTGCTTCGCGCCCCTGCACCCACCGCCCCCGCCGCCGCCGC
CGCCCGCCGAGCTCAAGGCGGAGCCGGGCTTCGAGCCCGCGGACTGCAAGCGGAAGGAGG
AGGCCGGGGCGCCGGGCGGCGGCGCAGGCATGGCGGCGGGCTTCCCGTACGCGCTGCGCGCTTACCTCGGC
TACCAGGCGGTGCCGAGCGGCAGCAGCGGGAGCCTCTCCACGTCCTCCTCGTCCAGCCCG
CCCGGCACGCCGAGCCCCGCTGACGCCAAGGCGCCCCCGACCGCCTGCTACGCGGGGGCC
GCGCCGGCGCCCTCGCAGGTCAAGAGCAAGGCCAAGAAGACCGTGGACAAGCACAGCGAC
GAGTACAAGATCCGGCGCGAGCGCAACAACATCGCCGTGCGCAAGAGCCGCGACAAGGCC
AAGATGCGCAACCTGGAGACGCAGCACAAGGTCCTGGAGCTCACGGCCGAGAACGAGCGG
CTGCAGAAGAAGGTGGAGCAGCTGTCGCGCGAGCTCAGCACCCTGCGGAACTTGTTCAAG
CAGCTGCCCGAGCCCCTGCTCGCCTCCTCCGGCCACTGCTAGCGCGGCCCCCGCGCGCGT
CCCCCTGCCGGCCGGGGCTGAGACTCCGGGGAGCGCCCGCGCCCGCGCCCTCGCCCCCGC
CCCCGGCGGCGCCGGCAAAACTTTGGCACTGGGGCACTTGGCAGCGCGGGGAGCCCGTCG
GTAATTTTAATATTTTATTATATATATATATCTATATTTTTGTCCAAACCAACCGCACAT
GCAGATGGGGCTCCCGCCCGTGGTGTTATTTAAAGAAGAAACGTCTATGTGTACAGATGA
ATGATAAACTCTCTGCTTCTCCCTCTGCCCCTCTCCAGGCGCCGGCGGGCGGGCCGGTTT
CGAAGTTGATGCAATCGGTTTAAACATGGCTGAACGCGTGTGTACACGGGACTGACGCAA
CCCACGTGTAACTGTCAGCCGGGCCCTGAGTAATCGCTTAAAGATGTTCCTACGGGCTTG
TTGCTGTTGATGTTTTGTTTTGTTTTGTTTTTTGGTCTTTTTTTGTATTATAAAAAATAA
TCTATTTCTATGAGAAAAGAGGCGTCTGTATATTTTGGGAATCTTTTCCGTTTCAAGCAT
TAAGAACACTTTTAATAAACTTTTTTTTGAGAATGGTTACAAAGCCTTTTGGGGGCAGTA
ATTGGCTTTTGTTTTTTATTTTTTTACTTTATTTTGGATTTGTAGGATTTTGTTTTTGCG
TTTCTGGTGTGTAGGGGGTTGTGTGTGGGGGGCTGCTGTTATTTTTGGAGGTTTTGGTGG
TTGGGTGGGGGTGTTGCAGCTGGTTTTTCTGCCTCCTCTGCTACTCCCCCTCCCACACAC
ACAGGGTCTGCTTGAGATGGGGTTCCAGCCCCGGGGGAAAGGGGAGAAGAGTAATGGGTC
AGGCATTCAGGCTGACTCAGAGCCCCTAGGCGCCGGGACGGGTGGCTGGGAACCCTGCTT
GAGAAGAGATTCCGGAGCCTCTGGCTGGTCCCGAGTGTCAGGCTTGGGTTTGGAAGGGCT
GGGAGGTCTGTGACCCCTGCCCTGTGTTTGGGGACTAGGTAGGCAGGCCTGTGACTGTAG
GAGGAGGGGGTTCAGGTCTTGGTCCTGCTGAGCCCGAGTCAGGGCAGATGCTTTTGGTCA
GTGTAGTGGGGTGGGTTGTTTAAAACACAGTTTGTGTATACATGTGTATTTTAAAGAGGG
GAGCCTGGGTGTGTGGGCGAGTCTGTGTTTGTGTGTCCC'''
a = 0
g = 0
t = 0
c = 0
length = len(DNA_seq)
for i in range(0, length):
    if DNA_seq[i] == "A":
        a += 1
    elif DNA_seq[i] == "T":
        t += 1
    elif DNA_seq[i] == "G":
        g += 1
    elif DNA_seq[i] == "C":
        c += 1
    else: 
        continue

GC_content = ((g+c)/(g+c+a+t))*100
print(f'GC content of the sequence is {GC_content} %')

#Task 3 - Hamming distance
seq_1 = 'TATAATGCTGACTTATAGCGCTATATATATATA'
seq_2 = 'TGGGTGTGTGGGCGAGTCTGTGTTTGTGTGTCC'
length = len(seq_1)
dist = 0
matches = 0
for i in range (0, length):
    if seq_1[i] != seq_2[i]:
        dist += 1
    else:
        matches += 1
print(f' No. of matches = {matches} and no. of mismatches = {dist} in sequences of length {length}')


#Task 4 - Consensus motif
motif_list = ['ATCCAGCT', 'GGGCAACT', 'ATGGATCT', 'AAGCAACC', 'TTGGAACT', 'ATGCCATT', 'ATGGCACT']
length_list = len(motif_list)
length_motif = len(motif_list[1])

dict = {'A':[0]*8, 'C':[0]*8, 'G':[0]*8 , 'T':[0]*8}
for motif in range (0, length_list):
    for base in range (0, length_motif):
        if motif_list[motif][base] == 'A':
            dict.get('A')[base] +=1
        elif motif_list[motif][base] == 'C':
            dict.get('C')[base] +=1
        elif motif_list[motif][base] == 'G':
            dict.get('G')[base] +=1
        elif motif_list[motif][base] == 'T':
            dict.get('T')[base] +=1
        else:
            continue
print(dict)


for consensus in range (0, length_motif):
    for name in dict.keys():
        if dict.get(name)[consensus] >= 4:
            print (name)



            
    
