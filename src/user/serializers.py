from rest_framework import serializers
from user.models import User


class UserDetailSerializer(serializers.ModelSerializer):
    """
    Serializer for User Model
    """
    password = serializers.CharField(
        style= {'input_type':'password'}
    )

    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name',
                  'email', 'password', 'username', 'is_staff')

    def create(self, validated_data):
        """
        Create and return a new `User` instance
        given the validated data.
        """
        print(validated_data)
        user=User.objects.create(**validated_data)
        user.set_password(validated_data['password'])
        user.save();
        return user;

    def update(self, instance, validated_data):
        """
        Update and return an existing `User` instance,
        given the validated data.
        """
        instance.first_name = validated_data.get(
            'first_name', instance.first_name)
        instance.last_name = validated_data.get(
            'last_name', instance.last_name)
        instance.email = validated_data.get(
            'email', instance.email)
        instance.username = validated_data.get(
            'username', instance.username)
        instance.is_staff = validated_data.get(
            'is_staff', instance.is_staff)
        instance.date_joined = validated_data.get(
            'date_joined', instance.date_joined)
        instance.save()
        return instance

class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for User Model
    """
    password = serializers.CharField(
        style= {'input_type':'password'}
    )
    class Meta:
        model = User
        fields = ('id',
                  'username', 'password')
