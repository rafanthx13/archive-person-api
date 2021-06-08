# Deploy in Heroku

1. Instalar Heroku CLI (Windows ou Linux)

2. Depois instalar no npm:
  + `npm install -g heroku`

3. Logar no Heroku CLI
  + ```
   heroku login -i
   ```

4. Criar projeto Heroku (cria remotamente)
 + `heroku create archive-person-api`

5. Set git remote heroku to https://git.heroku.com/archive-person-api.git
  + ````
    $ heroku git:remote -a archive-person-api` 
    ````
  + OutPut:
  ````
    Creating ⬢ archive-person-api... done
    https://archive-person-api.herokuapp.com/ | https://git.heroku.com/archive-person-api.git
  ````

6. Criar ClearDB/MySql no Heroku
  + `$ heroku addons:create cleardb:ignite` 
  + ````
    Creating cleardb:ignite on ⬢ archive-person-api... free
    Created cleardb-symmetrical-33358 as CLEARDB_DATABASE_URL
    Use heroku addons:docs cleardb to view documentation
    ````

7. Acesse as configuraçôes do banco e coloque em ENV e nas variáveis do Heroku
  + `heroku config | grep CLEARDB_DATABASE_URL`
  + Formato: `mysql://USER:PASSWORD@HOST/DB_NAME`
  + Com os dados passados, crio a conexâo com o banco de deploy e faço migrations, substituindo o DB por esse
  + Exemplo
    ````
    module.exports = {
      HOST: "us-cdbr-iron-east-02.cleardb.net",
      USER: "b7e2437887xxxa",
      PASSWORD: "0200xxx6",
      DB: "heroku_7643ec736354xxx"
    };
    ````

8. Você tem que setar 'DATABASE_URL'. 
  + Por CLI `heroku config:set DATABASE_URL='mysql://b7e2437887xxxa:0200xxx6@us-cdbr-iron-east-02.cleardb.net/heroku_7643ec736354xxx`
  + Verifique se está a url do mysql, porque, quando voce cria uma aplicaoa vem por default o postgres primeiro, e ela já coloca sua url lá. Essa URL posta pelo  postgres NÃO TEM COMO MUDAR, NEM DELETAR, A NÂO SER QUE VOCê TIRE ESSE ADD-ON. Depois de tirado ponha o 'DATABASE_URL' para o do mysql. Só assim vai funcionar. 
    SIM. Mesmo conifgurando manualmente no `settings.py` ele vai ler da 'DATABASE_URL' e vai acabar jogando pro postgres ao menos que o tire e coloque a do mysql
  + NÂO DEVE TER A PARTE DO RECONECT=TRUE
    

10. Baixe as libs e salve em requirements.txt

+ ````
     django-heroku==0.3.1
     django-environ==0.4.5
     gunicorn==20.1.0
  ````

11. Crie o Procfile
````
release: python manage.py makemigrations --no-input
release: python manage.py migrate --no-input

web: gunicorn archive_api.wsgi
````

12. Adicione no fim de `settings.py`

````
import django_heroku
django_heroku.settings(locals())
````
13. Fazer deploy para o heroku
+ `git push -u heroku master` | ou | `git push heroku HEAD:master`

14. Ver log do app heroku
+ `heroku logs --tail`