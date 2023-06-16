from django.db import models
from ozimiz_hackathon.models import TimestampModel
from django.contrib.auth.models import User
import uuid


STATUS = (
    ('DRAFT', 'Draft'),
    ('CLOSED', 'Closed'),
    ('OPEN', 'Open')
)


class Material(TimestampModel):
    id = models.UUIDField(
         primary_key=True,
         default=uuid.uuid4,
         editable=False
    )
    title = models.CharField(
        max_length=255
    )
    file = models.FileField(
        null=True,
        blank=True,
    )
    course = models.ForeignKey(
        to='Course',
        on_delete=models.CASCADE,
        related_name='materials'
    )

    class Meta:
        verbose_name = 'Материал'
        verbose_name_plural = 'Материалы'
        ordering = ('title',)


class Course(TimestampModel):
    title = models.CharField(
        max_length=255
    )
    description = models.TextField()
    duration = models.SmallIntegerField()
    status = models.CharField(
        max_length=6,
        choices=STATUS
    )
    teacher = models.ForeignKey(
        to=User,
        on_delete=models.PROTECT,
        related_name='courses',
        blank=True,
        null=True
    )
    students = models.ManyToManyField(
        to=User,
        blank=True,
        null=True
    )
    completed_by = models.ManyToManyField(
        to=User,
        through='CourseCompletion',
        related_name='completed_courses'
    )

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'
        ordering = ('title',)


class CourseCompletion(models.Model):
    user = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE
    )
    course = models.ForeignKey(
        to=Course,
        on_delete=models.CASCADE
    )
    completed_at = models.DateTimeField(auto_now_add=True)

