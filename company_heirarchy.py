from collections import defaultdict
import json
class heirarchy:

    #constructor that receives the contents of the text file. The constructor also initializes a grapgh to hold the mangers and their employees
    def __init__(self,employees):
        self.employees = employees
        self.graph = defaultdict(list)
        self.map = {}
        self.total_salary = 0

    #graph_heir polulates the graph for relationships between managers and employees and sums the total salary of all the employees
    def graph_heir(self):
        for e in self.employees:
            self.map[e['id']] = e['first_name']#creating a map for the ids and firstnames
            self.graph[e['manager']].append(e['id'])#creating the graph with a manger as a key, and a list of the employees under them as the value
            self.total_salary += e['salary'] #summing up all the salaries of all employees

    #print_heirachy prints the employee heirachy tree using BFS
    def print_heirarchy(self):   
        self.graph_heir()#calling the graph_heir function to build a graph for managers and employees

        q = []
        q.append(self.graph[None][0])
        while q:
            emp = q.pop()
            if emp in self.graph:
                print("Manager: ",self.map[emp])
                print("Employees of ",self.map[emp],": ",sorted(list(map(self.map.get,self.graph[emp]))))
                for e in self.graph[emp]:
                    q.append(e) 
        print("Total Salary: ","${:,.2f}".format(self.total_salary))
        
if __name__ == '__main__':
    #reading the file
    file = open("employees.txt",'r')
    employees = file.read()
    #loading the json inside the file
    e_list = json.loads(employees)
    #creating an instance of the heirachy class
    employee_heirarchy = heirarchy(e_list)
    #calling the print_heirachy
    employee_heirarchy.print_heirarchy()
    file.close()

