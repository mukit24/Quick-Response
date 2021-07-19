from django import template
from django.db.models import Q
from home.models import Profile
from problems.models import Solution

register = template.Library()


def point_rank(points):
    profiles = Profile.objects.all().order_by('-total_points')
    for i in range(1,len(profiles)+1):
        if profiles[i-1].total_points == points:
            return i

def vote_count(user):
    voter = Solution.objects.filter(author=user)
    total_vote = 0
    for v in voter:
        total_vote+=v.vote
    return total_vote

def star_count(user):
    best_answer = Solution.objects.filter(Q(author=user) & Q(best_answer=True)).count()
    print('yo')
    return best_answer
    

register.filter('point_rank', point_rank)
register.filter('star_count',star_count)
register.filter('vote_count',vote_count)