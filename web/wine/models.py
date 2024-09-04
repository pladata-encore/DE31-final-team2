from django.db import models


class Items(models.Model):
    unnamed_0 = models.BigIntegerField(db_column='Unnamed: 0', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    vintage_id = models.BigIntegerField(db_column='Vintage_Id', primary_key=True)  # Field name made lowercase.
    vintage_name = models.TextField(db_column='Vintage_Name', blank=True, null=True)  # Field name made lowercase.
    wine_id = models.BigIntegerField(db_column='Wine_Id', blank=True, null=True)  # Field name made lowercase.
    wine_name = models.TextField(db_column='Wine_Name', blank=True, null=True)  # Field name made lowercase.
    wine_name_kor = models.TextField(db_column='Wine_Name_Kor', blank=True, null=True)  # Field name made lowercase.
    year = models.TextField(db_column='Year', blank=True, null=True)  # Field name made lowercase.
    url = models.TextField(db_column='URL', blank=True, null=True)  # Field name made lowercase.
    ratings_count = models.BigIntegerField(db_column='Ratings_Count', blank=True, null=True)  # Field name made lowercase.
    ratings_average = models.FloatField(db_column='Ratings_Average', blank=True, null=True)  # Field name made lowercase.
    type_id = models.BigIntegerField(db_column='Type_Id', blank=True, null=True)  # Field name made lowercase.
    is_natural = models.BigIntegerField(blank=True, null=True)
    body = models.BigIntegerField(db_column='Body', blank=True, null=True)  # Field name made lowercase.
    acidity = models.FloatField(db_column='Acidity', blank=True, null=True)  # Field name made lowercase.
    intensity = models.FloatField(db_column='Intensity', blank=True, null=True)  # Field name made lowercase.
    sweetness = models.FloatField(db_column='Sweetness', blank=True, null=True)  # Field name made lowercase.
    tannin = models.FloatField(db_column='Tannin', blank=True, null=True)  # Field name made lowercase.
    flavor = models.TextField(db_column='Flavor', blank=True, null=True)  # Field name made lowercase.
    alcohol = models.FloatField(db_column='Alcohol', blank=True, null=True)  # Field name made lowercase.
    volume = models.BigIntegerField(db_column='Volume', blank=True, null=True)  # Field name made lowercase.
    food = models.TextField(db_column='Food', blank=True, null=True)  # Field name made lowercase.
    grape = models.TextField(db_column='Grape', blank=True, null=True)  # Field name made lowercase.
    region_name = models.TextField(db_column='Region_Name', blank=True, null=True)  # Field name made lowercase.
    region_id = models.BigIntegerField(db_column='Region_Id', blank=True, null=True)  # Field name made lowercase.
    country = models.TextField(db_column='Country', blank=True, null=True)  # Field name made lowercase.
    winery_id = models.BigIntegerField(db_column='Winery_Id', blank=True, null=True)  # Field name made lowercase.
    winery_name = models.TextField(db_column='Winery_Name', blank=True, null=True)  # Field name made lowercase.
    price_usd = models.FloatField(db_column='Price_USD', blank=True, null=True)  # Field name made lowercase.
    price_kor = models.BigIntegerField(db_column='Price_KOR', blank=True, null=True)  # Field name made lowercase.
    currency = models.TextField(db_column='Currency', blank=True, null=True)  # Field name made lowercase.
    bottle_medium = models.TextField(blank=True, null=True)
    bottle_small = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'items'
