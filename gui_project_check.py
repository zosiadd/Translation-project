import customtkinter as ctk


class CheckClass(ctk.CTkToplevel):
    """
        This class is used to create an application window to check for nucleotide sequence repeats.
    """

    def __init__(self, result_check):
        super().__init__()
        self.title("Translation App")
        self.minsize(800, 500)

        # Store the nucleotide sequence for comparison
        self.seq_nucleotide = result_check

        # Create and configure widgets
        self.Label = ctk.CTkLabel(master=self,
                                  text="Enter the amino acid sequence whose repeats you want to check\nExample: Met-Pro-Glu",
                                  font=("Ink Free", 25, "bold"),
                                  text_color="deeppink")
        self.Label.pack(padx=5, pady=10, expand=True)

        self.textbox_top = ctk.CTkTextbox(master=self, font=("Arial", 15), height=50)
        self.textbox_top.pack(padx=20, pady=20, fill=ctk.BOTH, expand=True)
        # This code snippet creates a button called compare, which runs the sequence_comparison function when clicked. The button reacts to mouseover by changing colors, and displays the comparison results in the textbox_bottom text area.
        self.compare = ctk.CTkButton(master=self,
                                     text="Compare",
                                     command=lambda: self.sequence_comparison(),
                                     fg_color="deeppink",
                                     hover_color="white",
                                     font=("Ink Free", 20, "bold"))
        self.compare.pack(padx=20, pady=20, expand=True)
        self.compare.bind("<Enter>",
                          lambda event: self.compare.configure(text_color="deeppink",
                                                               fg_color="white"))
        self.compare.bind("<Leave>",
                          lambda event: self.compare.configure(text_color="white",
                                                               fg_color="deeppink"))

        self.textbox_bottom = ctk.CTkTextbox(master=self, font=("Arial", 15))
        self.textbox_bottom.pack(padx=20, pady=20, fill=ctk.BOTH, expand=True)
        self.textbox_bottom.configure(state="disabled")

    def sequence_comparison(self):
        """
            Compares the user-provided amino acid sequence with the stored nucleotide sequence.
        """
        amino_acids_seq = self.textbox_top.get("0.0", "end").title().strip()
        self.textbox_bottom.configure(state="normal")
        self.textbox_bottom.delete("1.0", ctk.END)

        # Check if nucleotide sequence exists and amino acid sequence is provided
        if self.seq_nucleotide is not None and len(amino_acids_seq) > 0 and amino_acids_seq in self.seq_nucleotide:
            self.textbox_bottom.insert(ctk.END,
                                       f"{self.seq_nucleotide}\n\nUser-provided sequence: {amino_acids_seq}\nRepeated sequences will be highlighted in deeppink color")
            start_index = "1.0"
            # If the sequence is in a nucleotide sequence, both sequences are displayed and the text box is set to inactive mode.
            while True:
                start_index = self.textbox_bottom.search(amino_acids_seq, start_index, ctk.END)
                if not start_index:
                    break

                end_index = f"{start_index}+{len(amino_acids_seq)}c"
                self.textbox_bottom.tag_add("highlight", start_index, end_index)
                start_index = end_index

            self.textbox_bottom.tag_config("highlight", foreground="deeppink")
            self.textbox_bottom.configure(state="disabled")

        # If nucleotide sequence exists but amino acid sequence is not provided or not found
        elif self.seq_nucleotide is not None and len(amino_acids_seq) > 0:
            self.textbox_bottom.insert(ctk.END,
                                       f"{self.seq_nucleotide}\n\nUser-provided sequence: {amino_acids_seq}\nNo repeated amino acid sequences. Enter another sequence to see if it will repeat.")
            self.textbox_bottom.configure(state="disabled")

        # If nucleotide sequence is not provided
        elif self.seq_nucleotide is None:
            self.textbox_bottom.insert(ctk.END,
                                       "Please close this window and re-enter the correct sequence in the previous window.")
            self.textbox_bottom.configure(state="disabled")

        else:
            # If amino acid sequence is not provided
            self.textbox_bottom.insert(ctk.END,
                                       "The amino acid sequence was not entered by the user. Re-enter the correct sequence in the text box above")
            self.textbox_bottom.configure(state="disabled")
