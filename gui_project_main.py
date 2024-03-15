import customtkinter as ctk
from gui_project_translation_class import TranslationClass
from gui_project_second_gui import ToplevelWindow
from gui_project_slc import SaveLoadClear
from gui_project_check import CheckClass


class GuiInterface(ctk.CTk):
    """
        A class representing the graphical user interface (GUI) for the translation tool.
    """
    def __init__(self):
        super().__init__()

        self.minsize(900, 500)
        self.title("Translation App")
        ctk.set_appearance_mode("dark")

        # Variable to store the reference to the top-level window
        self.toplevel_window = None
        # Variable to store the reference to the Translation class instance
        self.translation_class = None

        # Create and configure widgets
        self.Label = ctk.CTkLabel(master=self,
                                  text="Enter sequence below",
                                  font=("Ink Free", 30, "bold"),
                                  text_color="deeppink")
        self.Label.pack(padx=5, pady=10)

        self.textbox = ctk.CTkTextbox(master=self,
                                      width=500,
                                      height=200,
                                      font=("Arial", 13, "bold"))
        self.textbox.pack(padx=20, pady=20, expand=True, fill=ctk.BOTH)

        # Initialize variable with an instance of SaveLoadClear class using textbox as a parameter.
        self.slc = SaveLoadClear(self.textbox)

        self.button_translation = ctk.CTkButton(master=self,
                                                text="Translation",
                                                command=lambda: self.open_window("result"),
                                                fg_color="deeppink",
                                                hover_color="white",
                                                font=("Ink Free", 20, "bold"),
                                                width=300)
        self.button_translation.pack(padx=20, pady=10, expand=True)
        self.button_translation.bind("<Enter>", lambda event: self.button_translation.configure(text_color="deeppink",
                                                                                                fg_color="white"))
        self.button_translation.bind("<Leave>", lambda event: self.button_translation.configure(text_color="white",
                                                                                                fg_color="deeppink"))

        self.button_load = ctk.CTkButton(master=self,
                                         text="Load",
                                         command=self.slc.load_file,
                                         fg_color="deeppink",
                                         hover_color="white",
                                         font=("Ink Free", 20, "bold"))
        self.button_load.pack(padx=20, pady=20, side=ctk.LEFT, expand=True)
        self.button_load.bind("<Enter>",
                              lambda event: self.button_load.configure(text_color="deeppink",
                                                                       fg_color="white"))
        self.button_load.bind("<Leave>",
                              lambda event: self.button_load.configure(text_color="white",
                                                                       fg_color="deeppink"))

        self.button_random = ctk.CTkButton(master=self,
                                           text="Random",
                                           fg_color="deeppink",
                                           command=self.random_seq,
                                           hover_color="white",
                                           font=("Ink Free", 20, "bold"))
        self.button_random.pack(padx=20, pady=20, side=ctk.LEFT, expand=True)
        self.button_random.bind("<Enter>",
                                lambda event: self.button_random.configure(text_color="deeppink",
                                                                           fg_color="white"))
        self.button_random.bind("<Leave>",
                                lambda event: self.button_random.configure(text_color="white",
                                                                           fg_color="deeppink"))

        self.button_check = ctk.CTkButton(master=self,
                                          text="Check",
                                          fg_color="deeppink",
                                          command=lambda: self.open_window("check"),
                                          hover_color="white",
                                          font=("Ink Free", 20, "bold"))
        self.button_check.pack(padx=20, pady=20, side=ctk.LEFT, expand=True)
        self.button_check.bind("<Enter>",
                               lambda event: self.button_check.configure(text_color="deeppink",
                                                                         fg_color="white"))
        self.button_check.bind("<Leave>",
                               lambda event: self.button_check.configure(text_color="white",
                                                                         fg_color="deeppink"))

        self.button_clear = ctk.CTkButton(master=self,
                                          text="Clear",
                                          command=self.slc.clear_message,
                                          fg_color="deeppink",
                                          hover_color="white",
                                          font=("Ink Free", 20, "bold"))
        self.button_clear.pack(padx=20, pady=20, side=ctk.LEFT, expand=True)
        self.button_clear.bind("<Enter>",
                               lambda event: self.button_clear.configure(text_color="deeppink",
                                                                         fg_color="white"))
        self.button_clear.bind("<Leave>",
                               lambda event: self.button_clear.configure(text_color="white",
                                                                         fg_color="deeppink"))

    def get_text(self):
        """
            Retrieves text from a textbox, converts it to uppercase, and removes leading/trailing whitespace.
        """
        self.translation_class = TranslationClass(self.textbox.get("0.0", "end").upper().strip())

        # Call the translation method on the translation_class instance and return the result.
        return self.translation_class.translation()

    def open_window(self, which_window):
        """
            Opens a new window based on the specified 'which_window'.
        """

        # Check if a top-level window exists or if it's already closed
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            if which_window == "result":
                # Create a new result window
                self.toplevel_window = ToplevelWindow()
                # Prevent interaction with other windows while the result window is open
                self.toplevel_window.grab_set()
                # Display the result in the result window
                self.toplevel_window.show_result(self.get_text())
            elif which_window == "check":
                # Retrieve text from the text widget and perform translation
                self.get_text()
                # Create a new check window with translation result
                self.toplevel_window = CheckClass(self.translation_class.result_check)
                # Prevent interaction with other windows while the check window is open
                self.toplevel_window.grab_set()
        else:
            # If a window is already open, bring it to focus
            self.toplevel_window.focus()

    def random_seq(self):
        """
            Generates a random mRNA sequence and inserts it into the text widget.
        """

        # Create a TranslationClass instance with no initial sequence
        self.translation_class = TranslationClass(None)
        return self.textbox.insert(ctk.END, self.translation_class.random_sequence())


if __name__ == "__main__":
    app = GuiInterface()
    app.mainloop()
