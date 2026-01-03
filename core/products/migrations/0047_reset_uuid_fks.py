# Generated migration to fix UUID FK type mismatches
# This migration resets products tables with correct UUID types

from django.db import migrations, models
import django.db.models.deletion
import uuid
import django.utils.timezone
from django.conf import settings
import uuid
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0046_alter_business_uuid_id_alter_category_id_and_more'),
    ]

    operations = [
        # Delete dependent tables first (in reverse dependency order)
        migrations.DeleteModel(
            name='SellerReport',
        ),
        migrations.DeleteModel(
            name='Review',
        ),
        migrations.DeleteModel(
            name='Wishlist',
        ),
        migrations.DeleteModel(
            name='Order',
        ),
        migrations.DeleteModel(
            name='Notification',
        ),
        migrations.DeleteModel(
            name='Product',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='Business',
        ),

        # Recreate with proper UUID types
        migrations.CreateModel(
            name='Business',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('business_name', models.CharField(max_length=255)),
                ('business_description', models.CharField(max_length=255)),
                ('business_contact_number', models.CharField(blank=True, max_length=255)),
                ('business_address', models.CharField(blank=True, max_length=255)),
                ('business_image', models.ImageField(default='default_business_image.png', upload_to='business_image/')),
                ('business_logo', models.ImageField(default='default_business_logo.png', upload_to='business_logo/')),
                ('business_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255, unique=True)),
                ('image', models.ImageField(default='default_category.png', upload_to='product_category/')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('product_name', models.CharField(max_length=255)),
                ('product_measurement', models.CharField(choices=[('Kilo', 'Per Kilo'), ('Gram', 'Per Gram'), ('Kiece', 'Per Piece'), ('Pack', 'Per Pack'), ('Liter', 'Per Liter')], default='Per Kilo', max_length=10)),
                ('product_description', models.TextField()),
                ('product_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('product_stock', models.PositiveIntegerField()),
                ('product_image', models.ImageField(default='default_product.png', upload_to='product_images/')),
                ('product_image1', models.ImageField(default='default_product.png', null=True, upload_to='product_images/')),
                ('product_image2', models.ImageField(default='default_product.png', null=True, upload_to='product_images/')),
                ('product_image3', models.ImageField(default='default_product.png', null=True, upload_to='product_images/')),
                ('product_image4', models.ImageField(default='default_product.png', null=True, upload_to='product_images/')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('product_category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='products', to='products.category')),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='products.business')),
            ],
        ),
        migrations.CreateModel(
            name='Wishlist',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
        migrations.AddConstraint(
            model_name='wishlist',
            constraint=models.UniqueConstraint(fields=('user', 'product'), name='products_wishlist_user_product_unique'),
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('rating', models.PositiveIntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)])),
                ('comment', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='products.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('order_quantity', models.IntegerField(default=1)),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Accepted', 'Accepted'), ('Rejected', 'Rejected')], default='Pending', max_length=20)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('buyer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product')),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('message', models.TextField()),
                ('quantity', models.IntegerField(default=1)),
                ('is_read', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notifications', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['created_at'],
            },
        ),
        migrations.CreateModel(
            name='SellerReport',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('buyer_name', models.CharField(max_length=100)),
                ('buyer_email', models.EmailField(max_length=254)),
                ('seller_name', models.CharField(max_length=100)),
                ('shop_name', models.CharField(max_length=100)),
                ('message', models.TextField()),
                ('evidence_image', models.ImageField(upload_to='evidence_images/')),
                ('submitted_at', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
