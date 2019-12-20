from django.db import models


class PersonManagerUsedWithoutCompany(Exception):
    pass


class PersonManager(models.Manager):

    def get_queryset(self):
        raise PersonManagerUsedWithoutCompany

    def with_company(self, company):
        return super().get_queryset().filter(company=company)
