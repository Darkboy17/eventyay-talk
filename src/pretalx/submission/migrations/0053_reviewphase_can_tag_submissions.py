# Generated by Django 3.1 on 2020-10-10 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("submission", "0052_auto_20201010_1307"),
    ]

    operations = [
        migrations.AddField(
            model_name="reviewphase",
            name="can_tag_submissions",
            field=models.CharField(default="never", max_length=12),
        ),
    ]