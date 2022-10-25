# Warsztaty DevOps dla studentów

## Wymagania sprzętowe

### Windows

* Windows 11 64-bit: Home lub Pro wersja 21H2 lub wyższa albo wersja Enterprise/Education 21H2 i wyższa
* Windows 10 64-bit: Home lub Pro 21H1 (build 19042) lub wyższa albo Enterprise/Education 20H2 (build 19042) i wyższa
* 64-bit processor with Second Level Address Translation (https://en.wikipedia.org/wiki/Second_Level_Address_Translation)
* 8GB system RAM lub więcej
* BIOS-level hardware wsparcie dla wirtualizacji włączone (więcej info: https://docs.docker.com/desktop/troubleshoot/topics/#virtualization)

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
4. [Założenie kont na serwisach: Github, Docker Hub, Snyk](#4-Załorzenie-kont-na-serwisach-Github-Docker-Hub-Snyk)
5. [Przygotowanie wirtualnego środowiska Python](#5-Przygotowanie-wirtualnego-środowiska-Python)
6. [Uruchomienie aplikacji internetowej (Flask), bazy danych i testów jednostkowych](#6-Uruchomienie-aplikacji-internetowej-Flask-i-testów-jednostkowych)
7. [Konteneryzacja aplikacji](#7-Konteneryzacja-aplikacji)

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
sudo apt-get install python
python -m ensurepip --upgrade
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

## 4. Założenie kont na serwisach: Github, Docker Hub, Snyk

<hr />

* Konto GitHub będzie nam potrzebne w celu stworzenia pipelinu (CI) wykorzystując narzędzie GitHub Actions. Pipeline służy do automatyzacji pewnych procesów. W tym wypadku tymi procesami będą: testy jednostkowe, lintowanie kodu, budowanie kontenera aplikacji i wysyłanie go na repozytorium, statyczna analiza kodu. (https://github.com/)
* Konto na repozytorium Dockerowym (Docker Hub) będzie wykorzystane w celu przechowania na nim naszego zbudowanego kontenera aplikacji. (https://hub.docker.com/)
* Konto Snyk zostanie wykorzystane w celu wykonania statycznej analizy kodu. (https://snyk.io/)

<br />
<hr />

## 5. Przygotowanie wirtualnego środowiska Python

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

## 6. Uruchomienie aplikacji internetowej (Flask), bazy danych i testów jednostkowych

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
$env:FLASK_APP = "true"
```

Instalujemy naszą aplikację jako bibliotekę wykorzystując bibliotekę setuptools. Poniższe polecenie wykonujemy w katalogu głównym projektu:

```sh
python -m pip install -e .[dev]
```

Budujemy paczkę (przy zmianach w projekcie każdorazowo przed wybudowaniem obrazu dokerowego).

```sh
python setup.py bdist_wheel
```

Przed uruchomieniem aplikacji musimy zadbać o bazę danych, z którą apliakcja będzie się probowała połączyć. Wystarczy, że skoczystamy z Dockera i wykonamy poniższe polecenie. Sprawi ono, że zostanie zaciagnięty obraz bazy danych PostgreSQL w wersji 14 z oficjalnego repozytoriusz dokerowego, a następnie na podstawie tego obrazu zostanie uruchomiony kontener z określonymi zmiennymi środowiskowymi wewnątrz niego.

<hr />

### Uruchomienie kontenera bazy danych i aplikacji

```sh
docker run --name postgres_workshops -e POSTGRES_DB=dev_database -e POSTGRES_USER=dev_user -e POSTGRES_PASSWORD=dev_user --network="host" -d postgres:14
```

Uruchomienie aplikacji.

```sh
flask run
```

<hr />

### Uruchomienie testów jednostkowych

```sh
pytest tests
```

<hr />

## 7. Konteneryzacja aplikacji

Cały stos aplikacji może być uruchomiony za pomocą polecenia docker-compose Dockera. Compose jest narzędziem do definiowania i uruchamiania aplikacji Dockera składających się z wielu kontenerów/aplikacji.

W tym celu przygotowany został plik `docker-compose.yaml`, w którym zdefiniowane jest sama usługi aplikacji, baza danych i odpowiednie dane konfiguracyjne.

### 7.1 Uruchomienie 

Aby uruchomić stos aplikacji wykonujemy polecenie:

    docker-compose up -d

### 7.2 Zatrzymanie

Aby zatrzymać stos aplikacji wykonujemy polecenie:

    docker-compose down

> **Uwaga:** Polecenie powinno być wykonane w folderze, w którym znajduje się odpowiedni plik `docker-compose.yaml`. W przeciwnym razie należy go wskazać za pomocą opcji `-f`.

## 8. Wdrożenie na platformie Kubernetes 

### 8.1 Instalacja Kubernetesa

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

### 8.2 Instalacja polecenia kubectl

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

### 8.3 Wdrożenie aplikacji

Wdrożenie aplikacji na platformie Kubernetes odbywa się poprzez odpowiednio przygotowane pliki (*deployment files*), w których zdefiniowane są obiekty składowe aplikacji.

W folderze z projektem znajduje się plik `k8s.yaml`, który zawiera definicje obiektów takich typów jak *PersistentVolume*, *ConfigMap*, *Service*, *Deploymmet* i *StatefulSet*.

Aby wdrożyć aplikację należy wykonać polecenie:

    kubectl apply -f k8s.yaml

> **Uwaga:**  *Polecenie to należy wykonać także po każdej modyfikacji obiektów wdrożenia w pliku `k8s.yaml`*

Aby zweryfikować wdrożenie należy wykonać polecenie:

    kubectl get pods

 Polecenie to powinno wyświetlić tabelę działających podów:

    NAME                      READY   STATUS    RESTARTS   AGE
    flaskr-6c45555bcf-bh8c2   0/1     Running   0          6s
    postgres-0                1/1     Running   0          6s

Aby usunąć wdrożenie należy wykonać polecenie:

    kubectl delete -f k8s.yaml

> **Więcej informacji:**  https://kubernetes.io/docs/reference/kubectl/cheatsheet/