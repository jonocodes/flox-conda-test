# Trying to get my python setup to work...

- flox
- conda
- python 3.12
- pip
- pdm
- fish shell

Almost working. It just needs to be in nested shells to work.

Perhaps I need to import the FHS from conda directly into the flox environment somehow.

My current setup:

- flox 1.3.14
- python 3.12
- nixpkgs.conda

My previous setup where conda was working:

- flox 1.3.10
- python 3.11
- nixpkgs.conda

## Steps to reproduce

> flox activate

> conda-shell -c fish

> conda init # this enables conda in your shell init. first time setting up conda only

> exit # need to restart shell for init's work to take place

> conda-shell -c fish

> eval /home/jono/.conda/bin/conda "shell.fish" "hook" $argv | source

> conda create -n test1

> conda activate test1

> conda env update -f conda_environment.yml

> pip install pdm # since pdm managed by python seems more agreeable then when installed by nix/flox

> pdm install

> ./try.py
> 3.0
> It worked......
