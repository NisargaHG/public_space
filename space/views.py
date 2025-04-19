from django.contrib import messages
from django.shortcuts import redirect
from django.utils.timezone import localtime
from space.models import Tweet, UserProfile, Follow
from django.contrib.auth.decorators import login_required
from datetime import time

@login_required
def post_tweet_view(request):
    if request.method == 'POST':
        content = request.POST.get('content', '').strip()
        if not content:
            messages.error(request, "Tweet content cannot be empty.")
            return redirect('space:post_limit')

        user = request.user
        try:
            user_profile = UserProfile.objects.get(user=user)
        except UserProfile.DoesNotExist:
            messages.error(request, "User profile not found.")
            return redirect('space:post_limit')

        # Fetch relationships
        followers_qs = Follow.objects.filter(followed=user)
        following_qs = Follow.objects.filter(follower=user)

        followers_count = followers_qs.count()
        following_count = following_qs.count()

        
        follower_ids = followers_qs.values_list('follower_id', flat=True)
        following_ids = following_qs.values_list('followed_id', flat=True)
        friends_count = len(set(follower_ids) & set(following_ids))

        now_time = localtime().time()
        today = localtime().date()

        rule_type = None
        tweet_limit = None
        allowed_time = True

        if following_count == 2:
            rule_type = 'two_following_limit'
            tweet_limit = 2


        elif friends_count > 10:
            rule_type = 'unlimited_friend_post'
            tweet_limit = None  

        elif following_count == 0:
            rule_type = 'one_post_time_slot'
            tweet_limit = 1
            
            allowed_time = time(10, 0) <= now_time <= time(10, 30)
            if not allowed_time:
                messages.error(request, "Posting is allowed only between 10:00 AM - 10:30 AM IST.")
                return redirect('space:post_limit')

        else:
            messages.error(request, "Posting is not allowed under current conditions.")
            return redirect('space:post_limit')

        
        tweets_today = Tweet.objects.filter(
            user=user,
            rule_type=rule_type,
            created_at__date=today
        ).count()

        if tweet_limit is not None and tweets_today >= tweet_limit:
            messages.error(request, f"You have reached your daily tweet limit under the '{rule_type}' rule.")
            return redirect('space:post_limit')

        
        Tweet.objects.create(user=user, content=content, rule_type=rule_type)
        messages.success(request, "Tweet posted successfully!")
        return redirect('space:post_limit')

    return redirect('space:post_limit')
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.timezone import localtime
from datetime import time
from space.models import UserProfile, Follow, Tweet

@login_required
def post_limit_view(request):
    user = request.user
    now_time = localtime().time()
    current_time_str = localtime().strftime("%I:%M %p")
    today = localtime().date()

    try:
        profile = UserProfile.objects.get(user=user)
    except UserProfile.DoesNotExist:
        return render(request, 'space/post_limit.html', {
            'followers': 0,
            'following': 0,
            'friends': 0,
            'time': current_time_str,
            'status': "You cannot post right now.",
            'reason': "Profile does not exist."
        })

    
    followers_qs = Follow.objects.filter(followed=user)
   
    following_qs = Follow.objects.filter(follower=user)

    followers_count = followers_qs.count()
    following_count = following_qs.count()

    
    follower_ids = followers_qs.values_list('follower_id', flat=True)
    following_ids = following_qs.values_list('followed_id', flat=True)
    friends_count = len(set(follower_ids) & set(following_ids))

    rule_type = None
    tweet_limit = None
    tweets_today = 0
    can_post = False
    reason = ""

    
    if following_count == 2:
        rule_type = 'two_following_limit'
        tweet_limit = 2
        tweets_today = Tweet.objects.filter(user=user, rule_type=rule_type, created_at__date=today).count()
        can_post = tweets_today < tweet_limit
        reason = f"You follow 2 people. You can post {tweet_limit} times/day. ({tweets_today} posted today)"

    elif friends_count > 10:
        rule_type = 'unlimited_friend_post'
        tweet_limit = None
        can_post = True
        reason = f"You have {friends_count} friends. You can post unlimited times/day."

    
    elif following_count == 0:
        rule_type = 'one_post_time_slot'
        tweet_limit = 1
        allowed_time = time(10, 0) <= now_time <= time(10, 30)
        tweets_today = Tweet.objects.filter(user=user, rule_type=rule_type, created_at__date=today).count()
        can_post = allowed_time and tweets_today < tweet_limit
        if not allowed_time:
            reason = "You can only post between 10:00 - 10:30 AM IST."
        elif tweets_today >= tweet_limit:
            reason = "You have already posted your allowed tweet for today."
        else:
            reason = "You are allowed to post one tweet between 10:00 - 10:30 AM IST."

    else:
        reason = "You are not eligible to post under the current conditions."

    status = "You can post!" if can_post else "You cannot post right now."

    return render(request, 'space/post_limit.html', {
        'followers': followers_count,
        'following': following_count,
        'friends': friends_count,
        'time': current_time_str,
        'status': status,
        'reason': reason
    })
from django.http import HttpResponse

def home(request):
    return HttpResponse("🌌 Welcome to the Public Space app!")
