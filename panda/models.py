from django.db import models

class Driver(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField()
    phone = models.TextField()
    address = models.TextField(default="")
    
    def to_object(self):
        return {
            "id": self.id,
            "name": self.name,
            "phone": self.phone,
            "address": self.address
        }

class Van(models.Model):
    id = models.TextField(default="",primary_key=True)
    driver_id = models.ForeignKey(Driver, on_delete=models.CASCADE)
    
    def to_object(self):
        return {
            "id": self.id,
            "driver_id": self.driver_id.to_object()["id"]
        }

class Route(models.Model):
    id = models.AutoField(primary_key=True)
    driver_id = models.ForeignKey(Driver, on_delete=models.CASCADE)
    descr = models.TextField(default="")
    shift = models.TextField(default="")
    company = models.TextField(default="")
    address = models.TextField(default="")

    def to_object(self):
        return {
            "id": self.id,
            "company": self.company,
            "address": self.address,
            "descr": self.descr,
            "shift": self.shift,
            "driver_id": self.driver_id.to_object()["id"]
        }

class Employee(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField()
    shift = models.TextField()
    address = models.TextField(default="")
    company = models.TextField(default="")
    comments = models.TextField(default="")
    phone = models.TextField()
    driver_id = models.ForeignKey(Driver, on_delete=models.CASCADE)
    started_at = models.DateTimeField(auto_now_add=True)
    route_id = models.ForeignKey(Route, on_delete=models.CASCADE)

    def to_object(self):
        return {
            "id": self.id,
            "name": self.name,
            "shift": self.shift,
            "address": self.address,
            "company": self.company,
            "comments": self.comments,
            "phone": self.phone,
            "driver_id": self.driver_id.to_object()["id"],
            "started_at": self.started_at,
            "route_id": self.route_id.to_object()["id"],
        }

class TrainingEmployee(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField()
    shift = models.TextField()
    address = models.TextField(default="")
    company = models.TextField(default="")
    phone = models.TextField()
    contracted = models.BooleanField(default=False)
    
    def to_object(self):
        return {
            "id": self.id,
            "name": self.name,
            "shift": self.shift,
            "address": self.address,
            "company": self.company,
            "phone": self.phone,
            "contracted": self.contracted
        }

