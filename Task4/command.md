### Scenariusz 1
```
docker volume create --name TestVolume
docker volume ls
docker run -v TestMount -it ubuntu
ls -l
cd TestMount/
touch demo.txt
nano demo.txt
docker ps
docker inspect NAME 
```
Na W10 podaje jakąś dziwną ścieżke wiec trzeba przejsc do katalogu 
`\\wsl$\docker-desktop-data\version-pack-data\community\docker\volumes`

Po ustawianiu dostępnego w W10 wolumenu był dostepny folder ale nie było jego zawartości pomimo tego, że zawartość była widoczna na W10
Ustawiane też jako -v były te woluminy z długim hash ale też nie chciało działac dla alpine a ubuntu nie mogłem zainstalować nano ani vima

Po wykonaiu poniższych komend w drugim kontenerze nie ma tego pliku - ciezko stwierdzić czemu tak jest
```
docker volume create --name TestVolume
docker run -v TestVolume -it ubuntu
echo "Hello world!" > demo.txt
docker run -v TestVolume -it ubuntu
```

### Scenariusz 2
```
docker run -v c:/coding:/coding -it alpine
```

### Scenariusz 3
```
docker volume create --name SharedVolume
docker run --name SharedVolumeDemo -v SharedVolume -it ubuntu
docker run --volumes-from SharedVolumeDemo -it ubuntu
echo "Hello world!" > demo.txt
cat demo.txt
cat demo.txt
```
