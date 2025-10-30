from django.db import models

# data types
#1.string --- gaplar
#2.int === raqamlar
#3.boolen --- true/yoki

class Tovar(models.Model):
    img = models.ImageField(upload_to='media')
    narhi = models.IntegerField()
    tavsifi = models.CharField(max_length=250)
    karta_tolovi = models.IntegerField(null=True)
    orginal = models.BooleanField(default=False)
    super_narh = models.BooleanField(default=False)
    rasm_main = models.ImageField(upload_to='media', null=True) 
    rasm_bir = models.ImageField(upload_to='media', null=True) 
    rasm_ikki = models.ImageField(upload_to='media', null=True)
    rasm_uch = models.ImageField(upload_to='media', null=True)
    rasm_tort = models.ImageField(upload_to='media', null=True)
    rasm_besh = models.ImageField(upload_to='media', null=True)
    rasm_olti = models.ImageField(upload_to='media', null=True)
    rasm_yeti = models.ImageField(upload_to='media', null=True)
    rasm_sakiz = models.ImageField(upload_to='media', null=True)
    rasm_toqiz = models.ImageField(upload_to='media', null=True)
    rasm_on = models.ImageField(upload_to='media', null=True)
   
    def __str__(self):
        return self.tavsifi
    



class Qoshimcha_Tovar(models.Model):
    rasm = models.ImageField(upload_to="media")
    asosiy_narh = models.IntegerField()
    malumot_uchun = models.CharField(max_length=250)
    is_arginal = models.BooleanField(default=False)
    is_karat_narh = models.IntegerField(null=True)
    
    def __str__(self):
        
        return self.malumot_uchun
    