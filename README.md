# RanqueamentoPLN
TERMOS: bioinformatics analysis gene
Significado das variaveis

terms_of_eachdoc = lista com os termos finais de cada doc corrente no for
docs_terms = lista de 20 posições com todos os termos de todas os documentos, é uma lista de de docs
terms_plus_frequencies = lista de termos e suas FREQUENCIAS de cada documento, size = nº de termos do doc
terms_plus_frequencies[i] = é uma tupla de (termo, frequencia)
terms = lista com o termos de todos os documentos, sem divisões e sem frequência
final_terms = lista com os termos sem duplicatas
terms_plus_logfreq = lista com termos e tf ponderada de cada documento. len= 20
terms_plus_logfreq[i] = lista com termos e tf com len= nº de termos do doc
DF = lista de size: 1202 com a o nº de documentos em que cada termo aparece
IDF = lista de size: 1202 com o inverse of document frequency
DF e IDF seguem a ordenação de final_terms