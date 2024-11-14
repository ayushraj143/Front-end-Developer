import tkinter as tk
import socket
import threading

class TextEditorClient:
    def __init__(self, host='127.0.0.1', port=12345):
        self.host = host
        self.port = port
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect((self.host, self.port))
        
        # Set up Tkinter window
        self.root = tk.Tk()
        self.root.title("Real-time Collaborative Text Editor")

        # Create a Text widget for editing
        self.text = tk.Text(self.root, wrap='word', undo=True, width=80, height=30)
        self.text.pack(padx=10, pady=10)

        # Start receiving messages in a separate thread
        threading.Thread(target=self.receive_messages, daemon=True).start()

        # Bind the event for text changes
        self.text.bind("<KeyRelease>", self.on_text_change)

    def on_text_change(self, event):
        # Send the current text to the server after any change
        current_text = self.text.get(1.0, tk.END)
        self.client_socket.send(current_text.encode('utf-8'))

    def receive_messages(self):
        while True:
            try:
                message = self.client_socket.recv(1024).decode('utf-8')
                if message:
                    self.text.delete(1.0, tk.END)
                    self.text.insert(tk.END, message)
            except:
                break

    def run(self):
        self.root.mainloop()

# Start the client
if __name__ == "__main__":
    client = TextEditorClient()
    client.run()
