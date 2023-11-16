# native-python-caller
Calls Python code from a native executable and uses CMake as the makefile generator. Based on Stackoverflow answer: https://stackoverflow.com/a/58847011/802203

# To build:
mkdir build-dir
cd build-dir
cmake ..
make

# To run
cd ..
./build-dir/host/host