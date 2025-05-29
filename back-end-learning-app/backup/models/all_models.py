from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator, EmailValidator

class Category(models.Model):
    category_name = models.CharField(
        max_length=255,
        blank=False,
        null=False,
        db_index=True
    )

    created_at = models.DateTimeField(
        blank=True,
        null=True,
        auto_now_add=True,
        db_index=True
    )
    updated_at = models.DateTimeField(
        blank=True,
        null=True,
        auto_now=True,
        db_index=True
    )

    class Meta:
        db_table = 'category'

    def __str__(self):
        return self.category_name
    
    def save(self, *args, **kwargs):
        self.category_name = self.category_name.title()
        super(Category, self).save(*args, **kwargs)


class Comment(models.Model):
    content = models.TextField()
    user = models.ForeignKey(
        'User',
        models.CASCADE,
        blank=False,
        null=False,
        db_index=True
    )
    course = models.ForeignKey(
        'Course',
        models.CASCADE,
        blank=False,
        null=False,
        db_index=True
    )

    created_at = models.DateTimeField(
        blank=True,
        null=True,
        auto_now_add=True,
        db_index=True
    )
    updated_at = models.DateTimeField(
        blank=True,
        null=True,
        auto_now=True,
        db_index=True
    )

    class Meta:
        db_table = 'comment'

    def __str__(self):
        return f'{self.user} - {self.course} - {self.content}'


class Course(models.Model):
    title = models.CharField(
        max_length=200,
        blank=False,
        null=False,
        db_index=True
    )
    description = models.TextField(
        blank=False,
        null=False
    )
    price = models.FloatField(
        validators=[MinValueValidator(0)],
        db_index=True
    )
    instructor = models.ForeignKey(
        'User',
        models.CASCADE,
        blank=True,
        null=True,
        db_index=True
    )
    discount = models.ForeignKey(
        'Discount',
        models.SET_NULL,
        blank=True,
        null=True,
        db_index=True
    )
    extent = models.ForeignKey(
        'Extent',
        models.CASCADE,
        blank=False,
        null=False,
        db_index=True
    )

    created_at = models.DateTimeField(
        blank=True,
        null=True,
        auto_now_add=True,
        db_index=True
    )
    updated_at = models.DateTimeField(
        blank=True,
        null=True,
        auto_now=True,
        db_index=True
    )

    class Meta:
        db_table = 'course'

    def __str__(self):
        return f'{self.title} - {self.price} - {self.instructor}'
    
    def save(self, *args, **kwargs):
        super(Course, self).save(*args, **kwargs)


class CourseCategory(models.Model):
    course = models.ForeignKey(
        Course,
        models.CASCADE,
        blank=False,
        null=False,
        db_index=True
    )
    category = models.ForeignKey(
        Category,
        models.CASCADE,
        blank=False,
        null=False,
        db_index=True
    )

    created_at = models.DateTimeField(
        blank=False,
        null=False,
        auto_now_add=True,
        db_index=True
    )
    updated_at = models.DateTimeField(
        blank=False,
        null=False,
        auto_now=True,
        db_index=True
    )

    class Meta:
        db_table = 'course_category'

    def __str__(self):
        return f'{self.course} - {self.category}'
    
    def save(self, *args, **kwargs):
        super(CourseCategory, self).save(*args, **kwargs)


class CourseStatus(models.Model):
    course = models.ForeignKey(
        Course,
        models.CASCADE,
        blank=False,
        null=False,
        db_index=True
    )
    status = models.ForeignKey(
        'Status',
        models.CASCADE,
        blank=False,
        null=False,
        db_index=True
    )

    created_at = models.DateTimeField(
        blank=True,
        null=True,
        auto_now_add=True,
        db_index=True
    )
    updated_at = models.DateTimeField(
        blank=True,
        null=True,
        auto_now=True,
        db_index=True
    )

    class Meta:
        db_table = 'course_status'
        unique_together = ('course', 'status')

    def __str__(self):
        return f'{self.course} - {self.status}'


