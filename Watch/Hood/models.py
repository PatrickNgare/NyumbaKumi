from django.db import models
from django.contrib.auth.models import User





#neigbourhood model
class Neigbourhood(models.Model):
    
    neighbourhood_name=models.CharField(max_length=60)
    neighbourhood_location=models.CharField(max_length=60)
    occupant_count=models.PositiveIntegerField()
    admin=models.ForeignKey(User,null=True,on_delete=models.CASCADE)

    @classmethod
    def create_neigborhood():
        pass

    @classmethod
    def delete_neigborhood():
       pass

    @classmethod
    def  find_neigborhood(neigborhood_id):
        pass

    @classmethod
    def update_neighborhood():
        pass

    @classmethod
    def update_occupants():
        pass

        


class User_profile(models.Model):
    name=models.CharField(max_length=60)
    neigbourhood=models.ForeignKey(Neigbourhood,null=True,on_delete=models.CASCADE)
    email=models.EmailField()
    user_id=models.ForeignKey(User,null=True)


class Business(models.Model):
    Bizname=models.CharField(max_length=60)
    user=models.ForeignKey(User, null=True,on_delete=models.CASCADE)
    neigbourhood=models.ForeignKey(Neigbourhood,on_delete=models.CASCADE)
    biz_email=models.EmailField()
    biz_desc=models.CharField(max_length=100)


    @classmethod
    def create_business():
        pass

    @classmethod
    def delete_business():
        pass

    @classmethod
    def find_business(business_id):
        pass

    @classmethod
    def update_business():
        pass









    
