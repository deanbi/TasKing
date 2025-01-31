# Generated by Django 3.2.2 on 2021-05-06 10:40

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=15)),
                ('description', models.TextField()),
                ('points', models.IntegerField(validators=[django.core.validators.MaxValueValidator(10)])),
                ('assignee', models.ForeignKey(default=None, on_delete=django.db.models.deletion.RESTRICT, related_name='assign', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
