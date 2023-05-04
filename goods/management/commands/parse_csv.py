import csv
import os
from pathlib import Path
from django.db import models
from django.core.management.base import BaseCommand, CommandError

from goods.models import HomeDcor,  HomeDecorDetail

class Command(BaseCommand):
    help = 'Load data from csv'

    def handle(self, *args, **options):

        HomeDcor.objects.all().delete()
        HomeDecorDetail.objects.all().delete()
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
                    price=row[3],
					image=row[4],
					quantity=row[5]
                )
                table1.save()

        with open(str(base_dir) + '/goods/goodfile/HomeDcor_detail.csv', newline='',encoding='ISO-8859-1') as f:
            reader = csv.reader(f, delimiter=",")
            next(reader) # skip the header line
            for row in reader:
                print(row)
                table2 = HomeDecorDetail.objects.create(
					rank=row[0],
					name=row[1],
					price=row[2],
					category=row[3],
					image=row[4],
					quantity=row[5],
					latitude=float(row[6]),
					longitude=float(row[7])
				)

                table2.save()

        print("data parsed successfully")