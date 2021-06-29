from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Userprofile(models.Model):
    class Meta:
        verbose_name_plural = "Userprofiles"

    BASIC = "basic"
    PRO = "pro"
    CHOICES_PLANS = (
        (BASIC, "Basic"),
        (PRO, "Pro")
    )

    user = models.OneToOneField(User, related_name="userprofile", on_delete=models.CASCADE)
    plan = models.CharField(max_length=20, choices=CHOICES_PLANS, default=BASIC)

    def category_limit(self):
        if self.plan == Userprofile.BASIC:
            return 5
        elif self.plan == Userprofile.PRO:
            return 50

    def category_count(self):
        print(self.user.categories.count())
        return self.user.categories.count()

    def bookmark_limit(self):
        if self.plan == Userprofile.BASIC:
            return 5
        elif self.plan == Userprofile.PRO:
            return float("inf")

    def bookmark_count(self):
        return self.user.bookmarks.count()