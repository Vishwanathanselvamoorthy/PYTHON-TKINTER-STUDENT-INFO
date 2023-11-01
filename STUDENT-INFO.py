import tkinter as tk


def add_student():
    
    name = entry_name.get()
    
    class_ = entry_class.get()
    
    section = entry_section.get()
    
    grade = entry_grade.get()
    
    roll = entry_roll.get()
    
    student_details = f"Name: {name}, Class: {class_}, Section: {section}, Grade: {grade}, Roll: {roll}"
    
    listbox_students.insert(tk.END, student_details)
    
    clear_fields()

def clear_fields():
    
    entry_name.delete(0, tk.END)
    
    entry_class.delete(0, tk.END)
    
    entry_section.delete(0, tk.END)
    
    entry_grade.delete(0, tk.END)
    
    entry_roll.delete(0, tk.END)

root = tk.Tk()

root.title("Student Details")

root.configure(bg="#faedcd")  



label_heading = tk.Label(root, text="STUDENT INFO", font=("Helvetica", 20, 'bold'),bg="#faedcd")

label_heading.grid(row=0, column=0, columnspan=2, pady=10, padx=5, sticky="ew")  


label_name = tk.Label(root, text="Name:", font=('Arial', 18,"bold"), bg="#faedcd")

label_name.grid(row=1, column=0, padx=5, pady=5, sticky="e")

entry_name = tk.Entry(root, font=('Arial', 12))

entry_name.grid(row=1, column=1, padx=5, pady=5)




label_class = tk.Label(root, text="Class:", font=('Arial', 18,"bold"),bg="#faedcd")

label_class.grid(row=2, column=0, padx=5, pady=5, sticky="e")

entry_class = tk.Entry(root, font=('Arial', 12))

entry_class.grid(row=2, column=1, padx=5, pady=5)



label_section = tk.Label(root, text="Section:", font=('Arial', 18,"bold"), bg="#faedcd")

label_section.grid(row=3, column=0, padx=5, pady=5, sticky="e")

entry_section = tk.Entry(root, font=('Arial', 12))

entry_section.grid(row=3, column=1, padx=5, pady=5)



label_grade = tk.Label(root, text="Grade:", font=('Arial', 18,"bold"), bg="#faedcd")

label_grade.grid(row=4, column=0, padx=5, pady=5, sticky="e")

entry_grade = tk.Entry(root, font=('Arial', 12))

entry_grade.grid(row=4, column=1, padx=5, pady=5)



label_roll = tk.Label(root, text="Roll:", font=('Arial', 18,"bold"),bg="#faedcd")

label_roll.grid(row=5, column=0, padx=5, pady=5, sticky="e")

entry_roll = tk.Entry(root, font=('Arial', 12))

entry_roll.grid(row=5, column=1, padx=5, pady=5)




button_add = tk.Button(root, text="Add Student", command=add_student, font=('Arial', 12,"bold"), bg='#d4a373', fg='black')

button_add.grid(row=6, column=0,  pady=20, padx=5)



button_clear = tk.Button(root, text="Clear Fields", command=clear_fields, font=('Arial', 12,"bold"), bg='#d4a373', fg='black')

button_clear.grid(row=6, column=1, pady=20, padx=5)





listbox_students = tk.Listbox(root, width=40, font=('Arial', 12,"bold"))

listbox_students.grid(row=7, column=0, columnspan=2, padx=5, pady=5)



root.mainloop()


