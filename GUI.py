import customtkinter as ctk
import Chatbot

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")


root = ctk.CTk()
root.geometry("800x500")
root.title("Chatbot")

# Create the chatbot's text area
text_area = ctk.CTkTextbox(root, width=700, height=350)
text_area.pack(pady=12,padx=10)



def send_message_enter(event):
  # Get the user's input
  user_input = input_field.get()

  # Clear the input field
  input_field.delete(0, ctk.END)
  text_area.insert(ctk.END,text=f"User: {user_input}\n")
  # Generate a response from the chatbot
  response = Chatbot.agent_executer.invoke({"input":user_input})
  # Display the response in the chatbot's text area
  text_area.insert(ctk.END,text=f"Chatbot: {response["output"]}\n")

def send_message():
  # Get the user's input
  user_input = input_field.get()

  # Clear the input field
  input_field.delete(0, ctk.END)
  text_area.insert(ctk.END, f"User: {user_input}\n")

  # Generate a response from the chatbot
  response = Chatbot.agent_executer.invoke({"input": user_input})
  # Display the response in the chatbot's text area
  text_area.insert(ctk.END, text=f"Chatbot: {response["output"]}\n")

# Create the user's input field
input_field = ctk.CTkEntry(root, width=700,placeholder_text="Enter your message here")
input_field.pack(pady=12,padx=10)
input_field.bind('<Return>', send_message_enter)
# Create the send button
send_button = ctk.CTkButton(root, text="Send", command=lambda: send_message())
send_button.pack()




root.mainloop()