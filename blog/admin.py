from django.contrib import admin
from .models import Profile
from django.utils.safestring import mark_safe


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['get_image', 'full_name', 'date_of_birth', 'email', 'phone', 'status', 'gender', 'created_at',]
    search_fields = ['first_name', 'last_name', 'email', 'phone',]
    list_filter =['date_of_birth', 'status', 'gender',]
    readonly_fields = ['created_at']
    list_editable = ['email', 'phone', 'status']
    
    def get_image(self, obj):
        if obj.image:
            return mark_safe(f"<img src={obj.image.url}  width='100px' height='100px' >")
        return 'Нету изображения'
    
    # def image_for_site(self, obj):
    #     if obj.image:
    #         return mark_safe(f"<img src={obj.image.url} alt='Avatar' class='img-fluid my-5' style='width:80px;'/>")
    #     return 'Нету изображения'
            
