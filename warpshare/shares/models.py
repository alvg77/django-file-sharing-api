from django.db import models

# Create your models here.
class Share(models.Model):
    id=models.BigAutoField(primary_key=True, null=False, auto_created=True)
    filepath=models.CharField(max_length=1000, null=False)
    shared_at=models.DateTimeField(auto_now=True)
    sender=models.ForeignKey('users.User', on_delete=models.CASCADE)
    reciever=models.ForeignKey('users.User', on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return f'Share id: {self.id}, title: {self.title}, description: {self.description}, url: {self.url}, image: {self.image}, created_at: {self.created_at}, updated_at: {self.updated_at}, shared_to: {self.shared_to}, shared_from: {self.shared_from}'
    
