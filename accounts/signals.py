from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import User, StaffProfile, StudentProfile


@receiver(post_save, sender=User)
def create_profile_handler(sender, instance, created, **kwargs):
    if not created:
        return
    # Create the profile object, only if it is newly created
    if instance.is_staff:
        # print('**** Staff is created *****' )
        StaffProfile.staff.get_or_create(user=instance)
    else:
        # print('**** Student is created *****')
        StudentProfile.student.get_or_create(user=instance)


# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     print('****', created)
#     if instance.is_staff:
#         print('**** Staff is created *****' )
#         # StaffProfile.staff.get_or_create(user=instance)
#     else:
#         print('**** Student is created *****')
#         StudentProfile.student.get_or_create(user=instance)


# # post_save.connect(create_user_profile, sender=User)
# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     if instance.is_staff:
#         instance.staffprofile.save()
#     else:
#         instance.studentprofile.save()
