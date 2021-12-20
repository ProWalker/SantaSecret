import datetime
import json
import os
import smtplib
import ssl

from dotenv import load_dotenv
from game_helper import create_pairs


def get_games_db():
    with open('games.json', 'r') as games_db:
        return json.load(games_db)


def get_game_users(game_id):
    with open('users.json', 'r') as users_db:
        users = json.load(users_db)
        return [user for user in users['users'] if user['game_id'] == game_id]


def send_mail(receiver_email, message):
    smtp_server = os.getenv('SMTP_SERVER')
    smtp_port = os.getenv('SMTP_PORT')
    smtp_password = os.getenv('SMTP_PASSWORD')
    sender_email = os.getenv('SENDER_EMAIL')
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, int(smtp_port), context=context) as server:
        server.login(sender_email, smtp_password)
        server.sendmail(sender_email, receiver_email, message)


def main():
    load_dotenv()
    games_db = get_games_db()
    date_today = datetime.date.today()
    for game in games_db['games']:
        date_send = datetime.datetime.strptime(game['date_send'], '%d.%m.%Y').date()
        if date_today >= date_send:
            game_users = get_game_users(game['game_id'])
            for secret_santa, receiver in create_pairs(game_users):
                message = f"""\
                            Subject: Тайный санта

                            Название игры: {game["name_game"]}.
                            Вы должны отправить подарок пользователю {receiver["user_name"]}
                            на адрес {receiver["user_email"]}.
                            Предпочтения получателя {receiver["user_wishlist"]}.
                            Письмо получателя санте: {receiver["letter_to_santa"]}.
                            Ограничения по цене подарка: {game["limit_price"]}.
                            Дата отправки подарка: {game["date_send"]}"""
                send_mail(secret_santa['user_email'], message.encode('utf-8'))


if __name__ == '__main__':
    main()
