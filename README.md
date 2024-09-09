# Projeto de Classificação de Imagens Termográficas

## Artigo
O artigo conta como foi todo o processo de desenvolvimento e de metodologia experimental, além de abordar conceitos importantes utilizados no pojeto

## Apresentação
Uma breve apresentação em pdf condensa as informações do artigo de forma mais objetivo e sintetizada.

## Instalação
Para instalar as dependências necessárias para executar de forma local, basta executa o arquivo `install-env.bat`.

## Exploração da Base de Dados

Este projeto utiliza a base de dados **DMR-IR**, que contém imagens termográficas de mamas coletadas pelo Laboratório Visual para Pesquisa em Mastologia da Universidade Federal Fluminense (UFF). As imagens foram capturadas com uma câmera térmica FLIR SC620 e possuem resolução de 480 x 640 pixels.

### Classes de Imagens
A base de dados inclui três classes de imagens:
- **Healthy (saudáveis)**
- **Sick (doentes)**
- **Unknown (desconhecidas)**

Para este projeto, utilizamos apenas as classes **Healthy** e **Sick**, descartando a classe **Unknown** devido à ausência de diagnóstico claro. As imagens foram baixadas em escala de cinza, uma vez que a análise termográfica foca na variação de temperatura, facilitada por imagens monocromáticas.

### Caminhos das Imagens
As imagens foram separadas em duas pastas:
- `healthy`: Imagens saudáveis.
- `sick`: Imagens doentes.

### Análise da Base de Dados
A análise inicial da base de dados revelou o número total de imagens em cada classe:
- Número de imagens saudáveis: `100`
- Número de imagens doentes: `100`

Exibimos algumas imagens dessas classes para visualização inicial, destacando as diferenças visuais entre as classes saudáveis e doentes.

## Limpeza dos Dados

Devido ao processo manual de download das imagens, foi necessário realizar uma limpeza. Apenas imagens frontais e classificadas como **healthy** ou **sick** foram mantidas. A classe **unknown** foi descartada para evitar introdução de ruído no treinamento do modelo.

## Pré-processamento

Realizamos o pré-processamento das imagens para garantir a consistência no tamanho e a remoção de imagens corrompidas ou mal formatadas. Todas as imagens foram convertidas para escala de cinza e redimensionadas para 640 x 480 pixels.

### Funções de Pré-processamento
As imagens passaram por diferentes etapas de pré-processamento:
- **Crop**: Aplicação de corte para focar na região de interesse.
- **Laplacian Filter**: Aplicação de filtro de contorno para realçar os detalhes das imagens.

As imagens foram salvas em pastas separadas conforme o pré-processamento aplicado:
- **healthy/crop** e **sick/crop**: Contêm as imagens após aplicação do crop.
- **healthy/laplacian** e **sick/laplacian**: Contêm as imagens após aplicação do filtro Laplacian.

Cada conjunto de imagens foi analisado visualmente após o pré-processamento para garantir a qualidade.

Após isso, as imagens foram formatadas para uso no modelo de aprendizagem. Diferentes técnicas de pré-processamento foram testadas, incluindo:
- Sem pré-processamento
- Crop
- Laplacian Filter
- **Mixup**: Técnica de data augmentation

Cada técnica foi aplicada individualmente e em combinação, totalizando seis diferentes condições para treinamento e teste.

## Modelos Utilizados
O projeto utiliza diferentes arquiteturas de CNN, incluindo:
- **ResNet50**
- **EfficientNet-B0**
- **VGG19**

Cada um desses modelos é ajustado conforme necessário para se adequar ao número de classes de saída (saudável ou doente).

## Treinamento
O treinamento é realizado utilizando o método de validação cruzada com K-Folds, com cada fold treinando e validando o modelo em subconjuntos diferentes do dataset.

Durante o treinamento, o otimizador **SGD** e a função de perda **Cross Entropy** são utilizados para ajustar os pesos do modelo.

## Avaliação do Modelo
Após o treinamento, o modelo é avaliado utilizando:
- **Acurácia:** Calculada sobre os dados de teste.
- **Matriz de confusão:** Exibida para visualizar a performance do modelo em distinguir as duas classes.

## Visualizações
O projeto inclui várias formas de visualização para ajudar a interpretar o desempenho do modelo:
- **Gráfico de Barras:** Mostra a média e o desvio padrão das acurácias para cada tipo de pré-processamento.
- **Matriz de Confusão:** Exibe os resultados da classificação em forma de matriz.
- **Curva de Aprendizado:** Mostra a evolução das perdas e da acurácia ao longo das épocas.
- **CAM (Class Activation Mapping):** Gera mapas de ativação para visualizar as regiões da imagem que mais contribuíram para a decisão do modelo.

## Conclusão
Este projeto fornece uma abordagem robusta para a detecção de tumores mamários utilizando CNNs e técnicas avançadas de visualização como CAM, possibilitando uma análise detalhada do comportamento do modelo e suas predições.