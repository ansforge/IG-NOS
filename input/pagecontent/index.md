### Introduction

Les nomenclatures des objets de santé (NOS) sont indissociables du Modèle des Objets de Santé (MOS) et sont mises à disposition du secteur santé-social par l’agence du numérique en santé.

Les NOS reposent sur un système de codification (code et libellé) des éléments structurés du MOS (catégorie d'établissement, profession, etc.).


###Indicateur
Chaque mois, les indicateurs sont mis à jour comptabilisant le nombre de nomenclatures présentes : terminologie de référence, jeux de valeurs et tables d’association. Les NOS sont disponibles en plusieurs formats : PDF, CSV (.tabs), XML, SVS, XML/FHIR et JSON/FHIR.

###Un référentiel commun
Les NOS sont découpées en trois familles :

- **Les terminologies de référence (TRE)** sont des nomenclatures officielles créées et maintenues :
-soit par l'agence du numérique en santé qui en est propriétaire.
Par exemple, la TRE_R87-TypeCarte est une nomenclature regroupant les différents types de cartes des professionnels (CPx) fournies par l’agence du numérique en santé ;
-soit par une organisation externe à l'agence du numérique en santé ; dans ce cas, l'agence du numérique en santé extrait la terminologie, la formate selon ses conventions de nommage et de structure, pour l'intégrer dans ses systèmes.
- **Les jeux de valeurs (JDV)** sont des nomenclatures constituées de codes extraits d’une ou plusieurs TRE. Un jeu de valeurs est créé à des fins applicatives.
Par exemple avec les JDV du répertoire opérationnel des ressources (ROR) ou bien du cadre d’interopérabilité des systèmes d’information de santé (CI-SIS).
- **Les tables d'association (ASS)** sont des tables assurant la correspondance entre les codes issus d'au moins deux TRE.
Par exemple, la codification des secteurs d'activité dans le répertoire ADELI est remplacée par une codification RPPS. Cette migration nécessite de créer une table associant les codes de secteurs d’activité ADELI à ceux des secteurs d’activité RPPS.

Pour plus d'informations sur la constitution de ces nomenclatures, se reporter au document « Conventions de nommage et de structure des nomenclatures et des tables ».



Les principales sections de l'IG  sont :
* Le contexte de l'IG et les points dont les implémenteurs doivent être familier avant dans s'avoir plus sur l'IG
* Ce que les Implémenteurs doivent mettre en place
* Un onglet "télécharger"


### Auteurs et contributeurs

| Role  | Nom | Organisation | Contact |
| --- | --- | --- | --- |
| **Primary Editor** | Prenom Nom | Agence du Numérique en Santé | prenom.nom@address.email |