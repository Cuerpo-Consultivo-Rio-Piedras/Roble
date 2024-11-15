# Generated by Django 4.2.16 on 2024-11-15 00:52

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("api", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Community",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=64)),
                (
                    "geometry",
                    django.contrib.gis.db.models.fields.GeometryField(srid=4326),
                ),
            ],
        ),
        migrations.CreateModel(
            name="LandUse",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("object_id", models.IntegerField()),
                (
                    "type",
                    models.CharField(
                        choices=[
                            ("P", "P"),
                            ("V", "V"),
                            ("A", "A"),
                            ("D", "D"),
                            ("C", "C"),
                            ("p", "P"),
                        ],
                        max_length=1,
                    ),
                ),
                (
                    "municipality",
                    models.CharField(
                        choices=[
                            ("ADJUNTAS", "Adjuntas"),
                            ("AGUADA", "Aguada"),
                            ("AGUADILLA", "Aguadilla"),
                            ("AGUAS_BUENAS", "Aguas Buenas"),
                            ("AIBONITO", "Aibonito"),
                            ("ANASCO", "Anasco"),
                            ("ARECIBO", "Arecibo"),
                            ("ARROYO", "Arroyo"),
                            ("BARCELONETA", "Barceloneta"),
                            ("BARRANQUITAS", "Barranquitas"),
                            ("BAYAMON", "Bayamon"),
                            ("CABO_ROJO", "Cabo Rojo"),
                            ("CAGUAS", "Caguas"),
                            ("CAMUY", "Camuy"),
                            ("CANOVANAS", "Canovanas"),
                            ("CAROLINA", "Carolina"),
                            ("CATANO", "Catano"),
                            ("CAYEY", "Cayey"),
                            ("CEIBA", "Ceiba"),
                            ("CIALES", "Ciales"),
                            ("CIDRA", "Cidra"),
                            ("COAMO", "Coamo"),
                            ("COMERIO", "Comerio"),
                            ("COROZAL", "Corozal"),
                            ("CULEBRA", "Culebra"),
                            ("DORADO", "Dorado"),
                            ("FAJARDO", "Fajardo"),
                            ("FLORIDA", "Florida"),
                            ("GUANICA", "Guanica"),
                            ("GUAYAMA", "Guayama"),
                            ("GUAYANILLA", "Guayanilla"),
                            ("GUAYNABO", "Guaynabo"),
                            ("GURABO", "Gurabo"),
                            ("HATILLO", "Hatillo"),
                            ("HORMIGUEROS", "Hormigueros"),
                            ("HUMACAO", "Humacao"),
                            ("ISABELA", "Isabela"),
                            ("JAYUYA", "Jayuya"),
                            ("JUANA_DIAZ", "Juana Diaz"),
                            ("JUNCOS", "Juncos"),
                            ("LAJAS", "Lajas"),
                            ("LARES", "Lares"),
                            ("LAS_MARIAS", "Las Marias"),
                            ("LAS_PIEDRAS", "Las Piedras"),
                            ("LOIZA", "Loiza"),
                            ("LUQUILLO", "Luquillo"),
                            ("MANATI", "Manati"),
                            ("MARICAO", "Maricao"),
                            ("MAUNABO", "Maunabo"),
                            ("MAYAGUEZ", "Mayaguez"),
                            ("MOCA", "Moca"),
                            ("MOROVIS", "Morovis"),
                            ("NAGUABO", "Naguabo"),
                            ("NARANJITO", "Naranjito"),
                            ("OROCOVIS", "Orocovis"),
                            ("PATILLAS", "Patillas"),
                            ("PENUELAS", "Penuelas"),
                            ("PONCE", "Ponce"),
                            ("QUEBRADILLAS", "Quebradillas"),
                            ("RINCON", "Rincon"),
                            ("RIO_GRANDE", "Rio Grande"),
                            ("SABANA_GRANDE", "Sabana Grande"),
                            ("SALINAS", "Salinas"),
                            ("SAN_GERMAN", "San German"),
                            ("SAN_JUAN", "San Juan"),
                            ("SAN_LORENZO", "San Lorenzo"),
                            ("SAN_SEBASTIAN", "San Sebastian"),
                            ("SANTA_ISABEL", "Santa Isabel"),
                            ("TOA_ALTA", "Toa Alta"),
                            ("TOA_BAJA", "Toa Baja"),
                            ("TRUJILLO_ALTO", "Trujillo Alto"),
                            ("UTUADO", "Utuado"),
                            ("VEGA_ALTA", "Vega Alta"),
                            ("VEGA_BAJA", "Vega Baja"),
                            ("VIEQUES", "Vieques"),
                            ("VILLALBA", "Villalba"),
                            ("YABUCOA", "Yabucoa"),
                            ("YAUCO", "Yauco"),
                        ],
                        max_length=255,
                    ),
                ),
                (
                    "clasi_put",
                    models.CharField(
                        choices=[
                            ("AGUA", "Agua"),
                            ("SREP-E", "Srep E"),
                            ("SU", "Su"),
                            ("SRC", "Src"),
                            ("SREP", "Srep"),
                            ("SREP-H", "Srep H"),
                            ("SREP-EH", "Srep Eh"),
                            ("SREP-A", "Srep A"),
                            ("VIAL", "Vial"),
                            ("SREP-AE", "Srep Ae"),
                            ("SREP-AH", "Srep Ah"),
                            ("SREP-EA", "Srep Ea"),
                            ("SREP-EP", "Srep Ep"),
                            ("SURNP", "Surnp"),
                            ("SURP", "Surp"),
                            ("SREP-AP", "Srep Ap"),
                            ("SREP-P", "Srep P"),
                        ],
                        max_length=255,
                    ),
                ),
                ("description", models.CharField(max_length=255)),
                ("shape_length", models.FloatField()),
                ("shape_area", models.FloatField()),
                (
                    "geometry",
                    django.contrib.gis.db.models.fields.GeometryField(srid=4326),
                ),
            ],
        ),
        migrations.CreateModel(
            name="StreetSegment",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("segment_id", models.FloatField()),
                ("fe_name", models.CharField()),
                (
                    "geometry",
                    django.contrib.gis.db.models.fields.GeometryField(srid=4326),
                ),
            ],
        ),
        migrations.CreateModel(
            name="TransmissionLine",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("fid", models.IntegerField()),
                ("gid", models.IntegerField()),
                ("region", models.CharField(max_length=64, null=True)),
                (
                    "municipality",
                    models.CharField(
                        choices=[
                            ("ADJUNTAS", "Adjuntas"),
                            ("AGUADA", "Aguada"),
                            ("AGUADILLA", "Aguadilla"),
                            ("AGUAS_BUENAS", "Aguas Buenas"),
                            ("AIBONITO", "Aibonito"),
                            ("ANASCO", "Anasco"),
                            ("ARECIBO", "Arecibo"),
                            ("ARROYO", "Arroyo"),
                            ("BARCELONETA", "Barceloneta"),
                            ("BARRANQUITAS", "Barranquitas"),
                            ("BAYAMON", "Bayamon"),
                            ("CABO_ROJO", "Cabo Rojo"),
                            ("CAGUAS", "Caguas"),
                            ("CAMUY", "Camuy"),
                            ("CANOVANAS", "Canovanas"),
                            ("CAROLINA", "Carolina"),
                            ("CATANO", "Catano"),
                            ("CAYEY", "Cayey"),
                            ("CEIBA", "Ceiba"),
                            ("CIALES", "Ciales"),
                            ("CIDRA", "Cidra"),
                            ("COAMO", "Coamo"),
                            ("COMERIO", "Comerio"),
                            ("COROZAL", "Corozal"),
                            ("CULEBRA", "Culebra"),
                            ("DORADO", "Dorado"),
                            ("FAJARDO", "Fajardo"),
                            ("FLORIDA", "Florida"),
                            ("GUANICA", "Guanica"),
                            ("GUAYAMA", "Guayama"),
                            ("GUAYANILLA", "Guayanilla"),
                            ("GUAYNABO", "Guaynabo"),
                            ("GURABO", "Gurabo"),
                            ("HATILLO", "Hatillo"),
                            ("HORMIGUEROS", "Hormigueros"),
                            ("HUMACAO", "Humacao"),
                            ("ISABELA", "Isabela"),
                            ("JAYUYA", "Jayuya"),
                            ("JUANA_DIAZ", "Juana Diaz"),
                            ("JUNCOS", "Juncos"),
                            ("LAJAS", "Lajas"),
                            ("LARES", "Lares"),
                            ("LAS_MARIAS", "Las Marias"),
                            ("LAS_PIEDRAS", "Las Piedras"),
                            ("LOIZA", "Loiza"),
                            ("LUQUILLO", "Luquillo"),
                            ("MANATI", "Manati"),
                            ("MARICAO", "Maricao"),
                            ("MAUNABO", "Maunabo"),
                            ("MAYAGUEZ", "Mayaguez"),
                            ("MOCA", "Moca"),
                            ("MOROVIS", "Morovis"),
                            ("NAGUABO", "Naguabo"),
                            ("NARANJITO", "Naranjito"),
                            ("OROCOVIS", "Orocovis"),
                            ("PATILLAS", "Patillas"),
                            ("PENUELAS", "Penuelas"),
                            ("PONCE", "Ponce"),
                            ("QUEBRADILLAS", "Quebradillas"),
                            ("RINCON", "Rincon"),
                            ("RIO_GRANDE", "Rio Grande"),
                            ("SABANA_GRANDE", "Sabana Grande"),
                            ("SALINAS", "Salinas"),
                            ("SAN_GERMAN", "San German"),
                            ("SAN_JUAN", "San Juan"),
                            ("SAN_LORENZO", "San Lorenzo"),
                            ("SAN_SEBASTIAN", "San Sebastian"),
                            ("SANTA_ISABEL", "Santa Isabel"),
                            ("TOA_ALTA", "Toa Alta"),
                            ("TOA_BAJA", "Toa Baja"),
                            ("TRUJILLO_ALTO", "Trujillo Alto"),
                            ("UTUADO", "Utuado"),
                            ("VEGA_ALTA", "Vega Alta"),
                            ("VEGA_BAJA", "Vega Baja"),
                            ("VIEQUES", "Vieques"),
                            ("VILLALBA", "Villalba"),
                            ("YABUCOA", "Yabucoa"),
                            ("YAUCO", "Yauco"),
                        ],
                        max_length=255,
                    ),
                ),
                ("major_proj", models.CharField(max_length=252, null=True)),
                ("asset_id", models.IntegerField(null=True)),
                ("short_desc", models.CharField(max_length=5000, null=True)),
                ("planned_cost", models.FloatField(null=True)),
                ("estimated_time", models.FloatField(null=True)),
                ("phase_name", models.CharField(max_length=252)),
                ("fid_1", models.IntegerField()),
                ("object_id", models.IntegerField()),
                ("circuit1", models.IntegerField()),
                ("working", models.IntegerField()),
                (
                    "geometry",
                    django.contrib.gis.db.models.fields.LineStringField(srid=4326),
                ),
            ],
        ),
        migrations.DeleteModel(
            name="POI",
        ),
    ]
