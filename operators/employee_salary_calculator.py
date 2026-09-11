normal_salary= int(input("Enter the salary of the employee: "))
bonus= int(input("Enter the bonus of the employee: "))
cuts= int(input("Enter the cuts of the employee: "))
total_salary= float(normal_salary) + float(bonus) 
cutting_salary= total_salary - float(cuts)
salary= 0
salary+= normal_salary
salary+= bonus
salary-= cuts
print("The regular salary of the employee is: ", normal_salary)
print("the salary of employee after adding bonus is: ", total_salary)
print("The salary of employee after cutting the cuts is: ", cutting_salary)
print("The final salary of the employee is: ", salary)