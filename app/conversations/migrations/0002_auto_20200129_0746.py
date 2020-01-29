# Generated by Django 2.2.9 on 2020-01-29 07:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('conversations', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='Conversations',
        ),
        migrations.AddField(
            model_name='message',
            name='conversations',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='messages', to='conversations.Conversations'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='conversations',
            name='participants',
            field=models.ManyToManyField(blank=True, related_name='conversation', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='message',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='messages', to=settings.AUTH_USER_MODEL),
        ),
    ]
