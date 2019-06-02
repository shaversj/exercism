def to_rna(dna_strand):
    table = {"G": "C", "C": "G", "T": "A", "A": "U"}
    results = [table.get(dna) for dna in dna_strand]
    return "".join(results)
