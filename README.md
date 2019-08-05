# FASTA&Furious
Este é uma tentativa de criar um executável em python para ajudar colegas de laboratório a extrair (subset) informações de um banco de dados de sequências biológicas (proteínas, genes...) no formato *.fasta* com base em uma lista de identificadores das sequências desejadas.

Durante meu doutorado na laboratório de biologia integrativa (Proteômica em Plantas - P8) por diversas vezes precisamos extrair apenas algumas proteínas de interesse do proteôma de alguma espécie. O procedimento padrão era utilizar o site [*FABOX*](http://users-birc.au.dk/palle/php/fabox/fasta_extractor.php), mas quando o banco se aproximava das 60k proteínas o servidor que hospeda a aplicação falha frequentemente e ficava inviável o procedimento. Quando precisei fazer essa extração pela primeira vez em 2016 descobri que os colegas passavam semanas buscando cada identificador dentro do banco e copiando cada sequência por vez para um arquivo novo. Eu tinha experiência 0 com bioinformática, e procurei ajuda. Primeiro um professor me mostrou como fazer via terminal no Ubunto com o [*blast+*](https://www.ncbi.nlm.nih.gov/guide/howto/run-blast-local) do NCBI instalado. O problema foi que ninguém do laboratório tinha experiência com o sistema operacional e não havia uma máquina para deixar com ele instalado. Depois, me interessei mais por R e aprendi a fazer essa tarefa em R e compartilhei o script (junto com um mini-curso) com os colegas. Meus colegas ainda me procuram frequentemente para fazer essa tarefa, assim, esse repositório é uma tentativa de criar um executável para Windows que faça essa extração e dê independência aos alunos do laboratório.

# Andamento
- Por enquanto, o script que executa a tarefa está parcialmente pronto, precisa ainda ser generalizado para aceitar qualquer arquivo .fasta como banco e um *.txt*, *.csv* ou *.xlsx* com os IDs;  
- Fiz um esboço de uma interface no Glade;  
- O script precisa ser aninhado a interface para que o usuário possa clicar nos botões da interface e o script fazer o trabalho;  
- Compilar para *.exe*;

# Alternativa
Uma interface que executa o script no R também seria interessante (por curiosidade).
