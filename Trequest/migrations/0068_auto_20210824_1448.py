# Generated by Django 3.2.5 on 2021-08-24 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Trequest', '0067_merge_20210824_1448'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='materialrequest',
            name='sent_on',
        ),
        migrations.AlterField(
            model_name='transportrequest',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Approved', 'Approved'), ('Expired', 'Expired'), ('Rejected', 'Rejected'), ('Cancelled', 'Cancelled')], default='Pending', max_length=200),
        ),
        migrations.AlterField(
            model_name='transportrequest',
            name='status2',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Approved', 'Approved'), ('Expired', 'Expired'), ('Rejected', 'Rejected'), ('Cancelled', 'Cancelled')], default='Pending', max_length=200),
        ),
        migrations.AlterField(
            model_name='transportrequest',
            name='status3',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Approved', 'Approved'), ('Expired', 'Expired'), ('Rejected', 'Rejected'), ('Cancelled', 'Cancelled')], default='Pending', max_length=200),
        ),
    ]
