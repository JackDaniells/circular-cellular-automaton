# Autômato celular circular

Implementação de um autômato celular circular em Python. Projeto executado na disciplina de Teoria da computação, do programa de Pós Graduação em Ciências da Computação da Universidade Federal de Santa Catarina.

# Problema 

Um autômato celular é uma coleção de células em uma grade de forma especificada que evolui através de um número de intervalos de tempo discretos de acordo com um conjunto de regras que descrevem o novo estado de uma célula com base nos estados de células vizinhas. 

A ordem do autômato celular é o número de células que ele contém. Células do autômatos de ordem ```n``` são numerados de 1 a ```n```.

A ordem da célula é o número de valores diferentes que ela pode conter. Normalmente, os valores de uma célula de ordem ```m``` são considerados números inteiros de 0 a ```m``` - 1.

Uma das propriedades mais fundamentais de um autômato celular é o tipo de grade na qual ele é calculado. Neste problema, examinamos o tipo especial de autômato celular - autômato celular circular de ordem ```n``` com células da ordem ```m```. Vamos denotar esse tipo de autômato celular como ```n,m-automato```.
Uma distância entre as células ```i``` e ```j``` em ```n,m-autômato``` é definida como ```min (|i − j|, n − |i − j|)```. Um ambiente ```d``` de uma célula é o conjunto de células a uma distância não maior que ```d```.

Em cada etapa de ```d```, os valores de todas as células são substituídos simultaneamente por novos valores. O novo valor da célula ```i``` após o passo ```d``` é calculado como a soma dos valores das células pertencentes ao ambiente d da célula ```i``` módulo ```m```.

A imagem a seguir mostra uma etapa do ```5,3-automato```

<img width="248" alt="Captura de Tela 2021-03-06 às 13 54 22" src="https://user-images.githubusercontent.com/11572814/110214479-76919500-7e83-11eb-9977-0b4b143788e1.png">

O problema é calcular o estado do ```n,m-automato``` após ```k``` etapas de ```d```.

## Entrada

arquivo: ```cell.in```

A primeira linha do arquivo de entrada contém quatro números inteiros ```n```, ```m```, ```d``` e ```k``` ```(1 ≤ n ≤ 500, 1 ≤ m ≤ 1 000 000, 0 ≤ d < n/2 , 1 ≤ k ≤ 10.000.000)```. A segunda linha contém ```n``` números inteiros de 0 a ```m``` - 1, representando os valores iniciais das células do autômato.

## Saída

arquivo: ```cell.out```

Produzir os valores das células do ```n,m-automato``` após após ```k``` etapas de ```d```.

## Exemplo de entrada e saída
<img width="575" alt="Captura de Tela 2021-03-06 às 14 01 28" src="https://user-images.githubusercontent.com/11572814/110214678-75ad3300-7e84-11eb-8d27-9470b4acd952.png">

# Setup

Certifique-se de ter o Python instalado e operando em sua máquina.
Link de donwload: https://www.python.org/downloads/

#Execução

Para executar o algoritmo proposto, utilize o seguinte comando abaixo: 
```
python3 circular-cellular-automaton.py 
```

Configure o arquivo ```cell.in```com a entrada desejada, respeitando o padrão apresentado no problema, e o resultado será salvo no arquivo ```cell.out```







