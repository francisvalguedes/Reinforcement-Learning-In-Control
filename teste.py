# import control as ct

# # Definir a função de transferência do sistema
# num = [1]      # Numerador
# den = [1, 2, 1]  # Denominador (s^2 + 2s + 1)

# sys_tf = ct.TransferFunction(num, den)  # Criando a função de transferência

# # Criando um sistema de entrada/saída linear
# sys_io = ct.LinearIOSystem(sys_tf, inputs="u", outputs="y")

# # Exibir o sistema
# print(sys_io)


# import control as ct

# # Definir a função de transferência do sistema
# num = [1]         # Numerador
# den = [1, 2, 1]   # Denominador (s^2 + 2s + 1)

# sys_tf = ct.TransferFunction(num, den)  # Criando a função de transferência

# # Converter para espaço de estados (necessário para um sistema dinâmico no Control)
# sys_ss = ct.tf2ss(sys_tf)

# # Criar um sistema de entrada/saída (Linear Time-Invariant System)
# sys_io = ct.LinearICSystem(sys_ss, inputs=["u"], outputs=["y"])

# # Exibir o sistema
# print(sys_io)


import control as ct

# Definir a função de transferência do sistema
num = [1]        # Numerador
den = [1, 2, 1]  # Denominador (s^2 + 2s + 1)

sys_tf = ct.TransferFunction(num, den)  # Criando a função de transferência

# Converter para espaço de estados
sys_ss = ct.tf2ss(sys_tf)

# Exibir os sistemas
print("Função de Transferência:")
print(sys_tf)

print("\nRepresentação no Espaço de Estados:")
print(sys_ss)
