import Tkinter as tk

class Customer:
  def __init__(self, name, afm, address, phone):
    self.name = name
    self.afm = afm
    self.address = address
    self.phone = phone

class Transaction:
  def __init__(self, date, name, afm, balance):
    self.date = date
    self.name = name
    self.afm = afm
    self.balance = balance

class MainWindow(tk.Tk):
  def __init__(self):
    tk.Tk.__init__(self)

    # Read all the lines in the customers.txt file and create a list of Customer objects
    with open("customers.txt", "r") as f:
      lines = f.readlines()
    self.customers = []
    for line in lines:
      name, afm, address, phone = line.split(",")
      self.customers.append(Customer(name, afm, address, phone))

    # Read all the lines in the transactions.txt file and create a list of Transaction objects
    with open("transactions.txt", "r") as f:
      lines = f.readlines()
    self.transactions = []
    for line in lines:
      date, name, afm, balance = line.split(",")
      self.trans

class MainWindow(tk.Tk):
  def __init__(self):
    tk.Tk.__init__(self)

    # Read all the lines in the customers.txt file and create a list of Customer objects
    with open("customers.txt", "r") as f:
      lines = f.readlines()
    self.customers = []
    for line in lines:
      name, afm, address, phone = line.split(",")
      self.customers.append(Customer(name, afm, address, phone))

    # Read all the lines in the transactions.txt file and create a list of Transaction objects
    with open("transactions.txt", "r") as f:
      lines = f.readlines()
    self.transactions = []
    for line in lines:
      date, name, afm, balance = line.split(",")
      self.transactions.append(Transaction(date, name, afm, balance))

    # Create the main menu
    self.main_menu = tk.Menu(self)

    self.customer_menu = tk.Menu(self.main_menu, tearoff=0)
    self.customer_menu.add_command(label="Create a new customer", command=self.create_customer)
    self.customer_menu.add_command(label="Update a customer's information", command=self.update_customer)
    self.customer_menu.add_command(label="Show a customer's information and transactions", command=self.show_customer)
    self.main_menu.add_cascade(label="Customers", menu=self.customer_menu)

    self.main_menu.add_command(label="Quit", command=self.destroy)
    self.config(menu=self.main_menu)

  # Function to create a new customer
  def create_customer(self):
    def submit():
      name = name_entry.get()
      afm = afm_entry.get()
      address = address_entry.get()
      phone = phone_entry.get()

      # Create a new Customer object
      customer = Customer(name, afm, address, phone)

      # Add the new customer to the customers list
      self.customers.append(customer)

      # Write the new customer to the customers.txt file
      with open("customers.txt", "a") as f:
        f.write("{},{},{},{}\n".format(name, afm, address, phone))

      # Close the create customer window
      create_customer_window.destroy()

    # Create the create customer window
    create_customer_window = tk.Toplevel(self)
    create_customer_window.title("Create a new customer")

    name_label = tk.Label(create_customer_window, text="Name:")
    name_label.grid(row=0, column=0)
    name_entry = tk.Entry(create_customer_window)
    name_entry.grid(row=0, column=1)

    afm_label = tk.Label(create_customer_window, text="AFM:")
    afm_label.grid(row=1, column=0)
    afm_entry = tk.Entry(create_customer_window)
    afm_entry.grid(row=1, column=1)

    address_label = tk.Label(create_customer_window, text="Address:")
    address_label.grid(row=2, column=0)
    address_entry = tk.Entry(create_customer_window)
    address_entry.grid(row=2, column=1)

    phone_label = tk.Label(create_customer_window, text="Phone:")
    phone_label.grid(row=3, column=0)
    phone_entry = tk.Entry(create_customer_window)
    phone_entry.grid(row=3, column=1)

    submit_button = tk.Button(create_customer_window, text="Submit", command=submit)
    submit_button.grid(row=4, column=0, columnspan=2)

  # Function to update a customer's information
  def update_customer(self):
    def submit():
      afm = afm_entry.get()
      name = name_entry.get()
      address = address_entry.get()
      phone = phone_entry.get()

      # Find the customer with the matching AFM and update its information
      found = False
      for customer in self.customers:
        if customer.afm == afm:
          customer.name = name
          customer.address = address
          customer.phone = phone
          found = True
          break

      if not found:
        tk.messagebox.showinfo("Error", "AFM not found")
        return

      # Write the updated customer information to the customers.txt file
      with open("customers.txt", "w") as f:
        for customer in self.customers:
          f.write("{},{},{},{}\n".format(customer.name, customer.afm, customer.address, customer.phone))

      # Close the update customer window
      update_customer_window.destroy()

    # Create the update customer window
    update_customer_window = tk.Toplevel(self)
    update_customer_window.title("Update a customer's information")

    afm_label = tk.Label(update_customer_window, text="AFM:")
    afm_label.grid(row=0, column=0)
    afm_entry = tk.Entry(update_customer_window)
    afm_entry.grid(row=0, column=1)

    name_label = tk.Label(update_customer_window, text="Name:")
    name_label.grid(row=1, column=0)
    name_entry = tk.Entry(update_customer_window)
    name_entry.grid(row=1, column=1)

    address_label = tk.Label(update_customer_window, text="Address:")
    address_label.grid(row=2, column=0)
    address_entry = tk.Entry(update_customer_window)
    address_entry.grid(row=2, column=1)

    phone_label = tk.Label(update_customer_window, text="Phone:")
    phone_label.grid(row=3, column=0)
    phone_entry = tk.Entry(update_customer_window)
    phone_entry.grid(row=3, column=1)

    submit_button = tk.Button(update_customer_window, text="Submit", command=submit)
    submit_button.grid(row=4, column=0, columnspan=2)

  # Function to show a customer's information and transactions
  def show_customer(self):
    def show_transactions():
      # Find the customer with the matching AFM and display its transactions
      found = False
      for customer in self.customers:
        if customer.afm == afm_entry.get():
          found = True
          break
      
      if not found:
        tk.messagebox.showinfo("Error", "AFM not found")
        return

      # Create the transactions window
      transactions_window = tk.Toplevel(self)
      transactions_window.title("Transactions for {}".format(customer.name))

      # Create a scrollable list of transactions
      transactions_frame = tk.Frame(transactions_window)
      transactions_frame.pack(fill=tk.BOTH, expand=True)
      scrollbar = tk.Scrollbar(transactions_frame)
      scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
      transactions_list = tk.Listbox(transactions_frame, yscrollcommand=scrollbar.set)
      transactions_list.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
      scrollbar.config(command=transactions_list.yview)

      # Add the customer's transactions to the list
      for transaction in self.transactions:
        if transaction.afm == customer.afm:
          transactions_list.insert(tk.END, "{}: {}".format(transaction.date, transaction.balance))

    # Create the show customer window
    show_customer_window = tk.Toplevel(self)
    show_customer_window.title("Show a customer's information and transactions")

    afm_label = tk.Label(show_customer_window, text="AFM:")
    afm_label.grid(row=0, column=0)
    afm_entry = tk.Entry(show_customer_window)
    afm_entry.grid(row=0, column=1)

    show_transactions_button = tk.Button(show_customer_window, text="Show Transactions", command=show_transactions)
    show_transactions_button.grid(row=1, column=0, columnspan=2)

if __name__ == "__main__":
  main_window = MainWindow()
  main_window.title("Customers")
  main_window.mainloop()
