# SUPERMARKET Management System
def store_item(item):
    while True:
        print('\n**********************')
        print('WELCOME TO SUPERMARKET')
        print('press 1 to view sales')
        print('press 2 to see inventory')
        print('press 3 to buy')
        print('press 4 to exit')
        print('**********************\n')
        
        try:
            menu = int(input('Enter number: '))
        except ValueError:
            print('Invalid input. Please enter a number.')
            continue

        if menu == 1:
            view_sales()
        elif menu == 2:
            display_inventory(item)
        elif menu == 3:
            buy(item)
        elif menu == 4:
            break
        else:
            print('Invalid Number')

def display_inventory(item):
    infile=open(item,'r')
    content = infile.readlines()
    for i in content:
        a = eval(i)
        for x, y in a.items():
            print(x, '= Rs', y[0], ', quantity =', y[1])
            print('__________________________________')
    infile.close()

def buy(item):
    file=open('receipt.txt','r')
    content=file.readline()
    receipt_no=int(content)
    file.close()
    cart = []

    while True:
        product = input('Enter product: ')
        quantity = int(input('Enter quantity: '))
        cart.append((product, quantity))
        user = input('Add more products? (yes/no): ')
        if user.lower() == 'no':
            break

    total_price = 0
    profit = 0

    print('\n---------------------')
    print('      CASH RECEIPT      ')
    print('----------------------')
    print('Receipt number {}:'.format(receipt_no))
    
    file=open(item,'r+')
    lines = file.readlines()

    for product, quantity in cart:
        for i in range(len(lines)):
            dic = eval(lines[i])
            for x, y in dic.items():
                if product.lower() == x:
                    c = input('Do you want to buy {} {}? (yes/no): '.format(quantity, product))
                    if c.lower() == 'yes':
                        print('{} = Rs {}'.format(product, y[0]))
                        print('Quantity = {}'.format(quantity))
                        total = y[0] * quantity
                        print('{} x {} = Rs{}'.format(product, quantity, total))
                        print('Total = Rs {}'.format(total))
                        total_price += total
                        profit=total-(quantity*y[2])
                        sale_tax=(total_price*18)/100
                        net_price=total_price+sale_tax
                        remaining_quantity = y[1] - quantity
                        profit = total - (quantity * y[2])
                        dic[x][1] = remaining_quantity
                        lines[i] = str(dic) + '\n'
                        break  
                    else:
                        break
    file.seek(0)
    file.writelines(lines)
    file.close()
    print('Tax = {}'.format(sale_tax))
    print('---------------------')
    print('Total price = Rs {}'.format(net_price))
    print('T H A N K  Y O U ! :)')
    print('\n')
    sale(receipt_no, cart, total_price, profit,total)
    receipt_no=receipt_no+1
    file=open('receipt.txt','w')
    file.write(str(receipt_no))
    file.close

def sale(receipt_no, cart, total_price, profit,total):
    file=open('sale.txt','a')
    file.write('---------------------\n')
    file.write('      CASH RECEIPT      \n')
    file.write('-----------------------\n')
    file.write('Receipt number: {}\n'.format(receipt_no))

    for product, quantity in cart:
        file.write('Product: {}\n'.format(product))
        file.write('Quantity: {}\n'.format(quantity))
        file.write('{} x {} = Rs{}\n'.format(product, quantity,total))
    
    file.write('Total price: Rs {}\n'.format(total_price))
    file.write('Profit: Rs {}\n'.format(profit))
    file.write('---------------------\n\n')
    file.close()
def view_sales():
    try:
        pas =int(input('Enter password: '))
        if pas ==123: 
            file=open('sale.txt','r')
            content=file.read()
            if not content:
                    print('No sales found')
            else:
                print(content)
    except ValueError as ve:
        print('invalid password',ve)
        
# Driver's code
item = 'item.txt'
store_item(item)
