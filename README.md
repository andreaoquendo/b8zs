# Codificação de Linha: B8ZS

Este projeto foi feito para a disciplina de Comunicação de Dados. O objetivo é fazer a comunicação por mensagens entre duas máquinas usando uma criptografia escolhida pela dupla (Cripto de Vegenère incluindo letras maiústculas e caracteres especiais) e a codificação de linha B8ZS.

Este projeto engloba a interface gráfica, criptografia e codificação do emissor e do receptor, além de plotar o gráfico do código de linha.

## Requisitos para rodar o projeto

Para executar o B8ZS, é necessário ter python e as bibliotecas socket, tkinter e matplotlib.

## Execução e funcionamento

Para executar o B8ZS, é necessário inserir nos terminais de cada uma das máquinas, no diretório do projeto:

```
$ python main.py
```

E aparecerá a seguinte interface para ambos o Host quanto para o Client.

<p align="center">
  <img src="https://user-images.githubusercontent.com/57603966/210002150-e2afad86-a860-4298-8627-353284c49b18.png">
</p>

Ambos devem estar conectados na mesma rede. O host deverá ser estabelecido primeiro, e só será conectado à sua respectiva interface quando o client for estabelecido e a mensagem poderá ser enviada (Client) ou recebida (Host).

<p align="center">
  <img height="300" src="https://user-images.githubusercontent.com/57603966/210003294-7a26c4e9-eeea-4056-8edd-61768e52515d.png">
</p>

<p align="center">
  <img height="300" src="https://user-images.githubusercontent.com/57603966/210003175-5edf7ea4-83b9-4dec-a34a-3f7d9ddd1466.png">
</p>


Ao receber a mensagem o gráfico do código de linha será impresso em uma aba separada também.

<p align="center">
  <img height="300" src="https://user-images.githubusercontent.com/57603966/210002397-29a4316f-766c-4568-911c-cf243862ae1c.png">
</p>

## Autores
Andrea Oquendo e Fernanda Neto
