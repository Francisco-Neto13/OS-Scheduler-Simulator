# Simulador de Sistema Operacional

Um projeto prático desenvolvido para implementar e visualizar os principais **conceitos de Sistemas Operacionais**, simulando o funcionamento de um SO real.  
O objetivo é permitir que o usuário atue como o **kernel** de um mini sistema operacional, controlando processos, filas e algoritmos de escalonamento.

---

## Objetivo

Implementar, de forma prática, os principais conceitos de **Sistemas Operacionais**, incluindo:

- Criação e gerenciamento de processos  
- Filas de **pronto** e **bloqueado**  
- Algoritmos de escalonamento (**FIFO**, **SJF**, **Round Robin**, **Prioridades**)  
- Troca de contexto e **quantum**  
- Consumo de **CPU** e **memória**

---

## Contexto

Nos bastidores de todo computador, o **Sistema Operacional** decide:
- Qual processo será executado,
- Por quanto tempo,
- E como os recursos serão compartilhados.

Neste projeto, **você será o kernel**: o núcleo responsável por tomar essas decisões e gerenciar os processos.  
O desafio é **simular o comportamento de um escalonador real**, permitindo que o usuário escolha o algoritmo e visualize a execução passo a passo.

---

## Descrição da Atividade

O projeto consiste em um **simulador de Sistema Operacional** desenvolvido em **Python**, com as seguintes funcionalidades:

### 1. Gerenciamento de Processos

Cada processo possui os seguintes atributos:

| Atributo | Descrição |
|-----------|------------|
| PID | Identificador único |
| Nome | Nome do processo |
| Tempo de CPU restante | Unidades de tempo que ainda precisa executar |
| Memória ocupada | Quantidade de memória utilizada |
| Prioridade | Valor de 1 a 5 (1 = mais alta) |
| Estado | Pronto, Executando, Bloqueado ou Finalizado |

---

### 2. Comandos Disponíveis

O sistema aceita comandos digitados no terminal:

| Comando | Função |
|----------|--------|
| `create <nome>` | Cria um processo com dados aleatórios |
| `list` | Lista todos os processos e seus estados |
| `run <algoritmo>` | Executa o escalonamento escolhido |
| `block <PID>` | Bloqueia um processo |
| `unblock <PID>` | Desbloqueia um processo |
| `kill <PID>` | Encerra um processo |
| `exit` | Encerra o sistema |

---

### 3. Algoritmos de Escalonamento

Durante a simulação, o usuário pode escolher o algoritmo de escalonamento:

| Comando | Algoritmo | Descrição |
|----------|------------|-----------|
| `run fifo` | **First In First Out** | Executa os processos na ordem de chegada |
| `run sjf` | **Shortest Job First** | Executa primeiro o processo com menor tempo de CPU |
| `run rr` | **Round Robin** | Executa por fatias de tempo (quantum = 2 ciclos) |
| `run prio` | **Prioridades** | Executa processos de maior prioridade primeiro |

---

### 4. Simulação

- Cada execução consome **1 unidade de CPU**.  
- O programa imprime, a cada ciclo:
  - A **ordem de execução**  
  - O **estado atual** de cada processo  

- O processo muda para o estado **Finalizado** quando o tempo de CPU restante chega a 0.  
- No **Round Robin**, após consumir o quantum, o processo volta ao final da fila se ainda tiver tempo restante.

---

### 5. Exemplo de Execução

```bash
SO> create chrome
SO> create vscode
SO> create spotify
SO> list
PID | Nome       | CPU | MEM | PRIO | Estado
1   | chrome     | 5   | 92  | 3    | Pronto
2   | vscode     | 2   | 76  | 1    | Pronto
3   | spotify    | 4   | 120 | 5    | Pronto
SO> run prio
Executando por Prioridade...
-> Executando vscode (PID 2) - CPU restante: 2
✓ Processo 2 finalizado!
-> Executando chrome (PID 1) - CPU restante: 5
...
