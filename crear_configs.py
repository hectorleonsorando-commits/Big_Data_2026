import os

# Crear archivos para Bloque 5

# PARTE 1 Docs
parte1_path = "Bloque5º Series temporales y forecasting/Parte1º/docs"

# requirements.txt
with open(f"{parte1_path}/requirements.txt", "w") as f:
    f.write("""# Core
numpy>=1.20.0
pandas>=1.3.0
scipy>=1.7.0

# Visualización
matplotlib>=3.4.0
seaborn>=0.11.0
plotly>=5.0.0

# Machine Learning
scikit-learn>=0.24.0
statsmodels>=0.12.0

# Jupyter
jupyterlab>=4.0.0
jupyter>=1.0.0
ipython>=7.0.0
""")

# environment.yml
with open(f"{parte1_path}/environment.yml", "w") as f:
    f.write("""name: big_data_bloque5_parte1
channels:
  - conda-forge
  - defaults
dependencies:
  - python=3.11
  - numpy
  - pandas
  - scipy
  - matplotlib
  - seaborn
  - scikit-learn
  - jupyter
  - jupyterlab
  - ipython
  - pip
  - pip:
    - statsmodels>=0.12.0
    - plotly>=5.0.0
""")

# PARTE 2 Docs
parte2_path = "Bloque5º Series temporales y forecasting/Parte2º/docs"

# requirements.txt
with open(f"{parte2_path}/requirements.txt", "w") as f:
    f.write("""# Core
numpy>=1.20.0
pandas>=1.3.0
scipy>=1.7.0

# Visualización
matplotlib>=3.4.0
seaborn>=0.11.0
plotly>=5.0.0

# Machine Learning
scikit-learn>=0.24.0
statsmodels>=0.12.0

# Jupyter
jupyterlab>=4.0.0
jupyter>=1.0.0
ipython>=7.0.0
""")

# environment.yml
with open(f"{parte2_path}/environment.yml", "w") as f:
    f.write("""name: big_data_bloque5_parte2
channels:
  - conda-forge
  - defaults
dependencies:
  - python=3.11
  - numpy
  - pandas
  - scipy
  - matplotlib
  - seaborn
  - scikit-learn
  - jupyter
  - jupyterlab
  - ipython
  - pip
  - pip:
    - statsmodels>=0.12.0
    - plotly>=5.0.0
""")

# BLOQUE 6
bloque6_path = "Bloque6º Proyecto_final_data_analyst_mayo_2026/docs"

# requirements.txt
with open(f"{bloque6_path}/requirements.txt", "w") as f:
    f.write("""# Core
numpy>=1.20.0
pandas>=1.3.0
scipy>=1.7.0

# Visualización
matplotlib>=3.4.0
seaborn>=0.11.0
plotly>=5.0.0

# Machine Learning
scikit-learn>=0.24.0
statsmodels>=0.12.0
xgboost>=1.5.0

# Jupyter
jupyterlab>=4.0.0
jupyter>=1.0.0
ipython>=7.0.0
""")

# environment.yml
with open(f"{bloque6_path}/environment.yml", "w") as f:
    f.write("""name: big_data_bloque6_proyecto_final
channels:
  - conda-forge
  - defaults
dependencies:
  - python=3.11
  - numpy
  - pandas
  - scipy
  - matplotlib
  - seaborn
  - scikit-learn
  - jupyter
  - jupyterlab
  - ipython
  - pip
  - pip:
    - statsmodels>=0.12.0
    - plotly>=5.0.0
    - xgboost>=1.5.0
""")

print("✓ Archivos requirements.txt y environment.yml creados")
