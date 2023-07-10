from django.db import models

# Create your models here.


class AllFile(models.Model):
    file_name = models.FileField("", upload_to="media")

    def __str__(self):
        return self.file_name
    


class Transaction(models.Model):

    TRANSACTION_METHOD = [
        ('Payment', 'payment'),
        ('Withdraw', 'withdraw'),
    ]

    reciever_name = models.CharField("Reciever Name", max_length=255,)
    account_number = models.IntegerField("Account Number")
    ammount = models.IntegerField("Ammount")
    method = models.CharField('Transaction Method',
                              max_length=255, choices=TRANSACTION_METHOD)
