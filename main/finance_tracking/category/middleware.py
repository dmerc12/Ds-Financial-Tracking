import logging
from django.urls import reverse
from django.contrib import messages
from urllib.parse import urlparse

from ..models import Category

class CategoryMiddleware:

    @staticmethod
    def update_category(request, form, category):
        logging.info('Beginning middleware method update category')
        category = Category.objects.get(pk=category.pk)
        category.name = form.cleaned_data['name']
        category.group = form.cleaned_data['group']
        category.save()
        logging.info('Finishing middleware method update category')
        messages.success(request, 'Category successfully updated!')

    @staticmethod
    def delete_category(request, category):
        logging.info('Beginning middleware method delete category')
        category.delete()
        logging.info('Finishing middleware method delete category')
        messages.success(request, 'Category successfully deleted!')
