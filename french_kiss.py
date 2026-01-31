import sys
import os
import requests
import json
import subprocess
from datetime import datetime

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_database():
    red = "\033[31m"
    yellow = "\033[33m"
    dark_gray = "\033[90m"
    reset = "\033[0m"
    
    database_text = f"""
{red}Базы данных находящиеся на серверах:{red}

{yellow}Сбербанк (клиенты):{yellow} {dark_gray}~200 млн.{dark_gray}                 {yellow}Delivery Club / Яндекс.Еда:{yellow} {dark_gray}22 млн.{dark_gray}               {yellow}Wildberries:{yellow} {dark_gray}34 млн.{dark_gray}
{yellow}DNS-shop:{yellow} {dark_gray}11 млн.{dark_gray}                             {yellow}Юла (Yula):{yellow} {dark_gray}30 млн.{dark_gray}                               {yellow}Avito (учетки):{yellow} {dark_gray}35 млн.{dark_gray}
{yellow}2ГИС (сотрудники):{yellow} {dark_gray}225 тыс.{dark_gray}                   {yellow}Магнит (персонал):{yellow} {dark_gray}130 тыс.{dark_gray}                       {yellow}СберСпасибо:{yellow} {dark_gray}5.2 млн.{dark_gray}
{yellow}HeadHunter (hh.ru):{yellow} {dark_gray}40 млн.{dark_gray}                   {yellow}Госуслуги (данные):{yellow} {dark_gray}~140 млн.{dark_gray}                     {yellow}Билайн (абоненты):{yellow} {dark_gray}8.7 млн.{dark_gray}
{yellow}МТС (клиенты):{yellow} {dark_gray}3.7 млн.{dark_gray}                       {yellow}МегаФон (база):{yellow} {dark_gray}1 млн.{dark_gray}                            {yellow}Tele2 (полная база):{yellow} {dark_gray}126 млн.{dark_gray}
{yellow}Тинькофф Банк:{yellow} {dark_gray}30 млн.{dark_gray}                        {yellow}Альфа-Банк (клиенты):{yellow} {dark_gray}3.5 тыс.{dark_gray}                    {yellow}ВТБ (спецвыборка):{yellow} {dark_gray}60 тыс.{dark_gray}
{yellow}Банк Открытие:{yellow} {dark_gray}10 млн.{dark_gray}                        {yellow}Почта Банк:{yellow} {dark_gray}780 тыс.{dark_gray}                              {yellow}Райффайзенбанк:{yellow} {dark_gray}800 тыс.{dark_gray}
{yellow}QIWI кошельки:{yellow} {dark_gray}22 млн.{dark_gray}                        {yellow}Яндекс.Такси (партнеры):{yellow} {dark_gray}15 млн.{dark_gray}                  {yellow}Ситимобил:{yellow} {dark_gray}33 млн.{dark_gray}
{yellow}ВкусВилл:{yellow} {dark_gray}2.5 млн.{dark_gray}                            {yellow}Перекресток:{yellow} {dark_gray}2.7 млн.{dark_gray}                             {yellow}Лента (база):{yellow} {dark_gray}130 тыс.{dark_gray}
{yellow}Ашан (сотрудники):{yellow} {dark_gray}1.4 тыс.{dark_gray}                   {yellow}Детский мир:{yellow} {dark_gray}567 тыс.{dark_gray}                             {yellow}Lamoda:{yellow} {dark_gray}11 млн.{dark_gray}
{yellow}Wildberries (фулл):{yellow} {dark_gray}50 млн.{dark_gray}                   {yellow}Ozon:{yellow} {dark_gray}9 млн.{dark_gray}                                      {yellow}Связной:{yellow} {dark_gray}22 млн.{dark_gray}
{yellow}Евросеть:{yellow} {dark_gray}20 млн.{dark_gray}                             {yellow}М.Видео:{yellow} {dark_gray}3.4 млн.{dark_gray}                                 {yellow}Эльдорадо:{yellow} {dark_gray}5.6 млн.{dark_gray}
{yellow}Ситилинк:{yellow} {dark_gray}2.8 млн.{dark_gray}                            {yellow}Онлайнер:{yellow} {dark_gray}4.2 млн.{dark_gray}                                {yellow}ТопШоп (TopShop):{yellow} {dark_gray}2.1 млн.{dark_gray}
{yellow}Гемотест (лаборатория):{yellow} {dark_gray}400 тыс.{dark_gray}              {yellow}Инвитро:{yellow} {dark_gray}4.5 млн.{dark_gray}                                 {yellow}Сбераптека:{yellow} {dark_gray}220 тыс.{dark_gray}
{yellow}Столото (лотореи):{yellow} {dark_gray}3 млн.{dark_gray}                     {yellow}1xBet:{yellow} {dark_gray}28 млн.{dark_gray}                                    {yellow}Фонбет:{yellow} {dark_gray}1.2 млн.{dark_gray}
{yellow}ВКонтакте (устаревшие базы):{yellow} {dark_gray}100 млн+.{dark_gray}        {yellow}Одноклассники (утечки):{yellow} {dark_gray}30 млн+.{dark_gray}                  {yellow}Mail.ru Group (старые):{yellow} {dark_gray}25 млн.{dark_gray}
{yellow}Яндекс (устаревшие хэши):{yellow} {dark_gray}50 млн.{dark_gray}             {yellow}Rambler (старая база):{yellow} {dark_gray}98 млн.{dark_gray}                    {yellow}Пикабу (Pikabu):{yellow} {dark_gray}8.5 млн.{dark_gray}
{yellow}Дром (Drom.ru):{yellow} {dark_gray}12.5 млн.{dark_gray}                     {yellow}Авто.ру:{yellow} {dark_gray}28 млн.{dark_gray}                                  {yellow}НН.ру (городской портал):{yellow} {dark_gray}2.7 млн.{dark_gray}
{yellow}Билеты.ру (концерты):{yellow} {dark_gray}7 млн.{dark_gray}                  {yellow}Kassir.ru:{yellow} {dark_gray}2.1 млн.{dark_gray}                               {yellow}Афиша.ру:{yellow} {dark_gray}1.2 млн.{dark_gray}
{yellow}Спортмастер:{yellow} {dark_gray}2.3 млн.{dark_gray}                         {yellow}Adidas Russia:{yellow} {dark_gray}340 тыс.{dark_gray}                           {yellow}Reebok Russia:{yellow} {dark_gray}180 тыс.{dark_gray}
{yellow}М.Видео (сотрудники):{yellow} {dark_gray}1.3 тыс.{dark_gray}                {yellow}СберЗдоровье:{yellow} {dark_gray}500 тыс.{dark_gray}                            {yellow}Яндекс.Здоровье:{yellow} {dark_gray}200 тыс.{dark_gray}
{yellow}Национальная Медиа Группа:{yellow} {dark_gray}1.1 тыс.{dark_gray}           {yellow}Газпромбанк (старая):{yellow} {dark_gray}15 тыс.{dark_gray}                     {yellow}МКБ (Московский Кредитный Банк):{yellow} {dark_gray}1.2 млн.{dark_gray}
{yellow}Совкомбанк:{yellow} {dark_gray}5.7 млн.{dark_gray}                          {yellow}Хоум Кредит Банк:{yellow} {dark_gray}500 тыс.{dark_gray}                        {yellow}Ренессанс Кредит:{yellow} {dark_gray}4.8 млн.{dark_gray}
{yellow}ТКС (Tinkoff Black):{yellow} {dark_gray}30 млн.{dark_gray}                  {yellow}Яндекс.Плюс:{yellow} {dark_gray}15 млн.{dark_gray}                              {yellow}Кинопоиск (учетки):{yellow} {dark_gray}8 млн.{dark_gray}
{yellow}IVI (ivi.ru):{yellow} {dark_gray}5.5 млн.{dark_gray}                        {yellow}More.tv:{yellow} {dark_gray}2.1 млн.{dark_gray}                                 {yellow}Start (стриминг):{yellow} {dark_gray}1.8 млн.{dark_gray}
{yellow}Яндекс.Музыка:{yellow} {dark_gray}10 млн.{dark_gray}                        {yellow}VK Музыка:{yellow} {dark_gray}12 млн.{dark_gray}                                {yellow}Zvuk (стриминг):{yellow} {dark_gray}1.5 млн.{dark_gray}
{yellow}СберМаркет:{yellow} {dark_gray}4.2 млн.{dark_gray}                          {yellow}Утконос:{yellow} {dark_gray}1.3 млн.{dark_gray}                                 {yellow}Азбука Вкуса:{yellow} {dark_gray}350 тыс.{dark_gray}
{yellow}Метро Кэш энд Керри (сотрудники):{yellow} {dark_gray}15 тыс.{dark_gray}     {yellow}Яндекс.Лавка:{yellow} {dark_gray}2.8 млн.{dark_gray}                            {yellow}Вайлдберриз (WB):{yellow} {dark_gray}34 млн.{dark_gray}
{yellow}Ozon (seller base):{yellow} {dark_gray}1.2 млн.{dark_gray}                  {yellow}Яндекс.Деньги (старая):{yellow} {dark_gray}45 млн.{dark_gray}                   {yellow}Вебмани (WM):{yellow} {dark_gray}25 млн.{dark_gray}
{yellow}PayPal Russia:{yellow} {dark_gray}4.5 млн.{dark_gray}                       {yellow}СБП (Система быстрых платежей, данные):{yellow} {dark_gray}16 млн.{dark_gray}   {yellow}Налоговая (служебные данные):{yellow} {dark_gray}неизв.{dark_gray}
{yellow}ПФР (данные пенсионеров):{yellow} {dark_gray}неизв.{dark_gray}              {yellow}МВД (служебные базы):{yellow} {dark_gray}неизв.{dark_gray}                      {yellow}РЖД (пассажиры):{yellow} {dark_gray}40 млн.{dark_gray}
{yellow}Аэрофлот (пассажиры):{yellow} {dark_gray}30 млн.{dark_gray}                 {yellow}S7 Airlines:{yellow} {dark_gray}12 млн.{dark_gray}                              {yellow}Уральские авиалинии:{yellow} {dark_gray}5 млн.{dark_gray}
{yellow}Ростелеком:{yellow} {dark_gray}3.3 млн.{dark_gray}                          {yellow}Дом.ру:{yellow} {dark_gray}1.8 млн.{dark_gray}                                  {yellow}МГТС:{yellow} {dark_gray}2.4 млн.{dark_gray}
{yellow}Корус (консалтинг):{yellow} {dark_gray}150 тыс.{dark_gray}                  {yellow}Финам (брокер):{yellow} {dark_gray}300 тыс.{dark_gray}                          {yellow}БКС Брокер:{yellow} {dark_gray}500 тыс.{dark_gray}
{yellow}Открытие Брокер:{yellow} {dark_gray}200 тыс.{dark_gray}                     {yellow}ВТБ Капитал:{yellow} {dark_gray}100 тыс.{dark_gray}                             {yellow}Сбер CIB:{yellow} {dark_gray}80 тыс.{dark_gray}
{yellow}Роснефть (сотрудники):{yellow} {dark_gray}1.5 млн.{dark_gray}               {yellow}Газпром (служебные данные):{yellow} {dark_gray}неизв.{dark_gray}                {yellow}Лукойл (сотрудники):{yellow} {dark_gray}200 тыс.{dark_gray}
{yellow}Росатом (контрагенты):{yellow} {dark_gray}неизв.{dark_gray}                 {yellow}Роскосмос (подрядчики):{yellow} {dark_gray}неизв.{dark_gray}                    {yellow}Рособрнадзор (ЕГЭ данные):{yellow} {dark_gray}неизв.{dark_gray}
{reset}
"""

    print(database_text)
    input("Нажмите Enter для продолжения...")
    clear_screen()
    print_banner()

