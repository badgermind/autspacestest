# ReadMe
This project is to enable deployment of the front end code from:
https://github.com/alan-turing-institute/AutSPACEs/tree/build-tmp
 
##To import code be aware that:

### There has been some renaming of slugs
what_autism_is -> autism
experiences_page -> viewstories
about_us -> about
my_stories -> mystories

which affects .html templates and matching .css files

### partials
statements of the form
{% include 'main/partials/something.html' %}
should be changed to
{% include ‘partials/something.html' %}

### change of app name
{% url ‘main:old_slug_name’ %}
should become {% url ‘demo:newslugname’ %}

### static references (css, js, images) should not have a leading slash
{% static '/css/something.css' %}
should become
{% static 'css/something.css' %}
This appears to apply to html comments as well

## running locally under OSX
install  https://postgresapp.com/
copy env_template to .env and add a Django secret and your username 