from django.core.exceptions import ValidationError
from datetime import date


def validate_image(image):
    file_size = image.file.size
    limit_kb = 150
    if file_size > limit_kb * 1024:
        raise ValidationError(f"Max size of the file is {limit_kb} KB")
    # limit_mb = 8
    # if file_size > limit_mb * 1024 * 1024:
    #    raise ValidationError(f"Max size of the file is {limit_kb} MB")


def validate_age(born):
    today = date.today()
    age = today.year - born.year - \
    ((today.month, today.day) < (born.month, born.day))
    age_limit = 15
    if age < age_limit:
        raise ValidationError(f"Minimum age must be {age_limit} years")



# if __name__ == "__main__":
#     print(validate_age(date(1979, 9, 18)))