class Crypto(models.Model):
    currency_usd = models.DecimalField(
        max_digits=30,
        decimal_places=2,
        validators=[MinValueValidator(0)],
        null=False,
        blank=False,
        db_index=True
    )
    suply = models.DecimalField(
        max_digits=30,
        decimal_places=20,
        validators=[MinValueValidator(0)],
        null=False,
        blank=False
    )
    amount_buy = models.DecimalField(
        max_digits=30,
        decimal_places=20,
        validators=[MinValueValidator(0)],
        null=False,
        blank=False
    )
    amount_sell = models.DecimalField(
        max_digits=30,
        decimal_places=20,
        validators=[MinValueValidator(0)],
        null=False,
        blank=False
    )
    crypto_name = models.CharField(
        max_length=100,
        null=False,
        blank=False,
        db_index=True
    )
    url_img = models.CharField(
        max_length=100,
        null=False,
        blank=False
    )
    author = models.ForeignKey(
        'User',
        models.CASCADE,
        blank=False,
        null=False,
        db_index=True
    )

    created_at = models.DateTimeField(
        blank=True,
        null=True,
        auto_now_add=True,
        db_index=True
    )
    updated_at = models.DateTimeField(
        blank=True,
        null=True,
        auto_now=True,
        db_index=True
    )

    class Meta:
        db_table = 'crypto'

    def __str__(self):
        return f'{self.crypto_name} - {self.amount_buy} - {self.amount_sell}'
    
    def save(self, *args, **kwargs):
        super(Crypto, self).save(*args, **kwargs)


class Detaillesson(models.Model):
    name = models.CharField(
        max_length=100,
        blank=False,
        null=False,
        db_index=True
    )
    content = models.TextField(
        blank=False,
        null=False
    )
    lesson = models.ForeignKey(
        'Lesson',
        models.CASCADE,
        blank=False,
        null=False,
        db_index=True
    )
    extent = models.ForeignKey(
        'Extent',
        models.CASCADE,
        blank=False,
        null=False,
        db_index=True
    )

    created_at = models.DateTimeField(
        blank=True,
        null=True,
        auto_now_add=True,
        db_index=True
    )
    updated_at = models.DateTimeField(
        blank=True,
        null=True,
        auto_now=True,
        db_index=True
    )

    class Meta:
        db_table = 'detaillesson'

    def __str__(self):
        return f'Tên: {self.name}, Bài Học: {self.lesson}, Mức độ: {self.extent}'


class Discount(models.Model):
    discount_percentage = models.DecimalField(
        validators=[MinValueValidator(0), MaxValueValidator(100)],
        max_digits=5,
        decimal_places=2,
        blank=False,
        null=False,
        default=0.0,
        db_index=True
    )
    code_name = models.CharField(
        max_length=255,
        blank=False,
        null=False,
        db_index=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        blank=True,
        null=True,
        db_index=True
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        blank=True,
        null=True,
        db_index=True
    )

    class Meta:
        db_table = 'discount'

    def __str__(self):
        return f'{self.code_name} - {self.discount_percentage}%'


class Enrollment(models.Model):
    user = models.ForeignKey(
        'User',
        models.CASCADE,
        blank=False,
        null=False,
        db_index=True
    )
    course = models.ForeignKey(
        Course,
        models.CASCADE,
        blank=False,
        null=False,
        db_index=True
    )

    created_at = models.DateTimeField(
        blank=True,
        null=True,
        auto_now_add=True,
        db_index=True
    )
    updated_at = models.DateTimeField(
        blank=True,
        null=True,
        auto_now=True,
        db_index=True
    )

    class Meta:
        db_table = 'enrollment'

    def __str__(self):
        return f'{self.user} - {self.course}'


