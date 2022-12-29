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

Ambos devem estar conectados na mesma rede. O host deverá ser estabelecido primeiro, e só será conectado à sua respectiva interface quando o client for estabelecido e a mensagem poderá ser enviada (Client) ou recebida (Host).

Ao receber a mensagem o gráfico da mensagem será impresso em uma aba separada também.

## Autores
Andrea Oquendo e Fernanda Neto