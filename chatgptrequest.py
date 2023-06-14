import openai
import tkinter as tk
import json

# Set your API key
openai.api_key = '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'

# Create an initial messages list
""" messages = [
    {"role": "system", "content": 'You are a helpful assistant.'},
    {"role": "assistant", "content": "Yes, adding multiple lines in a message can be useful when providing additional information or context to your request. Including chat history can also help the recipient better understand the issue and provide more effective assistance. Just make sure to only include relevant information and to format the message in a clear and organized way."},
    {'role': 'user', 'content': "can u generate a python script that would add new and delete old communications after 5 lines in the messages list"}
] """

# Get the response from the OpenAI API
def generate_response(messages):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    response_content = response.choices[0].message.content
    return response_content

# Add user request to the messages list
def add_request():
    user_input = input_field.get()
    messages.append({"role": "user", "content": user_input})
    update_messages_list()
    response = generate_response(messages)
    output_field.configure(state='normal')
    output_field.insert(tk.END, response + "\n")
    output_field.configure(state='disabled')
    input_field.delete(0, tk.END)

# Create the main window
root = tk.Tk()
root.title("ChatGPT")
# Get the screen width and height
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
# Set the application window size to match the screen size
root.geometry(f"{screen_width}x{screen_height}")

# Create a Listbox to display the messages
messages_listbox = tk.Listbox(root, font=("Arial", 12), width=80)
messages_listbox.pack(pady=10)

# Delete the selected item from the messages list
def delete_selected():
    selected_index = messages_listbox.curselection()
    if selected_index:
        messages.pop(selected_index[0])
        update_messages_list()

# Function to update the messages Listbox
def update_messages_list():
    messages_listbox.delete(0, tk.END)
    for message in messages:
        content = message["content"]
        messages_listbox.insert(tk.END, content)

# Create the input field
input_field = tk.Entry(root, font=("Arial", 14), width=200)
input_field.pack(ipadx=30, ipady=30, pady=10)

# Create the add to messages button
add_button = tk.Button(root, text="Add Request", font=("Arial", 14), command=add_request)
add_button.pack(pady=10)

# Create the delete selected button
delete_button = tk.Button(root, text="Delete Selected", font=("Arial", 14), command=delete_selected)
delete_button.pack(pady=10)

# Create the output field
output_field = tk.Text(root, font=("Arial", 14), state='disabled')
output_field.pack(fill=tk.BOTH, expand=True)
# Start with an empty messages list
messages = []

# Update the messages Listbox initially
update_messages_list()
# Start the GUI event loop
root.mainloop()