def print_admin_info():
    dark_gray = "\033[90m"
    yellow = "\033[33m"
    reset = "\033[0m"
    
    admin_banner = f"""
{dark_gray}X+;;++++++x++;;;;;;;;;;;;;;;;;;;;:;;;;;;;;;;;;;;;;;;;;;;;;;;;+{yellow}Ник - нейм:{reset}{dark_gray}</> https://xss.ru | root@user:~#{dark_gray}
{dark_gray}&&&&$+;;;;+;+;;;;;;;;;;:;;;;;;;;;;:;;;;;;;;;;;;;;;;;;;;;;;;;+X{yellow}Юзер - нейм:{reset}{dark_gray}@xss_ru{dark_gray}
{dark_gray}$$$$$&&$X++;;;;;;;;;;;;;;;:;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;xX{yellow}Номер телефона:{reset}{dark_gray}NULL{dark_gray}
{dark_gray}$$$$$$$$$$x+;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;x++;;;;;xxx{yellow}CEO:{reset}{dark_gray}https://t.me/ceo_xss_ru{dark_gray}
{dark_gray}$$$$$$$$$$X+;;;;;;;;;;;;;;;;;;;;;++;+xxx+++xXXx+;;;xxx;;;;+xxx{yellow}Xss - ru:{reset}{dark_gray}https://xss.ru{dark_gray}
{dark_gray}XXXX$$$$$$$x;;;;;;;;;;;;;;+;;;++++xx++XXxxxX$XXXx+;xXX;;;+xxxx{yellow}Xss - Search bot:{reset}{dark_gray}@xss_ru_search_bot{dark_gray}
{dark_gray}XXXXXXXXXX$X+;;;;;;;;;;;;;++++;++xxxxxxXXX$$$$$$$$X$XX+;+xxxxx{yellow}Xss - snoser bot:{reset}{dark_gray}@xss_ru_snoser_bot{dark_gray}
{dark_gray}xXxxxxXXXXXXx;;;;;;;+++;;++xx+++xxxXXXxx$$$$$$$$$$$$$$++xxxxxx{yellow}Xss - parser bot:{reset}{dark_gray}@xss_ru_parser_bot{dark_gray}
{dark_gray}xxxxxxxxxxxxx+;;;;;;+xxx++xxxxxxXXXXXXXX$$$$$$$$$$$$$$++xxxxXX{yellow}Xss - tools bot:{reset}{dark_gray}@xss_ru_tool_bot{dark_gray}
{dark_gray}xxxxxxxxxxxxxx+;;;;+xxXXXxxxXXXXXXXXXXX$$$$$$$$$$$$$$$++xxxXXX{yellow}Channel:{reset}{dark_gray}https://t.me/+yqwTnu4uLmRhNDFk{dark_gray}
{dark_gray}xxxxxxxxxxx+X$+;;;+xXXXXXXXXXXXXXXXXXXX$$$$$$$$$$$$$$x;+xXXxxx{dark_gray}
{dark_gray}xxxxxxxxxx+;;xx+;;xXXXXXXXXXXXXXXXXXXXXX$$$$$$$$$XXXx+;+x++++x{dark_gray}
{dark_gray}xxxxxxx+;;;;;;XX+;xXXXx+x++++++xxxxXXXXX$$$$$Xx++++++Xxx++++++{dark_gray}
{dark_gray}xxxxx+:;;;:;;:xxx+xXXXxx++++++++;++xxxXXXXXxxxxxxxXX$$$$$XXx++{dark_gray}
{dark_gray}xxx;::;;::;;;;;+xXXXXXXxx++++;;+x+++xxXXXXxx+;+X$xX$$$$$$$$XXX{dark_gray}
{dark_gray}xx;;;;;:::;:;;::xXXXXXXXXxxxxx+xXx+xxxX$$XXxxXXXX$$$$$$$$$$$XX{dark_gray}
{dark_gray}x;;;;;:::::::::::+XXXXX$$XXXXXXXXxxxXXX$$$XXX$$$$$$$X$$$$$XXXX{yellow}Не много обо мне:{reset}
{dark_gray};;;;;::::::::::::;;;XXXXX$$$XXXXXXXXXXX$$$$$$$$$$$$X+xXXXXXXXX{yellow}В комьюнити докса я нахожусь с 2020 года, не гонялся за феймом а только развивал свои способности{reset}
{dark_gray};;;:::::::::::::::;:+XXXXXX$$$$$$XXXXXX$$$$$$$$$$$$;+++xXXXXXx{yellow}В 2021 году мне стала не интересна тематика докса и я начал еще больше развивать себя, начал учить:{reset}
{dark_gray};;;::::::::::::::;;:;XXXXXX$$$$$$XXXXX$$$$$$$$$$$X;;;;+++xx+xX{yellow}Programming.{reset}
{dark_gray};::::::::::::::::::::+XXXXXXXXX$$$XXXX$$$$$$$$$$x;;;;;;++;+xXX{yellow}OSINT (все его ветви).{reset}
{dark_gray}:::::::::::::::::::::;XXXXXXXXX$$$$XX$$$$$$$$$$+;;;;;;;;;;;+XX{yellow}Kali/Arch Linux.{reset}
{dark_gray}::::::::::::::::::::::X$X$$$$$$$$$$$XXX$$$$$$$+:;::;;;;;;;;;;x{yellow}Pentesting.{reset}
{dark_gray}::::::::::::::::::;;::x$$X$$$$$$$$$$$$XXX$$$X+:::::::::::;;;;;{yellow}Social Engineering.{reset}
{dark_gray}::::::::::::::::::::::;+$$$X$$$$$XxxxxXXxXXXx::::::;;;::::;;:;{dark_gray}
{dark_gray}::::::::::::::::::::::::;;+XXX$$$$XXXXXXXXXX+:::;:::;:;;;;;;;:{yellow}За все время проведенное в комьюнити я не был валиднут ни разу!{reset}
{dark_gray}::::::::::::::::::::::::::;;;;;X$$$$$$$$$Xx;;;::::::;::::;;;;;{yellow}С начала 2026 года мной заинтересовалась Федеральная служба безопасности и с тех пор я работаю на них.{reset}
{dark_gray}:::::::::::;:::::::;;;;;::::::;;;+XXXXXx;;:::;:::::;;;;;;;;;;;{yellow}На данный момент учусь в колледже на Информационного безопасника.{reset}
{dark_gray}:::::::::::;;;::;;:;;:;;;;;::::::;;;;;;;:;;;;;;;;;;;;;;;;;;;;;{yellow}В будущем собираюсь встретиться с каждым своим фанатом и подарить ему свою книгу а так же мерч!{reset}
{dark_gray};;:::::::::;;;;;;;;;;;;;;;;;;;:::::;;;::::::;;;:;;;;;;;;;;;;;;{yellow}Ну а в остальном желаю вам только удачи, спасибо за внимание.{reset}
{reset}"""

    print(admin_banner)
    input("Нажмите Enter для продолжения...")
    clear_screen()
    print_banner()

