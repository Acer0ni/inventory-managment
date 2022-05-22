# Generated by Django 4.0.4 on 2022-05-22 20:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Warehouse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.TextField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='item',
            name='amount',
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('item_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stock', to='api.item')),
                ('warehouse_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stock', to='api.warehouse')),
            ],
        ),
        migrations.AddConstraint(
            model_name='stock',
            constraint=models.UniqueConstraint(fields=('item_id', 'warehouse_id'), name='unique location'),
        ),
    ]