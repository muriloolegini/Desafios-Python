import wmi

# Carrega informações #
c = wmi.WMI()
my_system = c.Win32_ComputerSystem()[0]

# Mostra resultados #
print(f'Marca: {my_system.Manufacturer}')
print(f'Modelo: {my_system.Model}')
print(f'Nome: {my_system.Name}')
print(f'QTD CPU: {my_system.numberOfProcessors}')
print(f'Arquitetura: {my_system.SystemType}')
print(f'Família: {my_system.SystemFamily}')