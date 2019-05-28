# Medidas Elétricas e Magnéticas
Código para cálculo de um divisor de tensão através dos dados de entrada e saída
desejados.

# Criação de um ambiente virtual
python3 -m venv env
source env/bin/activate

# Instalando dependências
pip install -r requirements.txt

# Utilização do comando
python resistor_search.py Vin Vout

# Para mais informações
python resistor_search.py --help