def print_help():
    white = "\033[97m"
    yellow = "\033[33m"
    cyan = "\033[36m"
    reset = "\033[0m"
    
    help_text = f"""
{white}Скрипт French Kiss предназначен для агрегации информации из комбинированных открытых и закрытых баз данных.
После запуска вам будет предложено ввести номер нужного запроса (1-26). Затем - сам поисковый запрос.

{yellow}Пример использования:{white}
1. Запускаете скрипт.
2. Видите меню с номерами (как выше).
3. Вводите номер нужного типа поиска, например: {cyan}1{white}
4. Система запросит данные: {cyan}"Введите номер телефона (РФ, UA, KZ, UZ):"{white}
5. Вы вводите запрос, например: {cyan}+79161234567{white}
6. Система производит поиск по выбранной базе и выводит результаты.

{yellow}Формат ввода для некоторых запросов:{white}
- Телефон: {cyan}+7... / 8... / 380...{white} (в международном или локальном формате)
- Госномер РФ: {cyan}A777AA077{white} (буквы латиница/кириллица, регион)
- ИНН: {cyan}10 или 12 цифр{white}
- Адрес: {cyan}Москва, ул. Ленина, 10, кв 5{white} (можно частично)

{yellow}Важно:{white}
- Результаты зависят от полноты данных в агрегированных базах.
- Скрипт работает в автономном режиме (локальные дампы).
- Используйте команду {cyan}--database{white} для получения информации о структуре и источниках данных.

Для начала работы просто запустите скрипт и следуйте подсказкам в терминале.
{reset}"""
    print(help_text)
    input("Нажмите Enter для продолжения...")
    clear_screen()
    print_banner()

