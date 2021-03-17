# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2021-03-17 10:57
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CommentModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_date', models.DateTimeField(auto_now_add=True)),
                ('description', models.TextField(max_length=1500, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TicketModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=2000)),
                ('views', models.IntegerField(default=0)),
                ('upvotes', models.IntegerField(default=0)),
                ('edited_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('total_donations', models.IntegerField(default=0)),
            ],
            options={
                'ordering': ('-upvotes',),
            },
        ),
        migrations.CreateModel(
            name='TicketStatusModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ticket_status', models.CharField(choices=[('Open', 'Open'), ('Working On', 'Working On'), ('Closed', 'Closed')], max_length=11, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='TicketTypeModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ticket_type', models.CharField(choices=[('Bug', 'Bug'), ('Feature', 'Feature')], max_length=7, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='UpvoteModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ticket', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='tickets.TicketModel')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='ticketmodel',
            name='ticket_status',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='tickets.TicketStatusModel'),
        ),
        migrations.AddField(
            model_name='ticketmodel',
            name='ticket_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='tickets.TicketTypeModel'),
        ),
        migrations.AddField(
            model_name='ticketmodel',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='commentmodel',
            name='ticket',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='tickets.TicketModel'),
        ),
        migrations.AddField(
            model_name='commentmodel',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
