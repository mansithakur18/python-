import tkinter as tk
from tkinter import filedialog, messagebox    #to open save and edit file, to take path from user and msg

def new_file():
    text.delete(1.0, tk.END) #clean text area or to delete all text 1.0 meanse first line first connecter to end
    
def open_file(): #to open file
    file_path = filedialog.askopenfilename(defaultextension=".txt", filetypes=[("text files", ".txt")]) #to open file dialog box
    if file_path:
        with open(file_path, 'r') as file: #open file in read mode
            text.delete(1.0, tk.END) #delete existing text
            text.insert(tk.END, file.read()) #insert content to text area
        
def save_file(): #to save file
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("text files", ".txt")]) #to open save dialog box
    if file_path:
        with open(file_path, 'w') as file: #open file in write mode
            file.write(text.get(1.0, tk.END)) #write content from text area to file
            messagebox.showinfo("Info", "File saved successfully!") #show success message
            
#create main window
root= tk.Tk()
root.title("Mansi's text editor")
root.geometry("800x600")

menu = tk.Menu(root) #create menu bar
root.config(menu=menu) #config menu to root window
file_menu = tk.Menu(menu) #create file menu
menu.add_cascade(label="File", menu=file_menu) #add file menu to menu bar
file_menu.add_command(label="New", command=new_file) #add new file option
file_menu.add_command(label="Open", command=open_file) #add open file option
file_menu.add_command(label="Save", command=save_file) #add save file option
file_menu.add_separator() #add separator
file_menu.add_command(label="Exit", command=root.quit) #add exit option

#text area
text = tk.Text(root, wrap= tk.WORD, font=("Helvetica", 12), fg ="black") #create text area with word wrap
text.pack(expand= tk.YES, fill= tk.BOTH) #pack text area to fill window

root.mainloop() #run the application