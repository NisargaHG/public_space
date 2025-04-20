from django.db import models
from django.contrib.auth.models import User
from datetime import date

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,related_name='profile')
    following = models.ManyToManyField(User, related_name='followed_by_profiles', blank=True)

    posts_today = models.PositiveIntegerField(default=0)
    post_limit_date = models.DateField(default=date.today)

    def reset_post_limit(self):
        """Reset the post limit at the beginning of a new day."""
        if self.post_limit_date != date.today():
            self.posts_today = 0
            self.post_limit_date = date.today()
            self.save()

    def can_post(self):
        """Check if the user can post based on current following count."""
        self.reset_post_limit()  
        following_count = self.following.count()
        if following_count == 2:
            return self.posts_today < 2  
        elif following_count == 0:
            return self.posts_today < 1  
        else:
            return self.posts_today < 5  

    def increment_post_count(self):
        """Increment the count of posts made today."""
        if self.can_post():
            self.posts_today += 1
            self.save()

    @property
    def friends(self):
        """Users that are both following and followed by this user."""
        return self.following.filter(followers=self)


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class Tweet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    rule_type = models.CharField(max_length=50, blank=True, null=True)  

    def __str__(self):
        return f"{self.user.username} - {self.created_at.strftime('%Y-%m-%d %H:%M')}"

class Follow(models.Model):
    follower = models.ForeignKey(User, related_name='followers', on_delete=models.CASCADE)
    followed = models.ForeignKey(User, related_name='following', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
