import EmployeeClass as e
import PayrollDeductionClass as p
def main():
    empinstance = e.Employee('Jimmy Smith', int(58475), 'Information Systems','Developer', float(6800.00))
    payrollinstance1 = p.Payroll('food court','8/14/2022',float(22.50),int(39119))
    payrollinstance2 = p.Payroll('gift contriubtion', '8/14/2022', float(25.00), int(58475))
    payrollinstance3 = p.Payroll('food court', '8/17/2022', float(15.25), int(21547))
    payrollinstance4 = p.Payroll('vending machine', '8/22/2022', float(3.00), int(58475))
    payrollinstance5 = p.Payroll('vending machine', '8/5/2022', float(2.75), int(58475))
    total = [payrollinstance1, payrollinstance2, payrollinstance3, payrollinstance4, payrollinstance5]
    salary = empinstance.get_monthlysalary()
    for rec in total:
        if rec.get_employeeid()==empinstance.get_idnumber():
            salary -= rec.get_charge()

    
    #empinstance.get_monthlysalary() - payrollinstance2.get_charge() - payrollinstance4.get_charge() - payrollinstance5.get_charge()
    print('*** Employee Pay ***')
    print('Name:',empinstance.get_name())
    print('ID Number:', empinstance.get_idnumber())
    print('Department:', empinstance.get_department())
    print(f'Gross Pay: {"${:,.2f}".format(empinstance.get_monthlysalary())}')
    print(f'Net Pay: {"${:,.2f}".format(salary)}')
    #format(phone.get_retail_price(), ',.2f'), sep=''
    
main()