## Docker installation
<hr>

### Windows
1. Należy upewnić się, że w systemie została włączona funkcjonalność WSL2 (Windows Subsystem for Linux 2). Aby sprawdzić czy WSL jest aktywny i w jakiej wersji należy w PowerShelu użyć komendy:
```sh
wsl -l -v
```
Jeśli jest aktywny w wersji drugiej to można przejść do kolejnego kroku. W przecinym razie należy wykonać następujące kroki:
* Przed zainstalowaniem WSL należy uruchomić funkcjonalność "Virtual Machine Platform" poprzez wykonanie polecenia w PowerShellu uruchomionym jako administrator (https://learn.microsoft.com/en-us/windows/wsl/install-manual#step-3---enable-virtual-machine-feature):
```sh
dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart
```
* uruchamiamy PowerShell jako administrator i wykonać komendę:
```sh
wsl --install
```
Ta komenda zainstaluje potrzebne rzeczy to uruchomienia WSL i zainstaluje Linuxa w dystrybucji Ubuntu. Jeśli to wykonaniu powyższego polecenia pojawi się help tekst od WSL, należy sprawdzić jakie są dostępne dystrybucje Linuxa poprzez wykonanie komedy:
```sh
wsl --list --online
```
Jeśli brakuje pożądanej dystrybucji to możemy ją zainstalować poprzez wykonanie komendy (jako dystrybuję można podać np. "Ubuntu"):
```sh
wsl --install -d <dystrybucja>
```
* tworzymy Linuowego użytkownika. Można to zrobić poprzez otworzenie dystrybucji Linuxa posługując się np. Start menu. Zostaniemy poproszeni o podanie username i password do nowo utworzonego użytkownika. Dany użytkownik zostanie powiąanym z konkre.

* podnosimy wersję WSL z wersji 1 do 2. Najpierw możemy sprawdzić, która obecnie wersja WSL jest używana wykonując polecenie:
```sh
wsl -l -v
```
Aby wybrać domyślną wersję WSL jako wersję 2, należy wykonać poniższą komendę:
```sh
wsl --set-default-version 2
```
Aby wybrać domyślną dystrybucję Linuxa możemy wykonać polecenie:
```sh
wsl -s <DistributionName>
```
Aby wybrać wersję WSL dla konkretnej dystrybucji Linuxa możemy skorzystać z polecenia:
```sh
wsl --set-version <distro name> 2
```
np.
```sh
wsl --set-version Ubuntu-20.04 2
```

<hr>

### Linux
