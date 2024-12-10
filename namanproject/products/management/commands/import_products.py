import csv
from django.core.management.base import BaseCommand
from products.models import Product
from datetime import datetime

class Command(BaseCommand):
    help = 'Import products from CSV Files database'

    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str, help='The path to the CSV file to import')

    def handle(self, *args, **kwargs):
        file_path = "Please provide File of CSV Path here"
        try:
            with open(file_path, mode='r') as file:
                reader = csv.DictReader(file)
                products = []
                skipped_rows = 0

                for row in reader:
                    try:
                        name = row['name']
                        category = row['category']
                        price = float(row['price'])
                        stock = int(row['stock'])
                        created_at = datetime.strptime(row['created_at'], '%Y-%m-%dT%H:%M:%S')

                        if not name or not category or price < 0 or stock < 0:
                            self.stderr.write(f'Invalid data: {row}')
                            skipped_rows += 1
                            continue

                        products.append(Product(
                            name=name,
                            category=category,
                            price=price,
                            stock=stock,
                            created_at=created_at
                        ))
                        

                    except (ValueError, KeyError) as e:
                        self.stderr.write(f'Error in processing row: {row}, {e}')
                        skipped_rows += 1
                print(products)        
                    
                if products:  # Only bulk insert if there are products to insert
                    Product.objects.bulk_create(products)
                    self.stdout.write(self.style.SUCCESS(f'Successfully imported {len(products)} products'))
                if skipped_rows > 0:
                    self.stdout.write(self.style.WARNING(f'Skipped {skipped_rows} rows due to errors'))

        except FileNotFoundError:
            self.stderr.write('File not found')
