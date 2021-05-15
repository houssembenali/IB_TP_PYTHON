# IB_TP_PYTHON
Ceci est le TP demander par IB

## Configuration Jenkins

### Configuration prérequis Jenkins
Nous avons indiquer l'addresse relative de l'application Gradle pour que Jenkins réussie a executer la commande gradle.

![Screenshot](doc/jenkins_config_gradle.png)
*Capture d'écran de la configuration de Gradle 7.0.1 sur Jenkins*

### Configuration JOB Jenkins
Aprés la création d'un nouveau Job Jenkins, on va configurer le répo. Github comme indique l'imprime écran ci-dessous
PS : n'oublier pas de cocher la case de Github webhook.

![Screenshot](doc/jenkins_config_git.png)
*Capture d'écran de la configuration du répo. Github dans la config. du job*

On va configurer la dérniére étape du Job c'est la configuration du build on séléctionnant la version Gradle précédament configurer et indiquant la tâche Gradle a executer. 

![Screenshot](doc/jenkins_config_build.png)
*Capture d'écran de la configuration de l'étape Build Gradle indiquant la version Gradle et la tâche a executer*

## Configuration Webhook

Le Webhook va nous permettre d'envoyer un signal a une déstination pour par exemple déclancher un Job de Jenkins comme dans notre cas.
On commence par configurer le Webhook dans le répo. Github on fournissant l'addresse IP publique (aprés exposition de Jenkins à internet on configurant le routeur)

![Screenshot](doc/webhook_github.png)
*Capture d'écran de la configuration du Webhook dans le répo. Github*

Ci-dessous le commit déclancheur qui va déclancher un signal vers Jenkins qui va déclancher un Job build.

![Screenshot](doc/webhook_github_commit_declencheur.png)
*Capture d'écran du commit déclancheur de Webhook*

l'imprime écran ci-dessous nous affiche que le signal webhook a été envoyer avec succée (en vert)

![Screenshot](doc/webhook_github_success.png)
*Capture d'écran de l'état en succée du webhook Github vers Jenkins*

L'imprime écran ci-dessous indique que le job Jenkins a été executer suite au signal webhook reçu par github.

![Screenshot](doc/webhook_jenkins_lunched.png)
*Capture d'écran du lancement du job Jenkins suis signal webhook envoyé par Github*

On indique ici le log des événnement webhook Jenkins reçu de la part de Github.

![Screenshot](doc/webhook_jenkins_preuve.png)
*Capture d'écran du log de la rebrique webhook sur Jenkins*
