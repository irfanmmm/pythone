from django.db import models
import uuid





# choice kodukkan

FAQ_TYPE = {
    ("rent_tracking","Rent Tracking"),
    ("new_deposit","New Deposit "),
    ("existing_deposit","Existing Deposit"),

}



# Create your models here.

# STEP 4 (Creatinga a class)

# (django -> db -> models -> class Model ) ithan recive cheyyunnad
class Testimonial(models.Model):
    # venda datas
    #                  CharField(1 - 255) Comon ayitt varunn value
    name = models.CharField(max_length=255, default="IRFAN")
    designation = models.CharField(max_length=255,)

    #                      TextField(unlimited letters)
    description = models.TextField(blank=True,null=True) # (blank=True,null=True -> empty ayitt send cheyyum [OPTIONAL] )
    image = models.ImageField(upload_to="testimonials/")


    # STEP 11

    # Testimonial object (4) -> name konduvaran an e function eyudunnad
    def __str__(self) :
        # string matrame retur cheyyu incase a number [str(self.number)]
        return self.name




# STEP 5 
# terminal 

# python manage.py makemigrations


# STEP 6 (Data Basilekk mattan)

# terminal 

# python manage.py migrate


# STEP 7 

# Open SQLlite3 


# STEP 8

# terminal

# python manage.py createsuperuser

# creat username & password


# STEP 9

# Login admin panal (http://127.0.0.1:8000/admin/)


# IMAGE UPLOAD CHEYYAN

class Promoters(models.Model):
    #                                      
    name = models.CharField(max_length=255)
    # IMAGE UPLOAD CHEYYAN
    image = models.ImageField(upload_to="promoters/")

    def __str__(self):
        return self.name

# 1 pip install pillow
# 2 python manage.py makemigrations
# 3 python manage.py migrate


class Faq(models.Model):
    title = models.CharField(max_length=255)
    discription = models.TextField()
    faq_type = models.CharField(max_length=255,choices=FAQ_TYPE)


    def __str__(self):
        return self.title
    

class Subscribe(models.Model):
    # (unique=True) 1 mail 1 pravashyam use chayyan kayiyum
    email = models.EmailField(unique=True)


    def __str__(self):
        return self.email

# class TestMode(models.Model):

#     # Automatically count cheyyan varan an AutoField() [200 cror -> vare kittum]
#     # BigAutoField() [morthan 200cror -> kittum]
#     id = models.BigAutoField()
#     #  normal 1,2,3 count use chayyan eq:[oru listin count chayyan] 

#     #   BigIntegerField() -> morthan 200 cror index available 
#     int = models.BigIntegerField()

#     # 0.1 -> 0.99 use chayyan
#     float = models.FloatField()

#     #  ( max_digit = [12345] digits , decimal_places = 2.22 -> dotin shesham ethrayan )
#     decimal = models.DecimalField(max_digits=5, decimal_places=2)

#     # Boolians add cheyyan (default=True/Fals, null=True = onnumillengilum ) oru check box okke handle chayyan / yes/no qusqions 
#     is_student = models.BooleanField(default=True)
    
#     # Date add cheyyan
#     dob = models.DateField()

#     # Date&Time  add cheyyan
#     date_time = models.DateTimeField()

#     # Time add cheyyan (auto_now_add=True -> eppoyan seve click cheyyunne Atime edukkum)
#     time = models.TimeField(auto_now_add=True)

#     # PDF / MP4 vedeo upload cheyyan 
#     #                   (upload_to="videos/" -> path)
#     video = models.FileField(upload_to="videos/") 

#     #       customerin change cheyyan kayiyatha id an (mostsequerd)
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4,editable=False)

    
class Car(models.Model):
    name = models.CharField(max_length=128)
    color = models.CharField(max_length=128)

    # 2 fieldum connect cheyyan   car deleat akkiyal 2 il nnnum deleat cheyyan (car multiple times creat cheyyam)
    manufacturer = models.ForeignKey("web.Manufacturer", on_delete=models.CASCADE)

    # 1 matrame creat cheyyan kayiyu
    # manufacturer = models.OneToOneField("web.Manufacturer", on_delete=models.CASCADE)

    def __str__(self):
        return self.name



class Manufacturer(models.Model):

    name = models.CharField(max_length=128)
    

    def __str__(self):
        return self.name




class Group(models.Model):
    name = models.CharField(max_length=128)
    
    # Multiple "StudentGroup" il add cheyyan kayiyum
    group = models.ManyToManyField("web.StudentGroup") 

    def __str__(self):
        return self.name

class StudentGroup(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name