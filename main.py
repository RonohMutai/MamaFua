import csv

# Read data from file
with open('mama_fua_data.csv', 'r') as f:
    reader = csv.DictReader(f)
    data = [row for row in reader]

# Initialize variables for totals
total_income = 0
total_laundry = 0
total_cleaning = 0

# Group data by customer and service type
customer_data = {}
for row in data:
    customer = row['customer_name']
    service = row['service_type']
    quantity = int(row['quantity'])
    price = float(row['price'])
    if customer not in customer_data:
        customer_data[customer] = {'laundry': 0, 'cleaning': 0, 'total': 0}
    if service == 'laundry':
        customer_data[customer]['laundry'] += quantity * price
        total_laundry += quantity * price
    elif service == 'cleaning':
        customer_data[customer]['cleaning'] += quantity * price
        total_cleaning += quantity * price
    customer_data[customer]['total'] += quantity * price
    total_income += quantity * price

# Write report to file
with open('mama_fua_report.txt', 'w') as f:
    f.write('Mama Fua Allocation Report\n\n')
    f.write('Total Income: KES {:.2f}\n\n'.format(total_income))
    f.write('Laundry Income: KES {:.2f}\n'.format(total_laundry))
    f.write('Cleaning Income: KES {:.2f}\n\n'.format(total_cleaning))
    f.write('Customer Breakdown:\n\n')
    for customer, customer_totals in customer_data.items():
        f.write('{}:\n'.format(customer))
        f.write('\tLaundry Income: KES {:.2f}\n'.format(customer_totals['laundry']))
        f.write('\tCleaning Income: KES {:.2f}\n'.format(customer_totals['cleaning']))
        f.write('\tTotal Income: KES {:.2f}\n\n'.format(customer_totals['total']))

