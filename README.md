Medidas Elétricas e Magnéticas
==============================
Código para cálculo de um divisor de tensão através dos dados de entrada e saída
desejados.

# Criação de um ambiente virtual
Linux
-----
* python3 -m pip install pipenv
* python3 -m pipenv install
* python3 -m pipenv shell

Windows
-------
* python -m pip install pipenv
* python -m pipenv install
* python -m pipenv shell

# Instalando dependências
pipenv install Pipfile

# Utilização do comando
python resistor_search.py Vin Vout

# Para mais informações
python resistor_search.py --help
