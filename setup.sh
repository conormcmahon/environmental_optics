
# Generate a new conda environment to house this package
#   This was set up assuming the library would be run on a virtual Linux environment on Windows (WSL)
#   BUT I think this should largely be extensible to other environments with some tweaks

conda create -n env_opt python=3
conda activate env_opt
conda install matplotlib
#conda install numpy
