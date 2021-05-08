## Bug Setup
Three separate branches, where the dependency tree is as follows:

```
dep_a (Poetry) -> dep_b (Poetry) -> dep_c (setup.py) -> grpcio
```

- dep_a - https://github.com/mtraynham/poetry_4051/tree/dep_a
- dep_b - https://github.com/mtraynham/poetry_4051/tree/dep_b
- dep_c - https://github.com/mtraynham/poetry_4051/tree/dep_c

## Recreating
Compare and contrast installs of 1.1.5 & 1.1.6

### poetry 1.1.5

```bash
pip install --upgrade poetry==1.1.5
poetry install -vvv
```

####  Clean Poetry Install
```
Creating virtualenv dep-a in /home/foobar/poetry_4051/.venv
Using virtualenv: /home/foobar/poetry_4051/.venv
Installing dependencies from lock file

Finding the necessary packages for the current system

Package operations: 4 installs, 0 updates, 0 removals

  • Installing six (1.16.0): Pending...
  • Installing six (1.16.0): Installing...
  • Installing six (1.16.0)
  • Installing grpcio (1.28.1): Pending...
  • Installing grpcio (1.28.1): Installing...
  • Installing grpcio (1.28.1)
  • Installing dep-c (0.1.0 f886f69): Pending...
  • Installing dep-c (0.1.0 f886f69): Cloning...
  • Installing dep-c (0.1.0 f886f69): Building...
  • Installing dep-c (0.1.0 f886f69)
  • Installing dep-b (0.1.0 1a00be6): Pending...
  • Installing dep-b (0.1.0 1a00be6): Cloning...
  • Installing dep-b (0.1.0 1a00be6): Building...
  • Installing dep-b (0.1.0 1a00be6)

Installing the current project: dep_a (0.1.0)
  - Building package dep-a in editable mode
  - Adding dep_a.pth to /home/foobar/poetry_4051/.venv/lib/python3.8/site-packages for /home/foobar/poetry_4051
  - Adding the dep_a-0.1.0.dist-info directory to /home/foobar/poetry_4051/.venv/lib/python3.8/site-packages
```

### poetry 1.1.6
```bash
pip install --upgrade poetry==1.1.6
poetry install -vvv
```

####  Clean Poetry Install
```
Creating virtualenv dep-a in /home/foobar/poetry_4051/.venv
Using virtualenv: /home/foobar/poetry_4051/.venv
Installing dependencies from lock file

Finding the necessary packages for the current system

Package operations: 2 installs, 0 updates, 0 removals, 2 skipped

  • Removing grpcio (1.28.1): Pending...
  • Removing grpcio (1.28.1): Skipped for the following reason: Not currently installed
  • Removing six (1.16.0): Pending...
  • Removing six (1.16.0): Skipped for the following reason: Not currently installed
  • Installing dep-c (0.1.0 f886f69): Pending...
  • Installing dep-c (0.1.0 f886f69): Cloning...
  • Installing dep-c (0.1.0 f886f69): Building...
  • Installing dep-c (0.1.0 f886f69)
  • Installing dep-b (0.1.0 1a00be6): Pending...
  • Installing dep-b (0.1.0 1a00be6): Cloning...
  • Installing dep-b (0.1.0 1a00be6): Building...
  • Installing dep-b (0.1.0 1a00be6)

Installing the current project: dep_a (0.1.0)
  - Building package dep-a in editable mode
  - Adding dep_a.pth to /home/foobar/poetry_4051/.venv/lib/python3.8/site-packages for /home/foobar/poetry_4051
  - Adding the dep_a-0.1.0.dist-info directory to /home/foobar/poetry_4051/.venv/lib/python3.8/site-packages
```
