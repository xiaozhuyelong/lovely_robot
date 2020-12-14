# Generated by Django 3.1.4 on 2020-12-09 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CitiesCity',
            fields=[
                ('city_code', models.DecimalField(decimal_places=0, max_digits=20, primary_key=True, serialize=False)),
                ('city_name', models.CharField(max_length=50)),
                ('city_level', models.CharField(max_length=50)),
                ('province_code', models.DecimalField(decimal_places=0, max_digits=20)),
                ('updated', models.DateTimeField()),
                ('created', models.DateTimeField()),
            ],
            options={
                'db_table': 'cities_city',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='CitiesCounty',
            fields=[
                ('county_code', models.DecimalField(decimal_places=0, max_digits=20, primary_key=True, serialize=False)),
                ('county_name', models.CharField(max_length=50)),
                ('county_level', models.CharField(max_length=50)),
                ('city_code', models.DecimalField(decimal_places=0, max_digits=20)),
                ('updated', models.DateTimeField()),
                ('created', models.DateTimeField()),
            ],
            options={
                'db_table': 'cities_county',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='CitiesProvince',
            fields=[
                ('province_code', models.DecimalField(decimal_places=0, max_digits=20, primary_key=True, serialize=False)),
                ('province_name', models.CharField(max_length=50, unique=True)),
                ('province_level', models.CharField(max_length=50)),
                ('updated', models.DateTimeField()),
                ('created', models.DateTimeField()),
            ],
            options={
                'db_table': 'cities_province',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('comment_id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('user_id', models.BigIntegerField()),
                ('user_name', models.CharField(max_length=50)),
                ('article_id', models.BigIntegerField(blank=True, null=True)),
                ('article_title', models.CharField(blank=True, max_length=255, null=True)),
                ('relation_table', models.CharField(blank=True, max_length=255, null=True)),
                ('parent_comment_id', models.BigIntegerField(blank=True, null=True)),
                ('parent_comment_user_id', models.BigIntegerField()),
                ('reply_comment_id', models.BigIntegerField(blank=True, null=True)),
                ('reply_comment_user_id', models.BigIntegerField(blank=True, null=True)),
                ('comment_level', models.IntegerField()),
                ('content', models.CharField(max_length=255)),
                ('status_id', models.IntegerField()),
                ('praise_num', models.IntegerField()),
                ('top_status', models.SmallIntegerField()),
                ('create_time', models.DateTimeField()),
            ],
            options={
                'db_table': 'comment',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Cost',
            fields=[
                ('cost_id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('user_id', models.BigIntegerField()),
                ('cost_context', models.CharField(max_length=255)),
                ('cost_money', models.DecimalField(decimal_places=2, max_digits=10)),
                ('tag', models.CharField(blank=True, max_length=255, null=True)),
                ('created', models.DateTimeField()),
                ('updated', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'cost',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DailyFiles',
            fields=[
                ('file_id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('file_path', models.CharField(blank=True, max_length=255, null=True)),
                ('file_url', models.CharField(blank=True, max_length=500, null=True)),
                ('file_size', models.BigIntegerField(blank=True, null=True)),
                ('user_id', models.BigIntegerField(blank=True, null=True)),
                ('created', models.DateTimeField()),
                ('updeted', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'daily_files',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Diary',
            fields=[
                ('diary_id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('diary_context', models.TextField(blank=True, null=True)),
                ('diary_html', models.TextField(blank=True, null=True)),
                ('dialy_date', models.DateTimeField(blank=True, null=True)),
                ('mood_type', models.IntegerField(blank=True, null=True)),
                ('mood', models.CharField(blank=True, max_length=255, null=True)),
                ('temperature', models.DecimalField(blank=True, decimal_places=1, max_digits=3, null=True)),
                ('weather_type', models.IntegerField(blank=True, null=True)),
                ('weather', models.CharField(blank=True, max_length=255, null=True)),
                ('status_id', models.SmallIntegerField(blank=True, null=True)),
                ('user_id', models.BigIntegerField(blank=True, null=True)),
                ('created', models.DateTimeField(blank=True, null=True)),
                ('updated', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'diary',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('event_id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('event_context', models.TextField()),
                ('time_cost', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('plan_time', models.DateTimeField(blank=True, null=True)),
                ('remind', models.IntegerField(blank=True, null=True)),
                ('remind_time', models.DateTimeField(blank=True, null=True)),
                ('deleted', models.IntegerField(blank=True, null=True)),
                ('status_id', models.IntegerField(blank=True, null=True)),
                ('created', models.DateTimeField(blank=True, null=True)),
                ('updated', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'event',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Label',
            fields=[
                ('label_id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('label_context', models.CharField(max_length=255)),
                ('label_type', models.IntegerField(blank=True, null=True)),
                ('relation_id', models.BigIntegerField(blank=True, null=True)),
                ('relation_table', models.IntegerField(blank=True, null=True)),
                ('user_id', models.BigIntegerField(blank=True, null=True)),
                ('created', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'label',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Learn',
            fields=[
                ('learn_id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('learn_title', models.CharField(max_length=255)),
                ('learn_html', models.TextField(blank=True, null=True)),
                ('learn_context', models.TextField()),
                ('dir', models.IntegerField(blank=True, null=True)),
                ('tag', models.CharField(blank=True, max_length=255, null=True)),
                ('status_id', models.IntegerField(blank=True, null=True)),
                ('user_id', models.BigIntegerField(blank=True, null=True)),
                ('updated', models.DateTimeField(blank=True, null=True)),
                ('created', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'learn',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'person',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SpringScheduledTask',
            fields=[
                ('cron_id', models.IntegerField(primary_key=True, serialize=False)),
                ('cron_key', models.CharField(max_length=128, unique=True)),
                ('cron_expression', models.CharField(max_length=20)),
                ('task_explain', models.CharField(max_length=50)),
                ('status_id', models.IntegerField()),
            ],
            options={
                'db_table': 'spring_scheduled_task',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TravelNote',
            fields=[
                ('travel_id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('travel_title', models.CharField(blank=True, max_length=255, null=True)),
                ('travel_img', models.BigIntegerField(blank=True, null=True)),
                ('travel_html', models.TextField(blank=True, null=True)),
                ('travel_note', models.TextField()),
                ('user_id', models.BigIntegerField()),
                ('province_code', models.BigIntegerField(blank=True, null=True)),
                ('city_code', models.BigIntegerField(blank=True, null=True)),
                ('longitude', models.DecimalField(blank=True, decimal_places=7, max_digits=20, null=True)),
                ('latitude', models.DecimalField(blank=True, decimal_places=7, max_digits=20, null=True)),
                ('tag', models.CharField(blank=True, max_length=255, null=True)),
                ('updated', models.DateTimeField(blank=True, null=True)),
                ('created', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'travel_note',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('user_id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('user_name', models.CharField(blank=True, max_length=255, null=True)),
                ('phone', models.CharField(blank=True, max_length=255, null=True)),
                ('email', models.CharField(blank=True, max_length=255, null=True, unique=True)),
                ('avatar', models.CharField(blank=True, max_length=255, null=True)),
                ('nick_name', models.CharField(blank=True, max_length=255, null=True)),
                ('pwd', models.CharField(blank=True, max_length=255, null=True)),
                ('salt', models.CharField(blank=True, max_length=255, null=True)),
                ('status_id', models.SmallIntegerField(blank=True, null=True)),
                ('created', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'user_info',
                'managed': False,
            },
        ),
    ]
