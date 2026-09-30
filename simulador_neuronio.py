import matplotlib.pyplot as plt
import numpy as np

# 1. PARÂMETROS DA SIMULAÇÃO
tempo_total = 100  # Tempo total da simulação em milissegundos (ms)
dt = 0.1  # Passo de tempo (intervalo de atualização)
passos = int(tempo_total / dt)
tempo = np.linspace(0, tempo_total, passos)

# 2. PARÂMETROS DO NEURÔNIO
v_repouso = -70.0  # Potencial de repouso do neurônio (em mV)
v_limiar = -55.0  # Limiar para o disparo/spike (em mV)
v_reset = -80.0  # Para onde o potencial vai logo após o spike (em mV)
resistencia = 10.0  # Resistência da membrana (em Ohms)
tau = 10.0  # Constante de tempo do neurônio (velocidade de reação)

# 3. ESTÍMULO (Corrente elétrica externa injetada no neurônio)
# Injetamos uma corrente constante de 2.5 miliamperes
corrente_injetada = np.ones(passos) * 2.5

# Vetor para guardar o histórico da voltagem do neurônio ao longo do tempo
voltagem = np.ones(passos) * v_repouso
spikes = []  # Lista para guardar o momento exato de cada spike

# 4. LOOP DE SIMULAÇÃO (O neurônio "vivendo" ao longo do tempo)
for t in range(1, passos):
    # Equação que calcula a nova voltagem baseada na corrente injetada
    dv = (
        -(voltagem[t - 1] - v_repouso) + resistencia * corrente_injetada[t]
    ) * (dt / tau)
    voltagem[t] = voltagem[t - 1] + dv

    # Se a voltagem passar do limiar, acontece o SPIKE!
    if voltagem[t] >= v_limiar:
        voltagem[t - 1] = 20.0  # Desenha a linha vertical do pico do spike (graficamente)
        voltagem[t] = v_reset  # Reseta o neurônio imediatamente
        spikes.append(tempo[t])  # Registra o tempo em que o spike aconteceu

# 5. EXIBIÇÃO DOS RESULTADOS (O Gráfico)
plt.figure(figsize=(10, 5))
plt.plot(tempo, voltagem, label="Potencial de Membrana (mV)", color="darkblue")
plt.axhline(
    y=v_limiar,
    color="red",
    linestyle="--",
    label="Limiar de Disparo (-55mV)",
)
plt.title("Simulador de Spikes Neuronais (Modelo Integrate-and-Fire)")
plt.xlabel("Tempo (ms)")
plt.ylabel("Voltagem da Membrana (mV)")
plt.legend()
plt.grid(True)
plt.show()

# Resumo impresso no terminal
print(f"Simulação concluída! O neurônio disparou {len(spikes)} spikes.")
