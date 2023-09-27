## Instruction to Prepare Environment

### Step 1 Install Miniconda

Download and install appropriate Miniconda for your operating system. Miniconda is a package and environment manager and can be download from (https://docs.conda.io/en/latest/miniconda.html). Verify that the Miniconda was already installed and ready to use by opening a terminal/command prompt and run the following command.

```
conda --version
```
### Step 2 Create your Conda environment.

Open a terminal/command prompt run the following command.  
```
conda create --name myenv python=3.9
```
Change the myenv with you preferred environment name.

### Step 3 Activate your Conda environment.  
In a terminal/command prompt run the following command.  
```
conda activate myenv
```
replace the myenv with your environment name.
### Step 4 Install Jupyter Notebook   
In a terminal/command prompt window with activated conda environment run the following command.
```
conda install jupyter
```

### Step 5 Make the environment available for Juypter Notebook  
In a terminal/command prompt window with activated conda environment run the following command.  
```
ipython kernel install --user --name=myenv (replace myenv with your env name)
```
### Step 6 Open the Jupyter Notebook  
In a terminal/command prompt window with activated conda environment run the following command.  
```
jupyter notebook
```
A new window will open in your default browser, select the proper kernel in this case myenv.   


Finally, if you want to install extra package simply in a terminal/command prompt window with activated conda environment run the following.
```
pip install package_name
```








