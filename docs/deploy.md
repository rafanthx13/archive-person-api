# Deploy in Heroku

1. Instalar Heroku CLI

2. `npm install -g heroku`

3. ```term
   heroku login -i
   ```

4. `heroku create archive-person-api`

5. + set git remote heroku to https://git.heroku.com/archive-person-api.git

6. `$ heroku git:remote -a archive-person-api` 
  Creating ⬢ archive-person-api... done
  https://archive-person-api.herokuapp.com/ | https://git.heroku.com/archive-person-api.git

``$ heroku addons:create cleardb:ignite`` (adicionar ClearDB:Mysql)
Creating cleardb:ignite on ⬢ archive-person-api... free
Created cleardb-symmetrical-33358 as CLEARDB_DATABASE_URL
Use heroku addons:docs cleardb to view documentation

6. `heroku config | grep CLEARDB_DATABASE_URL`
7. Com os dados passdos, crio a conexâo com o banco de deploy e faço migrations, substituindo o DB por esse
````
module.exports = {
  HOST: "us-cdbr-iron-east-02.cleardb.net",
  USER: "b7e2437887xxxa",
  PASSWORD: "0200xxx6",
  DB: "heroku_7643ec736354xxx"
};
````

7. Você tem que setar 'DATABASE_URL'. 
   ``heroku config:set DATABASE_URL='mysql://b7e2437887xxxa:0200xxx6@us-cdbr-iron-east-02.cleardb.net/heroku_7643ec736354xxx?reconnect=true'``
   
8. Verifique se está a url do mysql, porque, quando voce cria uma aplicaoa vem por default o postgres primeiro, e ela já coloca sua url lá. Essa URL posta pelo  postgres NÃO TEM COMO MUDAR, NEM DELETAR, A NÂO SER QUE VOCê TIRE ESSE ADD-ON. Depois de tirado ponha o 'DATABASE_URL' para o do mysql. Só assim vai funcionar. 
    SIM. Mesmo conifgurando manualmente no `settings.py` ele vai ler da 'DATABASE_URL' e vai acabar jogando pro postgres ao menos que o tire e coloque a do mysql

    NÂO DEVE TER A PARTE DO RECONECT=TRUE
    
9. Ponha as variaveis de ambietne no heroku e no seu env interno

10. Baixe as libs e salve em requirements.txt

11. ````
     django-heroku==0.3.1
     django-environ==0.4.5
     gunicorn==20.1.0
````
12. Crie o Procfile e adicione no fim de `settings.py`

````
import django_heroku
django_heroku.settings(locals())
````

## Deploy

``git push -u heroku master`` (fazer push par ao heroku, ele nao vai ler automaticamente do git)
ou
``git push heroku HEAD:master``


``heroku logs --tail``