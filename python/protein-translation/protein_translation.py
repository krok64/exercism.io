import re


codons = {'AUG': "Methionine", 'UUU': 'Phenylalanine', 'UUC': 'Phenylalanine', 'UUA': 'Leucine', 
    'UUG': 'Leucine', 'UCU': 'Serine', 'UCC': 'Serine', 'UCA': 'Serine', 'UCG': 'Serine',
    'UAU': 'Tyrosine', 'UAC': 'Tyrosine', 'UGU': 'Cysteine', 'UGC': 'Cysteine', 'UGG': 'Tryptophan',
    'UAA': 'STOP', 'UAG': 'STOP', 'UGA': 'STOP'}

def of_codon(cod):
    try:
        return codons[cod]
    except KeyError:
        raise ValueError

def of_rna(rna):
    result = []
    for i in re.findall("\w{3}", rna):
        codon = of_codon(i)
        if codon == 'STOP':
            break
        result.append(of_codon(i))
    return result
