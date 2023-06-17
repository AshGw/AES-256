## Installation ## 
### Docker ###
If you dont have docker already : 
<br>install it : 
<br>
**For wincdows :**
Visit this **[link](https://docs.docker.com/desktop/install/windows-install/)** 
<br>
**For Mac :** 
Visit this **[link](https://docs.docker.com/desktop/install/mac-install/)** 
<br>
**For Linux** : Visit the **[link](https://docs.docker.com/engine/install/)**

## Install & run the image ##
1) First step is to verify if docker is actually installed on your system , in the terminal run the command : 
```shell
docker --version
```
The result must contain information about Docker

2) Pulling the image
```shell
docker pull ashgw/ashcrypt:1.0
```
the image is quite lengthy so be patient with the installation process

3) run the image within a container and give it a name , here im giving it the name `nova`
```shell
docker run -it --name nova ashgw/ashcrypt:1.0
```
Now the container will run and it will automatically start the `CliCrypt.py` file 
<br>
Now if you want to simply use the container as a whole and look through the project and use different modules you can use 
```
docker exec -it nova bash
```
If you want to run the container with the same as you've ran it the first time use 
```
docker start -ia nova 
```
keep in  mind that you can either call by `id` or name.
<br>That's it so simple.
