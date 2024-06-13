# GenomeScanner_snakemake
**A new snakemake pipeline to classify prokaryotic and fungal genomes using an integrative conceptual framework**

Author: Ayixon Sanchez Reyes

Developers: Ayixon Sanchez Reyes, Karel Estrada

Affiliation:Computational Microbiology. Microbiological Observatory. Institute of Biotechnology, UNAM, Cuernavaca, MEXICO
           
Unidad Universitaria de Secuenciacion Masiva y Bioinformatica. Institute of Biotechnology, UNAM, Cuernavaca, MEXICO

Latest modification: Sun Dec 31, 2023

--------------------------------------


**=>The file check_commands_Snakefile_genomescanner.py mus be in $HOME**

**=>The path to database.msh and query genome must be defined in the Snakemake file**

"Examples:"

            snakemake help -qc1 -s /home/karel/bin/Snakefile_genomescanner  #  Show this help message"
            snakemake all --cores all --config REF=ecoli.fna DB=DB.msh -s /home/karel/bin/Snakefile_genomescanner  >> genomescanner.log  #  Run the entire pipeline using all available cores, your own Mash database (DB.msh), and the E.coli DNA genome for classification"
