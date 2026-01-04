from .models import UserSubscription

def get_active_subscription(user, plan):
    return UserSubscription.objects.filter(
        user=user,
        plan=plan,
        is_active=True
    ).first()
