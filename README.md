# CAR (Cadastro Ambiental Rural)
Visualização do panorama geral dos imóveis e áreas totais registradas em cada estado brasileiro.

## Introdução
Sabemos que o desmatamento é um tema recorrente em terras brasileiras, juntamente com as queimadas, por diversos fatores econômicos, políticos e sociais, e, como futuro engenheiro ambiental, o meu foco é descobrir uma maneira de coibir e/ou diminuir o desmatamento e conscientizar as pessoas sobre a importância de preservar o meio ambiente. E foi com esse intuito que vim apresentar o CAR (cadastro ambiental rural) como uma das soluções previstas para esse problema.

## Definição
Contextualizando, o CAR (cadastro ambiental rural) foi instituído pelo Novo Código Florestal (lei Federal 12.651/12), regulamentado pelo decreto Federal 7.830, de 17/10/2012, com o objetivo de integrar as informações ambientais dos imóveis rurais para criar uma base de dados para controle, monitoramento, planejamento ambiental e econômico e combate ao desmatamento.<br/>
Trata-se de um cadastro eletrônico de âmbito nacional que contempla **(i)** os dados do proprietário ou possuidor rural, **(ii)** a planta georreferenciada do perímetro do imóvel, **(iii)** as áreas de interesse social e **(iv)** as áreas de utilidade pública, com a informação da localização dos remanescentes de vegetação nativa, das áreas consolidadas e a localização das reservas legais, dentre outras.<br/>
A inscrição no cadastro é **obrigatória** para todos os proprietários e posseiros de imóveis rurais no país e traz inúmeras vantagens e benefícios, tais como:<br/>
1. Possibilidade de adesão ao Programa de Regularização Ambiental ("PRA");<br/>
2. Suspensão de sanções em função de infrações administrativas por supressão irregular de vegetação em áreas de Área de Preservação Permanente ("APP"), Reserva Legal e de uso restrito, cometidos até 22/07/2008;<br/>
3. Possibilidade de regularização das Áreas de Preservação Permanente e/ou Reserva Legal; e<br/>
4. Possibilidade de obtenção de crédito agrícola, em todas as suas modalidades, com taxas de juros menores, bem como limites e prazos maiores que os praticado no mercado.<br/><br/>

## Panorama Geral
Em resumo, o CAR veio tentar resolver o problema do desmatamento punindo os que desmatam e recompensando aqueles que preservam. A partir daí, fiz um levantamento da quantidade de imóveis registrados e a quantidade total da área e todos esse imóveis registrados, em hectares, em cada estado ,utilizando os dados do governo federal, criados em 8 de Agosto de 2018 e com a última atualização em 30 de Março de 2019, para ter acesso a esses dados, basta clicar [aqui](http://dados.gov.br/dataset/cadastro-ambiental-rural).

### Imóveis Registrados
Aqui temos um gráfico com os 10 estados com o maior e menor número de imóveis registrados pelo CAR<br/>
![imóveis maior](https://user-images.githubusercontent.com/48027825/94879535-d6989100-0436-11eb-9f97-b5272e8efe16.png)
![imóveis menor](https://user-images.githubusercontent.com/48027825/94879537-d7312780-0436-11eb-8714-e483346a66a0.png)

### Área total dos imóveis registrados
Aqui temos um gráfico com os 10 estados com a maior e menor área total (hectares) de todos os imóveis registrados pelo CAR<br/>
![area total imoveis maior](https://user-images.githubusercontent.com/48027825/94879560-ef08ab80-0436-11eb-9781-c6aac6ca0398.png)
![area total imoveis menor](https://user-images.githubusercontent.com/48027825/94879562-efa14200-0436-11eb-917a-d625dee9cce4.png)

### Área média dos imóveis registrados
Aqui temos um gráfico com os 10 estados com maior e menor área média (hectares) de cada imóvel registrado pelo CAR<br/>
![area média por imovel maior](https://user-images.githubusercontent.com/48027825/94879583-0051b800-0437-11eb-90ba-f04e7da1f7a2.png)
![area média por imovel menor](https://user-images.githubusercontent.com/48027825/94879585-00ea4e80-0437-11eb-98c0-be86159c828f.png)

Através desses dois ultimos gráficos, é notório que alguns estados possuem uma quantidade de imóveis proporcional a área de todos eles (Como Santa Catarina e Minas Gerais), enquanto outros possui uma quantidade de imóveis inversamente proporcional a área total de todos eles (Amazonas e Pará)

Para ter acesso a geração dos gráficos acima, clique [aqui](https://github.com/fernandessfae/CAR-Cadastro-Ambiental-Rural-/blob/master/panorama%20geral.py)
