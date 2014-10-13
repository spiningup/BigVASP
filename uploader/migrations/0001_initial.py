# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('docfile', models.FileField(upload_to=b'documents/%Y/%m/%d')),
                ('ISPIN', models.IntegerField(null=True)),
                ('IBRION', models.IntegerField(null=True)),
                ('ISIF', models.IntegerField(null=True)),
                ('ISYM', models.IntegerField(null=True)),
                ('LDAUTYPE', models.IntegerField(null=True)),
                ('IALGO', models.IntegerField(null=True)),
                ('NBANDS', models.IntegerField(null=True)),
                ('ISMEAR', models.IntegerField(null=True)),
                ('IDIPOL', models.IntegerField(null=True)),
                ('NFREE', models.IntegerField(null=True)),
                ('ICORELEVEL', models.IntegerField(null=True)),
                ('I_CONSTRAINED_M', models.IntegerField(null=True)),
                ('VOSKOWN', models.IntegerField(null=True)),
                ('NKREDX', models.IntegerField(null=True)),
                ('NKREDY', models.IntegerField(null=True)),
                ('NKREDZ', models.IntegerField(null=True)),
                ('NOMEGA', models.IntegerField(null=True)),
                ('EDIFF', models.FloatField(null=True)),
                ('EDIFFG', models.FloatField(null=True)),
                ('ENCUT', models.FloatField(null=True)),
                ('SIGMA', models.FloatField(null=True)),
                ('NELECT', models.FloatField(null=True)),
                ('NUPDOWN', models.FloatField(null=True)),
                ('EPSILON', models.FloatField(null=True)),
                ('EFIELD', models.FloatField(null=True)),
                ('PSTRESS', models.FloatField(null=True)),
                ('AEXX', models.FloatField(null=True)),
                ('HFSCREEN', models.FloatField(null=True)),
                ('CSHIFT', models.FloatField(null=True)),
                ('OMEGAMAX', models.FloatField(null=True)),
                ('ENCUTGW', models.FloatField(null=True)),
                ('volume', models.FloatField(null=True)),
                ('e_wo_entrp', models.FloatField(null=True)),
                ('efermi', models.FloatField(null=True)),
                ('GGA', models.CharField(max_length=20, null=True)),
                ('PRECFOCK', models.CharField(max_length=20, null=True)),
                ('LOPTICS', models.BooleanField(default=False)),
                ('LPEAD', models.BooleanField(default=False)),
                ('LMETAGGA', models.BooleanField(default=False)),
                ('LDAU', models.BooleanField(default=False)),
                ('LNONCOLLINEAR', models.BooleanField(default=False)),
                ('LSORBIT', models.BooleanField(default=False)),
                ('LDIPOL', models.BooleanField(default=False)),
                ('LMONO', models.BooleanField(default=False)),
                ('LBERRY', models.BooleanField(default=False)),
                ('LHFCALC', models.BooleanField(default=False)),
                ('ODDONLY', models.BooleanField(default=False)),
                ('EVENONLY', models.BooleanField(default=False)),
                ('LEPSILON', models.BooleanField(default=False)),
                ('LRPA', models.BooleanField(default=False)),
                ('LSPECTRAL', models.BooleanField(default=False)),
                ('ODDONLYGW', models.BooleanField(default=False)),
                ('EVENONLYGW', models.BooleanField(default=False)),
                ('LVDW', models.BooleanField(default=False)),
                ('natoms', models.IntegerField(null=True)),
                ('ncell', models.IntegerField(null=True)),
                ('reducedformula', models.CharField(max_length=50, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
