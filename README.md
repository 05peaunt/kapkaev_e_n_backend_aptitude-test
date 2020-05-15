# kapkaev_e_n_backend_aptitude-test
Результат выполнения тестового задания



недостатки: 

1) проект сделан на Django==2.2.7
2) команды python manage.py rqworker default нет в docker-compose.yml, нужно запускать вручную перед python manage.py runserver
3) чеки рендерятся в формат html как указано в задании и сохраняются в папке media/html (открываются нормально), 
затем в формат pdf и сохраняются в папке 

media/pdf, но их не получается открыть( wkhtmltopdf ругается на кодировку, пробовал исправить, не получилось

4) порт локалхоста для postgres в файле docker-compose.yml - 5433

Все остальное работает как в задании
