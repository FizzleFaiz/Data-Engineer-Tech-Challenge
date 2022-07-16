from crontab import CronTab 

cron = CronTab(user='user')

job = cron.new(command='python main.py')
job.minute.every(1)

cron.write()
