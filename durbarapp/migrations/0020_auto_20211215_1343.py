# Generated by Django 2.0.3 on 2021-12-15 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('durbarapp', '0019_merchantorder_order_absent_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='merchantorder',
            name='order_track',
            field=models.CharField(blank=True, choices=[('1', 'pending'), ('2', 'assign_for_pick'), ('3', 'picked'), ('4', 'hub_collected_for_ware_house'), ('5', 'in_transit'), ('6', 'hub_collected_for_delevery'), ('7', 'assign_for_delevery'), ('8', 'shiping'), ('9', 'delivered'), ('10', 'hold'), ('11', 'return_pending'), ('12', 'return_to_hub_for_ware_house '), ('13', 'hub_returned_to_ware_house'), ('14', 'return_to_hub'), ('15', 'assign_for_return'), ('16', 'picked_for_return'), ('17', 'return_to_merchent'), ('18', 'canceled'), ('19', 'picking_hold'), ('20', 'order_absent'), ('21', 'rider_cancel')], default='1', max_length=3),
        ),
    ]
