from django.contrib import admin
from django.contrib.admin.models import LogEntry

LogEntry.objects.all().delete()


from allauth.account.models import EmailAddress, EmailConfirmation


def unregister_admin_model(model):
    try:
        admin.site.unregister(model)
    except admin.sites.NotRegistered:
        pass

unregister_admin_model(EmailAddress)
unregister_admin_model(EmailConfirmation)