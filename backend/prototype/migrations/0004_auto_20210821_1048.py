# Generated by Django 3.1.7 on 2021-08-21 02:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prototype', '0003_auto_20210821_1044'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questionnaire',
            name='answerTime',
            field=models.TimeField(null=True),
        ),
        migrations.AlterField(
            model_name='questionnaire',
            name='endTime',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='questionnaire',
            name='limitNum',
            field=models.IntegerField(null=True),
        ),
    ]
