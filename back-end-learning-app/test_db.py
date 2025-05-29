import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dev_core.settings.settings')
django.setup()

import subprocess


class TestDB:
    prefix_cmd = 'python manage.py loaddata'
    
    list_data = {
        #* Course <- Category | Extent | Course
        'course': {
            'extent': f'{prefix_cmd} backup/data/extents.json',
            'course': f'{prefix_cmd} backup/data/courses.json',
        },
        #* Course <- Lesson
        'lesson': {
            'python': f'{prefix_cmd} backup/data/lessons.json',
        },
        #* Course <- Lesson <- Detail Lesson
        'detail_lesson': {
            'python': f'{prefix_cmd} backup/data/detaillessons.json',
        },
        #* User -> Userrole <- Role
        'user': {
            'role': f'{prefix_cmd} backup/data/roles.json',
            'user': f'{prefix_cmd} backup/data/users.json',
            'userrole': f'{prefix_cmd} backup/data/userroles.json',
        }
    }

    list_run_cmd = [
        #* Role
        f'{prefix_cmd} backup/data/roles.json', 
        #* User
        f'{prefix_cmd} backup/data/users.json',
        #* User -> Userrole <- Role
        f'{prefix_cmd} backup/data/userroles.json',
        #* Extent
        f'{prefix_cmd} backup/data/extents.json',
        #* Course - Category | Extent
        f'{prefix_cmd} backup/data/courses.json',
        #* Lesson <- Course
        f'{prefix_cmd} backup/data/lessons.json',
        #* Course <- Lesson <- Detail Lesson
        f'{prefix_cmd} backup/data/detaillessons.json',
    ]
    

    @staticmethod
    def create_all_data():
        for cmd in TestDB.list_run_cmd:
            subprocess.run(cmd)

    @staticmethod
    def create_one_data(path_cmd):
        subprocess.run(path_cmd)

if __name__ == '__main__':
    TestDB.create_all_data()