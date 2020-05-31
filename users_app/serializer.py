from rest_framework import exceptions, serializers
from users_app.models import (User, Invent)
from users_app.utils.validation import ValidateUser


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id","email","first_name","last_name","password","is_active"]
        extra_kwargs = {"password":{"write_only":True}}

    def validate(self, data):
        validate_data = ValidateUser().validate_register(**data)
        if isinstance(validate_data,list):
            raise serializers.ValidationError({"errors":validate_data})
        return validate_data

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        user.set_password(validated_data.get("password"))
        user.save()
        return user


class LoginSerializer(serializers.Serializer):
    """ Login serializer"""
    email = serializers.EmailField()
    password = serializers.CharField()

    
class InventSerializer(serializers.ModelSerializer):
    state = serializers.SerializerMethodField()
    user = serializers.SerializerMethodField()
    class Meta:
        model = Invent
        fields = ["id","about_invention","title","invent_media","state","location","user",
                  "updated_at","created_at"]
    
    
    def validate(self, data):
        validated_data = ValidateUser().validate_invention(**data)

        if isinstance(validated_data,list):
            raise serializers.ValidationError({"errors":validated_data})
        invent_info = {key:value for key, value in data.items()}
        return Invent.objects.create(user_id=self.context['request'].user.id,
                                     **invent_info)
    
    def get_state(self,obj):
        return str(obj.state)

    def get_user(self,obj):
        return dict(
            id=obj.user.id,
            first_name=obj.user.first_name,
            last_name=obj.user.last_name,
            profile_image=obj.user.profile_image)
