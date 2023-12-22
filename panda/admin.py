from django.contrib import admin
from .models import Driver, Van, Route, Employee, TrainingEmployee

admin.site.register(Driver)
admin.site.register(Van)
admin.site.register(Route)
admin.site.register(Employee)
admin.site.register(TrainingEmployee)
