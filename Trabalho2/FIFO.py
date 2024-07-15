page_faults = 0
lista = []
quadrosRAM = int(input())
paginasReferenciadas = int(input())

for num in range(paginasReferenciadas):
    pagina = int(input())
    #breakpoint()
    if pagina not in lista:
        if len(lista) <= (quadrosRAM - 1):
            page_faults += 1
            lista.append(pagina)
        elif len(lista) == quadrosRAM:
            page_faults += 1
            lista.pop(0)
            lista.append(pagina)       

print(page_faults) 