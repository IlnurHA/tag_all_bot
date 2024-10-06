# Tag All telegram bot

This is a bot to tag all users in a chat using emojis as a text

## How to start

> *Prerequisites:*
You need `api_id` and `api_hash` from Official Telegram Website \[[link](https://core.telegram.org/api/obtaining_api_id)\].
And `bot_token` from [BotFather](https://t.me/BotFather)

### Setting up env vars

Put the following env vars to `.env` file in project directory

```.env
ALL_TG_BOT_TELEGRAM_TOKEN=<bot_token>
ALL_TG_BOT_API_ID=<api_id>
ALL_TG_BOT_API_HASH=<api_hash>
ALL_TG_BOT_API_EMOJI_LIMIT=10
ALL_TG_BOT_LOGGER_LEVEL=INFO
```

`ALL_TG_BOT_API_EMOJI_LIMIT` is a (soft) limit to how many emojis to show in one message (default: **20**)

`ALL_TG_BOT_LOGGER_LEVEL` is a log level for logger to show (default: **INFO**; Should be one of "CRITICAL", "ERROR", "WARNING", "INFO", "DEBUG")

#### Start using python

1. Installing python from [official website](https://www.python.org/about/gettingstarted/)

2. Clone repository

    ```shell
    git clone https://github.com/IlnurHA/tag_all_bot.git
    cd tag_all_bot
    ```

3. Create environment

    **Linux**:

    ```shell
    python3 -m venv venv
    ```

    **Windows**:

    ```powershell
    py -m venv venv
    ```

4. Activate environment

    **Linux**:

    ```shell
    source venv/bin/activate
    ```

    **Windows**:

    ***CMD***

    ```cmd
    ./venv/Scripts/activate.bat
    ```

    or

    ***Powershell***

    ```powershell
    ./venv/Scripts/Activate.ps1
    ```

    > Make sure that you turned on execution of scenarios for windows powershell

5. Install dependencies

    ```shell
    python -m pip install -r requirements.txt
    ```

6. Execute `main.py`

    ```shell
    python main.py
    ```

#### Start using docker (buildning from source)

1. Install docker from [official website](https://docs.docker.com/get-started/)

2. Clone repository

    ```shell
    git clone https://github.com/IlnurHA/tag_all_bot.git
    cd tag_all_bot
    ```

3. Build docker image

    ```shell
    docker build . -t <name_of_image>
    ```

4. Execute docker image

    ```shell
    docker run -d -v "$(realpath .)/.env:/app/.env" <name_of_image>
    ```

5. **[Optional step]** Log saving

    Execute docker with one more parameter to save logs
    (You should specify it by yourself putting instead of `/absolute/path/for/logs/dir` path on your computer to save logs)

    ```shell
    docker run -d -v "$(realpath .)/.env:/app/.env" -v "/absolute/path/for/logs/dir:/app/logs" <name_of_image>
    ```
