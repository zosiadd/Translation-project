import customtkinter as ctk
from gui_project_slc import SaveLoadClear


class ToplevelWindow(ctk.CTkToplevel):
    """
        A class representing a top-level window to display translation results.
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title("Translation Result")
        self.geometry("700x700")
        self.resizable(False, False)


        # Create and configure widgets
        self.label = ctk.CTkLabel(self, text_color="deeppink", text="Here you will see the result of the translation",
                                  font=("Ink Free", 30, "bold"))
        self.label.pack(padx=20, pady=20, side=ctk.TOP)

        self.text = ctk.CTkTextbox(master=self, width=700, height=500, font=("Arial", 15))
        self.text.pack(padx=20, pady=20)

        # Save, Load, Clear functionality
        self.slc = SaveLoadClear(self.text)

        self.button = ctk.CTkButton(master=self,
                                    text="Save",
                                    command=self.slc.save_file,
                                    fg_color="deeppink",
                                    hover_color="white",
                                    font=("Ink Free", 30, "bold"))
        self.button.bind("<Enter>",
                         lambda event: self.button.configure(text_color="deeppink", fg_color="white"))
        self.button.bind("<Leave>",
                         lambda event: self.button.configure(text_color="white", fg_color="deeppink"))
        self.button.pack(padx=20, pady=20)


    def show_result(self, amino_acids_seq):
        """
            Displays the translation result in the textbox.
        """
        self.text.insert(index=0.0, text=amino_acids_seq)
        self.text.configure(state="disabled")
