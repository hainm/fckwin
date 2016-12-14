git clone https://github.com/tornadoweb/tornado
cd tornado
python setup.py build -c mingw32
python setup.py install
cd ..

git clone https://github.com/pallets/markupsafe
cd markupsafe
python setup.py build -c mingw32
python setup.py install
cd ..
