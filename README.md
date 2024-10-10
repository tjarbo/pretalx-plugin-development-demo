## Plugin Development for pretalx

This repository is used a reference of current issues and open questions for the plugin development procedure of pretalx. The idea is to use [Devcontainers](https://containers.dev/) to create a consistent environment to reproduce issues. 

## How to setup the environemnt?

The Visual Studio Code documentation contains a good starting guide. The most important ones are:

1. Install a container runtime and the extensions: https://code.visualstudio.com/docs/devcontainers/containers#_getting-started
2. Reopen the cloned repository in a devcontainer: https://code.visualstudio.com/docs/devcontainers/containers#_reopen-folder-in-container

## How to start the development server?

This section documents the steps that I did after starting the devcontainer to run the development server. It acts as a common summary, so that I do not have to repeat it for every issue.

#### Initial steps I did once:

1. `pip install -e .`
2. `python3 -m pretalx rebuild --npm-install`
3. `python3 -m pretalx collectstatic --noinput`
4. `python3 -m pretalx migrate`
4. `python3 -m pretalx init`
4. `python3 -m pretalx create_test_event`

#### Commands I execute every time to start the server:

1. `python3 -m pretalx runserver`
