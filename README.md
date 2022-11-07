# Warsztaty DevOps dla studentów

## Wymagania sprzętowe

### Windows

* Windows 11 64-bit: Home lub Pro wersja 21H2 lub wyższa albo wersja Enterprise/Education 21H2 i wyższa
* Windows 10 64-bit: Home lub Pro 21H1 (build 19042) lub wyższa albo Enterprise/Education 20H2 (build 19042) i wyższa
* 64-bit processor with Second Level Address Translation (https://en.wikipedia.org/wiki/Second_Level_Address_Translation)
* 8GB system RAM lub więcej
* BIOS-level hardware wsparcie dla wirtualizacji włączone (więcej info: https://docs.docker.com/desktop/troubleshoot/tdevops-workshops-for-studentsopics/#virtualization)

### Linux

Aby zainstalować Dockera musimy posiadać 64bitową wersję Ubuntu, jedną z wybranych:
* Ubuntu Jammy 22.04 (LTS)
* Ubuntu Impish 21.10
* Ubuntu Focal 20.04 (LTS)
* Ubuntu Bionic 18.04 (LTS)

### MacOS

* MacOS w wersji 10.15 lub wyższej. To jest Catalina, Big Sur, Monterey. Zalecane jest zaktualizowanie systemu do najnowszej wersji
* 4GB system RAM lub więcej
* VirtualBox przed wersją 4.3.30 nie może być zainstalowany, ponieważ nie jest kompatybilny z Docker Desktop

## Wymagane oprogramowanie

* Git (https://git-scm.com/)
* Python3 (https://www.python.org/)
* Docker (https://www.docker.com/)
* Minikube with kubectl (https://minikube.sigs.k8s.io/docs/start/)
* Pobranie i zainstalowanie Linux kernel update package (https://learn.microsoft.com/en-us/windows/wsl/install-manual#step-4---download-the-linux-kernel-update-package) (Windows)

## Wymagane konta internetowe

* GitHub (https://github.com/)
* DockerHub (https://hub.docker.com/)
* Snyk (https://snyk.io/)

## Plan warsztatu

1. [Instalacja Gita](#1-Instalacja-Gita)
2. [Instalacja Pythona](#2-Instalacja-Pythona)
3. [Instalacja Dockera](#3-Instalacja-Dockera)
4. [Założenie kont na serwisach: Github, Docker Hub, Snyk](#4-Założenie-kont-na-serwisach-Github-Docker-Hub-Snyk)
5. [Stoworzenie katalogu roboczego i sklonowanie repozytorium](#5-Stworzenie-katalogu-roboczego-i-sklonowanie-repozytorium)
6. [Przygotowanie wirtualnego środowiska Python](#6-Przygotowanie-wirtualnego-środowiska-Python)
7. [Uruchomienie aplikacji, bazy danych i testów jednostkowych](#7-Uruchomienie-aplikacji-bazy-danych-i-testów-jednostkowych)
8. [Konteneryzacja aplikacji](#8-Konteneryzacja-aplikacji)
9. [Orkiestryzacja aplikacji z użyciem narzędzia docker-compose](#9-Orkiestryzacja-aplikacji-z-użyciem-narzędzia-docker-compose)
10. [Ciągła integracja i wydanie](#10-Ciągła-integracja-i-wydanie)
11. [Wdrożenie aplikacji na platformie Kubernetes](#11-Wdrożenie-aplikacji-na-platformie-Kubernetes)
12. [Ćwiczenia](#12-Ćwiczenia)

<br />
<hr />

## 1. Instalacja Gita

<hr />

Pełna dokumentacja: https://git-scm.com/book/en/v2/Getting-Started-Installing-Git

### Windows

Przechodzimy na stronę z instalkami Gita dla windowsa: https://git-scm.com/download/win. Następnie pobieramy odpowiednią wersję i instalujemy.

### Linux

Dla dystrubucji opartych na Debianie wykonujemy polecenie:

```sh
sudo apt install git-all
```

### MacOS

Wykonujemy polecenie, po którego wykonaniu pokaże nam się poprozycja instalacji:

```sh
git --version
```

<br />
<hr />

## 2. Instalacja Pythona

<hr />

### Windows

Pobieramy plik instalacyjny Pythona w odpowiedniej wersji (najlepiej ostatniej stabilnej) ze strony: https://www.python.org/downloads/ i instalujemy.

### Linux

Wykonujemy poniższe polecenia, które zaktualizują narzędzie apt-get, zainstalują pythona w najnowszej dostępnej wersji na obecnego narzędzi pakietów i zaktualizują wersję menadżera pakietów (pip).

```sh
sudo apt-get update
sudo apt-get install python3
python3 -m ensurepip --upgrade
```

### MacOS

Pobieramy plik instalacyjny Pythona w odpowiedniej wersji (najlepiej ostatniej stabilnej) ze strony: https://www.python.org/downloads/macos/ i instalujemy.

<br />
<hr />

## 3. Instalacja Dockera

<hr />

### Windows

Pełna dokumentacja: https://docs.docker.com/desktop/install/windows-install/

1. Przed zainstalowaniem WSL należy uruchomić funkcjonalność "Virtual Machine Platform" poprzez wykonanie polecenia w PowerShellu uruchomionym jako administrator (https://learn.microsoft.com/en-us/windows/wsl/install-manual#step-3---enable-virtual-machine-feature):

    ```sh
    dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart
    ```

2. Instalujemy WSL (Windows Subsystem for Linux)

    ```sh
    wsl --install
    ```

    Ta komenda zainstaluje potrzebne rzeczy do uruchomienia WSL i zainstaluje Linuxa w domyślnej dystrybucji Ubuntu.

3. Restartujemy windowsa

4. Tworzymy Linuowego użytkownika. Można to zrobić poprzez otworzenie dystrybucji Linuxa posługując się np. Start menu. Zostaniemy poproszeni o podanie username i password do nowo utworzonego użytkownika. Dany użytkownik zostanie powiązany z konkretną dystrybucją.

5. Podnosimy wersję WSL z wersji 1 do 2. Najpierw możemy sprawdzić, która obecnie wersja WSL jest używana wykonując polecenie:

    ```sh
    wsl -l -v
    ```

    Aby wybrać domyślną wersję WSL jako wersję 2, należy wykonać poniższą komendę:

    ```sh
    wsl --set-default-version 2
    ```

6. Pobieramy aplikację Docker Desktop: https://docs.docker.com/desktop/install/windows-install/

7. Instalujemy Docker Desktop.

    * Po pojawieniu się okienka instalacji należy się upewnić, że wybrana jest opcja użycia WSL 2 zamiast Hyper-V

<hr />

### Linux

1. Odinstalowujemy stare wersje dockera:

    ```sh
    sudo apt-get remove docker docker-engine docker.io containerd runc
    ```

2. Instalujemy Dockera przy pomocy repozytorium.

* Aktualizujemy pakiet apt i instalujemy wybrane pakiety:

    ```sh
    sudo apt-get update
    sudo apt-get install \
        ca-certificates \
        curl \
        gnupg \
        lsb-release
    ```

* Dodajemy oficjalny klucz dockerowy GPG:

    ```sh
    sudo mkdir -p /etc/apt/keyrings
    curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
    ```

* Konfigurujemy repozytorium:

    ```sh
    echo \
        "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
        $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
    ```

<hr />

### MacOS

Pełna dokumentacja: https://docs.docker.com/desktop/install/mac-install/

1. Pobieramy instalkę w zależności o rodzaju procesora ze pełnej dokumentacji powyżej.

2. Instalujemy przy pomocy graficznego interfejsu uruchamiając instalkę lub przy pomocy wiersza poleceń (szczegóły w pełnej dokumentacji)

<br />
<hr />

### Dodanie użytkownika do grupy docker

```sh
sudo usermod -aG docker $USER && newgrp docker
```

## 4. Założenie kont na serwisach: Github, Docker Hub, Snyk

<hr />

* Konto GitHub będzie nam potrzebne w celu stworzenia pipelinu (CI) wykorzystując narzędzie GitHub Actions. Pipeline służy do automatyzacji pewnych procesów. W tym wypadku tymi procesami będą: testy jednostkowe, lintowanie kodu, budowanie kontenera aplikacji i wysyłanie go na repozytorium, statyczna analiza kodu. (https://github.com/)
* Konto na repozytorium Dockerowym (Docker Hub) będzie wykorzystane w celu przechowania na nim naszego zbudowanego kontenera aplikacji. (https://hub.docker.com/)
* Konto Snyk zostanie wykorzystane w celu wykonania statycznej analizy kodu. (https://snyk.io/)

<br />
<hr />

## 5. Stworzenie katalogu roboczego i sklonowanie repozytorium

<hr />

Forkujemy repozytorium porzez otworzenie oficjalnego repozytorium ```https://github.com/Jeremiaszmacura/devops-workshops-for-students``` i kliknięcie ikony z napisem fork (prawy góry róg). 
Po udanym forku klonujemy nowo utworzone repozytorium do wybranego katalogu roboczego na naszym systemie przy pomocy polecenia ```git clone https://github.com/Jeremiaszmacura/devops-workshops-for-students``` wykonanego z poziomu cmd/powershell/git bash/bash/sh/...

<br />
<hr />

## 6. Przygotowanie wirtualnego środowiska Python

<hr />

* Tworzymy wirtualne środowisko przy pomocy biblioteki venv. Następnie aktywujemy to środowisko. Dzięki temu stworzymy odseparowane środowisko do pracy nad aplikacją, a wszystkie zaisntalowane biblioteki pozostaną jedynie w tym środowisku i nie będą miały wpływu na pozostałe projekty Pythonowe znajdujące się w naszym systemie.

```sh
python3 -m venv .venv
source .venv/bin/activate (Linux)
.venv\Scripts\activate (Windows)
```

W przypadku problemów z aktywowaniem środowiska wirtualnego w systemie Windows można skorzystać z komendy:

```sh
Set-ExecutionPolicy Unrestricted -Scope Process
```

<br />
<hr />

## 7. Uruchomienie aplikacji, bazy danych i testów jednostkowych

<hr />

### Konfiguracja środowiska i instalacja zależności

Eksportujemy dwie zmienne, które informuja aplikację gdzie znajduje się plik wejściowy oraz, że będziemy pracować w trybie developerskim z opcją debugowania.

#### Linux

```sh
export FLASK_APP=flaskr/app.py
export FLASK_DEBUG=true
```

#### Windows (cmd)

```sh
set FLASK_APP=flaskr/app.py
set FLASK_DEBUG=true
```

#### Windows (powershell)

```sh
$env:FLASK_APP = "flaskr/app.py"
$env:FLASK_DEBUG = "true"
```

Instalujemy naszą aplikację jako bibliotekę wykorzystując bibliotekę setuptools. Poniższe polecenie wykonujemy w katalogu głównym projektu:

```sh
python -m pip install -e .[dev]
```

Budujemy paczkę (przy zmianach w projekcie każdorazowo przed wybudowaniem obrazu dokerowego).

```sh
python setup.py bdist_wheel
```

Przed uruchomieniem aplikacji musimy zadbać o bazę danych, z którą apliakcja będzie się probowała połączyć. 
Wystarczy, że skoczystamy z Dockera i wykonamy poniższe polecenie, które zaciągnie obraz bazy danych PostgreSQL w wersji 14 z oficjalnego repozytorium, a następnie na podstawie tego obrazu zostanie uruchomiony kontener z określonymi zmiennymi środowiskowymim, widocznymi wewnątrz niego.

<hr />

### Uruchomienie kontenera bazy danych i aplikacji

1. Uruchomienie bazty danych

```sh
docker run --name postgres_workshops -e POSTGRES_DB=dev_database -e POSTGRES_USER=dev_user -e POSTGRES_PASSWORD=dev_user -p 5432:5432 -d postgres:14
```

2. Uruchomienie aplikacji.

```sh
flask run
```

Aplikacja powinna być dostępna pod adresem http://localhost:5000 

<hr />

### Uruchomienie testów jednostkowych

```sh
python setup.py test
```

<br />
<hr />

## 8. Konteneryzacja aplikacji

<hr />

### Dockerfile

```text
FROM python:3.10
WORKDIR /app
COPY ./dist/flaskr-0.1.0-py3-none-any.whl .
RUN pip3 install flaskr-0.1.0-py3-none-any.whl
EXPOSE 5000
CMD ["gunicorn","-b","0.0.0.0:5000","-w","1","flaskr.app:create_app()"]
```

- ```FROM python:3.10``` określa bazowy obraz, który będziemy rozbudowywać. Jest to obraz z zainstalowanym Pythonem w wersji 3.10. 
- ```WORKDIR /app``` powoduje, że wszystkie polecenia zostaną domyślnie wykonane pod tą ścieżką w obrazie. 
- ```ENV FLASK_APP=flaskr/app.py``` oraz ```ENV FLASK_RUN_HOST=0.0.0.0``` ustawiają zmienne środowiskowe widoczne w obrazie.
- ```COPY ./dist/flaskr-0.1.0-py3-none-any.whl .``` powoduje przekopiowanie wybranych plików pomiędzy naszą maszyną hostującą, a obrazem, który zostanie stworzony. 
- ```RUN pip3 install flaskr-0.1.0-py3-none-any.whl``` wykonuje polecnie instalacji paczki z aplikacją.
- ```EXPOSE 5000``` pozwala na udostępnienie portu 5000 obrazu na zewnątrz, dzięki czemu możemy wykonywać na ten port zapytania z naszej maszyny hostującej i komunikować się z aplikacją w kontenerze. 
- ```CMD ["gunicorn","-b","0.0.0.0:5000","-w","1","flaskr.app:create_app()"]``` to polecenie zostanie wykonane za każdym razem gdy kontener jest uruchamiany.

<hr />

### Wybudowanie i uruchomienie aplikacji przy pomocy Dockerfile

W momencie kiedy Dockerfile jest już gotowy możemy na jego podstawie utworzyć obraz:

```sh
docker build -t flask-app:develop .
```

Parameter ```-t``` oznacza nazwę pod jaką zostanie utworzony obraz.

Ponieważ chcemy by kontener aplikacji i bazy danych komunikowały się między sobą tworzymy sieć typu bridge:

    docker network create -d bridge my-bridge-network
    
Zatrzymujemy i usuwamy poprzednio utworzony kontener bazy danych i uruchamiamy go jeszcze raz, tym razem z nowo utworzoną siecią:

```sh
docker container stop postgres_workshops
docker container rm postgres_workshops
docker run --name postgres_workshops -e POSTGRES_DB=dev_database -e POSTGRES_USER=dev_user -e POSTGRES_PASSWORD=dev_user --network=my-bridge-network -d postgres:14
```

Teraz, na podstawie utworzonego obrazu tworzymy i uruchmiamy kontener z aplikacją:

```sh
docker run -d -e FLASK_DEBUG="True" -e DATABASE_URI="postgresql://dev_user:dev_user@postgres_workshops:5432/dev_database" -p 5000:5000 --network=my-bridge-network --name flask_app flask-app:develop
```

- ```-d``` oznacza tryb ```detach``` podczas, którego kontener pracuje w tle, a na konsolę jest jedynie wypisywane ID tego kontenera. 
- ```-e``` powoduje dodanie zmiennej środowiskowej do uruchamianego kontenera. 
- ```-p 5000:5000``` mapuje lokalny port kontenera (5000) na port hosta (5000).
- ```--network="my-bridge-network"``` odpowiednio ustawia utworzoną wcześniej sieć.
- ```--name flask_app``` nadaje nawzę kontenerowi. 

Na końcu podajemy nazwę obrazu, na podstawie, którego ma zostać stworzony kontener.

> **Warto zwrócić uwagę, że w URI do bazy danych podany jest tym razem `postgres_workshops`.**

<hr />

### Przydatne komendy

Wypisanie logów z kontenera na standardowe wyjście:

```sh
docker logs <container>
```

Zatrzymnie działania uruchomionego kontenera:

```sh
docker stop <container>
```

Uruchomienie zbudowanego kontenera:

```sh
docker start <container>
```

Usunięcie zatrzymanego kontenera:

```sh
docker rm <container>
```

Usunięcie obrazu:

```sh
docker rmi <image>
```

Wypisanie dostepnych sieci dockerowych:

```sh
docker network ls
```

Usunięcie sieci dockerowej:

```sh
docker network rm <network>
```

Usunięcie wszystkich kontenerów i obrazów:

```sh
docker system prune
```

<hr />

### .dockerignore

Ten plik działa podobnie jak plik .gitignore w przypadku git'a. Pozwala określić katalogi i pliki, które nie będą kopiowane w przypadku komendy COPY w Dockerfile (choćby zawierały się w ścieżce do skopiowania w Dockerfile).

<br />
<hr />

## 9. Orkiestryzacja aplikacji z użyciem narzędzia docker-compose

<hr />

Cały stos aplikacji może być uruchomiony za pomocą polecenia docker-compose Dockera. Compose jest narzędziem do definiowania i uruchamiania aplikacji Dockera składających się z wielu kontenerów/aplikacji.

W tym celu przygotowany został plik `docker-compose.yaml`, w którym zdefiniowane jest sama usługi aplikacji, baza danych i odpowiednie dane konfiguracyjne.

> **Uwaga:** Polecenie powinno być wykonane w folderze, w którym znajduje się odpowiedni plik `docker-compose.yaml`. W przeciwnym razie należy go wskazać za pomocą opcji `-f`.

### Nim skorzystamy z narzędzia jakim jest docker-compose musimy zakończyć działanie i żywot naszych obecnie działających kontenerów przy pomocy poleceń

```sh
docker stop flask_app postgres_workshops
docker rm flask_app postgres_workshops
```

<hr />

### docker-compose.yaml

```text
version: '3.8'

services:

  flask-app:
    image: flask-app
    build:
      context: .
      dockerfile: ./Dockerfile
    ports:
      - 5000:5000
    environment:
      FLASK_DEBUG: 'True'
      DATABASE_URI: postgresql://${POSTGRES_USER}:${POSTGRES_PASSWORD}@${POSTGRES_HOST}:5432/${POSTGRES_DB}
    restart: on-failure
    depends_on:
      - database

  database:
    image: postgres:14
    env_file: .env
    environment:
      - POSTGRES_USER=${POSTGRES_USER}
      - POSTGRES_PASSWORD=${POSTGRES_PASSWORD}
      - POSTGRES_DB=${POSTGRES_DB}
    restart: always

```

Powyższy plik docker-compose.yaml definiuje zarówno kontenery z ich specifikacją, które mają zostać zbudowane jak i specyfikację sieci, w której mają pracować. Pierwsza z aplikacji określona w tym pliku to nasza aplikacja napisana w frameworku flask. 
* ```image``` określa nazwę obrazu, który ma zostać użyty do zbudowania kontenera.
* ```build``` zawiera dodatkowe parametry wykorzystane w procesie budowania kontenera na bazie wybranego obrazu. ```context``` określa kontekst, a ```dockerfile``` zawiera ścieżkę do pliku Dockerfile, na podstawie, którego zostanie zbudowany obraz.
* ```ports``` mapuje porty pomiędzy maszyną hostującą, a kontenerem ```HOST:CONTAINER```.
* ```environment``` pozwala na dodanie zmiennych środowiskowych do tworzonego kontenera.
* ```restart``` określa zachowanie kontenera w monemcie, gdyż jego praca zostanie zakończona. W tym wypadku, w momencie, kiedy kontener przestanie działać z powodu błędy, zostanie automatycznie ponownie powołany do życia.
* ```depends_on``` określa kolejność (zależność), w której kontenery mają zostać uruchomienione. Należy zwrócić uwagę, że nie oznacza to, że kontener, który później został utworzony nie będzie pierwszy gotowy do działania (aplikacja może polegać na kontenerze z bazą danych stąd najpierw uruchomimy kontener z tą bazą, natomiast może stać się tak, że naszą aplikacja szybciej skofiguruje swój kontener niż baza danych i wystąpi problem z połączeniem bazodanowym).
* ```env_file``` dodaje zmienne środowiskowe do kontenera na podstawie zewnętrznego pliku.

<hr />

### Uruchomienie skonteneryzowanych i skonfigurowanych aplikacji przy pomocy jednego polecenia

```sh
docker-compose up
```

W przypadku gdyby docker-compose nie był jeszcze zainstalowany razem z dockerem:

```sh
sudo apt-get install docker-compose
```

<hr />

### Przydatne komendy

Zatrzymanie kontenerów i usunięcie kontenerów wraz z obrazami:

```sh
docker-compose down --rmi all
```

<br />
<hr />

## 10. Ciągła integracja i wydanie

<hr />

W celu stworzenia pipelinu CI/CD użyjemy narzęcia GitHub Workflows. Jest to proste w uzyciu narzędzie, które pozwala na dużo więcej niż proste pipeliny CI/CD, a do tego pozwala nam trzymać je w postaci kodu na jednym repozytorium wraz z kodem samego projektu. GitHub udostępnia na swoje maszyny budujące, stąd nie musimy się przejmować o infraktrukturę. Kod pipelinu musi znajdować się w plikach z roszerzeniem ```.yml/.yaml``` w katalogu ```.github/workflows/```.

```.github/workflows/<nazwa_pliku>.yml:```

<hr />

### Aktywacja GitHub Action

Aktywujemy tą funkcjonalność poprzez przejście na zakładkę ```Actions``` na naszym sforkowanym repozytorium i kliknięcie przycisku aktywacji.

<hr />

### Dodanie GitHub Secrets do repozytorium

W celu poprawnego korzystania z narzędzia Snyk i serwisu Docker Hub musimy ustawić zmienne przechowujące dane wymagane do uwierzytelniania w tych serwisach jako sekrety na platformie GitHub. GitHub Actions będą w trakcie komunikacji z tymi serwisami korzystać z tych sekretów i będą one niewidoczne dla osób postronnych. Na platformie GitHub przechodzimy do zakładki ustawień będąc na naszym własnym zforkowanym repozytorium. W ustawieniach przechodzimy do zakładki sekretów dla akcji. Dodajemy trzy poniższe sekrety:
* Nazwa sekretu: ```SNYK_TOKEN```. Jego zawartością będzie token, który możemy pozyskać z naszego konta w serwisie Snyk ```https://snyk.io/account/```. 
* Nazwa sekretu: ```DOCKERHUB_USERNAME```. Wartość ustawiamy na naszą nazwę użytkownika w serwisie Docker Hub ```https://hub.docker.com/```. Po zalogowaniu do serwisu Docker Hub nasza nazwa użytkownika widnieje w prawym górnym roku.
* Nazwa sekretu: ```DOCKERHUB_TOKEN```. Wartość tego sekretu ustawiamy na token, którym możemy pozyskać z naszego konta w serwisie Docker Hub ```https://hub.docker.com/```. Po zalogowaniu do serwisu Docker Hub przechodzimy do zakładki ```Account Settings```, a następnie ```Security``` i tworzymy nasz nowy token, którego wartość kopiujemy do sekretu GitHub.

<hr />

### Automatyzacja testów jednostkowych

```text
name: Unit Tests

on:
  push:

jobs:
  unit-testing:
    runs-on: ubuntu-20.04
    
    env:
      FLASK_APP: flaskr/app.py

    steps:
      - uses: actions/checkout@v2

      - name: Set up Python 3.10
        uses: actions/setup-python@v1
        with:
          python-version: '3.10'

      - name: Setup app
        run: pip install -e .[dev]

      - name: Run unit tests
        run: python setup.py test
```

* ```name:``` określa nazwę dla danego workflow/akcji i pod nią będzie on widnieć na Githubie.
* ```on:``` określa sytuację, w której workflow zostanie uruchomiony. W tym przypadku będzie to w momencie, kiedy zostanie wypchnięty commit na zdalne repozytorium: ```push:```.
* ```job``` zawiera zadania, które w ramach tego workflow zostaną uruchomione.
* ```runs-on:``` określa maszynę budującą, na której dany workflow zostanie uruchomiony.
* ```env:``` pozwala na określenie zmiennych środowiskowych, które zostaną ustawione na maszynie budującej
* ```strategy: matrix:``` umożliwia uruchomienie zadania na wielu wersjach wskazanego języka/systemu operacyjnego
* ```steps:``` określa konkretne kroki, które zostaną wykonane w realizacji danego zadania.
* ```uses:``` pozwala na skorzystanie z gotowej akcji zdefiniowanej na zewnętrznym repozytorium.
* ```with:``` umożliwia przekazanie wybranych parametrów do danej akcji.

<hr />

### Automatyczne testowanie przy pomocy narzędzi typu linter (np. pytlint, black)

```text
name: Lint code

on:
  push:

jobs:
  lint-code:
    runs-on: ubuntu-20.04

    steps:
      - uses: actions/checkout@v2

      - name: Set up Python
        uses: actions/setup-python@v1
        with:
          python-version: '3.10'

      - name: Lint with pylint
        run: |
          pip install pylint
          pylint --exit-zero flaskr

      - name: Lint with black
        run: |
          pip install black
          python -m black --check .
```

<hr />

### Automatyzacja statycznej analizy kodu

```text
name: Static code analysis

on:
  push:
    branches:
      - 'master'
      - 'develop'

jobs:
  snyk-scan:
    runs-on: ubuntu-20.04
    steps:
      - uses: actions/checkout@master

      - name: Prepare requirements for Snyk
        run: |
          python -m pip install .

      - name: Run Snyk to check for vulnerabilities
        uses: snyk/actions/python-3.8@master
        continue-on-error: true
        env:
          SNYK_TOKEN: ${{ secrets.SNYK_TOKEN }}
```

<hr />

### Automatyczne budowanie i wdrażanie kontenerów

```text
name: Docker build and push

on:
  push:
    branches:
      - 'master'
      - 'develop'

jobs:
  docker:
    runs-on: ubuntu-20.04
    steps:
      - uses: actions/checkout@v3

      - name: Build project with setuptool
        run: |
          python -m pip install .[dev]
          python setup.py bdist_wheel

      - name: Set up QEMU
        uses: docker/setup-qemu-action@v2

      - name: Set up Docker Buildx
        uses: docker/setup-buildx-action@v2

      - name: Login to DockerHub
        uses: docker/login-action@v2 
        with:
          username: ${{ secrets.DOCKERHUB_USERNAME }}
          password: ${{ secrets.DOCKERHUB_TOKEN }}
          logout: true

      - name: Build and push
        id: docker_build
        uses: docker/build-push-action@v3
        with:
          context: .
          push: true
          tags: ${{ secrets.DOCKERHUB_USERNAME }}/devops-workshops:develop
```

<br />
<hr />

## 11. Wdrożenie aplikacji na platformie Kubernetes

<hr />

### 11.1 Instalacja Kubernetesa

### Windows

Po zainstalowaniu Docker Desktop wchodzimy w jego ustawienia (prawym klawiszem myszy na jego ikonie w pasku zadań, następnie wybieramy *settings*) i klikamy na **Enable Kubernetes**. 


O poprawnym uruchomieniu informuje zielony pasek w lewym-dolnym rogu Docker Desktop (powinny być widoczne dwa zielone paski: *Engine Running* świadczący o działaniu silnika Dockera oraz *Kubernetes Running* świadczący o działaniu Kubernetesa).

### Linux

Wykonujemy poniższe polecenia, które zainstalują **minikube**:

    curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64
    sudo install minikube-linux-amd64 /usr/local/bin/minikube

Uruchamiamy klaster poleceniem:

    minikube start

> **Więcej informacji:**  https://minikube.sigs.k8s.io/docs/start/

#### MacOS

Wykonujemy poniższe polecenia, które zainstalują **minikube**:

    curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-darwin-amd64
    sudo install minikube-darwin-amd64 /usr/local/bin/minikube

> **Więcej informacji:**  https://minikube.sigs.k8s.io/docs/start/

### 11.2 Instalacja polecenia kubectl

### Windows

Polecenie kubectl można zainstalować poprzez manager pakietów **Chocolatey**, który można pobrać z https://chocolatey.org/.
Po jego zainstalowaniu należy wykonać polecenie:

    choco install kubernetes-cli

### Linux

Wykonujemy polecenia:

    curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"
    sudo install -o root -g root -m 0755 kubectl /usr/local/bin/kubectl

> **Więcej informacji:**  https://kubernetes.io/docs/tasks/tools/install-kubectl-linux/


#### MacOS


1. Pobranie pliku w postaci binarnej.

Wykonujemy polecenia:

- dla architektury **Intel**:

       curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/darwin/amd64/kubectl"

- dla architektury **Apple Silicon**:

       curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/darwin/arm64/kubectl"

2. Instalacja

Wykonujemy polecenia:
    
    chmod +x ./kubectl
    sudo mv ./kubectl /usr/local/bin/kubectl
    sudo chown root: /usr/local/bin/kubectl

> **Więcej informacji:**  https://kubernetes.io/docs/tasks/tools/install-kubectl-macos/

---

### Weryfikacja instalacji

Po instalacji, by zweryfikować poprawność i wersję klienta należy wykonać:

    kubectl version --client

Oraz, by zweryfikować wersję zarówno klienta jak i serwera:

    kubectl version

Aby wyświetlić stan całego klastra należy wykonać:

    kubectl cluster-info

### 11.3 Wdrożenie aplikacji

Wdrożenie aplikacji na platformie Kubernetes odbywa się poprzez odpowiednio przygotowane pliki (*deployment files*), w których zdefiniowane są obiekty składowe aplikacji.

W folderze z projektem znajduje się plik `k8s.yaml`, który zawiera definicje obiektów takich typów jak *PersistentVolume*, *PersistentVolumeClaim*, *ConfigMap*, *Service*, *Deployment* i *StatefulSet*.

Za wdrożenie bazy danych odpowiada obiekt typu *StatefulSet*.

Za wdrożenie aplikacji odpowiada obiekt typu *Deployment*, w którym znajduje się definicja obrazu dokerowego aplikacji: `image: devops-workshops:develop`.

Można także uzupełnić nazwę obrazu (`devops-workshops:develop`) o nazwę własnego użytkownika serwisu **Dockerhub**, np. dla użytkownika `marcin` obraz powinien mieć nazwę `image: marcin/devops-workshops:develop`. W ten sposób nie użyty zostanie obraz wybudowany lokalnie, lecz ten wybudowany za pomocą Github actions.

Ostatecznie, by wdrożyć aplikację należy wykonać polecenie:

    kubectl apply -f k8s.yaml

> **Uwaga:**  *Polecenie to należy wykonać także po każdej modyfikacji obiektów wdrożenia w pliku `k8s.yaml`*

Aby zweryfikować wdrożenie należy wykonać polecenie:

    kubectl get pods

 Polecenie to powinno wyświetlić tabelę działających podów:

    NAME                      READY   STATUS    RESTARTS   AGE
    flaskr-6c45555bcf-bh8c2   0/1     Running   0          6s
    postgres-0                1/1     Running   0          6s

Aby uzyskać szczegółowe informacje o wybranym pod (w tym przypadku o aplikacji) należy wykonać polecenie:

     kubectl describe pod flaskr
     
Polecenie to pokaże także listę zdarzeń (*Events*), jest przydatne przy diagnostyce.

Aby usunąć wdrożenie należy wykonać polecenie:

    kubectl delete -f k8s.yaml

> **Więcej informacji:**  https://kubernetes.io/docs/reference/kubectl/cheatsheet/


## 12. Ćwiczenia

### 12.1 Dodaj nową akcję Github

Dodaj akcję do stworzenia wydania.
Akcja powinna być uruchomiona gdy zostanie stworzony i wypchnięty tag zaczynający się od `v` (np. `v0.1.0`).

Dokumentacja: https://github.com/marvinpinto/action-automatic-releases

Nie zapomnij dodać kroków przygotowania interpreteta Pythona i budowania samej paczki.

Budowanie powinno być wykonane za pomocą polecenia:

    python setup.py bdist_wheel
    
Paczka (plik z rozszerzeniem `.whl`) znajdzie się w folderze `dist`.

Następnie spróbuj dodać i wypchnąć tag komendami Git z linii poleceń:

    git tag v0.1.0
    git push origin develop --tags

### 12.2 Dodaj kolejny serwis do Docker Compose

Dodaj nowy serwis (w pliku `docker-compose.yaml`) o nazwie `pgadmin` z obrazem `dpage/pgadmin4`. 
Umożliwi on edycję/przeglądanie bazy danych.

Konieczne będzie zdefiniowanie zmiennych środowiskowych, niezbędnych do zalogowania do panelu administracyjnego:
- `PGADMIN_DEFAULT_EMAIL`: adres email do logowania.
- `PGADMIN_DEFAULT_PASSWORD`: wybrane hasło.

Więcej informacji: https://www.pgadmin.org/docs/pgadmin4/latest/container_deployment.html

Należy także pamiętać o sekcji `ports`, serwis działa domyślnie na porcie 80.

Uruchom zaktualizowany stos aplikacji poleceniem `docker-compose up`. 
Używając przeglądarki zaloguj się do panelu administracyjnego, dziajającego na wybranym porcie. 

### 12.3 Zabezpiecz URI do bazy danych we wdrożeniu Kubernetesa

Obecnie URI do bazy danych jest podany w pliku `k8s.yaml` w postaci czystego tekstu. 

Aby zabezpieczyć wrażliwe dane można użyć obiektu typu *Secret*. 

Przechowaj w obiekcie URI dla bazy danych, który następnie zostanie wstrzyknięty jako zmienna środowiskowa.

Stwórz taki obiekt używając `kubectl` o nazwie `database-data`:

    kubectl create secret generic database-data --from-literal=DATABASE_URI=postgresql://prod_user:prod_password@postgres:5432/prod_db

Następnie użyj go w deploymencie (`k8s.yaml`).

Dokumentacja: https://kubernetes.io/docs/concepts/configuration/secret/

Sprawdź czy został utworzony poleceniem:

    kubectl get secret database-data
    
Można także edytować secret poleceniem:

    kubectl edit secrets database-data

Przeprowadź wdrożenie za pomocą polecenia `kubectl apply -f k8s.yaml` i sprawdź działanie aplikacji.

