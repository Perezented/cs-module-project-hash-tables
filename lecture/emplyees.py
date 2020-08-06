records = [
    ("Alice", "Engineering"),
    ("Bob", "Sales"),
    ("Carol", "Sales"),
    ("Dave", "Engineering"),
    ("Erin", "Engineering"),
    ("Frank", "Engineering"),
    ("Grace", "Marketing"),
    ("Hank", "Marketing")
]


# dept_indx = {
#     'Sales': ['Bob', 'Carol'],
#     'Marketing': ['Grace'],
#     'Engineering': ['...']
# }
# which employees are in a given department

dept_inx = {}
for name, dept in records:
    if dept not in dept_inx:
        dept_inx[dept] = []
    dept_inx[dept].append(name)


def add_employee(name, dept):
    records.append((name, dept))
    if dept not in dept_inx:
        dept_inx[dept] = []
    dept_inx[dept].append(name)


def emp_by_dept(d):
    #     emp = []

    #     for name, dept in records:
    #         if dept == d:
    #             emp.append(name)

    #     return emp
    return dept_inx[d]


print(dept_inx)

print('')
print('#'*80)
print('')

print('Sales')
print(emp_by_dept('Sales'))
print('')
print('Marketing')
print(emp_by_dept('Marketing'))

add_employee("Hank2", "Marketing")

print('')
print('#'*80)
print('')

print(dept_inx)
