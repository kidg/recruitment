# -*- coding: utf-8 -*-
__author__ = 'RedWall'

import csv

from django.core.management import BaseCommand
from interview.models import Candidate

#python manege.py import_candidates --path file.csv

class Command(BaseCommand):
    help = '从一个CSV文件的内容中读取候选人列表，导入到数据库中'

    def add_arguments(self, parser):
        parser.add_argument('--path', type=str)

    def handle(self, *args, **options):
        path = options['path']
        with open(path, 'rt', encoding='gbk') as f:
            reader = csv.reader(f, dialect='excel', delimiter=";")
            for row in reader:
                candidate = Candidate.objects.create(
                    username = row[0]
                )
                print(candidate)