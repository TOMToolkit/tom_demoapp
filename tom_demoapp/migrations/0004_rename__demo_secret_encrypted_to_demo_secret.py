"""Rename _demo_secret_encrypted -> demo_secret and convert to EncryptedModelField.

Replaces the descriptor pattern (BinaryField + EncryptedProperty) with a
single EncryptedModelField that Django introspects as a normal field.
The underlying column stays a BinaryField at the SQL level — no data
migration is needed because the Fernet ciphertext format is unchanged.
"""

from django.db import migrations

import tom_common.encryption


class Migration(migrations.Migration):

    dependencies = [
        ('demoapp', '0003_remove_demoprofile_demo_secret_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='demoprofile',
            old_name='_demo_secret_encrypted',
            new_name='demo_secret',
        ),
        migrations.AlterField(
            model_name='demoprofile',
            name='demo_secret',
            field=tom_common.encryption.EncryptedModelField(blank=True, null=True),
        ),
    ]
