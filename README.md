
# Trying to get conda/python 3.12/flox to work

My system may be in a weird state, but I think this should be a way to reproduce the errors.

My current setup:
flox 1.3.14
python 3.12
python312Packages.conda

My previous setup where conda was working:
flox 1.3.10
python 3.11
nixpkgs.conda

## Steps to reproduce

> flox activate

> bash  # since I'm using fish and conda wont work in fish for not

> conda init  # this enables conda in your shell init

> exit  # need to restart shell for init's work to take place

> bash

> python -V
Python 3.12.9

> conda info

> conda create -n test1

> conda activate test1

> python -V
Could not start dynamically linked executable: python
NixOS cannot run dynamically linked executables intended for generic
linux environments out of the box. For more information, see:
https://nix.dev/permalink/stub-ld
(test1) 

> conda env update -f conda_environment.yml 
Channels:
 - conda-forge
 - defaults
Platform: linux-64
Collecting package metadata (repodata.json): done
Solving environment: done

Downloading and Extracting Packages:

Preparing transaction: done
Verifying transaction: done
Executing transaction: done
Installing pip dependencies: - Ran pip subprocess with arguments:
['/home/jono/.conda/envs/test1/bin/python', '-m', 'pip', 'install', '-U', '-r', '/home/jono/src/flox-conda-test/condaenv.f66l8dcm.requirements.txt', '--exists-action=b']
Pip subprocess output:

Pip subprocess error:
/nix/store/f2krmq3iv5nibcvn4rw7nrnrciqprdkh-python3-3.12.9/bin/python3.12: can't open file '/home/jono/src/flox-conda-test/shell.posix': [Errno 2] No such file or directory

CondaError: Conda has not been initialized.

To enable full conda functionality, please run 'conda init'.
For additional information, see 'conda init --help'.


Could not start dynamically linked executable: /home/jono/.conda/envs/test1/bin/python
NixOS cannot run dynamically linked executables intended for generic
linux environments out of the box. For more information, see:
https://nix.dev/permalink/stub-ld

failed

CondaEnvException: Pip failed

(test1) 


