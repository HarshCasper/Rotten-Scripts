#!/bin/bash
#
# Sets up virtual env and configures PATH for the project.
# Install openCV in virtual environment (what was a major issue)
#


#############################
# System Requirements (!!!) #
#############################

# Reload environment variables (.bash_profile in Mac; .profile in Ubuntu)
source ~/.bash_profile 2>/dev/null || source ~/.profile

# see if Xcode is downloaded on your machine
xcode-select -p


# updating Homebrew
brew update

# Launch the virtual environment if it exists
VIRTUALENV="edging"
if workon $VIRTUALENV 2>/dev/null; then
	echo "Launching virtual environment '$VIRTUALENV'..."
else
	echo "Creating virtual environment '$VIRTUALENV'..."

  # https://virtualenvwrapper.readthedocs.org/en/latest/
  # - "-p `which python2.7`": gives location of python2.7 in your machine
  # - "no-site-packages": don't borrow any libraries from your machine (total isolation)
  # - "$VIRTUALENV": name of virtual environment
  mkvirtualenv -p `which python2.7` --no-site-packages $VIRTUALENV

  # Install the project's requirements from requirements.txt
  pip install -r requirements.txt
fi

# additional packages and libraries
brew install cmake pkg-config
brew install jpeg libpng libtiff openexr
brew install eigen tbb

###################################
# Compiling and installing openCV #
###################################

# downloading openCV
cd ~
git clone https://github.com/Itseez/opencv.git
cd opencv
git checkout 3.1.0

# downloading free academic tools
cd ~
git clone https://github.com/Itseez/opencv_contrib
cd opencv_contrib
git checkout 3.1.0


# installation of openCV (special case of python27)
cd ~/opencv
if [ ! -d "build" ]; then
    mkdir build
    cd build
    cmake -D CMAKE_BUILD_TYPE=RELEASE -D CMAKE_INSTALL_PREFIX=/usr/local \
    	-D PYTHON2_PACKAGES_PATH=~/.virtualenvs/retrieval/lib/python2.7/site-packages \
    	-D PYTHON2_LIBRARY=/usr/local/Cellar/python/2.7.11/Frameworks/Python.framework/Versions/2.7/bin \
    	-D PYTHON2_INCLUDE_DIR=/usr/local/Frameworks/Python.framework/Headers \
    	-D INSTALL_C_EXAMPLES=OFF -D INSTALL_PYTHON_EXAMPLES=ON \
    	-D BUILD_EXAMPLES=ON \
    	-D OPENCV_EXTRA_MODULES_PATH=~/opencv_contrib/modules ..
    make -j4
    sudo make install
fi

echo "Finished installing OpenCV and all other requirements"

###############
# Final works #
###############

# Append project's subdirectories to the path in order to be able to call their
# modules from python later.
# if [ -z "$PROJECT_ROOT" ]; then
#   export PROJECT_ROOT=$PWD/retrieval
# 	echo "Using PROJECT_ROOT=$PROJECT_ROOT"
# fi
#
# echo "Appending project directories to PYTHONPATH..."
#
# export PYTHONPATH=$PYTHONPATH:$PROJECT_ROOT
#
# for dir in $PROJECT_ROOT/*; do
# 	export PYTHONPATH=$PYTHONPATH:$dir
# done
