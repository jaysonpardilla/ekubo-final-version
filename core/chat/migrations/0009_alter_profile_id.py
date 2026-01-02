# Modified: original migration attempted to change `profile.id` to UUID which
# fails on existing Postgres data (bigint -> uuid conversion). This project
# uses a safe migration strategy: `0002` adds a `uuid_id` column and
# backfills UUIDs. Keep this migration as a no-op to avoid casting errors.

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0008_alter_customuser_is_seller'),
    ]

    operations = [
        # No-op: handled by 0002 safe migration which adds `uuid_id`.
    ]
