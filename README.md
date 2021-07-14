# ratemyfrogs

RateMyFrogs is the premier location for rating frogs of all shapes and sizes. All frogs are from Creative Commons and are on the Public Domain taken from the [Creative Commons Catalog API](https://api.creativecommons.engineering/v1/). Currently the website is live at [ratemyfrogs.com](https://www.ratemyfrogs.com)! Feel free to send a pull request, I'll be keeping an eye on this repo for a while for any new changes, bug fixes, and improvements to merge into development. Thanks for taking part in this cool project!

## main - local
### Requirements:
- python3.9
- django>=3.0,<4.0
- python-dotenv
- requests

⚠️ Recommended: Use virtualenv to set up the environment so that requirements do not conflict with any existing installations

### Steps to get it running:
1. clone the repository `git clone git@github.com:emilkovacev/ratemyfrogs.git`
2. enter the repository `cd ratemyfrogs/`
3. Install requirements `pip install -r requirements.txt`

3. generate .env file with a django secret key `python generate_key.py`
4. migrate database `python manage.py makemigrations && python manage.py migrate`
5. configure admin panel `python manage.py createsuperuser` and follow the instructions
6. populate database `python manage.py batch-populate 10`
7. run website `python manage.py runserver`
Access the [website](http://localhost:8000/) or [admin panel](http://localhost:8000/admin/) and login

*Disclaimer: ratemyfrogs **does not** collect or store any personally identifiable information from users. All images present on the website are labeled as on the public domain by Creative Commons.*
