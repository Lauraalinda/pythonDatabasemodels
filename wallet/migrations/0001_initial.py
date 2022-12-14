# Generated by Django 4.0.6 on 2022-08-01 19:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_type', models.CharField(blank=True, max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Symbol', models.CharField(blank=True, max_length=10)),
                ('name', models.CharField(blank=True, max_length=15)),
                ('country', models.CharField(blank=True, max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=15)),
                ('last_name', models.CharField(blank=True, max_length=15)),
                ('gender', models.CharField(blank=True, max_length=1)),
                ('address', models.TextField()),
                ('age', models.PositiveSmallIntegerField()),
                ('nationality', models.CharField(blank=True, max_length=15)),
                ('id_number', models.CharField(blank=True, max_length=15)),
                ('phone_number', models.CharField(blank=True, max_length=15)),
                ('email', models.EmailField(max_length=254)),
                ('profile_picture', models.ImageField(default=False, upload_to='')),
                ('marital_status', models.CharField(blank=True, max_length=15)),
                ('signature', models.ImageField(default=False, upload_to='')),
                ('employment_status', models.CharField(default=False, max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datecreated', models.DateField(blank=True)),
                ('message', models.CharField(blank=True, max_length=40)),
                ('status', models.BooleanField()),
                ('image', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Third_Party',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(blank=True, max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(blank=True, max_length=20)),
                ('transaction_cost', models.IntegerField(blank=True)),
                ('currency', models.CharField(max_length=20)),
                ('status', models.BooleanField()),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wallet.account')),
            ],
        ),
        migrations.CreateModel(
            name='Wallet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('balance', models.IntegerField(blank=True)),
                ('pin', models.SmallIntegerField(blank=True)),
                ('currency', models.CharField(blank=True, max_length=10)),
                ('active', models.BooleanField()),
                ('datecreated', models.DateTimeField()),
                ('customer', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='wallet.customer')),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction_type', models.CharField(blank=True, max_length=15)),
                ('datetime', models.DateTimeField()),
                ('status', models.BooleanField()),
                ('account_origin', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='wallet.account')),
                ('third_party', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wallet.third_party')),
            ],
        ),
        migrations.CreateModel(
            name='Reward',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('points', models.IntegerField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('transaction', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wallet.transaction')),
                ('wallet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wallet.wallet')),
            ],
        ),
        migrations.CreateModel(
            name='Receipt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(blank=True)),
                ('receipt_file', models.FileField(blank=True, upload_to='')),
                ('transaction', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='wallet.transaction')),
            ],
        ),
        migrations.CreateModel(
            name='Loan_model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('loan_type', models.CharField(blank=True, max_length=15)),
                ('amount', models.IntegerField(blank=True)),
                ('datetime', models.DateTimeField()),
                ('loan_terms', models.CharField(blank=True, max_length=120)),
                ('payment_due_date', models.DateField()),
                ('guaranter', models.CharField(blank=True, max_length=20)),
                ('duration', models.CharField(default=True, max_length=15)),
                ('interest_rate', models.IntegerField()),
                ('balance', models.IntegerField()),
                ('status', models.BooleanField(default=True)),
                ('wallet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wallet.wallet')),
            ],
        ),
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_issued', models.DateTimeField(blank=True)),
                ('card_status', models.BooleanField()),
                ('security_code', models.PositiveSmallIntegerField(blank=True)),
                ('signature', models.ImageField(upload_to='')),
                ('issuer', models.CharField(max_length=20)),
                ('account', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='wallet.account')),
            ],
        ),
        migrations.AddField(
            model_name='account',
            name='account_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wallet.customer'),
        ),
        migrations.AddField(
            model_name='account',
            name='wallet',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wallet.wallet'),
        ),
    ]