def print_banner():
    red = "\033[31m"
    yellow = "\033[33m"
    dark_gray = "\033[90m"
    reset = "\033[0m"
    
    banner = f"""{red}
  █████▒██▀███  ▓█████  ███▄    █  ▄████▄   ██░ ██       ██ ▄█▀ ██▓  ██████   ██████ 
▓██   ▒▓██ ▒ ██▒▓█   ▀  ██ ▀█   █ ▒██▀ ▀█  ▓██░ ██▒      ██▄█▒ ▓██▒▒██    ▒ ▒██    ▒    
▒████ ░▓██ ░▄█ ▒▒███   ▓██  ▀█ ██▒▒▓█    ▄ ▒██▀▀██░     ▓███▄░ ▒██▒░ ▓██▄   ░ ▓██▄     
░▓█▒  ░▒██▀▀█▄  ▒▓█  ▄ ▓██▒  ▐▌██▒▒▓▓▄ ▄██▒░▓█ ░██      ▓██ █▄ ░██░  ▒   ██▒  ▒   ██▒     
░▒█░   ░██▓ ▒██▒░▒████▒▒██░   ▓██░▒ ▓███▀ ░░▓█▒░██▓     ▒██▒ █▄░██░▒██████▒▒▒██████▒▒    
 ▒ ░   ░ ▒▓ ░▒▓░░░ ▒░ ░░ ▒░   ▒ ▒ ░ ░▒ ▒  ░ ▒ ░░▒░▒     ▒ ▒▒ ▓▒░▓  ▒ ▒▓▒ ▒ ░▒ ▒▓▒ ▒ ░  
 ░       ░▒ ░ ▒░ ░ ░  ░░ ░░   ░ ▒░  ░  ▒    ▒ ░▒░ ░     ░ ░▒ ▒░ ▒ ░░ ░▒  ░ ░░ ░▒  ░ ░ 
 ░ ░     ░░   ░    ░      ░   ░ ░ ░         ░  ░░ ░     ░ ░░ ░  ▒ ░░  ░  ░  ░  ░  ░    
          ░        ░  ░         ░ ░ ░       ░  ░  ░     ░  ░    ░        ░        ░ 
                                  ░                                   
{yellow}
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
French kiss - информационный агрегатор. Базы: 10 ТБ (публичные данные) + 17 ТБ (закрытые источники)
Использование - исключительно в исследовательских целях. Ответственность лежит на пользователе.

Доступные команды:
--database - базы данных. 
--help - инструкция.
--admin-info - информация о создателе.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
{dark_gray}
             Прямой поиск по дампам                           Юридические лица и структуры
┌──────────────────────────────────────────────────┐┌──────────────────────────────────────────────────┐
│ [1]  Телефон (РФ, UA, KZ, UZ)                    ││ [14] Юр. лицо по ОГРН                            │
│ [2]  Email (все домены)                          ││ [15] Юр. лицо по ИНН                             │
│ [3]  ФИО (Ф, ФИ, ФИО)                            ││ [16] ИП по ОГРНИП                                │
│ [4]  ИНН (физ/юр)                                ││ [17] ИП по ИНН                                   │
│ [5]  СНИЛС                                       ││ [18] Физ. лицо по ИНН                            │
│ [6]  Госномер РФ (A777AA07)                      ││ [19] Компании/ИП по ФИО                          │
│ [7]  Госномер UA (ВО4561АХ)                      ││ [20] Фин. отчётность по ОГРН                     │
│ [8]  VIN (XTA21150053965897)                     ││ [21] Фин. отчётность по ИНН                      │
│ [9]  IP-адрес (8.8.8.8)                          ││ [22] Госзакупки по ОГРН                          │
│ [10] Адрес (Москва, ул. Островитянова, 9к4, 94)  ││ [23] Госзакупки по ИНН                           │
│ [11] VK (vk.com/id1)                             ││ [24] Исполнит. производства по ОГРН              │
│ [12] OK (ok.ru/profile/58460)                    ││ [25] Исполнит. производства по ИНН               │
│ [13] FB (facebook.com/id12345)                   ││ [26] Банки по БИК                                │
└──────────────────────────────────────────────────┘└──────────────────────────────────────────────────┘
{reset}
"""
    print(banner)

