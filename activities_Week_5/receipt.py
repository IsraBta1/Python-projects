""""
BYU - Idaho
CSE 111
Student Name: Israel Betancourt
Receipt Activity
This program reads product information from a CSV file and processes a request for products, calculating the total cost including sales tax. It handles various exceptions that may occur during file operations and data processing.

Enhancement: Added an interactive order entry option so the user can enter products and quantities manually and print a second receipt.
"""

import csv
import sys
import time
from pathlib import Path


def read_dictionary(filename, key_column_index):
    """Read a CSV file into a dictionary using the requested key column."""
    products = {}
    with open(filename, newline='') as csv_file:
        reader = csv.reader(csv_file)
        next(reader, None)
        for row in reader:
            if row:
                key = row[key_column_index]
                products[key] = row
    return products


def get_receipt_lines(order_rows, products_dict, store_name='Isura Store', customer_name=None):
    """Return a list of receipt lines for the given order rows."""
    lines = [store_name]
    if customer_name:
        lines.append(f'Customer: {customer_name}')

    total_items = 0
    subtotal = 0.0

    for product_id, quantity in order_rows:
        product_info = products_dict[product_id]
        product_name = product_info[1]
        price = float(product_info[2])
        total_items += quantity
        subtotal += quantity * price

        lines.append(f'{product_name}: {quantity} @ {price:.2f}')

    sales_tax = subtotal * 0.06
    total = subtotal + sales_tax

    lines.append(f'Number of Items: {total_items}')
    lines.append(f'Subtotal: {subtotal:.2f}')
    lines.append(f'Sales Tax: {sales_tax:.2f}')
    lines.append(f'Total: {total:.2f}')
    lines.append('Thank you for shopping at the Isura Store.')
    lines.append(time.ctime())

    return lines


def safe_filename(text):
    """Return a filename-safe version of the text."""
    safe_text = ''.join(ch if ch.isalnum() else '_' for ch in text.strip())
    return safe_text or 'customer'


def ask_customer_name():
    """Ask the user politely for their name."""
    name = input('Please enter the customer name: ').strip()
    return name if name else None


def print_receipt(order_rows, products_dict, store_name='Isura Store', customer_name=None):
    """Print a receipt for the given order rows."""
    lines = get_receipt_lines(order_rows, products_dict, store_name, customer_name)
    for line in lines:
        print(line)
    return lines


def save_receipt(lines, filename):
    """Save receipt lines to a text file."""
    with open(filename, 'w', encoding='utf-8', newline='') as receipt_file:
        receipt_file.write('\n'.join(lines) + '\n')


def archive_receipt(lines, base_path, prefix='receipt'):
    """Save a receipt to a uniquely named file and append it to a log."""
    timestamp = time.strftime('%Y%m%d_%H%M%S')
    receipt_path = base_path / f'{prefix}_{timestamp}.txt'
    save_receipt(lines, receipt_path)

    log_path = base_path / 'receipt_log.txt'
    with open(log_path, 'a', encoding='utf-8', newline='') as log_file:
        log_file.write('\n'.join(lines) + '\n\n')

    return receipt_path, log_path


def collect_user_order(products_dict):
    """Collect a user order from keyboard input."""
    order_rows = []

    while True:
        product_id = input('Enter product ID for the order (blank to finish): ').strip()
        if product_id == '':
            break

        if product_id not in products_dict:
            print('Unknown product ID. Please try again.')
            continue

        quantity_text = input('Enter quantity for product {}: '.format(product_id)).strip()
        try:
            quantity = int(quantity_text)
            if quantity <= 0:
                raise ValueError
        except ValueError:
            print('Quantity must be a positive integer.')
            continue

        order_rows.append((product_id, quantity))

    return order_rows


def main():
    base_path = Path(__file__).parent
    products_file = base_path / 'products.csv'
    request_file = base_path / 'request.csv'

    try:
        products_dict = read_dictionary(products_file, 0)

        order_rows = []

        with open(request_file, newline='') as request_csv:
            request_reader = csv.reader(request_csv)
            next(request_reader, None)
            for row in request_reader:
                if not row:
                    continue

                product_id = row[0]
                quantity = int(row[1])
                order_rows.append((product_id, quantity))

        lines = print_receipt(order_rows, products_dict)
        receipt_path, log_path = archive_receipt(lines, base_path, prefix='receipt_request')
        print(f'Receipt saved to: {receipt_path}')
        print(f'Receipt log updated: {log_path}')

        if sys.stdin.isatty():
            print()
            response = input('Would you like to enter your own order? (y/n): ').strip().lower()
            if response == 'y':
                customer_name = ask_customer_name()
                user_order = collect_user_order(products_dict)
                if user_order:
                    print()  # blank line between receipts
                    lines = print_receipt(user_order, products_dict, customer_name=customer_name)
                    name_part = safe_filename(customer_name) if customer_name else 'manual'
                    receipt_path, log_path = archive_receipt(lines, base_path, prefix=f'receipt_manual_{name_part}')
                    print(f'Receipt saved to: {receipt_path}')
                    print(f'Receipt log updated: {log_path}')
                else:
                    print('No manual order entered.')

    except FileNotFoundError as err:
        print('Error: missing file')
        print(err)
    except PermissionError as err:
        print('Error: permission denied')
        print(err)
    except KeyError as err:
        print('Error: unknown product ID in the request.csv file')
        print(err)


if __name__ == '__main__':
    main()
