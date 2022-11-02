from privacy import password
from privacy import sender
import random
import smtplib


class SecretSanta:

    def __init__(self):
        self.info = dict()
        self.selection = dict()
        self.participants = 0
        self.budget = 0

    def get_info(self):
        self.participants = int(input('Сколько людей участвует в Тайном Санте?:'))
        self.budget = int(input('Какой бюджет вашего Тайного Санты?:'))

        for i in range(1, self.participants + 1):
            name = input('Какие имена участников {}?:'.format(i))
            email = input('Какие у них почты?: ')
            address = input('Какие у них адресы?: ')
            request = input('Что они хотят получить на праздник?: ')
            self.info[name] = [email, address, request]

    def assign(self):
        choices = [name for name in self.info]

        for person in self.info:
            secret_person = random.choice(choices)
            while secret_person == person or secret_person in self.selection:
                secret_person = random.choice(choices)
                if secret_person in self.selection and self.selection[secret_person] == person:
                    continue
                elif secret_person == person:
                    continue
                break
            self.selection[person] = secret_person
            ind = choices.index(secret_person)
            choices.pop(ind)

    def send_emails(self):
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender, password)
        print('Успешный вход.')
        for person, sp in self.selection.items():
            receiver = self.info[person][0]
            sp_address = self.info[sp][1]
            sp_request = self.info[sp][2]
            message = 'СУБЪЕКТ: ТАЙНЫ САНТА\n' \
                      'Привет {}, \n\n' \
                      'ТССС, имя того, кому ты должен подарить {}.\n\n' \
                      'Бюджет составляет ${}\n\n' \
                      'Список желаний: {}\n\n' \
                      'Адрес получателя подарка: {}\n\n' \
                      'Кайфуй!'.format(person, sp, self.budget, sp_request, sp_address)
            server.send_message(sender, receiver, message)
        print('Супер')
        server.quit

    def start(self):
        self.get_info()
        self.assign()
        self.send_emails()


if __name__ == '__main__':
    secret_santa = SecretSanta()
    secret_santa.start()