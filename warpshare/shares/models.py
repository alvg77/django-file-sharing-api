from django.db import models

# Create your models here.
class Share(models.Model):
    id=models.BigAutoField(primary_key=True, null=False, auto_created=True)
    filename=models.CharField(max_length=1000, null=False)
    url=models.CharField(max_length=2048, null=False, blank=False)
    created_at=models.DateTimeField(auto_now_add=True)
    shared_at=models.DateTimeField(auto_now=True)
    shared_to=models.ForeignKey('users.User', on_delete=models.CASCADE)
    shared_from=models.ForeignKey('users.User', on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return f'Share id: {self.id}, title: {self.title}, description: {self.description}, url: {self.url}, image: {self.image}, created_at: {self.created_at}, updated_at: {self.updated_at}, shared_to: {self.shared_to}, shared_from: {self.shared_from}'
    
