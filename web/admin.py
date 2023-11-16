from django.contrib import admin
from web.models import Testimonial, Promoters,Faq,Subscribe,Car,Manufacturer,Group,StudentGroup

# Register your models here.


# STEP 12
# Order cheyyan
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'designation', 'description','image')



# STEP 10

# testimonial import cheyyuga (modelinullil eyudiya class)
admin.site.register(Testimonial,TestimonialAdmin)


class PromoterAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'image')


admin.site.register(Promoters,PromoterAdmin)

# list shapil display cheyyana an
class FaqAdmin(admin.ModelAdmin):
    list_display = ('id','title', 'faq_type','discription')


admin.site.register(Faq,FaqAdmin)

admin.site.register(Subscribe)

admin.site.register(Car)

admin.site.register(Manufacturer)

admin.site.register(Group)

admin.site.register(StudentGroup)