class Exercise(models.Model):
    title = models.CharField(
        max_length=255,
        db_index=True
    )
    description = models.TextField(
        blank=False,
        null=False
    )
    detail_lesson = models.ForeignKey(
        'Detaillesson',
        models.CASCADE,
        blank=False,
        null=False,
        db_index=True
    )
    extent = models.ForeignKey(
        'Extent',
        models.CASCADE,
        blank=False,
        null=False,
        db_index=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        blank=True,
        null=True,
        db_index=True
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        blank=True,
        null=True,
        db_index=True
    )

    class Meta:
        db_table = 'exercise'

    def __str__(self):
        return f'{self.title} - {self.extent}'


class Extent(models.Model):
    extent_name = models.CharField(
        max_length=100,
        blank=False,
        null=False,
        db_index=True
    )
    extent_time = models.PositiveIntegerField(
        validators=[MinValueValidator(1)],
        blank=False,
        null=False
    )

    created_at = models.DateTimeField(
        blank=True,
        null=True,
        auto_now_add=True,
        db_index=True
    )
    updated_at = models.DateTimeField(
        blank=True,
        null=True,
        auto_now=True,
        db_index=True
    )

    class Meta:
        db_table = 'extent'

    def __str__(self):
        return f'{self.extent_name} - {self.extent_time} minutes'


class Invoice(models.Model):
    user = models.ForeignKey(
        'User',
        models.CASCADE,
        blank=False,
        null=False,
        db_index=True
    )
    total = models.DecimalField(
        validators=[MinValueValidator(0)],
        max_digits=30,
        decimal_places=2,
        blank=False,
        null=False,
        db_index=True
    )
    status = models.ForeignKey(
        'Status',
        models.CASCADE,
        blank=False,
        null=False,
        db_index=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        blank=True,
        null=True,
        db_index=True
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        blank=True,
        null=True,
        db_index=True
    )

    class Meta:
        db_table = 'invoice'

    def __str__(self):
        return f'{self.user} - {self.total} - {self.status}'


class InvoiceDetails(models.Model):
    invoice = models.ForeignKey(
        Invoice,
        models.CASCADE,
        blank=False,
        null=False,
        db_index=True
    )
    shopping_cart_details = models.ForeignKey(
        'ShoppingcartDetails',
        models.CASCADE,
        blank=False,
        null=False,
        db_index=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        blank=True,
        null=True,
        db_index=True
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        blank=True,
        null=True,
        db_index=True
    )

    class Meta:
        db_table = 'invoicedetails'

    def __str__(self):
        return f'{self.invoice} - {self.shopping_cart_details}'


class Lesson(models.Model):
    name = models.CharField(
        max_length=255,
        blank=False,
        null=False,
        db_index=True
    )
    description = models.TextField(
        blank=False,
        null=False
    )
    course = models.ForeignKey(
        'Course',
        models.CASCADE,
        blank=False,
        null=False,
        db_index=True
    )
    instructor = models.ForeignKey(
        'User',
        models.CASCADE,
        blank=False,
        null=False,
        db_index=True
    )

    created_at = models.DateTimeField(
        blank=True,
        null=True,
        auto_now_add=True,
        db_index=True
    )
    updated_at = models.DateTimeField(
        blank=True,
        null=True,
        auto_now=True,
        db_index=True
    )

    class Meta:
        db_table = 'lesson'

    def __str__(self):
        return f'{self.name} - {self.course} - {self.instructor}'


class LessonStatus(models.Model):
    lesson = models.ForeignKey(
        Lesson,
        models.CASCADE,
        blank=False,
        null=False,
        db_index=True
    )
    status = models.ForeignKey(
        'Status',
        models.CASCADE,
        blank=False,
        null=False,
        db_index=True
    )

    created_at = models.DateTimeField(
        blank=True,
        null=True,
        auto_now_add=True,
        db_index=True
    )
    updated_at = models.DateTimeField(
        blank=True,
        null=True,
        auto_now=True,
        db_index=True
    )

    class Meta:
        db_table = 'lesson_status'
        unique_together = ('lesson', 'status')

    def __str__(self):
        return f'{self.lesson} - {self.status}'


