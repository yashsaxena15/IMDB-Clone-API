from rest_framework.throttling import UserRateThrottle

class CreateReviewThrottle(UserRateThrottle):
    scope = 'review-create'

class ReviewListThrottle(UserRateThrottle):
    scope = 'review-list'