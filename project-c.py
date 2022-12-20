def create_customer():
  name = raw_input("Enter the customer's name: ")
  afm = raw_input("Enter the customer's AFM: ")
  address = raw_input("Enter the customer's address: ")
  phone = raw_input("Enter the customer's phone: ")

  with open("customers.txt", "a") as f:
    f.write("{},{},{},{}\n".format(name, afm, address, phone))

def update_customer():
  afm = raw_input("Enter the AFM of the customer you want to update: ")

  with open("customers.txt", "r") as f:
      
    lines = f.readlines()

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
    print "No customer with AFM {} was found.", afm

def show_customer():
  afm = raw_input("Enter the AFM of the customer you want to see: ")

  with open("customers.txt", "r") as f:
    lines = f.readlines()

  found = False
  for line in lines:
    if line.split(",")[1] == afm:
      name, afm, address, phone = line.split(",")
      print "Name: ", name
      print "AFM: ", afm
      print "Address: ", address
      print "Phone: ", phone
      found = True
      break

  if not found:
    print "No customer with this AFM was found."

  with open("transactions.txt", "r") as f:
    lines = f.readlines()

  print "Transactions:"
  for line in lines:
    if line.split(",")[0] == afm:
        afm, date, name, balance = line.split(",")
        print date + " " + name + " " + afm + " " + balance
      #print "- " date, " ", name, " ", afm, " ", balance #.format(date, name, afm, balance))
        
def main():
  while True:
    print "1. Create a new customer"
    print "2. Update a customer's information"
    print "3. Show a customer's information and transactions"
    print "4. Quit"
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
      print "Invalid option. Please try again."

main()
