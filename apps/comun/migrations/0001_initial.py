# Generated by Django 4.1.7 on 2023-04-21 21:33

from django.db import migrations, models
import django.db.models.deletion
import django_tenants.postgresql_backend.base


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Address",
            fields=[
                ("state", models.BooleanField(default=True, verbose_name="Estado")),
                (
                    "created_date",
                    models.DateField(
                        auto_now_add=True, verbose_name="Fecha de creacion"
                    ),
                ),
                (
                    "modified_data",
                    models.DateField(
                        auto_now=True, verbose_name="Fecha de Modificacion"
                    ),
                ),
                (
                    "deleted_date",
                    models.DateField(
                        auto_now=True, verbose_name="Fecha de Eliminacion"
                    ),
                ),
                (
                    "id",
                    models.CharField(max_length=200, primary_key=True, serialize=False),
                ),
                ("description", models.CharField(max_length=255)),
            ],
            options={
                "verbose_name": "Direccion",
                "verbose_name_plural": "Tipos de direcciones",
            },
        ),
        migrations.CreateModel(
            name="AffectationIgv",
            fields=[
                (
                    "id",
                    models.CharField(max_length=200, primary_key=True, serialize=False),
                ),
                ("state", models.BooleanField(default=True)),
                ("exportation", models.BooleanField(default=False)),
                ("free", models.BooleanField(default=False)),
                ("description", models.CharField(max_length=200)),
            ],
            options={
                "verbose_name": "tipos de afectación igv",
                "verbose_name_plural": "tipo de afectación igv",
            },
        ),
        migrations.CreateModel(
            name="Company",
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
                ("state", models.BooleanField(default=True, verbose_name="Estado")),
                (
                    "created_date",
                    models.DateField(
                        auto_now_add=True, verbose_name="Fecha de creacion"
                    ),
                ),
                (
                    "modified_data",
                    models.DateField(
                        auto_now=True, verbose_name="Fecha de Modificacion"
                    ),
                ),
                (
                    "deleted_date",
                    models.DateField(
                        auto_now=True, verbose_name="Fecha de Eliminacion"
                    ),
                ),
                (
                    "ruc",
                    models.CharField(max_length=11, unique=True, verbose_name="ruc"),
                ),
                ("name", models.CharField(max_length=250, verbose_name="nombre")),
                (
                    "direction",
                    models.CharField(max_length=250, verbose_name="direccion"),
                ),
                (
                    "email",
                    models.EmailField(
                        blank=True, max_length=250, null=True, verbose_name="correo"
                    ),
                ),
            ],
            options={
                "verbose_name": "Empresa",
                "verbose_name_plural": "Empresas",
            },
        ),
        migrations.CreateModel(
            name="CompanySchema",
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
                (
                    "schema_name",
                    models.CharField(
                        db_index=True,
                        max_length=63,
                        unique=True,
                        validators=[
                            django_tenants.postgresql_backend.base._check_schema_name
                        ],
                    ),
                ),
                ("state", models.BooleanField(default=True, verbose_name="Estado")),
                (
                    "created_date",
                    models.DateField(
                        auto_now_add=True, verbose_name="Fecha de creacion"
                    ),
                ),
                (
                    "modified_data",
                    models.DateField(
                        auto_now=True, verbose_name="Fecha de Modificacion"
                    ),
                ),
                (
                    "deleted_date",
                    models.DateField(
                        auto_now=True, verbose_name="Fecha de Eliminacion"
                    ),
                ),
                (
                    "company",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="comun.company"
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Currency",
            fields=[
                (
                    "id",
                    models.CharField(max_length=200, primary_key=True, serialize=False),
                ),
                ("state", models.BooleanField(default=True)),
                ("symbol", models.CharField(max_length=200)),
                ("description", models.CharField(max_length=200)),
            ],
            options={
                "verbose_name": "Currency",
                "verbose_name_plural": "Currencies",
            },
        ),
        migrations.CreateModel(
            name="Department",
            fields=[
                ("state", models.BooleanField(default=True, verbose_name="Estado")),
                (
                    "created_date",
                    models.DateField(
                        auto_now_add=True, verbose_name="Fecha de creacion"
                    ),
                ),
                (
                    "modified_data",
                    models.DateField(
                        auto_now=True, verbose_name="Fecha de Modificacion"
                    ),
                ),
                (
                    "deleted_date",
                    models.DateField(
                        auto_now=True, verbose_name="Fecha de Eliminacion"
                    ),
                ),
                (
                    "id",
                    models.CharField(max_length=20, primary_key=True, serialize=False),
                ),
                ("description", models.CharField(max_length=200)),
            ],
            options={
                "verbose_name": "Departamento",
                "verbose_name_plural": "Departamentos",
            },
        ),
        migrations.CreateModel(
            name="DocumentType",
            fields=[
                (
                    "id",
                    models.CharField(max_length=200, primary_key=True, serialize=False),
                ),
                ("state", models.BooleanField(default=True)),
                ("short", models.CharField(blank=True, max_length=200, null=True)),
                ("description", models.CharField(max_length=200)),
            ],
            options={
                "verbose_name": "Tipos de documentos",
                "verbose_name_plural": "Tipo de documento",
            },
        ),
        migrations.CreateModel(
            name="IdentityDocument",
            fields=[
                ("state", models.BooleanField(default=True, verbose_name="Estado")),
                (
                    "created_date",
                    models.DateField(
                        auto_now_add=True, verbose_name="Fecha de creacion"
                    ),
                ),
                (
                    "modified_data",
                    models.DateField(
                        auto_now=True, verbose_name="Fecha de Modificacion"
                    ),
                ),
                (
                    "deleted_date",
                    models.DateField(
                        auto_now=True, verbose_name="Fecha de Eliminacion"
                    ),
                ),
                (
                    "id",
                    models.CharField(max_length=200, primary_key=True, serialize=False),
                ),
                ("description", models.CharField(max_length=200)),
            ],
            options={
                "verbose_name": "docuumento de identidad",
                "verbose_name_plural": "docuumentos de identidades",
            },
        ),
        migrations.CreateModel(
            name="ItemType",
            fields=[
                (
                    "id",
                    models.CharField(max_length=2, primary_key=True, serialize=False),
                ),
                ("description", models.CharField(max_length=255)),
            ],
            options={
                "verbose_name": "tipos de producto",
                "verbose_name_plural": "tipo de producto",
            },
        ),
        migrations.CreateModel(
            name="Module",
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
                ("state", models.BooleanField(default=True, verbose_name="Estado")),
                (
                    "created_date",
                    models.DateField(
                        auto_now_add=True, verbose_name="Fecha de creacion"
                    ),
                ),
                (
                    "modified_data",
                    models.DateField(
                        auto_now=True, verbose_name="Fecha de Modificacion"
                    ),
                ),
                (
                    "deleted_date",
                    models.DateField(
                        auto_now=True, verbose_name="Fecha de Eliminacion"
                    ),
                ),
                ("name", models.CharField(max_length=250, verbose_name="nombre")),
            ],
            options={
                "verbose_name": "Modulo",
                "verbose_name_plural": "Modulos",
            },
        ),
        migrations.CreateModel(
            name="OperationType",
            fields=[
                (
                    "id",
                    models.CharField(max_length=200, primary_key=True, serialize=False),
                ),
                ("state", models.BooleanField(default=True)),
                ("exportation", models.BooleanField(default=True)),
                ("description", models.CharField(max_length=200)),
            ],
            options={
                "verbose_name": "Tipo de operacion",
                "verbose_name_plural": "Tipos de operaciones",
            },
        ),
        migrations.CreateModel(
            name="PaymentCondition",
            fields=[
                (
                    "id",
                    models.CharField(max_length=200, primary_key=True, serialize=False),
                ),
                ("name", models.CharField(max_length=200)),
                ("days", models.IntegerField(default=0)),
                ("locked", models.BooleanField(default=False)),
                ("state", models.BooleanField(default=True)),
            ],
            options={
                "verbose_name": "Condicion de pago",
                "verbose_name_plural": "Condiciones de pago",
            },
        ),
        migrations.CreateModel(
            name="PaymentMethodType",
            fields=[
                (
                    "id",
                    models.CharField(max_length=200, primary_key=True, serialize=False),
                ),
                ("state", models.BooleanField(default=True)),
                ("description", models.CharField(max_length=200)),
            ],
            options={
                "verbose_name": "Tipos de metodos de pagos",
                "verbose_name_plural": "Tipo de metodo de pago",
            },
        ),
        migrations.CreateModel(
            name="PersonType",
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
                ("state", models.BooleanField(default=True, verbose_name="Estado")),
                (
                    "created_date",
                    models.DateField(
                        auto_now_add=True, verbose_name="Fecha de creacion"
                    ),
                ),
                (
                    "modified_data",
                    models.DateField(
                        auto_now=True, verbose_name="Fecha de Modificacion"
                    ),
                ),
                (
                    "deleted_date",
                    models.DateField(
                        auto_now=True, verbose_name="Fecha de Eliminacion"
                    ),
                ),
                ("description", models.TextField()),
            ],
            options={
                "verbose_name": "Tipo de perosna",
                "verbose_name_plural": "Tipos de personas",
            },
        ),
        migrations.CreateModel(
            name="Unit",
            fields=[
                (
                    "id",
                    models.CharField(max_length=20, primary_key=True, serialize=False),
                ),
                ("state", models.BooleanField(default=True)),
                ("symbol", models.CharField(blank=True, max_length=200, null=True)),
                ("description", models.CharField(max_length=200)),
            ],
            options={
                "verbose_name": "tipos de unidades",
                "verbose_name_plural": "Tipo de unidad",
            },
        ),
        migrations.CreateModel(
            name="Province",
            fields=[
                ("state", models.BooleanField(default=True, verbose_name="Estado")),
                (
                    "created_date",
                    models.DateField(
                        auto_now_add=True, verbose_name="Fecha de creacion"
                    ),
                ),
                (
                    "modified_data",
                    models.DateField(
                        auto_now=True, verbose_name="Fecha de Modificacion"
                    ),
                ),
                (
                    "deleted_date",
                    models.DateField(
                        auto_now=True, verbose_name="Fecha de Eliminacion"
                    ),
                ),
                (
                    "id",
                    models.CharField(max_length=20, primary_key=True, serialize=False),
                ),
                ("description", models.CharField(max_length=200)),
                (
                    "department",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="comun.department",
                    ),
                ),
            ],
            options={
                "verbose_name": "Provincia",
                "verbose_name_plural": "Provincias",
            },
        ),
        migrations.CreateModel(
            name="Domain",
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
                (
                    "domain",
                    models.CharField(db_index=True, max_length=253, unique=True),
                ),
                ("is_primary", models.BooleanField(db_index=True, default=True)),
                (
                    "tenant",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="domains",
                        to="comun.companyschema",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="District",
            fields=[
                ("state", models.BooleanField(default=True, verbose_name="Estado")),
                (
                    "created_date",
                    models.DateField(
                        auto_now_add=True, verbose_name="Fecha de creacion"
                    ),
                ),
                (
                    "modified_data",
                    models.DateField(
                        auto_now=True, verbose_name="Fecha de Modificacion"
                    ),
                ),
                (
                    "deleted_date",
                    models.DateField(
                        auto_now=True, verbose_name="Fecha de Eliminacion"
                    ),
                ),
                (
                    "id",
                    models.CharField(max_length=20, primary_key=True, serialize=False),
                ),
                ("description", models.CharField(max_length=200)),
                (
                    "province",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="comun.province"
                    ),
                ),
            ],
            options={
                "verbose_name": "Distrito",
                "verbose_name_plural": "Distritos",
            },
        ),
    ]
