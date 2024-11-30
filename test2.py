from Bio.Seq import Seq
from Bio.SeqUtils import gc_fraction
import matplotlib.pyplot as plt

def transcribe_dna(sequence):
    rna_sequence = sequence.transcribe()
    print(f"Transcribed RNA: {rna_sequence}")
    return rna_sequence

def main():
    # This is a test sequence
    dna_sequence = Seq("AGTACACTGGTACCTAGGCTAAGTCCGATGGTCAAGTAC")

    print("Starting DNA Analysis...\n")
    rna_sequence = transcribe_dna(dna_sequence)
    print("\nDNA Analysis Complete!")

if __name__ == "__main__":
    main()
