from django.contrib.auth.base_user import BaseUserManager

class CustomUserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_product_buyer(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        self.is_productBuyer = True
        return self._create_user(email, password, **extra_fields)

    
    def _create_product_manager(self, email, first_name, last_name, location, phone, service_type, rate, password=None):
        product_manager = self.model(
            email=self.normalize(email),
            first_name=first_name,
            last_name=last_name,
            phone=phone,
            location=location,
            service_type=service_type,
        )
        product_manager.set_password(password)
        product_manager.is_productManager = True
        product_manager.save(using=self.db)
        return product_manager

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)