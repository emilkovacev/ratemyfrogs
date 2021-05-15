from django.contrib import admin
from .models import Frog, User

admin.site.register(Frog)
admin.site.register(User)

if __name__ == '__main__':
    load_frogs()

