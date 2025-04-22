from django.db import models

# Create your models here.
class AbstractPartType(models.Model):
    id = models.IntegerField(primary_key=True)
    parent_abstract_part_type = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    depends_on = models.ForeignKey('self', models.DO_NOTHING, db_column='depends_on', related_name='abstractparttype_depends_on_set', blank=True, null=True)
    part_filename = models.CharField(max_length=20, blank=True, null=True)
    eapt = models.CharField(max_length=100)
    gapt = models.CharField(max_length=100, blank=True, null=True)
    faft = models.CharField(max_length=100, blank=True, null=True)
    saft = models.CharField(max_length=100, blank=True, null=True)
    iaft = models.CharField(max_length=100, blank=True, null=True)
    jaft = models.CharField(max_length=100, blank=True, null=True)
    sw_aft = models.CharField(max_length=100, blank=True, null=True)
    baft = models.CharField(max_length=100, blank=True, null=True)
    modified_rule = models.IntegerField(blank=True, null=True)
    eut = models.TextField(blank=True, null=True)
    gut = models.TextField(blank=True, null=True)
    fut = models.TextField(blank=True, null=True)
    sut = models.TextField(blank=True, null=True)
    iut = models.TextField(blank=True, null=True)
    jut = models.TextField(blank=True, null=True)
    swut = models.TextField(blank=True, null=True)
    but = models.TextField(blank=True, null=True)
    part_paired = models.IntegerField(blank=True, null=True)
    schematic_picname1 = models.CharField(max_length=9, blank=True, null=True)
    schematic_picname2 = models.CharField(max_length=9, blank=True, null=True)
    block_family_compatibility = models.IntegerField(blank=True, null=True)
    repair_cost_modifier = models.DecimalField(max_digits=100, decimal_places=7, blank=True, null=True)
    scrap_value_modifier = models.DecimalField(max_digits=100, decimal_places=7, blank=True, null=True)
    garage_category = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'abstract_part_type'


class AttachmentPoint(models.Model):
    id = models.IntegerField(primary_key=True)
    attachment_point = models.CharField(max_length=100)

    class Meta:
        managed = True
        db_table = 'attachment_point'


class Brand(models.Model):
    id = models.IntegerField(primary_key=True)
    brand = models.CharField(max_length=100, blank=True, null=True)
    pic_name = models.CharField(max_length=50, blank=True, null=True)
    is_stock = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'brand'


class BrandedPart(models.Model):
    id = models.IntegerField(primary_key=True)
    part_type = models.ForeignKey('PartType', models.DO_NOTHING)
    model = models.ForeignKey('Model', models.DO_NOTHING)
    mfg_date = models.DateTimeField()
    qty_avail = models.IntegerField()
    retail_price = models.IntegerField()
    max_item_wear = models.SmallIntegerField(blank=True, null=True)
    engine_block_family_id = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'branded_part'


class DriverClass(models.Model):
    id = models.SmallIntegerField(primary_key=True)
    driver_class = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'driver_class'


class Key(models.Model):
    profile_id = models.ForeignKey('Profile', models.DO_NOTHING, db_column='profile_id')
    session_key = models.CharField(max_length=100)

    class Meta:
        managed = True
        db_table = 'key'


class Login(models.Model):
    customer_id = models.IntegerField(unique=True)
    login_name = models.CharField(primary_key=True, max_length=32)
    password = models.CharField(max_length=32)
    login_level = models.SmallIntegerField()

    class Meta:
        managed = True
        db_table = 'login'


