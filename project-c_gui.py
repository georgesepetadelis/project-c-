import Tkinter as tk

class CustomerApp:
  def __init__(self, root):
    self.root = root
    self.create_widgets()

  def create_widgets(self):
    # Create widgets for each option
    self.option1_button = tk.Button(self.root, text="Create a new customer", command=self.create_customer)
    self.option2_button = tk.Button(self.root, text="Update a customer's information", command=self.update_customer)
    self.option3_button = tk.Button(self.root, text="Show a customer's information and transactions", command=self.show_customer)
    self.option4_button = tk.Button(self.root, text="Quit", command=self.root.destroy)

    # Place widgets in the window
    self.option1_button.pack()
    self.option2_button.pack()
    self.option3_button.pack()
    self.option4_button.pack()

  def create_customer(self):
    name = self.ask_input("Enter the customer's name: ")
    afm = self.ask_input("Enter the customer's AFM: ")
    address = self.ask_input("Enter the customer's address: ")
    phone = self.ask_input("Enter the customer's phone: ")

    with open("customers.txt", "a") as f:
      f.write("{},{},{},{}\n".format(name, afm, address, phone))

  def update_customer(self):
    afm = self.ask_input("Enter the AFM of the customer you want to update: ")

    with open("customers.txt", "r") as f:
      lines = f.readlines()

    found = False
    with open("customers.txt", "w") as f:
      for line in lines:
        if line.split(",")[1] == afm:
          name = self.ask_input("Enter the updated name: ")
          address = self.ask_input("Enter the updated address: ")
          phone = self.ask_input("Enter the updated phone: ")
          f.write("{},{},{},{}\n".format(name, afm, address, phone))
          found = True
        else:
          f.write(line)

    if not found:
      self.show_message("No customer with AFM {} was found.".format(afm))

  def show_customer(self):
    afm = self.ask_input("Enter the AFM of the customer you want to see: ")

    with open("customers.txt", "r") as f:
      lines = f.readlines()

    found = False
    for line in lines:
      if line.split(",")[1] == afm:
        name, afm, address, phone = line.split(",")
        message = "Name: {}\nAFM: {}\nAddress: {}\nPhone: {}".format(name, afm, address, phone)
        self.show_message(message)
        found = True
        break

        if not found:
            
            self.show_message("No customer with this AFM was found.")

            with open("transactions.txt", "r") as f:
                lines = f.readlines()

                message = "Transactions:\n"
                for line in lines:
                    if line.split(",")[0] == afm:
                        afm, date, name, balance = line.split(",")
                        message += "{} {} {} {}\n".format(date, name, afm, balance)
                        self.show_message(message)

    def ask_input(self, prompt):
        # Create a new window to ask for input
        input_window = tk.Toplevel(self.root)
        input_window.title("Give input")
        label = tk.Label(input_window, text=prompt)
        entry = tk.Entry(input_window)

        # Create a button to submit the input
        def submit():
          # Get the input and close the window
          input_value = entry.get()
          input_window.destroy()

        button = tk.Button(input_window, text="Submit", command=submit)

        # Place the widgets in the window
        label.pack()
        entry.pack()
        button.pack()

        # Wait for the input window to be closed
        self.root.wait_window(input_window)
        return input_value

    def show_message(self, message):

        # Create a new window to show the message
        message_window = tk.Toplevel(self.root)
        message_window.title("Message")

        # Create a label to display the message
        label = tk.Label(message_window, text=message)
        label.pack()

        # Create a button to close the window
        button = tk.Button(message_window, text="Close", command=message_window.destroy)
        button.pack()

def main():
    root = tk.Tk()
    app = CustomerApp(root)
    root.mainloop()


main()

