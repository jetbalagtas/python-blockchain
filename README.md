This is a blockchain project written in Python.

1. Install python from https://www.python.org/

2. Ensure you are running the version you downloaded and installed with:

        python --version
        -- or --
        python


3. If they don't match, put this in your `~/.bash_profile` or if you use zsh, `~/.zshrc`

        alias python='python3'

4. If running `python` or `python --version` still won't match the downloaded version:

        source ~/.bash_profile

        run `python` or `python --version` again

5. Alternatively and if you don't want to mess with bash, you can simply run:

        `python3` (if you installed Python 3.x)

### To Use Locally

In the project directory, you can run this in the terminal:

        python node.py
    
(defaults to running on localhost port 5000 (`localhost:5000`))

### Manage 3rd party packages via Python-focused virtual envs on a per project basis with Anaconda. Then RUN YOUR VIRTUAL ENV:

If you use zsh:

    source ~/.bash_profile

(no need if you already use/source `~/.bash_profile` -- when installed, Anaconda appends the conda setup script there)

    source activate <YOUR_ENVIRONMENT_NAME>

### In development, to run multiple nodes (to simulate running multiple machines locally):
1. Open a new tab or instance of your terminal window
2. Navigate to your project folder
3. Run your virtual env in that instance
4. Run `python node.py -p <port>` or `python node.py --port <port>` wherein, `<port>` is the port you specify for your localhost.

#### 3rd party packages used by this app (and managed with Anaconda): ####
  - PyCrypto
  - Flask and all the packages it depends on **(use Postman to test and manipulate data)**
  - CORS (flask-cors)