class Model(models.Model):
    id = models.IntegerField(primary_key=True)
    brand = models.ForeignKey(Brand, models.DO_NOTHING)
    e_model = models.CharField(max_length=100, blank=True, null=True)
    g_model = models.CharField(max_length=100, blank=True, null=True)
    f_model = models.CharField(max_length=100, blank=True, null=True)
    s_model = models.CharField(max_length=100, blank=True, null=True)
    i_model = models.CharField(max_length=100, blank=True, null=True)
    j_model = models.CharField(max_length=100, blank=True, null=True)
    sw_model = models.CharField(max_length=100, blank=True, null=True)
    b_model = models.CharField(max_length=100, blank=True, null=True)
    e_extra_info = models.CharField(max_length=100, blank=True, null=True)
    g_extra_info = models.CharField(max_length=100, blank=True, null=True)
    f_extra_info = models.CharField(max_length=100, blank=True, null=True)
    s_extra_info = models.CharField(max_length=100, blank=True, null=True)
    i_extra_info = models.CharField(max_length=100, blank=True, null=True)
    j_extra_info = models.CharField(max_length=100, blank=True, null=True)
    sw_extra_info = models.CharField(max_length=100, blank=True, null=True)
    b_extra_info = models.CharField(max_length=100, blank=True, null=True)
    e_short_model = models.CharField(max_length=50, blank=True, null=True)
    g_short_model = models.CharField(max_length=50, blank=True, null=True)
    f_short_model = models.CharField(max_length=50, blank=True, null=True)
    s_short_model = models.CharField(max_length=50, blank=True, null=True)
    i_short_model = models.CharField(max_length=50, blank=True, null=True)
    j_short_model = models.CharField(max_length=50, blank=True, null=True)
    sw_short_model = models.CharField(max_length=50, blank=True, null=True)
    b_short_model = models.CharField(max_length=50, blank=True, null=True)
    debug_string = models.CharField(max_length=255, blank=True, null=True)
    debug_sort_string = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'model'

class Part(models.Model):
    id = models.IntegerField(primary_key=True)
    parent_part = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    branded_part = models.ForeignKey(BrandedPart, models.DO_NOTHING)
    percent_damage = models.SmallIntegerField()
    item_wear = models.IntegerField()
    attachment_point = models.ForeignKey(AttachmentPoint, models.DO_NOTHING, blank=True, null=True)
    owner_id = models.IntegerField(blank=True, null=True)
    part_name = models.CharField(max_length=100, blank=True, null=True)
    repair_cost = models.IntegerField(blank=True, null=True)
    scrap_value = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'part'


class PartGrade(models.Model):
    id = models.IntegerField(primary_key=True)
    e_text = models.CharField(max_length=50, blank=True, null=True)
    g_text = models.CharField(max_length=50, blank=True, null=True)
    f_text = models.CharField(max_length=50, blank=True, null=True)
    part_grade = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'part_grade'


