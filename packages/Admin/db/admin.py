from django.contrib import admin

from .models import (AttachmentPoint, Player, Part, AbstractPartType, PlayerType, SkinType, Model, Profile, Key, Vehicle, Warehouse, StockVehicleAttributes, StockAssembly, BrandedPart, PartGrade, DriverClass, SvaCarClass, SvaModeRestriction)

# Register your models here.
admin.site.register(AttachmentPoint)
admin.site.register(Player)
admin.site.register(Part)
admin.site.register(AbstractPartType)
admin.site.register(PlayerType)
admin.site.register(SkinType)
admin.site.register(Model)
admin.site.register(Profile)
admin.site.register(Key)
admin.site.register(Vehicle)
admin.site.register(Warehouse)
admin.site.register(StockVehicleAttributes)
admin.site.register(StockAssembly)
admin.site.register(BrandedPart)
admin.site.register(PartGrade)
admin.site.register(DriverClass)
admin.site.register(SvaCarClass)
admin.site.register(SvaModeRestriction)
