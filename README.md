# Docs

## Anaconda
### What was done initially

```
conda install --name tiktok python=3.8
conda install ncurses
```
### Getting Conda Started

```
conda activate tiktok

```

## Virtual Env

### Setup python v-env

```
virtualenv -p `which python3` venv
source venv/bin/activate
pip install -r requirements.txt
```

### Activating venv

```
source venv/bin/activate
```

### creating requirements.txt

```
pip install TikTokApi
python -m playwright install
pip freeze > requirements.txt
```

## Some docs

- https://github.com/davidteather/TikTok-Api
- https://gist.github.com/davidteather/7c30780bbc30772ba11ec9e0b909e99d
- 
