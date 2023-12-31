# Generated by Django 4.2.5 on 2023-09-29 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_faq'),
    ]

    operations = [
        migrations.AddField(
            model_name='testimonial',
            name='image',
            field=models.ImageField(default='abcd', upload_to='testimonials/'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='faq',
            name='faq_type',
            field=models.CharField(choices=[('rent_tracking', 'Rent Tracking'), ('new_deposit', 'New Deposit '), ('existing_deposit', 'Existing Deposit')], max_length=255),
        ),
    ]
