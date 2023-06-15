class Employee:

    def __init__(self, name, number):
        
        self.__employee_name = name
        self.__employee_number = number

    def set_employeeName(self, x):
        
        self.__employee_name = x
    
    def set_employeeNumber(self, x):

        self.__employee_number = x
    
    def get_employeeName(self):
        
        return self.__employee_name
    
    def get_employeeNumber(self):

        return self.__employee_number
    
class ProductionWorker(Employee):

    def __init__(self, name, number, shift_number, hourly_pay):
        super().__init__(name, number)
        self.__shift_number = shift_number
        self.__hourly_pay = hourly_pay

    def set_shiftNumber(self, x):
        
        self.__shift_number = x
    
    def set_hourly_pay(self, x):

        self.__hourly_pay = x
    
    def get_shiftNumber(self):
        
        return self.__shift_number
    
    def get_hourlyPay(self):

        return self.__hourly_pay
    
name = input("Enter your name: ")
idNUm = input("Enter your employee number: ")
shift = input("Enter your shift (Day or Night): ")
hourlyPay = input("Enter your hourly pay: ")

shift = shift.upper()
shiftNum = 0

if(shift == "DAY"):
    shiftNum = 1

if(shift == "NIGHT"):
    shiftNum = 2

Worker = ProductionWorker(name, idNUm, shiftNum, hourlyPay)

print("")
print("Your Information")
print("Employee Name: ", Worker.get_employeeName())
print("Employee Number: ", Worker.get_employeeNumber())
print("Shift Number: ", Worker.get_shiftNumber())
print("Hourly Pay: ", Worker.get_hourlyPay())
