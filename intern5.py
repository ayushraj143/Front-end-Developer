import tkinter as tk
from tkinter import messagebox
import requests

# Function to fetch movie details from OMDb API
def get_movie_details():
    movie_title = entry.get().strip()
    if not movie_title:
        messagebox.showwarning("Input Error", "Please enter a movie title!")
        return
    
    # OMDb API URL (replace 'your_api_key' with your actual API key)
    api_key = 'your_api_key'  # Replace with your OMDb API key
    url = f"http://www.omdbapi.com/?t={movie_title}&apikey={api_key}"
    
    try:
        # Fetch data from OMDb API
        response = requests.get(url)
        data = response.json()

        if data['Response'] == 'True':
            # Display movie details
            title_var.set(f"Title: {data['Title']}")
            year_var.set(f"Year: {data['Year']}")
            genre_var.set(f"Genre: {data['Genre']}")
            director_var.set(f"Director: {data['Director']}")
            plot_var.set(f"Plot: {data['Plot']}")
            actors_var.set(f"Actors: {data['Actors']}")
            poster_url = data.get('Poster', 'N/A')
            if poster_url != 'N/A':
                poster_label.config(text=f"Poster: {poster_url}")
            else:
                poster_label.config(text="Poster: Not available")
        else:
            messagebox.showerror("Error", "Movie not found!")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to retrieve data: {str(e)}")

# Set up the main window using Tkinter
root = tk.Tk()
root.title("Movie Information App")

# Title for the app
title = tk.Label(root, text="Movie Information Finder", font=("Arial", 16))
title.grid(row=0, column=0, columnspan=2, pady=10)

# Label and entry field for the movie title
movie_label = tk.Label(root, text="Enter Movie Title:", font=("Arial", 12))
movie_label.grid(row=1, column=0, padx=10, pady=10, sticky='e')

entry = tk.Entry(root, font=("Arial", 12), width=30)
entry.grid(row=1, column=1, padx=10, pady=10)

# Button to get movie details
search_button = tk.Button(root, text="Search", font=("Arial", 12), command=get_movie_details)
search_button.grid(row=2, column=0, columnspan=2, pady=10)

# Labels to display movie details
title_var = tk.StringVar()
year_var = tk.StringVar()
genre_var = tk.StringVar()
director_var = tk.StringVar()
plot_var = tk.StringVar()
actors_var = tk.StringVar()

# Title
title_label = tk.Label(root, textvariable=title_var, font=("Arial", 12))
title_label.grid(row=3, column=0, columnspan=2, pady=5)

# Year
year_label = tk.Label(root, textvariable=year_var, font=("Arial", 12))
year_label.grid(row=4, column=0, columnspan=2, pady=5)

# Genre
genre_label = tk.Label(root, textvariable=genre_var, font=("Arial", 12))
genre_label.grid(row=5, column=0, columnspan=2, pady=5)

# Director
director_label = tk.Label(root, textvariable=director_var, font=("Arial", 12))
director_label.grid(row=6, column=0, columnspan=2, pady=5)

# Plot
plot_label = tk.Label(root, textvariable=plot_var, font=("Arial", 12), wraplength=350)
plot_label.grid(row=7, column=0, columnspan=2, pady=5)

# Actors
actors_label = tk.Label(root, textvariable=actors_var, font=("Arial", 12))
actors_label.grid(row=8, column=0, columnspan=2, pady=5)

# Poster URL (optional, you can display an image if you want)
poster_label = tk.Label(root, text="Poster: Not available", font=("Arial", 12), wraplength=350)
poster_label.grid(row=9, column=0, columnspan=2, pady=5)

# Run the Tkinter event loop
root.mainloop()
