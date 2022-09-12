# Test of the pangeo forge

 - Starting point : https://pangeo-forge.readthedocs.io/en/latest/introduction_tutorial/intro_tutorial_part2.html
 - Also the example of eNATL60 data fluxed by Takaya : https://github.com/pangeo-forge/staged-recipes/pulls?q=is%3Apr+roxyboy

 - Installation of libraries :
 
```
conda create -n forge
conda activate forge
conda install -c conda-forge pangeo-forge-recipes```
conda install ipykernel
python -m ipykernel install --user --name forge --display-name forge
```