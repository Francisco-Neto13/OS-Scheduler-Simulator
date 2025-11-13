import random

class Processo:
    PID_COUNTER = 1

    def __init__(self, nome, cpu_max=10):
        self.pid = Processo.PID_COUNTER
        Processo.PID_COUNTER += 1
        self.nome = nome
        self.cpu_restante = random.randint(1, cpu_max)
        self.memoria_ocupada = random.randint(20, 200)
        self.prioridade = random.randint(1, 5)
        self.estado = "Pronto"
        print(f" Processo '{nome}' criado (PID: {self.pid}) com CPU: {self.cpu_restante}, Mem: {self.memoria_ocupada}MB, Pri: {self.prioridade}")

    def __str__(self):
        return f"{self.pid:<4}| {self.nome:<12}| {self.cpu_restante:<4}| {self.memoria_ocupada:<4}| {self.prioridade:<6}| {self.estado}"