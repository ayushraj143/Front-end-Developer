import tkinter as tk
from tkinter import messagebox

# Create the main window
root = tk.Tk()
root.title("Interactive Resume")
root.geometry("600x600")

# Set up fonts
font_title = ("Helvetica", 18, "bold")
font_header = ("Helvetica", 14, "bold")
font_content = ("Helvetica", 12)

# Resume Sections
personal_info = {
    "Name": "John Doe",
    "Email": "johndoe@email.com",
    "Phone": "+1234567890",
    "LinkedIn": "linkedin.com/in/johndoe"
}

skills = ["Python", "JavaScript", "Machine Learning", "Data Analysis", "SQL", "Docker"]
experience = [
    {"title": "Software Developer", "company": "ABC Corp", "year": "2020-2023", "description": "Developed web applications using Python and Django."},
    {"title": "Data Analyst", "company": "XYZ Ltd", "year": "2018-2020", "description": "Analyzed business data and built interactive dashboards using Python."}
]
education = [
    {"degree": "Bachelor of Science in Computer Science", "school": "University of Example", "year": "2014-2018"}
]

# Function to display personal details
def show_personal_details():
    details = "\n".join([f"{key}: {value}" for key, value in personal_info.items()])
    messagebox.showinfo("Personal Information", details)

# Function to display skills
def show_skills():
    skills_list = "\n".join(skills)
    messagebox.showinfo("Skills", skills_list)

# Function to display experience
def show_experience():
    experience_list = "\n".join([f"{exp['title']} at {exp['company']} ({exp['year']})\n{exp['description']}\n" for exp in experience])
    messagebox.showinfo("Experience", experience_list)

# Function to display education
def show_education():
    education_list = "\n".join([f"{edu['degree']} from {edu['school']} ({edu['year']})" for edu in education])
    messagebox.showinfo("Education", education_list)

# Function to quit the application
def quit_app():
    root.quit()

# Create title label
title_label = tk.Label(root, text="John Doe - Interactive Resume", font=font_title, pady=10)
title_label.pack()

# Create buttons to display sections
personal_button = tk.Button(root, text="Personal Information", font=font_header, command=show_personal_details, width=25)
personal_button.pack(pady=5)

skills_button = tk.Button(root, text="Skills", font=font_header, command=show_skills, width=25)
skills_button.pack(pady=5)

experience_button = tk.Button(root, text="Experience", font=font_header, command=show_experience, width=25)
experience_button.pack(pady=5)

education_button = tk.Button(root, text="Education", font=font_header, command=show_education, width=25)
education_button.pack(pady=5)

# Quit button
quit_button = tk.Button(root, text="Quit", font=font_content, command=quit_app, width=25)
quit_button.pack(pady=20)

# Start the Tkinter event loop
root.mainloop()
