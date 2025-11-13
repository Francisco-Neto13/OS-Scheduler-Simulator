from kernel import Kernel

def main():
    kernel = Kernel()

    while True:
        try:
            comando_completo = input("SO> ").strip().lower()
            if not comando_completo:
                continue

            partes = comando_completo.split()
            comando = partes[0]
            argumento = partes[1] if len(partes) > 1 else None

            
            if comando == 'create' and argumento:
                kernel.criar_processo(argumento)

            elif comando == 'list':
                kernel.listar_processos()

            elif comando == 'run' and argumento:
                algoritmos_validos = ['fifo', 'sjf', 'rr', 'prio']
                if argumento in algoritmos_validos:
                    kernel.run_escalonador(argumento)
                else:
                    print(f"Algoritmo desconhecido: {argumento}. Use: {', '.join(algoritmos_validos)}")
            
            elif comando == 'block' and argumento:
                try:
                    kernel.bloquear_processo(int(argumento))
                except ValueError:
                    print("O argumento para 'block' deve ser o PID (número inteiro).")

            elif comando == 'unblock' and argumento:
                try:
                    kernel.desbloquear_processo(int(argumento))
                except ValueError:
                    print("O argumento para 'unblock' deve ser o PID (número inteiro).")

            elif comando == 'kill' and argumento:
                try:
                    kernel.matar_processo(int(argumento))
                except ValueError:
                    print("O argumento para 'kill' deve ser o PID (número inteiro).")

            elif comando == 'exit':
                print("Encerrando simulador do SO.")
                break

            else:
                print(f"Comando '{comando}' desconhecido ou incompleto.")
                print("Comandos: create <nome>, list, run <algoritmo>, block <PID>, unblock <PID>, kill <PID>, exit")

        except Exception as e:
            print(f"Ocorreu um erro: {e}")

if __name__ == "__main__":
    main()