class PartType(models.Model):
    id = models.IntegerField(primary_key=True)
    abstract_part_type = models.ForeignKey(AbstractPartType, models.DO_NOTHING)
    part_type = models.CharField(max_length=100)
    part_filename = models.CharField(max_length=20, blank=True, null=True)
    part_grade = models.ForeignKey(PartGrade, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'part_type'

class PlayerType(models.Model):
    id = models.IntegerField(primary_key=True)
    player_type = models.CharField(max_length=100)

    class Meta:
        managed = True
        db_table = 'player_type'        


class Player(models.Model):
    id = models.IntegerField(primary_key=True)
    customer_id = models.IntegerField()
    player_type = models.ForeignKey('PlayerType', models.DO_NOTHING)
    sanctioned_score = models.IntegerField(blank=True, null=True)
    challenge_score = models.IntegerField(blank=True, null=True)
    last_logged_in = models.DateTimeField(blank=True, null=True)
    times_logged_in = models.SmallIntegerField(blank=True, null=True)
    bank_balance = models.IntegerField()
    num_cars_owned = models.SmallIntegerField()
    is_logged_in = models.SmallIntegerField(blank=True, null=True)
    driver_style = models.SmallIntegerField()
    lp_code = models.IntegerField()
    lp_text = models.CharField(max_length=9, blank=True, null=True)
    car_num1 = models.CharField(max_length=2)
    car_num2 = models.CharField(max_length=2)
    car_num3 = models.CharField(max_length=2)
    car_num4 = models.CharField(max_length=2)
    car_num5 = models.CharField(max_length=2)
    car_num6 = models.CharField(max_length=2)
    dl_number = models.CharField(max_length=20, blank=True, null=True)
    persona = models.CharField(max_length=30)
    address = models.CharField(max_length=128, blank=True, null=True)
    residence = models.CharField(max_length=20, blank=True, null=True)
    vehicle_id = models.IntegerField(blank=True, null=True)
    current_race_id = models.IntegerField(blank=True, null=True)
    offline_driver_skill = models.IntegerField(blank=True, null=True)
    offline_grudge = models.IntegerField(blank=True, null=True)
    offline_reputation = models.IntegerField(blank=True, null=True)
    total_time_played = models.IntegerField(blank=True, null=True)
    car_info_setting = models.IntegerField(blank=True, null=True)
    stock_classic_class = models.SmallIntegerField(blank=True, null=True)
    stock_muscle_class = models.ForeignKey(DriverClass, models.DO_NOTHING, db_column='stock_muscle_class', blank=True, null=True)
    modified_classic_class = models.ForeignKey(DriverClass, models.DO_NOTHING, db_column='modified_classic_class', related_name='player_modified_classic_class_set', blank=True, null=True)
    modified_muscle_class = models.ForeignKey(DriverClass, models.DO_NOTHING, db_column='modified_muscle_class', related_name='player_modified_muscle_class_set', blank=True, null=True)
    outlaw_class = models.ForeignKey(DriverClass, models.DO_NOTHING, db_column='outlaw_class', related_name='player_outlaw_class_set', blank=True, null=True)
    drag_class = models.ForeignKey(DriverClass, models.DO_NOTHING, db_column='drag_class', related_name='player_drag_class_set', blank=True, null=True)
    challenge_rung = models.IntegerField(blank=True, null=True)
    offline_ai_car_class = models.SmallIntegerField(blank=True, null=True)
    offline_ai_skin_id = models.IntegerField(blank=True, null=True)
    offline_ai_car_bpt_id = models.IntegerField(blank=True, null=True)
    offline_ai_state = models.SmallIntegerField(blank=True, null=True)
    body_type = models.IntegerField(blank=True, null=True)
    skin_color = models.IntegerField(blank=True, null=True)
    hair_color = models.IntegerField(blank=True, null=True)
    shirt_color = models.IntegerField(blank=True, null=True)
    pants_color = models.IntegerField(blank=True, null=True)
    offline_driver_style = models.IntegerField(blank=True, null=True)
    offline_driver_attitude = models.IntegerField(blank=True, null=True)
    evaded_fuzz = models.IntegerField(blank=True, null=True)
    pinks_won = models.IntegerField(blank=True, null=True)
    num_unread_mail = models.IntegerField(blank=True, null=True)
    total_races_run = models.IntegerField(blank=True, null=True)
    total_races_won = models.IntegerField(blank=True, null=True)
    total_races_completed = models.IntegerField(blank=True, null=True)
    total_winnings = models.IntegerField(blank=True, null=True)
    insurance_risk_points = models.IntegerField(blank=True, null=True)
    insurance_rating = models.IntegerField(blank=True, null=True)
    challenge_races_run = models.IntegerField(blank=True, null=True)
    challenge_races_won = models.IntegerField(blank=True, null=True)
    challenge_races_completed = models.IntegerField(blank=True, null=True)
    cars_lost = models.IntegerField(blank=True, null=True)
    cars_won = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'player'





class Profile(models.Model):
    customer_id = models.IntegerField()
    profile_name = models.CharField(max_length=32)
    server_id = models.IntegerField()
    create_stamp = models.IntegerField()
    last_login_stamp = models.IntegerField()
    number_games = models.IntegerField()
    id = models.IntegerField(primary_key=True)
    is_online = models.BooleanField()
    game_purchase_stamp = models.IntegerField()
    game_serial_number = models.CharField(max_length=32)
    time_online = models.IntegerField()
    time_in_game = models.IntegerField()
    game_blob = models.CharField(max_length=512)
    personal_blob = models.CharField(max_length=256)
    picture_blob = models.CharField(max_length=1)
    dnd = models.BooleanField()
    game_start_stamp = models.IntegerField()
    current_key = models.CharField(max_length=400)
    profile_level = models.SmallIntegerField()
    shard_id = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'profile'


class PtSkin(models.Model):
    id = models.IntegerField(primary_key=True)
    creator_id = models.IntegerField(blank=True, null=True)
    skin_type = models.ForeignKey('SkinType', models.DO_NOTHING, blank=True, null=True)
    part_type = models.ForeignKey(PartType, models.DO_NOTHING, blank=True, null=True)
    e_skin = models.CharField(max_length=100, blank=True, null=True)
    g_skin = models.CharField(max_length=20, blank=True, null=True)
    f_skin = models.CharField(max_length=20, blank=True, null=True)
    s_skin = models.CharField(max_length=20, blank=True, null=True)
    i_skin = models.CharField(max_length=20, blank=True, null=True)
    j_skin = models.CharField(max_length=20, blank=True, null=True)
    sw_skin = models.CharField(max_length=20, blank=True, null=True)
    b_skin = models.CharField(max_length=20, blank=True, null=True)
    price = models.IntegerField()
    part_filename = models.CharField(max_length=20, blank=True, null=True)
    h0 = models.SmallIntegerField(blank=True, null=True)
    s0 = models.SmallIntegerField(blank=True, null=True)
    v0 = models.SmallIntegerField(blank=True, null=True)
    c0 = models.SmallIntegerField(blank=True, null=True)
    x0 = models.SmallIntegerField(blank=True, null=True)
    y0 = models.SmallIntegerField(blank=True, null=True)
    h1 = models.SmallIntegerField(blank=True, null=True)
    s1 = models.SmallIntegerField(blank=True, null=True)
    v1 = models.SmallIntegerField(blank=True, null=True)
    c1 = models.SmallIntegerField(blank=True, null=True)
    x1 = models.SmallIntegerField(blank=True, null=True)
    y1 = models.SmallIntegerField(blank=True, null=True)
    h2 = models.SmallIntegerField(blank=True, null=True)
    s2 = models.SmallIntegerField(blank=True, null=True)
    v2 = models.SmallIntegerField(blank=True, null=True)
    c2 = models.SmallIntegerField(blank=True, null=True)
    x2 = models.SmallIntegerField(blank=True, null=True)
    y2 = models.SmallIntegerField(blank=True, null=True)
    h3 = models.SmallIntegerField(blank=True, null=True)
    s3 = models.SmallIntegerField(blank=True, null=True)
    v3 = models.SmallIntegerField(blank=True, null=True)
    c3 = models.SmallIntegerField(blank=True, null=True)
    x3 = models.SmallIntegerField(blank=True, null=True)
    y3 = models.SmallIntegerField(blank=True, null=True)
    h4 = models.SmallIntegerField(blank=True, null=True)
    s4 = models.SmallIntegerField(blank=True, null=True)
    v4 = models.SmallIntegerField(blank=True, null=True)
    c4 = models.SmallIntegerField(blank=True, null=True)
    x4 = models.SmallIntegerField(blank=True, null=True)
    y4 = models.SmallIntegerField(blank=True, null=True)
    h5 = models.SmallIntegerField(blank=True, null=True)
    s5 = models.SmallIntegerField(blank=True, null=True)
    v5 = models.SmallIntegerField(blank=True, null=True)
    c5 = models.SmallIntegerField(blank=True, null=True)
    x5 = models.SmallIntegerField(blank=True, null=True)
    y5 = models.SmallIntegerField(blank=True, null=True)
    h6 = models.SmallIntegerField(blank=True, null=True)
    s6 = models.SmallIntegerField(blank=True, null=True)
    v6 = models.SmallIntegerField(blank=True, null=True)
    c6 = models.SmallIntegerField(blank=True, null=True)
    x6 = models.SmallIntegerField(blank=True, null=True)
    y6 = models.SmallIntegerField(blank=True, null=True)
    h7 = models.SmallIntegerField(blank=True, null=True)
    s7 = models.SmallIntegerField(blank=True, null=True)
    v7 = models.SmallIntegerField(blank=True, null=True)
    c7 = models.SmallIntegerField(blank=True, null=True)
    x7 = models.SmallIntegerField(blank=True, null=True)
    y7 = models.SmallIntegerField(blank=True, null=True)
    default_flag = models.IntegerField(blank=True, null=True)
    creator_name = models.CharField(max_length=24, blank=True, null=True)
    comment_text = models.CharField(max_length=128, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'pt_skin'


class SkinType(models.Model):
    id = models.IntegerField(primary_key=True)
    skin_type = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'skin_type'


class StockAssembly(models.Model):
    parent_branded_part = models.OneToOneField(BrandedPart, models.DO_NOTHING, primary_key=True)  # The composite primary key (parent_branded_part_id, child_branded_part_id, attachment_point_id) found, that is not supported. The first column is selected.
    child_branded_part = models.ForeignKey(BrandedPart, models.DO_NOTHING, related_name='stockassembly_child_branded_part_set')
    attachment_point = models.ForeignKey(AttachmentPoint, models.DO_NOTHING)
    config_default = models.SmallIntegerField()
    physics_default = models.SmallIntegerField()

    class Meta:
        managed = True
        db_table = 'stock_assembly'
        unique_together = (('parent_branded_part', 'child_branded_part', 'attachment_point'), ('parent_branded_part', 'child_branded_part', 'attachment_point'),)


class StockVehicleAttributes(models.Model):
    branded_part = models.OneToOneField(BrandedPart, models.DO_NOTHING, primary_key=True)
    car_class = models.ForeignKey('SvaCarClass', models.DO_NOTHING, db_column='car_class', blank=True, null=True)
    ai_restriction_class = models.IntegerField(blank=True, null=True)
    mode_restriction = models.ForeignKey('SvaModeRestriction', models.DO_NOTHING, db_column='mode_restriction', blank=True, null=True)
    sponsor = models.IntegerField(blank=True, null=True)
    vin_branded_part = models.ForeignKey(BrandedPart, models.DO_NOTHING, related_name='stockvehicleattributes_vin_branded_part_set', blank=True, null=True)
    track_id = models.IntegerField(blank=True, null=True)
    vin_crc = models.IntegerField()
    retail_price = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'stock_vehicle_attributes'


class SvaCarClass(models.Model):
    sva_car_class = models.IntegerField(primary_key=True)
    description = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'sva_car_class'


class SvaModeRestriction(models.Model):
    sva_mode_restriction = models.IntegerField(primary_key=True)
    description = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'sva_mode_restriction'


class Vehicle(models.Model):
    id = models.OneToOneField(Part, models.DO_NOTHING, db_column='id', primary_key=True)
    skin = models.ForeignKey(PtSkin, models.DO_NOTHING)
    flags = models.IntegerField()
    class_field = models.SmallIntegerField(db_column='class')  # Field renamed because it was a Python reserved word.
    info_setting = models.SmallIntegerField()
    damage_info = models.BinaryField(blank=True, null=True)
    damage_cached = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'vehicle'


class Warehouse(models.Model):
    branded_part_id = models.IntegerField(primary_key=True)  # The composite primary key (branded_part_id, skin_id, player_id) found, that is not supported. The first column is selected.
    skin_id = models.IntegerField()
    player_id = models.IntegerField()
    qty_avail = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'warehouse'
        unique_together = (('branded_part_id', 'skin_id', 'player_id'),)
