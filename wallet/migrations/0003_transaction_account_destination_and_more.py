# Generated by Django 4.0.6 on 2022-08-25 16:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0002_rename_loan_model_loan_rename_symbol_currency_symbol'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='account_destination',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='account_origin', to='wallet.account'),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='account_origin',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='account_destination', to='wallet.account'),
        ),
    ]
