from django import template

register = template.Library()


from home.models import Profile

def point_rank(points):
    profiles = Profile.objects.all().order_by('-total_points')
    for i in range(1,len(profiles)+1):
        if profiles[i-1].total_points == points:
            return i

register.filter('point_rank', point_rank)