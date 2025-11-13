def escalonar_fifo(kernel):
    print("\n Iniciando escalonamento: **FIFO**")
    fila_trabalho = list(kernel.fila_pronto)
    _executar_nao_preemptivo(kernel, fila_trabalho)

def escalonar_sjf(kernel):
    print("\n Iniciando escalonamento: **SJF** (Menor Tempo de CPU Primeiro)")

    fila_trabalho_ordenada = sorted(
        [kernel.processos[pid] for pid in kernel.fila_pronto], 
        key=lambda p: p.cpu_restante
    )
    fila_trabalho = [p.pid for p in fila_trabalho_ordenada]
    _executar_nao_preemptivo(kernel, fila_trabalho)

def escalonar_prioridades(kernel):
    print("\n Iniciando escalonamento: **PRIORIDADES** (1 = Mais Alta)")
    fila_trabalho_ordenada = sorted(
        [kernel.processos[pid] for pid in kernel.fila_pronto], 
        key=lambda p: p.prioridade
    )
    fila_trabalho = [p.pid for p in fila_trabalho_ordenada]
    _executar_nao_preemptivo(kernel, fila_trabalho)

def escalonar_rr(kernel, quantum=2):
    print(f"\n Iniciando escalonamento: **ROUND ROBIN** (Quantum = {quantum})")
    fila_trabalho = list(kernel.fila_pronto)
    ciclo = 0

    while fila_trabalho:
        proximo_pid = fila_trabalho.pop(0)
        p = kernel.processos[proximo_pid]
        
        kernel.troca_de_contexto(proximo_pid)
        ciclo += 1
        print(f"\n--- Ciclo {ciclo} ---")
        
        finalizou = False
        for q in range(quantum):
            finalizou = kernel.ciclo_cpu(proximo_pid)
            if finalizou:
                break
        
        if not finalizou and p.cpu_restante > 0:
            print(f"Quantum expirado. Processo {proximo_pid} volta para o final da fila.")
            fila_trabalho.append(proximo_pid)
        
        kernel.atualizar_fila_pronto()


def _executar_nao_preemptivo(kernel, fila_trabalho):
    ciclo = 0

    for proximo_pid in fila_trabalho:
        p = kernel.processos[proximo_pid]
        
        if p.estado != "Pronto": 
            continue

        kernel.troca_de_contexto(proximo_pid)
        
        while p.cpu_restante > 0:
            ciclo += 1
            print(f"\n--- Ciclo {ciclo} ---")
            if kernel.ciclo_cpu(proximo_pid):
                break 
        
        kernel.atualizar_fila_pronto()