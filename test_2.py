
"""
This program will display the class exam averages based on the total number of grades. The first calculation will display the number of grades.
The second calculation will display the average of the total grades. The third calculation will display the total percentage of the grades abover average. 
There will be three functions. The first function will initialize the apllication. The second function will calcualte the total percentage above average. 
The third function will calculate the percentage of total grades above average. 

Function 1 will initialize the application.
Function 2 will sum all the total number of grades.
Function 3 will multiply all of the grades by 100 and divide it by the total number of grades. 

It will output the percentage above average. And after the code has ran, it will output the percentage of the total grades above average. 

"""

"""
# funtion1
add total number of grades

# function2
add sum of all grades / total number of grades

# function3 
n*100 / len(grades)

main
"""
infile = open("Final.txt" , 'r')
grades = [line.rstrip() for line in infile]
infile.close()
for i in range(len(grades)):
    grades[i] = int(grades[i])
average = sum(grades) / len(grades)
num = 0
for grade in grades:
    if grade > average:
        num += 1
print("Number of grades:" , len(grades))
print("Average grade:" , average)
print("Percentage of grades above average: {0:.2f}%"
                    .format(100 * num / len(grades)))
