This is a blockchain project written in Python.

1. Install python from https://www.python.org/

2. Ensure you are running the version you downloaded and installed with:

        `python --version` or `python`

3. If they don't match, put this in your `~/.bash_profile` or if you use zsh, `~/.zshrc`

        `alias python='python3'`

4. If running `python` still won't match the downloaded version,

        `source ~/.bash_profile` after editing it.

        run `python` again

5. Alternatively and if you don't want to mess with bash, you can simply run:

        `python3` (if you installed Python 3.x)

### To Use Locally

In the project directory, you can run this in the terminal:

    `python node.py`

### Manage your Python virtual envs on per project basis with Anaconda. Then when running a that virtual env

    `source ~/.bash_profile` first if you use zsh (no need if you already use/source `~/.bash_profile` -- the conda setup is there)

    `source activate <YOUR_ENVIRONMENT_NAME>`
