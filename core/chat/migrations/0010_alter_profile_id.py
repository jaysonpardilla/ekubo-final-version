# Modified: originally toggled `profile.id`; kept as no-op to avoid schema conflicts
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0009_alter_profile_id'),
    ]

    operations = [
        # No-op migration to preserve existing integer PKs and avoid casting errors.
    ]
