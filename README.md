# Jogo Gyges
O jogo Gyges foi criado por Claude Leroy em 1984. Esse jogo é tradicionalmente praticado entre dois jogadores. Para jogar, utiliza-se um tabuleiro de 6x6 casas, mais duas casas de vitória, totalizando 38 casas. Além disso, são utilizadas 12 peças, de 3 níveis diferentes (diferenciadas pelo número de camadas que possuem), sendo 4 peças de cada nível. Na imagem abaixo, pode-se observar a dispodição do tabuleiro e das peças.

<p align="center">
    <img src="https://raw.githubusercontent.com/gustavo-c-cunha/Jogo-Gyges/master/posicaoPecas.png"> 
</p>

No início da partida, as peças são posicionadas nas colunas do tabuleiro mais proximas de cada jogador, sendo 6 peças em cada uma dessas colunas, com duas peças de cada nível (observar imagem acima). O Objetivo do jogo é levar uma das peças até a casa de vitória do lado adversário. Para isso, os jogadores realizam movimentos em turnos alternados, movimentando uma peça por vez. Todas as peças podem ser movimentadas por qualquer um dos jogadores, repeitando apenas uma restrição: os participantes só podem movimentar a peça que está mais próxima de si.

As peças podem ser movimentadas vertical e horizontalmente, podendo percorrer o número de casas correspondente ao seu nível, assim, uma peça de nível 1 só pode percorrer uma casa por vez, enquanto uma peça de nível 3 pode percorrer 3 casas. Durante o movimento, as peças não podem transitar sobre outras peças, sendo permitido apenas encerrar o movimento sobre outra peça. Caso esta situação ocorra, o jogador tem duas opções, são elas:
  - Acrescentar o número de movimentos da peça que estava na casa a sua peça, podendo movimentá-la novamente. Por exemplo, se uma peça de nível 2 encerrou seus movimentos sobre uma peça de nível 3, o jogador pode movimentar sua peça de nível 2 por mais 3 casas.
  - Reposicionar a peça que estava na casa anteriormente, sendo permitido posicioná-la em qualquer posição do tabuleiro, com exceção última coluna do jogador adversário que está sem peças (Ver exeplo na imagem abaixo).

<p align="center">
    <img src="https://raw.githubusercontent.com/gustavo-c-cunha/Jogo-Gyges/master/exemploReposicionar.png"> 
</p>

As casas de vitória só podem ser alcançadas pelas duas casas imediatamente vizinhas (ver imagem abaixo), sendo que para alcança-las, este deve ser o último movimento da peça. Por exemplo, uma peça de nível 3, só pode se posicionar na casa de vitória se já tiver realizado seus 2 movimentos anteriores.

<p align="center">
    <img src="https://raw.githubusercontent.com/gustavo-c-cunha/Jogo-Gyges/master/casasVizinhas.png"> 
</p>


Ao atingir a casa de vitória do adversário, o jogador vence a partida. Todas as regras do jogo estão listadas abaixo em detalhes.

## Regras:
- Cada jogador só pode movimentar a peça que está mais próxima de si.
- As peças só podem ser movimentadas nos eixos vertical e horizontal.
- As peças devem obrigatoriamente, percorrer o número de casas correspondente ao seu nível.
- As peças não podem transitar sobre outras peças.
- As peças podem encerrar sua jogada sobre outra peça, onde há duas opções:
  - Adquirir a quantidade de movimentos da peça em que está abaixo e continuar o movimento, ou
  - Ficar na casa e escolher uma posição para a peça que ocupava a casa anteriormente, sendo que a nova posição escolhida não pode ser atrás da última coluna vazia do adversário.
- As casas de vitória só podem ser alcançadas pelas duas casas que fazem vizinhança com esta, assim, a casa de vitória do jogador 1, só pode ser alcançada a partir das casas (3,1) e (4,1) e a casa de vitória do jogador 2, só pode ser alcançada a partir das casas (3,6) e (4,6).
- Ao atingir a casa de vitória do adversário o jogador vence a partida.

