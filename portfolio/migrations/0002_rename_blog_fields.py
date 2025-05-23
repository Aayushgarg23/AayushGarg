from django.db import migrations, models
import django.db.models.deletion

class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='image',
            new_name='cover_image',
        ),
        migrations.RenameField(
            model_name='blog',
            old_name='date',
            new_name='published_date',
        ),
        migrations.AddField(
            model_name='blog',
            name='excerpt',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='blog',
            name='read_time',
            field=models.PositiveIntegerField(default=5, help_text='Estimated reading time in minutes'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='blog',
            name='url',
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='category',
            field=models.CharField(default='Uncategorized', max_length=100),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='BlogAuthor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('avatar', models.ImageField(blank=True, upload_to='blog_authors/')),
                ('bio', models.TextField(blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='blog',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='blogs', to='portfolio.blogauthor'),
        ),
    ] 