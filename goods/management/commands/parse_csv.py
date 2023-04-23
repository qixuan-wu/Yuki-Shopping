import csv
import os
from pathlib import Path
from django.db import models
from django.core.management.base import BaseCommand, CommandError

from goods.models import HomeDcor, HomeFurnishing, HomeImprovement

class Command(BaseCommand):
    help = 'Load data from csv'

    def handle(self, *args, **options):

        HomeDcor.objects.all().delete()
        HomeFurnishing.objects.all().delete()
        HomeImprovement.objects.all().delete()
        print("tables dropped successfully")

        base_dir = Path(__file__).resolve().parent.parent.parent.parent
        with open(str(base_dir) + '/goods/goodfile/HomeDcor.csv', newline='',encoding='ISO-8859-1') as f:

            reader = csv.reader(f, delimiter=",")
            next(reader) # skip the header line
            for row in reader:
                print(row)
                table1 = HomeDcor.objects.create(
                    rank=row[0],
                    name=row[1],
                    ratings=row[2],
                    price=row[3]
                )
                table1.save()
        
        with open(str(base_dir) + '/goods/goodfile/HomeFurnishing.csv', newline='',encoding='ISO-8859-1') as f:
            reader = csv.reader(f, delimiter=",")
            next(reader) # skip the header line
            for row in reader:
                print(row)
                table2 = HomeFurnishing.objects.create(
                    rank=row[0],
                    name=row[1],
                    ratings=row[2],
                    price=row[3]
                )
                table2.save()

        with open(str(base_dir) + '/goods/goodfile/HomeImprovement.csv', newline='',encoding='ISO-8859-1') as f:
            reader = csv.reader(f, delimiter=",")
            next(reader) # skip the header line
            for row in reader:
                print(row)
                table3 = HomeImprovement.objects.create(
                    rank=row[0],
                    name=row[1],
                    ratings=row[2],
                    price=row[3]
                )
                table3.save()
        print("data parsed successfully")
