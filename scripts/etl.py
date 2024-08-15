import subprocess
import os

print("---Running data generation...---")
subprocess.run(['python', os.path.join('scripts', 'generate.py')])

print("---Running data transformation...---")
subprocess.run(['python', os.path.join('scripts', 'transform.py')])

print("---Loading data into PostgreSQL...---")
subprocess.run(['python', os.path.join('scripts', 'load.py')])

print("---ETL process completed successfully.---")
