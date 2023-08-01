import pandas as pd

df = pd.read_csv('notas_alunos.csv', sep = ';')

df['media'] = (df['nota_1'] + df['nota_2']) / 2
df['situacao'] = df.apply(lambda row: 'REPROVADO' if (row['faltas'] > 5 or row['media'] < 7) else 'APROVADO', axis=1)

df.to_csv('alunos_situacao.csv', index=False)

maior_numero_faltas = df['faltas'].max()
media_geral_notas = df['media'].mean()
maior_media = df['media'].max()

print("Maior número de faltas:", maior_numero_faltas)
print("Média geral das notas dos alunos:", media_geral_notas)
print("Maior média:", maior_media)
