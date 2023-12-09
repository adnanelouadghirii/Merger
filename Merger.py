import tkinter as tk
from tkinter import filedialog
from pypdf import PdfMerger

def merge_pdfs():
    pdfs = filedialog.askopenfilenames(title="Select PDF files to merge", filetypes=[("PDF files", "*.pdf")])
    merger = PdfMerger()
    if pdfs:
        for pdf in pdfs:
            merger.append(pdf)
        save_path = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")])
        if save_path:
            merger.write(save_path)
            merger.close()
            status_label.config(text="PDFs merged successfully!")
        else:
            status_label.config(text="Merge canceled or no file selected.")
    else:
        status_label.config(text="No files selected for merging.")

# Create main window

root = tk.Tk()
root.geometry("500x300")  # Width x Height
root.title("Simple PDF Merger")

# Create and place widgets
merge_button = tk.Button(root, text="Merge PDFs", command=merge_pdfs)
merge_button.pack(pady=20)

status_label = tk.Label(root, text="", fg="green")
status_label.pack()

root.mainloop()