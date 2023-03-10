import numpy as np
import pandas as pd
import statsmodels.api as sm

# Carregando o conjunto de dados
df = pd.read_csv("time_series_data.csv", index_col='timestamp', parse_dates=True)

# Dividindo o conjunto de dados em treinamento e teste
train_data = df[:int(0.8*(len(df)))]
test_data = df[int(0.8*(len(df))):]

# Treinar o modelo SARIMA
model = sm.tsa.SARIMAX(train_data['target_variable'], order=(1, 0, 1), seasonal_order=(1, 1, 1, 12))
model_fit = model.fit()

# Fazer previsões nos dados de teste
predictions = model_fit.predict(start=test_data.index[0], end=test_data.index[-1], dynamic=False)

# Avaliar o desempenho do modelo
error = np.mean((test_data['target_variable'] - predictions)**2)
print("Erro quadrático médio: ", error)
