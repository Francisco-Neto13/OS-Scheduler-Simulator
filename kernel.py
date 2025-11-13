from collections import deque
from processo import Processo
import escalonadores 

class Kernel:
    def __init__(self):
        self.processos = {}
        self.fila_pronto = deque()
        self.fila_bloqueado = deque()
        self.pid_executando = None


    def criar_processo(self, nome):
        novo_processo = Processo(nome)
        self.processos[novo_processo.pid] = novo_processo
        self.fila_pronto.append(novo_processo.pid)

    def _mover_para(self, pid, nova_fila_deque, novo_estado):
        if pid not in self.processos:
            print(f"Erro: PID {pid} não encontrado.")
            return False

        p = self.processos[pid]

        try:
            self.fila_pronto.remove(pid)
        except ValueError:
            pass
        try:
            self.fila_bloqueado.remove(pid)
        except ValueError:
            pass
        
        if novo_estado == "Pronto":
            self.fila_pronto.append(pid)
        elif novo_estado == "Bloqueado":
            self.fila_bloqueado.append(pid)

        p.estado = novo_estado
        return True

    def bloquear_processo(self, pid):
        p = self.processos.get(pid)
        if p and p.estado == "Pronto":
            if self._mover_para(pid, self.fila_bloqueado, "Bloqueado"):
                print(f"Processo {pid} bloqueado e movido para a Fila de Bloqueado.")
        else:
            print(f"Processo {pid} não pode ser bloqueado (Estado: {p.estado if p else 'Não Encontrado'}).")

    def desbloquear_processo(self, pid):
        p = self.processos.get(pid)
        if p and p.estado == "Bloqueado":
            if self._mover_para(pid, self.fila_pronto, "Pronto"):
                print(f"Processo {pid} desbloqueado e movido para a Fila de Pronto.")
        else:
            print(f"Processo {pid} não pode ser desbloqueado (Estado: {p.estado if p else 'Não Encontrado'}).")

    def matar_processo(self, pid):
        if self._mover_para(pid, deque(), "Finalizado"):
            if self.pid_executando == pid:
                self.pid_executando = None
            print(f"Processo {pid} encerrado (Finalizado).")

    def listar_processos(self):
        """Exibe todos os processos em formato de tabela."""
        if not self.processos:
            print("Nenhum processo criado.")
            return

        print("\nPID | Nome        | CPU | MEM | PRIO | Estado")
        print("----|-------------|-----|-----|------|------------")
        processos_ordenados = sorted(self.processos.values(), key=lambda p: p.pid)

        for p in processos_ordenados:
            print(p)
        print("----|-------------|-----|-----|------|------------")
        print(f"Prontos: {list(self.fila_pronto)} | Bloqueados: {list(self.fila_bloqueado)}")
        print(f"Executando: {self.pid_executando if self.pid_executando else 'Nenhum'}\n")

    
    def troca_de_contexto(self, novo_pid):
        if self.pid_executando and self.processos[self.pid_executando].cpu_restante > 0:
            self.processos[self.pid_executando].estado = "Pronto"

        self.pid_executando = novo_pid
        if novo_pid is not None:
            self.processos[novo_pid].estado = "Executando"

    def ciclo_cpu(self, pid):
        p = self.processos[pid]
        p.cpu_restante -= 1
        
        print(f"-> Executando {p.nome} (PID {p.pid}) - CPU restante: {p.cpu_restante}")

        if p.cpu_restante <= 0:
            self._mover_para(p.pid, deque(), "Finalizado")
            print(f"✓ Processo {p.pid} ({p.nome}) finalizado!")
            self.pid_executando = None
            return True
        
        return False

    def atualizar_fila_pronto(self):
        self.fila_pronto = deque([p.pid for p in self.processos.values() if p.estado == "Pronto"])


    def run_escalonador(self, algoritmo):
        if not self.fila_pronto:
            print("⚠️ Nenhuma processo na Fila de Pronto para executar.")
            return

        if algoritmo == 'fifo':
            escalonadores.escalonar_fifo(self)
        elif algoritmo == 'sjf':
            escalonadores.escalonar_sjf(self)
        elif algoritmo == 'rr':
            escalonadores.escalonar_rr(self)
        elif algoritmo == 'prio':
            escalonadores.escalonar_prioridades(self)
        else:
            print(f"⚠️ Algoritmo {algoritmo} não suportado.")