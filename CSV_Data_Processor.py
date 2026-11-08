import csv
from io import StringIO

data = """Employee,Sales
Pujitha,15000
Ravi,20000
Sita,18000
Kiran,12000
Arun,25000
Priya,22000
"""
reader = csv.DictReader(StringIO(data))
sales_values = []
employee_count = 0
for row in reader:
    employee_count += 1
    try:
        sales = float(row["Sales"])

        if sales >= 0:
            sales_values.append(sales)
        else:
            print("Invalid negative sales value")

    except (ValueError, TypeError):
        print("Invalid sales value")
total = sum(sales_values)
average = total / len(sales_values)
highest = max(sales_values)
lowest = min(sales_values)
report = f"""
CSV DATA PROCESSING REPORT
--------------------------
Total Records: {employee_count}
Valid Records: {len(sales_values)}
Total Sales: Rs. {total:.2f}
Average Sales: Rs. {average:.2f}
Highest Sales: Rs. {highest:.2f}
Lowest Sales: Rs. {lowest:.2f}
"""
print(report)
