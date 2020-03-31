# Generated by Django 3.0.4 on 2020-03-31 05:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('exam_duration', models.DurationField(null=True)),
                ('published_status', models.BooleanField(default=False)),
                ('pub_date', models.DateTimeField(verbose_name='published date')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.TextField()),
                ('question_type', models.CharField(default='', max_length=50)),
                ('exam', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exams.Exam')),
            ],
        ),
        migrations.CreateModel(
            name='Answers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer_text', models.TextField()),
                ('answer_image', models.ImageField(upload_to='')),
                ('answer_type', models.CharField(choices=[('IM', 'Image'), ('TX', 'Text')], default='TX', max_length=2)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exams.Question')),
            ],
        ),
    ]