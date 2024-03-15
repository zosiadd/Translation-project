# Importing a module named customtkinter and using it under the alias ctk. In addition, import the filedialog function from this module.
import customtkinter as ctk
from customtkinter import filedialog


class SaveLoadClear:
    """
        SaveLoadClear is a class that manages the saving, loading and clearing of data.
    """

    def __init__(self, textbox):
        self.textbox = textbox
        self.sequence = []

    def save_file(self):
        """
            Saves the contents of the textbox to a file.
        """
        if filename := filedialog.asksaveasfilename(defaultextension=".txt",
                                                    filetypes=[("Text", ".txt"), ("FASTA", ".fasta")]):
            with open(filename, "w") as file:
                file.write(self.textbox.get(1.0, ctk.END))

    def load_file(self):
        """
            Loads the contents of the selected file into the textbox, skipping lines containing the ">" character.
        """

        # Clear any existing content in the textbox
        self.clear_message()
        if filename := filedialog.askopenfilename():
            with open(filename, "r") as file:
                lines = file.read().splitlines()
                lines = [line for line in lines if ">" not in line]

                # Process each line from the file
                for line in lines:
                    if line != "":
                        # Check if the line starts with "AUG" and ends with a stop codon
                        if line[:3] != "AUG" and line[-3:] != ["UAA", "UGA", "UAG"]:
                            # If not, add start and stop codons
                            self.sequence.append("AUG" + line + "UAA")
                        else:
                            self.sequence.append(line)

                # Insert the processed sequence into the textbox
                self.textbox.insert(ctk.END, "".join(self.sequence))

    def clear_message(self):
        """
            Clears the content of the textbox.
        """
        self.textbox.delete("1.0", ctk.END)