def phone_search():
    phone = input("Введите номер телефона (РФ, UA, KZ, UZ): ").strip()
    
    yellow = "\033[33m"
    dark_gray = "\033[90m"
    reset = "\033[0m"
    
    api1_url = f"https://api.depsearch.sbs/quest={phone}?token=0jv8SQHONMpyRmyRKImo8jT1d4AYqsNu"
    api2_token = "7007109128:rLhEaKSf"
    api2_url = "https://leakosintapi.com/"
    
    all_results = []
    
    try:
        response1 = requests.get(api1_url)
        if response1.status_code == 200:
            data1 = response1.json()
            if "results" in data1 and data1["results"]:
                result = data1["results"][0]
                print(f"\nInformation by number: {phone}")
                items = list(result.items())
                for i, (key, value) in enumerate(items[:-1]):
                    if key != "data":
                        prefix = "├─" if i < len(items) - 2 else "└─"
                        print(f"{prefix}{yellow}{key}:{yellow} {dark_gray}{value}.{dark_gray}")
                all_results.append({"api": "API1", "data": result})
            else:
                print(f"\nNo results found in API1 for {phone}")
        else:
            print(f"\nAPI1 request failed with status code: {response1.status_code}")
    except Exception as e:
        print(f"\nError calling API1: {e}")
    
    try:
        data2 = {"token": api2_token, "request": phone, "limit": 100, "lang": "ru"}
        response2 = requests.post(api2_url, json=data2)
        if response2.status_code == 200:
            data2_result = response2.json()
            if "List" in data2_result:
                print(f"\nInformation by number: {phone}")
                first_db = list(data2_result["List"].keys())[0] if data2_result["List"] else "No results"
                if first_db != "No results":
                    db_data = data2_result["List"][first_db]
                    if "Data" in db_data and db_data["Data"]:
                        record = db_data["Data"][0]
                        items = list(record.items())
                        for i, (key, value) in enumerate(items[:-1]):
                            prefix = "├─" if i < len(items) - 2 else "└─"
                            print(f"{prefix}{yellow}{key}:{yellow} {dark_gray}{value}.{dark_gray}")
                all_results.append({"api": "API2", "data": data2_result})
            else:
                print(f"\nNo results found in API2 for {phone}")
        else:
            print(f"\nAPI2 request failed with status code: {response2.status_code}")
    except Exception as e:
        print(f"\nError calling API2: {e}")
    
    save_choice = input("\nВведите Y чтобы сохранить результат (Enter чтобы продолжить): ").strip().upper()
    if save_choice == "Y":
        save_to_html_french_kiss(phone, all_results)
        print("Результаты сохранены в french-kiss.html")
    
    input("\nНажмите Enter для продолжения...")
    clear_screen()
    print_banner()

