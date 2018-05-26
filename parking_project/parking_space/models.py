from django.db import models


class ParkingSpace(models.Model):
    code = models.CharField(max_length=300, help_text='Identifier provided by the parking admin')
    camera = models.ForeignKey('camera.Camera', verbose_name='Camera input', related_name='parking_spaces')
    parking = models.ForeignKey('parking.Parking', related_name='parking_spaces')

    upper_right_x = models.IntegerField(verbose_name='Upper Right x')
    upper_right_y = models.IntegerField(verbose_name='Upper Right y')
    bottom_left_x = models.IntegerField(verbose_name='Bottom Left x')
    bottom_left_y = models.IntegerField(verbose_name='Bottom Left y')

    is_occupied = models.BooleanField(default=False)

    times_extended = models.IntegerField(null=True, blank=True)
    start_date = models.DateTimeField(null=True, blank=True)
    expiration_date = models.DateTimeField(null=True, blank=True)
