from django.db import models

class Account(models.Model):
    login = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=20)
    email = models.CharField(max_length=80, unique=True)
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    title = models.CharField(max_length=50, default="Doctor")

    def __str__(self) -> str:
        return self.title + " " + self.name + " " + self.surname
    
class Location(models.Model):
    city = models.CharField(max_length=20)
    # code = models.CharField(max_length=7)
    # street = models.CharField(max_length=20)
    # houseNo = models.CharField(max_length=2)
    # apartNo = models.CharField(max_length=2)
    # commune = models.CharField(max_length=20)
    # voivodeship = models.CharField(max_length=20)

    def __str__(self) -> str:
        return "city: " + self.city# + " street: " + self.street

class Clinic(models.Model):
    name = models.CharField(max_length=30)
    # phoneNo = models.CharField(max_length=12)
    # NIP = models.CharField(max_length=10)
    # REGON = models.CharField(max_length=9)
    # owner = models.ForeignKey(Account, on_delete=models.CASCADE, verbose_name="Owner")
    location = models.ForeignKey(Location, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return "clinic: " + self.name

class Patient(models.Model):
    pesel = models.CharField(max_length=11, primary_key=True)
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    # gender = models.CharField(max_length=1)
    # birth = models.DateField()
    # location = models.ForeignKey(Location, on_delete=models.CASCADE)
    # phoneNo = models.CharField(max_length=12)
    # NIP = models.CharField(max_length=10)
    # healthNo = models.CharField(max_length=20)
    # added = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name + " " + self.surname
    
class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    clinic = models.ForeignKey(Clinic, on_delete=models.CASCADE)
    date = models.DateTimeField()

