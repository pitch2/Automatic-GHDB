import tkinter as tk
from tkinter import ttk, messagebox
import webbrowser

class GoogleSearchBuilder:
    def __init__(self, root):
        self.root = root
        self.root.title("Google Advanced Search Builder")
        
        # Configure main window
        self.root.geometry("500x600")
        self.root.resizable(True, True)
        
        # Initialize search parameters
        self.search_fields = {
            "Research": "",
            "Type": "",
            "Inurl": "",
            "Site": "",
            "Intitle": "",
            "Before": "",
            "After": "",
            "Numrange Start": "",
            "Numrange End": ""
        }
        
        self.create_widgets()

    def create_widgets(self):
        # Create main frame with padding
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Create and place all entry fields
        for i, (label_text, _) in enumerate(self.search_fields.items()):
            ttk.Label(main_frame, text=label_text).grid(row=i, column=0, padx=5, pady=5, sticky=tk.W)
            entry = ttk.Entry(main_frame, width=40)
            entry.grid(row=i, column=1, padx=5, pady=5, sticky=(tk.W, tk.E))
            self.search_fields[label_text] = entry
        
        # Create buttons frame
        button_frame = ttk.Frame(main_frame)
        button_frame.grid(row=len(self.search_fields), column=0, columnspan=2, pady=20)
        
        # Create buttons
        ttk.Button(button_frame, text="Generate Query", command=self.generate_query).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="Search in Browser", command=self.open_browser).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="Clear All", command=self.clear_fields).pack(side=tk.LEFT, padx=5)
        
        # Create result display
        self.result_var = tk.StringVar()
        self.result_var.set("Your search query will appear here")
        result_label = ttk.Label(main_frame, textvariable=self.result_var, wraplength=400)
        result_label.grid(row=len(self.search_fields) + 1, column=0, columnspan=2, pady=10)

    def generate_query(self):
        query_parts = []
        
        # Get values from entry fields
        values = {k: v.get().strip() for k, v in self.search_fields.items()}
        
        # Add basic search terms
        if values["Research"]:
            query_parts.append(f"'{values["Research"]}'")
            
        # Add file type
        if values["Type"]:
            query_parts.append(f':{values["Type"]}')
            
        # Add URL filter
        if values["Inurl"]:
            query_parts.append(f'inurl:{values["Inurl"]}')
            
        # Add site filter
        if values["Site"]:
            query_parts.append(f'site:{values["Site"]}')
            
        # Add title filter
        if values["Intitle"]:
            query_parts.append(f'intitle:"{values["Intitle"]}"')
            
        # Add date filters
        if values["Before"]:
            query_parts.append(f'before:{values["Before"]}')
        if values["After"]:
            query_parts.append(f'after:{values["After"]}')
            
        # Add number range
        if values["Numrange Start"] or values["Numrange End"]:
            if not (values["Numrange Start"] and values["Numrange End"]):
                messagebox.showerror("Error", "Both start and end values are required for numrange")
                return
            query_parts.append(f'numrange:{values["Numrange Start"]}..{values["Numrange End"]}')
        
        # Combine all parts
        self.current_query = " ".join(query_parts)
        self.result_var.set(f"Generated Query: {self.current_query}")
        return self.current_query

    def open_browser(self):
        query = self.generate_query()
        if query:
            encoded_query = query.replace(' ', '+')
            webbrowser.open_new_tab(f"https://www.google.com/search?q={encoded_query}")

    def clear_fields(self):
        for entry in self.search_fields.values():
            entry.delete(0, tk.END)
        self.result_var.set("Your search query will appear here")

def main():
    root = tk.Tk()
    app = GoogleSearchBuilder(root)
    root.mainloop()

if __name__ == "__main__":
    main()
