from Bank_account import *

Ali_Naderi = BankAccount(1000, "Ali")
Sara_Salmani = BankAccount(2000, "Sara")

Ali_Naderi.get_balance()
Sara_Salmani.get_balance()

Ali_Naderi.deposit(1500)

Ali_Naderi.withdraw(500)
Sara_Salmani.withdraw(2500)

Ali_Naderi.transfer(400, Sara_Salmani)

Mina_Ahmadi = IntrestRewardAccount(1000 , "Mina")
Mina_Ahmadi.get_balance()
Mina_Ahmadi.deposit(100)

Kian_Moradi = FeeAccount(1000 , "Kian")
Kian_Moradi.deposit(500)
Kian_Moradi.transfer(1000 , Ali_Naderi)
Kian_Moradi.transfer(100 , Sara_Salmani)
