from django.shortcuts import redirect
from dev_core.settings.settings import ADMIN_TEMPLATES

def error_404_view(request, exception):
    # print('Error 404')
    return redirect('/') if ADMIN_TEMPLATES==False else redirect('/admin/login/')