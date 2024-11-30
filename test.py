from Bio.Seq import Seq
import matplotlib.pyplot as plt

# Define a sample DNA sequence
dna_sequence = Seq("AGCTTAGCTAGCTAACCGGTTAGCTAGCTAACGGTAGCTAGCTAA")

# Calculate base composition
base_counts = {
    "A": dna_sequence.count("A"),
    "T": dna_sequence.count("T"),
    "C": dna_sequence.count("C"),
    "G": dna_sequence.count("G")
}

# Convert counts to percentages
total_bases = sum(base_counts.values())
base_percentages = {base: (count / total_bases) * 100 for base, count in base_counts.items()}

# Create a pie chart for visualization
labels = base_percentages.keys()
sizes = base_percentages.values()
colors = ['#FF9999', '#66B2FF', '#99FF99', '#FFCC99']
plt.figure(figsize=(6, 6))
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140, colors=colors)
plt.title("DNA Base Composition")
plt.show()
