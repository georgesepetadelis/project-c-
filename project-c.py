# Customer list program

# Function to create a new customer
def create_customer():
  name = raw_input("Enter the customer's name: ")
  afm = raw_input("Enter the customer's AFM: ")
  address = raw_input("Enter the customer's address: ")
  phone = raw_input("Enter the customer's phone: ")

  # Add the new customer to the customers.txt file
  with open("customers.txt", "a") as f:
    f.write("{},{},{},{}\n".format(name, afm, address, phone))

# Function to update a customer's information by AFM
def update_customer():
  afm = raw_input("Enter the AFM of the customer you want to update: ")

  # Read all the lines in the customers.txt file
  with open("customers.txt", "r") as f:
    lines = f.readlines()

  # Find the line with the matching AFM and update it
  found = False
  with open("customers.txt", "w") as f:
    for line in lines:
      if line.split(",")[1] == afm:
        name = raw_input("Enter the updated name: ")
        address = raw_input("Enter the updated address: ")
        phone = raw_input("Enter the updated phone: ")
        f.write("{},{},{},{}\n".format(name, afm, address, phone))
        found = True
      else:
        f.write(line)

  if not found:
    print("No customer with AFM {} was found.".format(afm))

# Function to show a customer's information and transactions
def show_customer():
  afm = raw_input("Enter the AFM of the customer you want to see: ")

  # Read all the lines in the customers.txt file
  with open("customers.txt", "r") as f:
    lines = f.readlines()

  # Find the line with the matching AFM and print it
  found = False
  for line in lines:
    if line.split(",")[1] == afm:
      name, afm, address, phone = line.split(",")
      print("Name: {}".format(name))
      print("AFM: {}".format(afm))
      print("Address: {}".format(address))
      print("Phone: {}".format(phone))
      found = True
      break

  if not found:
    print("No customer with AFM {} was found.".format(afm))

  # Read all the lines in the transactions.txt file
  with open("transactions.txt", "r") as f:
    lines = f.readlines()

  # Find all the transactions for the customer with the matching AFM and print them
  print("Transactions:")
  for line in lines:
    if line.split(",")[0] == afm:
      date, name, afm, balance = line.split(",")
      print("{} - {} - {} - {}".format(date, name, afm, balance))

# Main function
def main():
  while True:
    print("1. Create a new customer")
    print("2. Update a customer's information")
    print("3. Show a customer's information and transactions")
    print("4. Quit")
    option = raw_input("Enter an option: ")

    if option == "1":
      create_customer()
    elif option == "2":
      update_customer()
    elif option == "3":
      show_customer()
    elif option == "4":
      break
    else:
      print("Invalid option. Please try again.")

# Call the main function
main()