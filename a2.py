
Learn-To-Program
================


Assignments completed for course LTP provided by University of Toronto on coursera.org

def get_length(dna):
    ''' (str) -> int

    Return the length of the DNA sequence dna.

    >>> get_length('ATCGAT')
    6
    >>> get_length('ATCG')
    4
    '''
    return len(dna)



def is_longer(dna1, dna2):
    ''' (str, str) -> bool

    Return True if and only if DNA sequence dna1 is longer than DNA sequence
    dna2.

    >>> is_longer('ATCG', 'AT')
    True
    >>> is_longer('ATCG', 'ATCGGA')
    False
    '''
    if len(dna1)>len(dna2):
        return True
    else:
        return False



def count_nucleotides(dna, nucleotide):
    ''' (str, str) -> int

    Return the number of occurrences of nucleotide in the DNA sequence dna.

    >>> count_nucleotides('ATCGGC', 'G')
    2
    >>> count_nucleotides('ATCTA', 'G')
    0
    '''
    return dna.count(nucleotide)



def contains_sequence(dna1, dna2):
    ''' (str, str) -> bool

    Return True if and only if DNA sequence dna2 occurs in the DNA sequence
    dna1.

    >>> contains_sequence('ATCGGC', 'GG')
    True
    >>> contains_sequence('ATCGGC', 'GT')
    False
    
    '''
    if dna1.find(dna2)!=-1:
       return True
    else:
       return False

def is_valid_sequence(val):
    ''' (str) -> bool

    Return True if and only if the DNA sequence is valid (that is, it contains only nucleotide characters: 'A', 'T', 'C' and 'G')

    >>> is_valid_sequence('ATCGGC')
    True
    >>> is_valid_sequence('ATCGGCM')
    False
    
    '''
    flag=True
    non=['A','T','C','G']
    for each in val:
      if each not in non:
        flag=False
      
    return flag



def insert_sequence(a,b,c):
    ''' (str,str,int) -> str
    
    Return the DNA sequence obtained by inserting the second DNA sequence into the first DNA sequence at the given index
    >>> insert_sequence('ATCGGC','AT',2)
    ATATCGGC
    >>> insert_sequence('ATCGGCM','DC',3)
    ATCDCGGCM
    
    '''
    return a[:c]+b+a[c:]


def get_complement(val):
    ''' (str) -> str
    Return the nucleotide's complement. 
    >>> get_complement('A')
    T
    >>> get_complement('G')
    C
    
    '''
    if val=='A':
        return 'T'
    elif val=='T':
        return 'A'
    elif val=='C':
        return 'G'
    elif val=='G':
        return 'C'




def get_complementary_sequence(val):
    ''' (str) -> str
    Return the DNA sequence that is complementary to the given DNA sequence.  
    >>> get_complementary_sequence('ATCG')
    TAGC
    >>> get_complementary_sequence('GC')
    CG
    
    '''
    a=''
    for each in val:
      if each=='A':
        a=a+'T'
      elif each=='T':
        a=a+'A'
      elif each=='C':
        a=a+'G'
      elif each=='G':
        a=a+'C'
    return a