class Payment(models.Model):
    user = models.ForeignKey(
        'User',
        models.CASCADE,
        blank=False,
        null=False,
        db_index=True
    )
    amount = models.DecimalField(
        validators=[MinValueValidator(0)],
        max_digits=30,
        decimal_places=20,
        blank=False,
        null=False,
        db_index=True
    )
    currency = models.CharField(
        max_length=50,
        blank=False,
        null=False,
        db_index=True
    )
    invoice = models.ForeignKey(
        'Invoice',
        models.CASCADE,
        blank=False,
        null=False,
        db_index=True
    )

    created_at = models.DateTimeField(
        blank=True,
        null=True,
        auto_now_add=True,
        db_index=True
    )
    updated_at = models.DateTimeField(
        blank=True,
        null=True,
        auto_now=True,
        db_index=True
    )

    class Meta:
        db_table = 'payment'

    def __str__(self):
        return f'{self.user} - {self.amount} - {self.invoice}'


class Status(models.Model):
    status_name = models.CharField(
        max_length=255,
        db_index=True
    )

    created_at = models.DateTimeField(
        blank=True,
        null=True,
        auto_now_add=True,
        db_index=True
    )
    updated_at = models.DateTimeField(
        blank=True,
        null=True,
        auto_now=True,
        db_index=True
    )

    class Meta:
        db_table = 'status'

    def __str__(self):
        return self.status_name


class Shoppingcart(models.Model):
    user = models.ForeignKey(
        'User',
        models.CASCADE,
        blank=False,
        null=False,
        db_index=True
    )

    created_at = models.DateTimeField(
        blank=True,
        null=True,
        auto_now_add=True,
        db_index=True
    )
    updated_at = models.DateTimeField(
        blank=True,
        null=True,
        auto_now=True,
        db_index=True
    )

    class Meta:
        db_table = 'shoppingcart'

    def __str__(self):
        return f'{self.user} - {self.created_at}'


class ShoppingcartDetails(models.Model):
    shopping_cart = models.ForeignKey(
        Shoppingcart,
        models.CASCADE,
        blank=False,
        null=False,
        db_index=True
    )
    course = models.ForeignKey(
        Course,
        models.CASCADE,
        blank=False,
        null=False,
        db_index=True
    )
    quantity = models.PositiveIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(1)],
        blank=False,
        null=False
    )

    created_at = models.DateTimeField(
        blank=True,
        null=True,
        auto_now_add=True,
        db_index=True
    )
    updated_at = models.DateTimeField(
        blank=True,
        null=True,
        auto_now=True,
        db_index=True
    )

    class Meta:
        db_table = 'shoppingcart_details'

    def __str__(self):
        return f'{self.shopping_cart} - {self.course} - {self.quantity}'


class User(models.Model):
    username = models.CharField(
        max_length=255,
        blank=False,
        null=False,
        unique=True,
        db_index=True
    )
    email = models.EmailField(
        max_length=255,
        blank=False,
        null=False,
        unique=True,
        db_index=True,
        validators=[EmailValidator()]
    )
    password = models.CharField(
        max_length=255,
        blank=False,
        null=False
    )

    created_at = models.DateTimeField(
        blank=True,
        null=True,
        auto_now_add=True,
        db_index=True
    )
    updated_at = models.DateTimeField(
        blank=True,
        null=True,
        auto_now=True,
        db_index=True
    )

    class Meta:
        db_table = 'user'

    def __str__(self):
        return self.username


class UserProfile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
        db_index=True
    )
    bio = models.TextField(
        blank=True,
        null=True
    )
    profile_picture = models.ImageField(
        upload_to='profile_pictures/',
        blank=True,
        null=True
    )

    created_at = models.DateTimeField(
        blank=True,
        null=True,
        auto_now_add=True,
        db_index=True
    )
    updated_at = models.DateTimeField(
        blank=True,
        null=True,
        auto_now=True,
        db_index=True
    )

    class Meta:
        db_table = 'user_profile'

    def __str__(self):
        return self.user.username
