#!/usr/bin/env python3

# Read: https://en.wikipedia.org/wiki/DNA_and_RNA_codon_tables

# RNA codons table
def parse_codons() -> None:
  codons = """Ala A GCU, GCC, GCA, GCG  
  Leu L UUA, UUG, CUU, CUC, CUA, CUG
  Arg R CGU, CGC, CGA, CGG, AGA, AGG  
  Lys K AAA, AAG
  Asn N AAU, AAC  
  Met M AUG
  Asp D GAU, GAC  
  Phe F UUU, UUC
  Cys C UGU, UGC  
  Pro P CCU, CCC, CCA, CCG
  Gln Q CAA, CAG  
  Ser S UCU, UCC, UCA, UCG, AGU, AGC
  Glu E GAA, GAG  
  Thr T ACU, ACC, ACA, ACG
  Gly G GGU, GGC, GGA, GGG  
  Trp W UGG
  His H CAU, CAC  
  Tyr Y UAU, UAC
  Ile I AUU, AUC, AUA 
  Val V GUU, GUC, GUA, GUG
  - Stop UAG, UGA, UAA
  - Start AUG
  """.strip()

  d = {}
  for c in codons.split('\n'):
    c = c.strip().split(' ')
    k = c[1]
    if len(c) == 3:
      v = [c[-1].lower()]
    else:
      v = c[2:len(c)]
      for acid in range(len(v)):
        v[acid] = v[acid].replace(',','').lower()
    for vv in v:
      d[vv] = k

  return d

codons = parse_codons()

def rna_to_codons(rna_string: str) -> str:
  return [rna_string[i:i+3] for i in range(0, len(rna_string), 3)]

def translation(rna_string: str) -> list[str]:
  """Translate raw RNA string to amino acids."""
  aa = []
  for codon in rna_to_codons(rna_string):
    aa.append(codons[codon])
  return aa

def demutate(rna_string: str) -> str:
  rna = list(rna_string.lower())
  return ''.join(_ for _ in rna[::2])

def rna_to_dna(rna_string: str) -> str:
  return rna_string.replace('u', 't')

def dna_to_rna(dna_string: str) -> str:
  return dna_string.replace('t', 'u')

if __name__ == "__main__":
  mutated_c = 'aagguuccaaccgguuccaauu'
  c = 'agucaccgucau'
  print(rna_to_codons(c))
  print(translation(c))
  print(demutate(mutated_c))
  print(demutate('cccc'))