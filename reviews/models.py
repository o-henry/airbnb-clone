from django.db import models
from core import models as core_models

# Create your models here.


class Review(core_models.TimeStampedModel):

    """ Review Model Definition """

    # 모델에 모든 필드를 만든후 , foreign key가 필요한 필드를 하위에 추가합니다.

    review = models.TextField()
    accuracy = models.IntegerField()
    communication = models.IntegerField()
    cleanliness = models.IntegerField()
    location = models.IntegerField()
    check_in = models.IntegerField()
    value = models.IntegerField()
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    room = models.ForeignKey("rooms.Room", on_delete=models.CASCADE)

    # 연결된 Object에서 value를 얻을 수 있습니다.
    def __str__(self):
        return f"{self.review} - {self.room}"
