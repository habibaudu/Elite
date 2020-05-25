from rest_framework import exceptions, serializers
from users_app.models import User
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

    