def save_to_html_french_kiss(phone, results):
    from datetime import datetime
    
    current_date = datetime.now().strftime("%d.%m.%Y %H:%M:%S")
    
    # Получаем данные из обоих API
    api1_data = None
    api2_data = None
    
    for result in results:
        if result["api"] == "API1":
            api1_data = result["data"]
        elif result["api"] == "API2":
            api2_data = result["data"]
    
    # Создаем HTML с новой структурой
    html_content = f'''<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>French Kiss Report - {phone}</title>
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}
        
        body {{
            font-family: 'Courier New', monospace;
            background-color: #0a0a0a;
            color: #cccccc;
            line-height: 1.4;
            padding: 15px;
            min-height: 100vh;
        }}
        
        .container {{
            max-width: 1200px;
            margin: 0 auto;
            background-color: #111111;
            border: 1px solid #222222;
        }}
        
        .header {{
            padding: 20px;
            border-bottom: 1px solid #222222;
        }}
        
        .title {{
            color: #ffffff;
            font-size: 1.3em;
            font-weight: normal;
            margin-bottom: 5px;
            letter-spacing: 1px;
        }}
        
        .subtitle {{
            color: #666666;
            font-size: 0.85em;
        }}
        
        .metadata {{
            padding: 15px 20px;
            border-bottom: 1px solid #222222;
            font-size: 0.85em;
            color: #888888;
            display: flex;
            justify-content: space-between;
        }}
        
        .metadata-item {{
            margin-right: 20px;
        }}
        
        .content {{
            padding: 20px;
        }}
        
        .api-section {{
            margin-bottom: 30px;
        }}
        
        .api-header {{
            background-color: #151515;
            padding: 10px 15px;
            border-bottom: 1px solid #222222;
            color: #ffffff;
            font-size: 0.9em;
            margin-bottom: 15px;
        }}
        
        .api-content {{
            padding: 0 15px 15px 15px;
        }}
        
        .api-info {{
            color: #888888;
            font-size: 0.85em;
            margin-bottom: 15px;
            padding: 10px;
            border: 1px solid #333333;
            background-color: #0f0f0f;
        }}
        
        .record {{
            margin-bottom: 20px;
            padding-bottom: 20px;
            border-bottom: 1px solid #1a1a1a;
            display: flex;
            gap: 20px;
        }}
        
        .record:last-child {{
            margin-bottom: 0;
            padding-bottom: 0;
            border-bottom: none;
        }}
        
        .record-data {{
            flex: 1;
            min-width: 0;
        }}
        
        .record-photos {{
            width: 350px;
            flex-shrink: 0;
            display: flex;
            flex-direction: column;
        }}
        
        .photos-header {{
            color: #ffffff;
            font-size: 0.9em;
            margin-bottom: 15px;
            padding-bottom: 5px;
            border-bottom: 1px solid #333333;
            text-align: center;
        }}
        
        .photo-container {{
            width: 100%;
            margin-bottom: 15px;
            border: 1px solid #333333;
            border-radius: 4px;
            overflow: hidden;
            background-color: #151515;
        }}
        
        .photo-img {{
            width: 100%;
            height: 300px;
            object-fit: cover;
            display: block;
        }}
        
        .photo-info {{
            padding: 10px;
            background-color: #0f0f0f;
            border-top: 1px solid #333333;
        }}
        
        .photo-title {{
            color: #ffffff;
            font-size: 0.85em;
            margin-bottom: 5px;
        }}
        
        .photo-source {{
            color: #888888;
            font-size: 0.75em;
            word-break: break-all;
        }}
        
        .no-photo {{
            display: flex;
            align-items: center;
            justify-content: center;
            color: #666666;
            font-size: 0.9em;
            width: 100%;
            height: 300px;
            background-color: #0f0f0f;
        }}
        
        .record-line {{
            margin: 5px 0;
            display: flex;
            align-items: flex-start;
        }}
        
        .line-prefix {{
            color: #666666;
            margin-right: 8px;
            min-width: 10px;
            flex-shrink: 0;
        }}
        
        .record-key {{
            color: #888888;
            min-width: 140px;
            flex-shrink: 0;
        }}
        
        .record-value {{
            color: #cccccc;
            flex: 1;
            word-break: break-word;
        }}
        
        .data-group {{
            margin-bottom: 15px;
        }}
        
        .group-title {{
            color: #aaaaaa;
            font-size: 0.85em;
            margin-bottom: 8px;
            padding-left: 18px;
            text-transform: uppercase;
        }}
        
        .footer {{
            padding: 15px 20px;
            border-top: 1px solid #222222;
            color: #555555;
            font-size: 0.8em;
            text-align: center;
            background-color: #0f0f0f;
        }}
        
        .no-data {{
            color: #666666;
            font-style: italic;
            padding: 20px;
            text-align: center;
            border: 1px solid #222222;
        }}
        
        .api1-record {{
            margin-bottom: 15px;
            padding: 15px;
            border: 1px solid #333333;
            background-color: #0f0f0f;
        }}
        
        .api1-source {{
            color: #ff9900;
            font-size: 0.8em;
            margin-bottom: 10px;
            padding-bottom: 5px;
            border-bottom: 1px solid #444444;
        }}
        
        .api1-data {{
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
            gap: 10px;
        }}
        
        .api1-item {{
            margin: 3px 0;
        }}
        
        .api1-key {{
            color: #888888;
            font-size: 0.85em;
        }}
        
        .api1-value {{
            color: #cccccc;
            font-size: 0.85em;
            word-break: break-word;
        }}
        
        .photo-gallery {{
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(150px, 1fr));
            gap: 10px;
            margin-top: 10px;
        }}
        
        .gallery-photo {{
            width: 100%;
            height: 150px;
            border-radius: 4px;
            overflow: hidden;
            border: 1px solid #333333;
            background-color: #0f0f0f;
        }}
        
        .gallery-img {{
            width: 100%;
            height: 100%;
            object-fit: cover;
        }}
        
        .gallery-info {{
            color: #888888;
            font-size: 0.75em;
            text-align: center;
            margin-top: 5px;
            word-break: break-all;
        }}
        
        .summary {{
            padding: 15px;
            margin-bottom: 20px;
            border: 1px solid #222222;
            background-color: #151515;
        }}
        
        .summary-title {{
            color: #ffffff;
            font-size: 0.9em;
            margin-bottom: 10px;
        }}
        
        .summary-stats {{
            display: flex;
            gap: 20px;
            color: #888888;
            font-size: 0.85em;
        }}
        
        .summary-stat {{
            display: flex;
            flex-direction: column;
        }}
        
        .stat-value {{
            color: #cccccc;
            font-size: 1.1em;
        }}
        
        .stat-label {{
            color: #666666;
            font-size: 0.8em;
        }}
        
        @media (max-width: 900px) {{
            .record {{
                flex-direction: column;
            }}
            
            .record-photos {{
                width: 100%;
                order: -1;
                margin-bottom: 20px;
            }}
            
            .photo-container {{
                max-width: 400px;
                margin-left: auto;
                margin-right: auto;
            }}
            
            .api1-data {{
                grid-template-columns: 1fr;
            }}
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <div class="title">French Kiss Report</div>
            <div class="subtitle">Информационный агрегатор</div>
        </div>
        
        <div class="metadata">
            <div class="metadata-item">Дата: {current_date}</div>
            <div class="metadata-item">Запрос: {phone}</div>
        </div>
        
        <div class="content">
            <div class="summary">
                <div class="summary-title">ОБЩАЯ СТАТИСТИКА ПОИСКА</div>
                <div class="summary-stats">
'''
    
    # Собираем статистику
    api1_count = 0
    api2_count = 0
    total_records = 0
    total_leaks = 0
    
    if api1_data and "results" in api1_data:
        api1_count = len(api1_data["results"])
        total_records += api1_count
        total_leaks += len(set([r.get("data", "Unknown") for r in api1_data["results"]]))
    
    all_leaks = []
    if api2_data and "List" in api2_data:
        for db_name, db_data in api2_data.get("List", {}).items():
            if "Data" in db_data and db_data["Data"]:
                records = []
                for record in db_data["Data"]:
                    formatted_record = {}
                    for key, value in record.items():
                        if value:  
                            formatted_record[key] = value
                    if formatted_record:
                        records.append(formatted_record)
                
                if records:
                    all_leaks.append({
                        "db_name": db_name,
                        "records": records
                    })
                    api2_count += len(records)
        
        total_records += api2_count
        total_leaks += len(all_leaks)
    
    html_content += f'''
                    <div class="summary-stat">
                        <div class="stat-value">{total_records}</div>
                        <div class="stat-label">Всего записей</div>
                    </div>
                    <div class="summary-stat">
                        <div class="stat-value">{total_leaks}</div>
                        <div class="stat-label">Источников данных</div>
                    </div>
                    <div class="summary-stat">
                        <div class="stat-value">{api1_count}</div>
                        <div class="stat-label">API1 записей</div>
                    </div>
                    <div class="summary-stat">
                        <div class="stat-value">{api2_count}</div>
                        <div class="stat-label">API2 записей</div>
                    </div>
                </div>
            </div>
    '''
    
    # Секция API1
    if api1_data and "results" in api1_data and api1_data["results"]:
        html_content += '''
            <div class="api-section">
                <div class="api-header">API1 - ДАННЫЕ ИЗ ОТКРЫТЫХ БАЗ</div>
                <div class="api-content">
        '''
        
        if "search_time_seconds" in api1_data:
            html_content += f'''
                    <div class="api-info">
                        Время поиска: {api1_data["search_time_seconds"]} секунд | Найдено записей: {len(api1_data["results"])}
                    </div>
            '''
        
        for result in api1_data["results"]:
            source = result.get("data", "Unknown Source")
            
            html_content += f'''
                    <div class="api1-record">
                        <div class="api1-source">{source}</div>
                        <div class="api1-data">
            '''
            
            # Сортируем ключи для лучшего отображения
            sorted_keys = sorted(result.keys())
            for key in sorted_keys:
                if key != "data" and result[key]:
                    html_content += f'''
                            <div class="api1-item">
                                <span class="api1-key">{key}: </span>
                                <span class="api1-value">{result[key]}</span>
                            </div>
                    '''
            
            html_content += '''
                        </div>
                    </div>
            '''
        
        html_content += '''
                </div>
            </div>
        '''
    
    # Секция API2
    if all_leaks:
        html_content += '''
            <div class="api-section">
                <div class="api-header">API2 - ДАННЫЕ ИЗ УТЕЧЕК</div>
                <div class="api-content">
        '''
        
        for leak in all_leaks:
            html_content += f'''
                    <div class="api-section" style="margin-bottom: 20px; border: 1px solid #222222;">
                        <div class="api-header" style="margin-bottom: 0;">{leak["db_name"]}</div>
                        <div class="api-content">
            '''
            
            # Сначала собираем все записи для этой утечки
            records_with_photos = []
            photo_urls = []
            
            for record in leak["records"]:
                # Ищем URL аватарки
                avatar_url = None
                avatar_keys = ['Avatar', 'avatar', 'Photo', 'photo', 'ProfileImage', 'profile_image']
                for key in avatar_keys:
                    if key in record:
                        avatar_url = record[key]
                        break
                
                if avatar_url and avatar_url not in photo_urls:
                    photo_urls.append(avatar_url)
                
                records_with_photos.append({
                    'record': record,
                    'avatar_url': avatar_url
                })
            
            # Теперь отображаем все записи с фото в одном блоке
            for i, record_data in enumerate(records_with_photos):
                record = record_data['record']
                avatar_url = record_data['avatar_url']
                
                html_content += f'''
                        <div class="record">
                            <div class="record-data">
                '''
                
                # Группируем данные по категориям
                personal_info = {}
                contact_info = {}
                location_info = {}
                education_info = {}
                other_info = {}
                
                personal_fields = ['FirstName', 'LastName', 'NickName', 'Gender', 'BDay', 'Relationship']
                contact_fields = ['Phone', 'Email', 'VkID', 'Link']
                location_fields = ['City', 'Country', 'Region']
                education_fields = ['Education', 'University', 'School']
                
                for key, value in record.items():
                    if key in avatar_keys:
                        continue  # Аватарку обрабатываем отдельно
                    
                    if key in personal_fields:
                        personal_info[key] = value
                    elif key in contact_fields:
                        contact_info[key] = value
                    elif key in location_fields:
                        location_info[key] = value
                    elif key in education_fields:
                        education_info[key] = value
                    elif key not in ['Description', 'desc', 'Bio']:
                        other_info[key] = value
                
                # Описание отдельно
                description = record.get('Description') or record.get('desc') or record.get('Bio')
                
                # Выводим описание если есть
                if description:
                    html_content += f'''
                                <div class="data-group">
                                    <div class="group-title">Описание</div>
                                    <div class="record-line">
                                        <div class="record-value" style="color: #aaaaaa; font-style: italic;">"{description}"</div>
                                    </div>
                                </div>
                    '''
                
                # Личная информация
                if personal_info:
                    html_content += '''
                                <div class="data-group">
                                    <div class="group-title">Личная информация</div>
                    '''
                    for key, value in personal_info.items():
                        html_content += f'''
                                    <div class="record-line">
                                        <span class="line-prefix">├─</span>
                                        <span class="record-key">{key}:</span>
                                        <span class="record-value">{value}</span>
                                    </div>
                        '''
                    html_content += '''
                                </div>
                    '''
                
                # Контактная информация
                if contact_info:
                    html_content += '''
                                <div class="data-group">
                                    <div class="group-title">Контактная информация</div>
                    '''
                    for key, value in contact_info.items():
                        html_content += f'''
                                    <div class="record-line">
                                        <span class="line-prefix">├─</span>
                                        <span class="record-key">{key}:</span>
                                        <span class="record-value">{value}</span>
                                    </div>
                        '''
                    html_content += '''
                                </div>
                    '''
                
                # Локация
                if location_info:
                    html_content += '''
                                <div class="data-group">
                                    <div class="group-title">Местоположение</div>
                    '''
                    for key, value in location_info.items():
                        html_content += f'''
                                    <div class="record-line">
                                        <span class="line-prefix">├─</span>
                                        <span class="record-key">{key}:</span>
                                        <span class="record-value">{value}</span>
                                    </div>
                        '''
                    html_content += '''
                                </div>
                    '''
                
                # Образование
                if education_info:
                    html_content += '''
                                <div class="data-group">
                                    <div class="group-title">Образование</div>
                    '''
                    for key, value in education_info.items():
                        html_content += f'''
                                    <div class="record-line">
                                        <span class="line-prefix">├─</span>
                                        <span class="record-key">{key}:</span>
                                        <span class="record-value">{value}</span>
                                    </div>
                        '''
                    html_content += '''
                                </div>
                    '''
                
                # Прочая информация
                if other_info:
                    html_content += '''
                                <div class="data-group">
                                    <div class="group-title">Дополнительно</div>
                    '''
                    for key, value in other_info.items():
                        html_content += f'''
                                    <div class="record-line">
                                        <span class="line-prefix">├─</span>
                                        <span class="record-key">{key}:</span>
                                        <span class="record-value">{value}</span>
                                    </div>
                        '''
                    html_content += '''
                                </div>
                    '''
                
                html_content += '''
                            </div>
                '''
                
                # Блок с фото
                html_content += '''
                            <div class="record-photos">
                                <div class="photos-header">ФОТО ИЗ УТЕЧКИ</div>
                '''
                
                if avatar_url:
                    name = f"{record.get('FirstName', '')} {record.get('LastName', '')}".strip()
                    if not name:
                        name = record.get('NickName', 'Пользователь')
                    
                    html_content += f'''
                                <div class="photo-container">
                                    <img src="{avatar_url}" alt="{name}" class="photo-img" onerror="this.style.display='none'; this.parentNode.innerHTML='<div class=\\'no-photo\\'>Фото недоступно</div>';">
                                    <div class="photo-info">
                                        <div class="photo-title">{name}</div>
                                        <div class="photo-source">
                                            Источник: {leak["db_name"]}<br>
                                            URL: {avatar_url[:80]}{'...' if len(avatar_url) > 80 else ''}
                                        </div>
                                    </div>
                                </div>
                    '''
                    
                    # Если есть дополнительные фото в других записях этой же утечки
                    if i == 0 and len(photo_urls) > 1:
                        html_content += '''
                                <div class="photos-header" style="margin-top: 20px;">ДОПОЛНИТЕЛЬНЫЕ ФОТО</div>
                                <div class="photo-gallery">
                        '''
                        
                        for j, photo_url in enumerate(photo_urls[1:6]):  # Ограничим 5 дополнительными фото
                            html_content += f'''
                                    <div class="gallery-photo">
                                        <img src="{photo_url}" alt="Доп. фото {j+1}" class="gallery-img" onerror="this.style.display='none'; this.parentNode.innerHTML='<div class=\\'no-photo\\' style=\\'height:150px;\\'>Фото {j+1}</div>';">
                                        <div class="gallery-info">Фото {j+1}</div>
                                    </div>
                            '''
                        
                        if len(photo_urls) > 6:
                            html_content += f'''
                                    <div class="gallery-photo">
                                        <div class="no-photo" style="height:150px;">+{len(photo_urls)-6}</div>
                                        <div class="gallery-info">Еще фото</div>
                                    </div>
                            '''
                        
                        html_content += '''
                                </div>
                        '''
                else:
                    html_content += '''
                                <div class="photo-container">
                                    <div class="no-photo">Фото не найдено в утечке</div>
                                </div>
                    '''
                
                html_content += '''
                            </div>
                        </div>
                '''
            
            html_content += '''
                        </div>
                    </div>
            '''
        
        html_content += '''
                </div>
            </div>
        '''
    
    # Если нет данных вообще
    if not api1_data and not all_leaks:
        html_content += '''
            <div class="api-section">
                <div class="api-header">РЕЗУЛЬТАТЫ ПОИСКА</div>
                <div class="api-content">
                    <div class="no-data">По данному запросу не найдено информации ни в одном источнике</div>
                </div>
            </div>
        '''
    
    html_content += f'''
        </div>
        
        <div class="footer">
            © French-kiss.com | Использование исключительно в исследовательских целях<br>
            Данные получены из API1 и API2 источников
        </div>
    </div>
    
    <script>
        // Добавляем обработчик ошибок для изображений
        document.addEventListener('DOMContentLoaded', function() {{
            const images = document.querySelectorAll('img');
            images.forEach(img => {{
                img.addEventListener('error', function() {{
                    if (!this.parentNode.querySelector('.no-photo')) {{
                        const noPhoto = document.createElement('div');
                        noPhoto.className = 'no-photo';
                        noPhoto.textContent = 'Фото недоступно';
                        this.parentNode.innerHTML = '';
                        this.parentNode.appendChild(noPhoto);
                    }}
                }});
            }});
        }});
    </script>
</body>
</html>'''
    
    filename = f"french-kiss-{phone.replace('+', '').replace(' ', '')}.html"
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    return filename

def main():
    print_banner()
    while True:
        user_input = input("root@search:~# ").strip()
        if user_input == "--database":
            print_database()
        elif user_input == "--admin-info":
            print_admin_info()
        elif user_input == "--help":
            print_help()
        elif user_input == "1":
            phone_search()
        elif user_input:
            break

if __name__ == "__main__":
    main()
