import random


class TranslationClass:
    """
        A class for translating mRNA sequences into amino acid sequences.
    """
    def __init__(self, sequence):

        # Dictionary mapping mRNA codons to amino acids
        self.amino_acids = {
            "UUU": "Phe", "UUC": "Phe",
            "UUA": "Leu", "UUG": "Leu",
            "CUU": "Leu", "CUC": "Leu", "CUA": "Leu", "CUG": "Leu",
            "AUU": "Ile", "AUC": "Ile", "AUA": "Ile",
            "AUG": "Met",
            "GUU": "Val", "GUC": "Val", "GUA": "Val", "GUG": "Val",
            "UCU": "Ser", "UCC": "Ser", "UCA": "Ser", "UCG": "Ser",
            "CCU": "Pro", "CCC": "Pro", "CCA": "Pro", "CCG": "Pro",
            "ACU": "Thr", "ACC": "Thr", "ACA": "Thr", "ACG": "Thr",
            "GCU": "Ala", "GCC": "Ala", "GCA": "Ala", "GCG": "Ala",
            "UAU": "Tyr", "UAC": "Tyr",
            "UAA": "Stp", "UAG": "Stp",
            "CAU": "His", "CAC": "His",
            "CAA": "Gln", "CAG": "Gln",
            "AAU": "Asn", "AAC": "Asn",
            "AAA": "Lys", "AAG": "Lys",
            "GAU": "Asp", "GAC": "Asp",
            "GAA": "Glu", "GAG": "Glu",
            "UGU": "Cys", "UGC": "Cys",
            "UGA": "Stp", "UGG": "Trp",
            "CGU": "Arg", "CGC": "Arg", "CGA": "Arg", "CGG": "Arg",
            "AGU": "Ser", "AGC": "Ser",
            "AGA": "Arg", "AGG": "Arg",
            "GGU": "Gly", "GGC": "Gly", "GGA": "Gly", "GGG": "Gly"
        }

        self.nitrogenous_bases = {"A", "G", "C", "U"}
        self.sequence = sequence
        self.codon_list = self.generate_codon_list()
        self.result_check = None

    def generate_codon_list(self):
        """
            Generates a list of codons from the input sequence.
        """
        return [self.sequence[i:i + 3] for i in range(0, len(self.sequence or ""), 3) if
                self.sequence is not None]

    def check_sequence(self):
        """
            Checks if the input sequence contains only nitrogenous bases and is a multiple of 3 in length.
        """
        return all(character in self.nitrogenous_bases and
                   len(self.sequence) % 3 == 0 for character in self.sequence)

    def check_codons(self):
        """
            Checks if the start codon 'AUG' and at least one stop codon are present in the codon list.
        """
        return all(codon in self.codon_list for codon in ["AUG"]) and any(
            stop_codon in self.codon_list for stop_codon in ["UAA", "UAG", "UGA"])

    def translation(self):
        """
            Translates the mRNA sequence into an amino acid sequence.
        """

        # Check if the sequence and codons are valid
        if self.check_sequence() and self.check_codons():
            result = []
            current_sequence = ""
            codon_start_found = False  # # Variable to track if the start codon has been found

            # Translate codons into amino acids
            for codon in self.codon_list:
                if codon == "AUG":
                    codon_start_found = True
                    current_sequence += f"{self.amino_acids[codon]}-"

                elif self.amino_acids[codon] == "Stp" and codon_start_found:
                    result.append(current_sequence[:-1])
                    current_sequence = ""
                    codon_start_found = False

                elif codon_start_found:
                    current_sequence += f"{self.amino_acids[codon]}-"

            # Generate the result string
            self.result_check = "\n".join([f"Sekwencja aminokwasowa {i}: {seq}" for i, seq in enumerate(result, start=1)])

            return f"Podana sekwencja nukleotydowa: \n{self.sequence}\n\n" + self.result_check

        else:
            # If sequence is invalid, return an error message
            return ("The sequence should contain only nitrogenous bases and full codons, with codon start and stop.\n"
                    "Close this window and re-enter the correct sequence again in the previous window.")

    def random_sequence(self):
        """
            Generates a random mRNA sequence.
        """
        return "".join(["AUG"] + random.choices(
            [aminoacid for aminoacid in self.amino_acids.keys() if aminoacid not in ["AUG", "UAA", "UGA", "UAG"]],
            k=random.randint(3, 10)) + [
                           random.choice([key for key, value in self.amino_acids.items() if value == "Stp"])])
