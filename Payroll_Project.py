# Edmond Cheung, BSAN 3##
# Problem 8

class Employee:
	# An employee
	def __init__(self):
		 self.name = ""
		 self.employeeType = ""
		 self.hoursWorked = 0
		 self.payRate = 0

	def employeeNameSet(self, name):	
		# employeeNameSet checks if the name the user entered is valid. If it is, it sets the name. If not, it asks a valid name before it sets the name.
		self.name = name
		if name == "":
			validEmployeeName = 0
		else:
			validEmployeeName = 1
		while validEmployeeName == 0:
			print("Invalid name entered.")
			self.name = input("What is the employee's name? ")
			if self.name == "":
				print("Invalid name entered.")
			else:
				validEmployeeName = 1
	
	def employeeTypeSet(self):
		# Asks for the type of employee (salaried or hourly). It cleans user input in case the user forgot to capitalize, and it continues to run until the user enters a valid response.
		validEmployeeType = 0
		self.employeeType = str()
		while validEmployeeType == 0:
			employeeType = input("Enter employee's classification (Salaried or Hourly): ")
			employeeType = employeeType.capitalize()
			if employeeType ==  "Salaried" or employeeType == "Hourly":
				validEmployeeType = 1
				self.employeeType = employeeType
			else:
				print("Invalid employee type.")

	def payRateSet(self):
		# Depending on the type of employee, payRateSet requests the salary or hourly wage. Both are stored in the same variable.
		payRateValid = 0
		while payRateValid == 0:
			try:
				if self.employeeType == "Salaried":
					self.payRate = input("Enter weekly salary: ")
				else:
					self.payRate = input("Enter hourly wage: ")	
				self.payRate = float(self.payRate)
				payRateValid = 1		
			except ValueError:
				print("You did not enter valid pay rate.\n")
		
	def hoursWorkedSet(self):
		# Asks for the number of hours worked by the employee.
		validHoursWorked = 0
		hoursWorked = float()
		while validHoursWorked == 0:
			try:
				self.hoursWorked = float(input("Enter the number of hours worked: "))
				validHoursWorked = 1
			except ValueError:
				print("You did not enter a valid number of hours worked.\n")

class SalariedEmployee(Employee):
	# For salaried employees. It sets the weekly salary as the employee's pay.
	def __init__(self):
		self.pay = 0
	
	def calculatePay(self):
		self.pay = self.payRate

class HourlyEmployee(Employee):
	# For hourly employees. It calculates the employee's pay and sets it as the employee's pay.
	def __init__(self):
		self.pay = 0	
	
	def calculatePay(self):
		self.pay = self.payRate * self.hoursWorked

def printSummary():
# Prints out employee name and employee pay followed by summary information 
	print("\nEmployee Payroll:")				
	payrollTotal = 0
	hoursTotal = 0	
	averageHours = 0
	for person in employeeList:
		print(person.name + ": $" + str(person.pay))
		payrollTotal = payrollTotal + person.pay
		hoursTotal = hoursTotal + person.hoursWorked
	averageHours = hoursTotal / len(employeeList)
			
	print("\n" + "Number of employees:", totalEmployees)
	print("Number of salaried employees:", sEmployees)
	print("Total payroll: $" + str(payrollTotal))
	print("Average number of hours worked per employee:", str(averageHours), "\n")

selection = int() # Users enter 1, 2, or 3 depending on what menu option they want
employee = "" # Placeholder to be used for an Employee object.
employeeList = list() # List that holds the Employee objects
sEmployees = 0 # Count of the number of salaried employees
totalEmployees = 0 # Count of the total number of employees

while True:
	print("Main menu.")
	print("To enter information for employees, type 1.")
	print("To view employee information, type 2.")
	print("To exit, type 3.")
	selection = input()
	
	if selection == "1":
		print("You selected 1. \n")
		addingEmployees = 1
		while addingEmployees == 1:
			employeeName = input("What is the employee's name? ")
			employee = Employee()
			employee.employeeNameSet(employeeName) # Checks whether the name is valid
			employeeName = employee.name
			employee.employeeTypeSet()
			
			if employee.employeeType == "Salaried":
				employee = SalariedEmployee()
				employee.employeeNameSet(employeeName) # Sets the employee name
				employee.employeeType = "Salaried" # Sets the employee type in the new instance
			else:
				employee = HourlyEmployee()
				employee.employeeNameSet(employeeName) # Sets the employee name
				employee.employeeType = "Hourly" # Sets the employee type in the new instance
			
			# Asks for the number of hours worked and the pay rate. Then, it calculates the employee's pay
			employee.hoursWorkedSet()
			employee.payRateSet()
			employee.calculatePay()

			if employee.employeeType == "Salaried":
				sEmployees = sEmployees + 1
				totalEmployees = totalEmployees + 1
			else:
				totalEmployees = totalEmployees + 1
			employeeList.append(employee)
			
			# After each employee's info is entered, it asks whether the user wants to continue
			done = input("\nDo you want to continue adding employees? (Y/N)? ")
			done = done.upper()
			if done == "Y":
				continue
			elif done == "N":
				addingEmployees = 0
		printSummary()

	elif selection == "2":
		print("You selected 2. \n")
		# Checks first to see if there is employee info. Then, it prints out employee name and employee pay followed by summary information. 	
		if len(employeeList) == 0:
			print("No employee info found. Please enter employee info first.\n")
			continue
		printSummary()
		
	elif selection == "3":
		print("You selected 3. \n")
		print("Goodbye.")
		quit()
	
	else:
		# In case users don't enter a "1", "2", or "3"
		print("Please enter a 1, 2, or 3.\n")
