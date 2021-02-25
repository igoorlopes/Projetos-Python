cigarros_dia = int(input('Quantos cigarros você fuma por dia?'))
anos_fumante = int(input('Por quantos anos você fuma?'))
cigarro = 10
anos_fumante_em_dias = anos_fumante * 365
minutos_perdidos_dia = cigarros_dia * cigarro 
minutos_perdidos_anos = minutos_perdidos_dia * anos_fumante_em_dias
dias_perdidos = minutos_perdidos_anos / 1440
print(f'Um fumante perde 10 minutos de vida a cada cigarro!!')
print(f'Você perdeu um total de {dias_perdidos:.0f} dias de vida')
